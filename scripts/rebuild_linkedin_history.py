#!/usr/bin/env python3
"""Rebuild unified LinkedIn post history from BOTH sources:
    1. A LinkedIn analytics CSV export (if provided) — historical metrics
    2. performance-data/*.md — Apify-scraped snapshots (current + ongoing)

Dedupes by post URL. If a URL appears in both, performance-data wins
(it's the fresher source with Apify engagement numbers).

Outputs:
    - history/linkedin-posts-history.jsonl — one line per post with tags + metrics
    - config/linkedin-patterns.json — structured stats (top/bottom, hook/style/CTA tables)
    - config/aayush-linkedin-patterns.md — human-readable patterns for /write-posts

Usage:
    python3 scripts/rebuild_linkedin_history.py                              # perf-data only
    python3 scripts/rebuild_linkedin_history.py --csv path/to/analytics.csv  # + CSV

Re-run any time new perf-data snapshots land or you get a fresh CSV export.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

# Import classifier + helpers from the CSV ingester (same heuristics)
# Allow import without pip install via sys.path tweak
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
from ingest_linkedin_csv import (  # type: ignore
    classify_hook,
    classify_style,
    classify_cta,
    count_specifics,
    summarize_patterns,
    render_markdown,
)


SNAPSHOT_BLOCK_RE = re.compile(
    r"## Snapshots\s*\n+```json\s*\n(?P<json>.*?)\n```",
    re.DOTALL,
)
META_RE = re.compile(r"^\*\*(\w+[\s\w]*)\*\*:\s*(.+)$", re.MULTILINE)
CONTENT_BLOCK_RE = re.compile(r"## Content\s*\n+(?P<content>.+?)(?=\n## |\Z)", re.DOTALL)


def parse_performance_md(path: Path) -> dict[str, Any] | None:
    """Read one Apify-generated markdown file. Return a dict or None if malformed."""
    raw = path.read_text(encoding="utf-8")

    # Extract metadata
    meta = {k.strip().lower(): v.strip() for k, v in META_RE.findall(raw)}
    url = meta.get("url", "").strip()
    post_id = meta.get("post id", "").strip()
    posted_at = meta.get("posted", "").strip()
    if not url:
        return None

    # Extract post content (Markdown blockquotes — strip "> " prefix)
    content_match = CONTENT_BLOCK_RE.search(raw)
    if content_match:
        raw_content = content_match.group("content").strip()
        # Unblockquote
        content_lines = []
        for line in raw_content.split("\n"):
            if line.startswith(">"):
                content_lines.append(line[1:].lstrip())
            else:
                content_lines.append(line)
        post_text = "\n".join(content_lines).strip()
    else:
        post_text = ""

    # Extract latest snapshot
    snap_match = SNAPSHOT_BLOCK_RE.search(raw)
    snapshots = []
    if snap_match:
        try:
            snapshots = json.loads(snap_match.group("json"))
        except json.JSONDecodeError:
            snapshots = []

    latest = snapshots[-1] if snapshots else {}

    return {
        "post_id": post_id,
        "url": url,
        "posted_at": posted_at,
        "post_text": post_text,
        "latest_snapshot_date": latest.get("snapshot_date", ""),
        "reactions": int(latest.get("total_reactions", 0) or 0),
        "comments": int(latest.get("comments", 0) or 0),
        "reposts": int(latest.get("reposts", 0) or 0),
        "reaction_breakdown": latest.get("reactions", {}),
        "snapshot_count": len(snapshots),
        "all_snapshots": snapshots,
        "source": "performance-data",
    }


def parse_csv(path: Path) -> list[dict[str, Any]]:
    """Parse a LinkedIn analytics CSV export. Returns list of dicts."""
    out: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            post = row.get("Post content", "").strip()
            url = row.get("URL", "").strip()
            if not post or not url:
                continue
            out.append({
                "post_id": "",  # CSV doesn't expose stable id
                "url": url,
                "posted_at": row.get("Date posted", "").strip(),
                "post_text": post,
                "latest_snapshot_date": row.get("Date posted", "").strip(),
                "reactions": int(row.get("total_reactions:", "0") or "0"),
                "comments": int(row.get("comments:", "0") or "0"),
                "reposts": int(row.get("reposts:", "0") or "0"),
                "reaction_breakdown": {
                    "LIKE": int(row.get("like:", "0") or "0"),
                    "SUPPORT": int(row.get("support:", "0") or "0"),
                    "LOVE": int(row.get("love:", "0") or "0"),
                    "INSIGHT": int(row.get("insight:", "0") or "0"),
                    "CELEBRATE": int(row.get("celebrate:", "0") or "0"),
                },
                "snapshot_count": 1,
                "all_snapshots": [],
                "source": "csv",
            })
    return out


def enrich_entry(base: dict[str, Any]) -> dict[str, Any]:
    """Add hook/style/CTA classifications + specifics + composite engagement."""
    post = base["post_text"]
    reactions = base["reactions"]
    comments = base["comments"]
    reposts = base["reposts"]

    # Composite weight: comments > reposts > reactions for intent signal
    composite = reactions + (comments * 3) + (reposts * 5)

    return {
        "url": base["url"],
        "post_id": base["post_id"],
        "date": base["posted_at"][:10] if base["posted_at"] else "",
        "source": base["source"],
        "first_line": post.split("\n")[0][:120] if post else "",
        "length_chars": len(post),
        "hook_pattern": classify_hook(post),
        "style": classify_style(post),
        "ctas": classify_cta(post),
        "specifics": count_specifics(post),
        "metrics": {
            "reactions": reactions,
            "comments": comments,
            "reposts": reposts,
            "reaction_breakdown": base["reaction_breakdown"],
            "composite_engagement": composite,
            "snapshot_count": base["snapshot_count"],
            "latest_snapshot_date": base["latest_snapshot_date"],
        },
        "post_full": post,
    }


def normalize_url(url: str) -> str:
    """Strip query string + trailing slashes for dedupe key."""
    clean = url.split("?")[0].rstrip("/")
    return clean.lower()


def merge_by_url(csv_entries: list[dict[str, Any]], perf_entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Dedupe. performance-data wins when URL collision."""
    seen: dict[str, dict[str, Any]] = {}
    # Perf first — it's the authoritative current source
    for e in perf_entries:
        key = normalize_url(e["url"])
        seen[key] = e
    # CSV fills in anything perf doesn't have (older posts outside the 25-post window)
    for e in csv_entries:
        key = normalize_url(e["url"])
        if key not in seen:
            seen[key] = e
    return list(seen.values())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", help="Optional LinkedIn analytics CSV export path")
    ap.add_argument("--perf-dir", default="performance-data",
                    help="Directory of Apify post markdowns (default: performance-data)")
    args = ap.parse_args()

    repo = Path(__file__).parent.parent
    perf_dir = repo / args.perf_dir
    history_dir = repo / "history"
    config_dir = repo / "config"
    history_dir.mkdir(exist_ok=True)

    # Parse Apify markdowns
    perf_raw: list[dict[str, Any]] = []
    for md in sorted(perf_dir.glob("post-*.md")):
        parsed = parse_performance_md(md)
        if parsed:
            perf_raw.append(parsed)
    perf_entries = [enrich_entry(e) for e in perf_raw]
    print(f"[merge] performance-data: {len(perf_entries)} posts parsed", file=sys.stderr)

    # Parse CSV if provided
    csv_entries: list[dict[str, Any]] = []
    if args.csv:
        csv_path = Path(args.csv)
        if not csv_path.is_file():
            print(f"[merge] CSV not found: {csv_path}", file=sys.stderr)
            sys.exit(1)
        csv_raw = parse_csv(csv_path)
        csv_entries = [enrich_entry(e) for e in csv_raw]
        print(f"[merge] csv: {len(csv_entries)} posts parsed", file=sys.stderr)

    merged = merge_by_url(csv_entries, perf_entries)
    print(f"[merge] unique posts after dedupe: {len(merged)}", file=sys.stderr)

    # Sort newest first
    merged.sort(key=lambda e: e.get("date", ""), reverse=True)

    # Write JSONL
    jsonl_path = history_dir / "linkedin-posts-history.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as out:
        for e in merged:
            out.write(json.dumps(e, ensure_ascii=False) + "\n")

    # Write patterns JSON
    summary = summarize_patterns(merged)
    json_path = config_dir / "linkedin-patterns.json"
    json_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    # Write markdown for /write-posts prompt
    md_path = config_dir / "aayush-linkedin-patterns.md"
    md_path.write_text(render_markdown(summary, merged), encoding="utf-8")

    print(f"[merge] wrote {jsonl_path}")
    print(f"[merge] wrote {json_path}")
    print(f"[merge] wrote {md_path}")
    print("", file=sys.stderr)
    print("Top 5 posts across all sources:", file=sys.stderr)
    for e in merged[:5] if not merged[0].get("metrics") else sorted(merged, key=lambda x: -x["metrics"]["composite_engagement"])[:5]:
        m = e.get("metrics", {})
        print(f"  {e.get('date','?')} | {e.get('hook_pattern','?')} | {e.get('style','?')} | engagement={m.get('composite_engagement','?')} | {e.get('source','?')}", file=sys.stderr)
        print(f"    {e.get('first_line','')[:80]}", file=sys.stderr)


if __name__ == "__main__":
    main()
