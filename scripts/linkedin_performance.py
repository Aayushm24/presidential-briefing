#!/usr/bin/env python3
"""Snapshot LinkedIn post engagement via Apify and upsert per-post markdown files.

Usage:
    APIFY_TOKEN=xxx \\
    LINKEDIN_PROFILE_URL=https://www.linkedin.com/in/aayush-maheshwari/ \\
    python3 scripts/linkedin_performance.py

    # Preview without writing:
    python3 scripts/linkedin_performance.py --dry-run

Env:
    APIFY_TOKEN           Apify API token (required).
    LINKEDIN_PROFILE_URL  Profile to scrape (required).
    APIFY_ACTOR_ID        Actor ID (default: A3cAPGpwBEG8RJwse — harvestapi/linkedin-profile-posts).
    MAX_POSTS             Number of latest posts to fetch (default: 25).
    OUTPUT_DIR            Output directory (default: performance-data).

Output: one markdown file per post at OUTPUT_DIR/post-<id>.md.
Each file has metadata + a Snapshots JSON block that grows by one entry per run.

Stderr stats line:
    [linkedin-performance] posts_fetched=25 files_created=3 files_updated=22
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests  # type: ignore
except ImportError:
    print(
        "[linkedin-performance] requests not installed. Run: pip install requests",
        file=sys.stderr,
    )
    sys.exit(2)


APIFY_BASE = "https://api.apify.com/v2"
SNAPSHOT_BLOCK_RE = re.compile(
    r"## Snapshots\s*\n+```json\s*\n(?P<json>.*?)\n```",
    re.DOTALL,
)


def call_apify(actor_id: str, token: str, profile_url: str, max_posts: int) -> list[dict]:
    """Fire the actor synchronously and return the dataset items."""
    url = f"{APIFY_BASE}/acts/{actor_id}/run-sync-get-dataset-items"
    resp = requests.post(
        url,
        params={"token": token, "timeout": 300},
        json={"profileUrls": [profile_url], "maxPosts": max_posts},
        timeout=310,
    )
    if resp.status_code not in (200, 201):
        print(
            f"[linkedin-performance] apify error: {resp.status_code} {resp.text[:200]}",
            file=sys.stderr,
        )
        sys.exit(1)
    items = resp.json()
    if not isinstance(items, list):
        print(
            f"[linkedin-performance] unexpected apify response shape: {type(items).__name__}",
            file=sys.stderr,
        )
        sys.exit(1)
    return items


def snapshot_from_post(post: dict, snapshot_date: str) -> dict:
    """Extract a single day's snapshot from an Apify post record.

    Fails loud if the actor schema drifts — we'd rather break the workflow
    than silently write empty snapshots.
    """
    engagement = post.get("engagement")
    if not isinstance(engagement, dict):
        raise ValueError(f"post {post.get('id')} missing engagement object")
    if "likes" not in engagement:
        raise ValueError(f"post {post.get('id')} missing engagement.likes")

    reactions = {}
    for r in engagement.get("reactions") or []:
        rtype = r.get("type")
        count = r.get("count")
        if rtype and isinstance(count, int):
            reactions[rtype] = count

    return {
        "snapshot_date": snapshot_date,
        "total_reactions": engagement.get("likes", 0),
        "comments": engagement.get("comments", 0),
        "reposts": engagement.get("shares", 0),
        "reactions": reactions,
    }


def parse_existing_snapshots(path: Path) -> list[dict]:
    """Read existing Snapshots array from a post file. Returns [] if absent or unparseable."""
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    match = SNAPSHOT_BLOCK_RE.search(text)
    if not match:
        return []
    try:
        data = json.loads(match.group("json"))
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def blockquote(content: str) -> str:
    """Prefix every line of content with '> ' for markdown blockquote."""
    return "\n".join(f"> {line}" if line else ">" for line in content.split("\n"))


def title_from_content(content: str, limit: int = 80) -> str:
    """Build a file-header title from the first line of content."""
    first = content.strip().split("\n", 1)[0].strip()
    if len(first) <= limit:
        return first
    return first[: limit - 1].rstrip() + "…"


def render_post_file(post: dict, snapshots: list[dict]) -> str:
    """Produce the full markdown body for a post file."""
    title = title_from_content(post.get("content", "") or "(no content)")
    snapshots_json = json.dumps(snapshots, indent=2, ensure_ascii=False)
    return (
        f"# {title}\n\n"
        f"**URL**: {post.get('linkedinUrl', '')}\n"
        f"**Post ID**: {post.get('id', '')}\n"
        f"**Posted**: {(post.get('postedAt') or {}).get('date', '')}\n\n"
        "## Content\n\n"
        f"{blockquote(post.get('content', '') or '')}\n\n"
        "## Snapshots\n\n"
        "```json\n"
        f"{snapshots_json}\n"
        "```\n"
    )


def upsert_post_file(
    post: dict, output_dir: Path, snapshot_date: str, dry_run: bool
) -> str:
    """Write or update a post file. Returns 'created', 'updated', or 'dry-run'."""
    post_id = post.get("id")
    if not post_id:
        raise ValueError("post missing id")

    path = output_dir / f"post-{post_id}.md"
    snapshots = parse_existing_snapshots(path)
    new_snap = snapshot_from_post(post, snapshot_date)

    if snapshots and snapshots[-1].get("snapshot_date") == snapshot_date:
        snapshots[-1] = new_snap
    else:
        snapshots.append(new_snap)

    status = "created" if not path.exists() else "updated"

    verb = "create" if status == "created" else "update"
    if dry_run:
        print(f"[linkedin-performance] DRY_RUN would {verb}: {path}", file=sys.stderr)
        return "dry-run"

    path.write_text(render_post_file(post, snapshots), encoding="utf-8")
    return status


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args()

    token = os.environ.get("APIFY_TOKEN")
    profile_url = os.environ.get("LINKEDIN_PROFILE_URL")
    actor_id = os.environ.get("APIFY_ACTOR_ID", "A3cAPGpwBEG8RJwse")
    max_posts = int(os.environ.get("MAX_POSTS", "25"))
    output_dir = Path(os.environ.get("OUTPUT_DIR", "performance-data"))

    if not token:
        print("[linkedin-performance] APIFY_TOKEN not set", file=sys.stderr)
        return 2
    if not profile_url:
        print("[linkedin-performance] LINKEDIN_PROFILE_URL not set", file=sys.stderr)
        return 2

    output_dir.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    posts = call_apify(actor_id, token, profile_url, max_posts)
    snapshot_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    created = updated = 0
    for post in posts:
        try:
            result = upsert_post_file(post, output_dir, snapshot_date, args.dry_run)
        except ValueError as e:
            print(f"[linkedin-performance] skip: {e}", file=sys.stderr)
            continue
        if result == "created":
            created += 1
        elif result == "updated":
            updated += 1

    elapsed = time.time() - t0
    print(
        f"[linkedin-performance] posts_fetched={len(posts)} "
        f"files_created={created} files_updated={updated} "
        f"dry_run={int(args.dry_run)} elapsed_s={elapsed:.1f}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
