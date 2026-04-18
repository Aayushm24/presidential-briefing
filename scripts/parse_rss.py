#!/usr/bin/env python3
"""Parse an RSS/Atom feed URL and output JSONL of items from the last 24 hours.

Usage:
    python3 scripts/parse_rss.py <feed_url>

Output (one JSON object per line on stdout):
    {"title": "...", "url": "...", "summary": "...", "source": "<domain>", "type": "rss", "published": "..."}

Skips items with no parseable date or older than 24h. Strips HTML. Cap summary at 500 chars.
"""

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


def parse_feed(url: str):
    domain = urlparse(url).netloc
    cutoff = datetime.now(timezone.utc) - timedelta(hours=24)

    try:
        feed = feedparser.parse(url, request_headers={"User-Agent": "presidential-briefing/1.0"})
    except Exception as e:
        print(f"[parse_rss] failed to fetch {url}: {e}", file=sys.stderr)
        return

    if feed.bozo and not feed.entries:
        print(f"[parse_rss] malformed feed {url}: {feed.bozo_exception}", file=sys.stderr)
        return

    for entry in feed.entries:
        # Date extraction — try published_parsed, then updated_parsed
        published_tuple = (
            getattr(entry, "published_parsed", None)
            or getattr(entry, "updated_parsed", None)
        )
        if not published_tuple:
            continue

        try:
            published_dt = datetime.fromtimestamp(time.mktime(published_tuple), tz=timezone.utc)
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

        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    parse_feed(sys.argv[1])
