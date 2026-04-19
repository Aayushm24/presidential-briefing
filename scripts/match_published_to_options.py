#!/usr/bin/env python3
"""Attribute each scraped LinkedIn post to a generated /write-posts option.

For every post in performance-data/ not yet attributed, compute Jaccard
similarity of 3-gram word shingles (first 3 lines only — hook structure is
what matters) against every option in workspace/YYYY-MM-DD/posts.json from
the last 14 days.

Buckets:
    jaccard >= 0.6   → variant_of        (clearly the option, adapted)
    0.25–0.59        → inspired_by        (same hook shape, different execution)
    < 0.25           → organic            (Aayush wrote it fresh)

Output: history/option-pickups.jsonl (append-only, one line per attributed post).

Run from the repo root:
    python3 scripts/match_published_to_options.py
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
from rebuild_linkedin_history import parse_performance_md  # type: ignore


LOOKBACK_DAYS = 14
SHINGLE_N = 3
VARIANT_THRESHOLD = 0.60
INSPIRED_THRESHOLD = 0.25
WORD_RE = re.compile(r"[a-z0-9]+")


def shingles(text: str, n: int = SHINGLE_N, max_lines: int = 3) -> set[tuple[str, ...]]:
    """N-gram word shingles from the first `max_lines` non-empty lines."""
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()][:max_lines]
    words = WORD_RE.findall(" ".join(lines).lower())
    if len(words) < n:
        return {tuple(words)} if words else set()
    return {tuple(words[i : i + n]) for i in range(len(words) - n + 1)}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def load_existing_pickups(path: Path) -> dict[str, dict[str, Any]]:
    """Return {post_url: entry}. Latest-wins if duplicates."""
    out: dict[str, dict[str, Any]] = {}
    if not path.is_file():
        return out
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            url = entry.get("post_url", "")
            if url:
                out[url] = entry
    return out


def parse_posted_date(posted_at: str) -> date | None:
    if not posted_at:
        return None
    try:
        return datetime.fromisoformat(posted_at.replace("Z", "+00:00")).date()
    except ValueError:
        try:
            return date.fromisoformat(posted_at[:10])
        except ValueError:
            return None


def load_candidate_options(workspace_dir: Path, around: date, window_days: int) -> list[dict[str, Any]]:
    """Collect every option from posts.json files within window_days of `around`."""
    candidates: list[dict[str, Any]] = []
    if not workspace_dir.is_dir():
        return candidates
    lo = around - timedelta(days=window_days)
    hi = around + timedelta(days=1)  # allow same-day publish after brief
    for day_dir in sorted(workspace_dir.iterdir()):
        if not day_dir.is_dir():
            continue
        try:
            day = date.fromisoformat(day_dir.name)
        except ValueError:
            continue
        if not (lo <= day <= hi):
            continue
        posts_path = day_dir / "posts.json"
        if not posts_path.is_file():
            continue
        try:
            data = json.loads(posts_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for opt in data.get("options", []):
            candidates.append({
                "brief_date": day_dir.name,
                "option": opt.get("option"),
                "template": opt.get("template", ""),
                "hook_pattern": opt.get("hook_pattern", ""),
                "post": opt.get("post", ""),
            })
    return candidates


def attribute(post_text: str, candidates: list[dict[str, Any]]) -> dict[str, Any]:
    """Return best-match attribution for this published post."""
    if not candidates:
        return {"attribution": "organic", "reason": "no candidate options in window"}

    post_sh = shingles(post_text)
    if not post_sh:
        return {"attribution": "organic", "reason": "post too short to shingle"}

    best = {"jaccard": 0.0}
    for cand in candidates:
        j = jaccard(post_sh, shingles(cand["post"]))
        if j > best["jaccard"]:
            best = {
                "jaccard": round(j, 3),
                "brief_date": cand["brief_date"],
                "option": cand["option"],
                "source_template": cand["template"],
                "source_hook": cand["hook_pattern"],
            }

    if best["jaccard"] >= VARIANT_THRESHOLD:
        return {"attribution": "variant_of", **best}
    if best["jaccard"] >= INSPIRED_THRESHOLD:
        return {"attribution": "inspired_by", **best}
    return {"attribution": "organic", "best_jaccard": best["jaccard"]}


def main() -> None:
    repo = Path(__file__).parent.parent
    perf_dir = repo / "performance-data"
    workspace_dir = repo / "workspace"
    history_dir = repo / "history"
    history_dir.mkdir(exist_ok=True)
    pickups_path = history_dir / "option-pickups.jsonl"

    existing = load_existing_pickups(pickups_path)
    print(f"[match] loaded {len(existing)} existing attributions", file=sys.stderr)

    new_entries: list[dict[str, Any]] = []
    for md in sorted(perf_dir.glob("post-*.md")):
        parsed = parse_performance_md(md)
        if not parsed:
            continue
        url = parsed["url"]
        if url in existing:
            continue  # already attributed

        posted = parse_posted_date(parsed["posted_at"])
        if posted is None:
            print(f"[match] skip {md.name}: unparseable posted_at", file=sys.stderr)
            continue

        candidates = load_candidate_options(workspace_dir, posted, LOOKBACK_DAYS)
        attr = attribute(parsed["post_text"], candidates)

        entry = {
            "post_url": url,
            "post_id": parsed["post_id"],
            "published_date": posted.isoformat(),
            "first_line": parsed["post_text"].split("\n")[0][:120] if parsed["post_text"] else "",
            **attr,
        }
        new_entries.append(entry)

    if new_entries:
        with pickups_path.open("a", encoding="utf-8") as f:
            for e in new_entries:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")

    buckets = {"variant_of": 0, "inspired_by": 0, "organic": 0}
    for e in new_entries:
        buckets[e.get("attribution", "organic")] = buckets.get(e.get("attribution", "organic"), 0) + 1

    print(
        f"[match] new attributions: {len(new_entries)} "
        f"(variant_of={buckets['variant_of']} inspired_by={buckets['inspired_by']} organic={buckets['organic']})",
        file=sys.stderr,
    )
    print(f"[match] wrote {pickups_path}")


if __name__ == "__main__":
    main()
