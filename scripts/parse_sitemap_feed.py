#!/usr/bin/env python3
"""Sitemap-based feed scraper — rescue for sites without valid RSS.

Reads sources.csv for rows where access_method=sitemap. For each:
    1. Fetch sitemap.xml (always public; search engines need it)
    2. Filter URLs by `feed_filter` (e.g., /blog/ or /p/)
    3. Keep URLs with <lastmod> within last 24h
    4. Fetch each post page (Googlebot UA if feed_ua=googlebot) and extract
       <title> + <meta name="description">
    5. Emit JSONL items in the same shape as parse_rss.py

Usage:
    python3 scripts/parse_sitemap_feed.py --csv config/sources.csv --stats-json /path/to/stats.json

Output: one JSON object per line on stdout (same shape as parse_rss.py output)
    {"title": "...", "url": "...", "summary": "...", "source": "<domain>", "type": "rss", "published": "..."}

Stderr + stats-json: per-source + per-URL diagnostics.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse

SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
GOOGLEBOT_UA = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
DEFAULT_UA = "presidential-briefing/1.0"
PAGE_FETCH_TIMEOUT = 10
SITEMAP_FETCH_TIMEOUT = 15
MAX_URLS_PER_SOURCE = 10  # safety cap — sitemaps can have thousands

TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
META_DESC_RE = re.compile(
    r'<meta[^>]+(?:name|property)="(?:description|og:description)"[^>]+content="([^"]+)"',
    re.IGNORECASE,
)


def http_get(url: str, ua: str, timeout: int) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def extract_sitemap_entries(sitemap_url: str, url_filter: str, cutoff: datetime) -> tuple[list[tuple[str, str]], str | None]:
    """Return (entries_within_24h, error). entries = [(lastmod, loc), ...] sorted newest first."""
    try:
        data = http_get(sitemap_url, DEFAULT_UA, SITEMAP_FETCH_TIMEOUT)
    except Exception as e:
        return [], f"sitemap_fetch_failed: {e}"

    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        return [], f"sitemap_parse_failed: {e}"

    entries: list[tuple[str, str]] = []
    for u in root.findall("sm:url", SITEMAP_NS):
        loc_el = u.find("sm:loc", SITEMAP_NS)
        lm_el = u.find("sm:lastmod", SITEMAP_NS)
        if loc_el is None or not loc_el.text:
            continue
        loc = loc_el.text.strip()
        if url_filter and url_filter not in loc:
            continue
        lastmod_raw = lm_el.text.strip() if lm_el is not None and lm_el.text else ""
        # Parse lastmod — sitemaps typically use ISO 8601
        try:
            lastmod_dt = datetime.fromisoformat(lastmod_raw.replace("Z", "+00:00"))
        except ValueError:
            # Some sitemaps only have date. Treat as end of that day.
            try:
                lastmod_dt = datetime.fromisoformat(lastmod_raw[:10]).replace(tzinfo=timezone.utc)
                lastmod_dt = lastmod_dt + timedelta(hours=23, minutes=59)
            except ValueError:
                continue  # unparseable, skip

        # Normalize to UTC-aware for safe comparison
        if lastmod_dt.tzinfo is None:
            lastmod_dt = lastmod_dt.replace(tzinfo=timezone.utc)
        if lastmod_dt < cutoff:
            continue
        entries.append((lastmod_dt.isoformat(), loc))

    entries.sort(reverse=True)  # newest first
    return entries, None


def extract_page_metadata(html: bytes) -> tuple[str, str]:
    """Return (title, summary) from HTML. Empty strings if not found."""
    try:
        text = html.decode("utf-8", errors="replace")
    except Exception:
        return "", ""

    title_m = TITLE_RE.search(text)
    title = ""
    if title_m:
        title = re.sub(r"\s+", " ", title_m.group(1)).strip()
        # Decode common HTML entities
        title = (
            title.replace("&amp;", "&")
            .replace("&#x27;", "'")
            .replace("&quot;", '"')
            .replace("&lt;", "<")
            .replace("&gt;", ">")
        )

    desc_m = META_DESC_RE.search(text)
    summary = ""
    if desc_m:
        summary = re.sub(r"\s+", " ", desc_m.group(1)).strip()[:500]
        summary = (
            summary.replace("&amp;", "&")
            .replace("&#x27;", "'")
            .replace("&quot;", '"')
            .replace("&lt;", "<")
            .replace("&gt;", ">")
        )

    return title, summary


def scrape_source(row: dict, out) -> dict:
    """Scrape one sitemap source. Emit items to `out`. Return per-source summary."""
    name = row.get("name", "").strip()
    sitemap_url = (row.get("feed_url") or "").strip()
    url_filter = (row.get("feed_filter") or "").strip()
    ua_tag = (row.get("feed_ua") or "").strip().lower()
    ua = GOOGLEBOT_UA if ua_tag == "googlebot" else DEFAULT_UA

    result = {
        "name": name,
        "sitemap_url": sitemap_url,
        "filter": url_filter,
        "ua": ua_tag or "default",
        "status": "ok",
        "error": None,
        "urls_in_window": 0,
        "items_scraped": 0,
        "page_errors": [],
    }

    cutoff = datetime.now(timezone.utc) - timedelta(hours=24)
    entries, err = extract_sitemap_entries(sitemap_url, url_filter, cutoff)
    if err:
        result["status"] = "sitemap_error"
        result["error"] = err
        print(f"[parse_sitemap] {name}: {err}", file=sys.stderr)
        return result

    result["urls_in_window"] = len(entries)
    if not entries:
        return result

    # Cap to top N most recent so we never hammer a site
    for lastmod_iso, post_url in entries[:MAX_URLS_PER_SOURCE]:
        try:
            html = http_get(post_url, ua, PAGE_FETCH_TIMEOUT)
        except Exception as e:
            result["page_errors"].append({"url": post_url, "error": str(e)[:150]})
            continue

        title, summary = extract_page_metadata(html)
        if not title:
            result["page_errors"].append({"url": post_url, "error": "no_title_extracted"})
            continue

        domain = urlparse(post_url).netloc
        item = {
            "title": title,
            "url": post_url,
            "summary": summary,
            "source": domain,
            "type": "rss",  # downstream schema parity with RSS items
            "published": lastmod_iso,
        }
        print(json.dumps(item, ensure_ascii=False), file=out)
        result["items_scraped"] += 1

    return result


def iter_sitemap_rows(csv_path: str):
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row.get("access_method") or "").strip() != "sitemap":
                continue
            yield row


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="Path to sources.csv")
    ap.add_argument("--stats-json", help="Write per-source stats to this path")
    args = ap.parse_args()

    rows = list(iter_sitemap_rows(args.csv))
    if not rows:
        print("[parse_sitemap] no sitemap-access sources in CSV", file=sys.stderr)
        if args.stats_json:
            with open(args.stats_json, "w") as f:
                json.dump({"sources_total": 0, "per_source": []}, f)
        return

    per_source: list[dict] = []
    total_items = 0
    for row in rows:
        summary = scrape_source(row, sys.stdout)
        per_source.append(summary)
        total_items += summary["items_scraped"]
        print(
            f"[parse_sitemap] {summary['name']}: {summary['items_scraped']} items "
            f"({summary['urls_in_window']} urls in 24h window, status={summary['status']})",
            file=sys.stderr,
        )

    sources_ok = sum(1 for s in per_source if s["status"] == "ok")
    sources_failed = len(per_source) - sources_ok
    print(
        f"[parse_sitemap] sources_total={len(per_source)} sources_ok={sources_ok} "
        f"sources_failed={sources_failed} items_total={total_items}",
        file=sys.stderr,
    )

    if args.stats_json:
        with open(args.stats_json, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "sources_total": len(per_source),
                    "sources_ok": sources_ok,
                    "sources_failed": sources_failed,
                    "items_total": total_items,
                    "cutoff_utc": (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat(),
                    "per_source": per_source,
                },
                f,
                indent=2,
                ensure_ascii=False,
            )


if __name__ == "__main__":
    main()
