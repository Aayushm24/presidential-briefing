#!/usr/bin/env python3
"""Parse RSS/Atom feeds and output items from the last 24 hours.

Two modes:

    # Single feed (legacy):
    python3 scripts/parse_rss.py <feed_url>

    # All feeds from sources.csv (preferred):
    python3 scripts/parse_rss.py --csv config/sources.csv

Output: one JSON object per line on stdout.
    {"title": "...", "url": "...", "summary": "...", "source": "<domain>", "type": "rss", "published": "..."}

Skips items with no parseable date, older than 24h, or without a title.
Strips HTML. Caps summary at 500 chars.

Also emits a stats line on stderr:
    [parse_rss] feeds_total=41 feeds_processed=38 feeds_failed=3 items_returned=47
"""

import argparse
import csv
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse

try:
    import feedparser  # type: ignore
except ImportError:
    print(
        "[parse_rss] feedparser not installed. Run: pip install feedparser",
        file=sys.stderr,
    )
    sys.exit(2)


def strip_html(s: str) -> str:
    if not s:
        return ""
    s = re.sub(r"<script[^>]*>[^<]*</script>", " ", s, flags=re.IGNORECASE)
    s = re.sub(r"<style[^>]*>[^<]*</style>", " ", s, flags=re.IGNORECASE)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_one_feed(url: str, cutoff: datetime, out) -> tuple[int, bool]:
    """Parse a single feed. Returns (items_emitted, success)."""
    try:
        feed = feedparser.parse(
            url, request_headers={"User-Agent": "presidential-briefing/1.0"}
        )
    except Exception as e:
        print(f"[parse_rss] failed to fetch {url}: {e}", file=sys.stderr)
        return 0, False

    if feed.bozo and not feed.entries:
        print(
            f"[parse_rss] malformed feed {url}: {feed.bozo_exception}",
            file=sys.stderr,
        )
        return 0, False

    domain = urlparse(url).netloc
    count = 0
    for entry in feed.entries:
        published_tuple = (
            getattr(entry, "published_parsed", None)
            or getattr(entry, "updated_parsed", None)
        )
        if not published_tuple:
            continue

        try:
            published_dt = datetime.fromtimestamp(
                time.mktime(published_tuple), tz=timezone.utc
            )
        except (ValueError, OverflowError):
            continue

        if published_dt < cutoff:
            continue

        title = strip_html(getattr(entry, "title", "")).strip()
        if not title:
            continue

        link = getattr(entry, "link", "").strip()
        summary_raw = (
            getattr(entry, "summary", "")
            or getattr(entry, "description", "")
            or ""
        )
        summary = strip_html(summary_raw)[:500]

        item = {
            "title": title,
            "url": link,
            "summary": summary,
            "source": domain,
            "type": "rss",
            "published": published_dt.isoformat(),
        }
        print(json.dumps(item, ensure_ascii=False), file=out)
        count += 1

    return count, True


def iter_feeds_from_csv(csv_path: str):
    """Yield feed_url strings from sources.csv where access_method == 'rss'."""
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("access_method", "").strip() != "rss":
                continue
            feed_url = (row.get("feed_url") or "").strip()
            if not feed_url:
                continue
            yield feed_url


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", help="Path to sources.csv. Iterates every RSS row.")
    ap.add_argument(
        "url",
        nargs="?",
        help="Single feed URL (legacy mode). Mutually exclusive with --csv.",
    )
    args = ap.parse_args()

    if not args.csv and not args.url:
        ap.print_help(sys.stderr)
        sys.exit(2)
    if args.csv and args.url:
        print("--csv and url are mutually exclusive", file=sys.stderr)
        sys.exit(2)

    cutoff = datetime.now(timezone.utc) - timedelta(hours=24)
    feeds = list(iter_feeds_from_csv(args.csv)) if args.csv else [args.url]

    total_processed = 0
    total_failed = 0
    total_items = 0

    for feed_url in feeds:
        count, ok = parse_one_feed(feed_url, cutoff, sys.stdout)
        total_items += count
        if ok:
            total_processed += 1
        else:
            total_failed += 1

    print(
        f"[parse_rss] feeds_total={len(feeds)} feeds_processed={total_processed} "
        f"feeds_failed={total_failed} items_returned={total_items}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
