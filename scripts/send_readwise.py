#!/usr/bin/env python3
"""Send a brief to Readwise Reader via API v3.

Replaces the email-to-Readwise-inbox flow. Cleaner title (no PDB prefix),
proper HTML rendering of markdown headers/block quotes/bold/links.

Usage:
    python3 scripts/send_readwise.py <path-to-brief.md> <github-blob-url>

Required env:
    READWISE_TOKEN   - get at https://readwise.io/access_token

Exits 0 on success, 1 on failure. Non-zero exit = pipeline fails the Deliver step.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path


READER_API_URL = "https://readwise.io/api/v3/save/"


def extract_title(md: str) -> str:
    """Return the first H1 line stripped of the '# ' prefix.
    The H1 IS the title — no PDB/date prefix, no truncation."""
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    # Fallback: first non-empty line
    for line in md.splitlines():
        if line.strip():
            return line.strip()[:200]
    return "Daily brief"


def md_to_html(md: str) -> str:
    """Convert markdown to HTML. Prefer the `markdown` library if available,
    else use a minimal fallback that handles our brief's structure."""
    try:
        import markdown  # type: ignore
        return markdown.markdown(
            md,
            extensions=["extra", "fenced_code", "tables", "nl2br", "sane_lists"],
        )
    except ImportError:
        return _fallback_md_to_html(md)


def _fallback_md_to_html(md: str) -> str:
    """Minimal markdown->HTML converter for when the `markdown` lib isn't installed.
    Handles: H1-H3, paragraphs, bold, italic, inline code, links, block quotes,
    dash lists, horizontal rules."""
    lines = md.split("\n")
    out: list[str] = []
    in_list = False
    in_blockquote = False
    para: list[str] = []

    def flush_para() -> None:
        if para:
            out.append("<p>" + " ".join(para).strip() + "</p>")
            para.clear()

    def inline(s: str) -> str:
        # Links [text](url)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        # Bold **text**
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        # Italic *text* (only single-asterisk, not already bold)
        s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
        # Inline code `text`
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        return s

    for line in lines:
        stripped = line.strip()

        # Horizontal rule
        if re.match(r"^---+$", stripped):
            flush_para()
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("<hr>")
            continue

        # Headings
        h_match = re.match(r"^(#{1,3})\s+(.+)$", stripped)
        if h_match:
            flush_para()
            if in_list:
                out.append("</ul>")
                in_list = False
            level = len(h_match.group(1))
            out.append(f"<h{level}>{inline(h_match.group(2))}</h{level}>")
            continue

        # Block quote
        if stripped.startswith(">"):
            flush_para()
            content = stripped.lstrip(">").strip()
            if not in_blockquote:
                out.append("<blockquote>")
                in_blockquote = True
            out.append(f"<p>{inline(content)}</p>")
            continue
        else:
            if in_blockquote:
                out.append("</blockquote>")
                in_blockquote = False

        # Dash list items
        if re.match(r"^-\s+", stripped):
            flush_para()
            if not in_list:
                out.append("<ul>")
                in_list = True
            content = stripped[2:].strip()
            out.append(f"<li>{inline(content)}</li>")
            continue
        else:
            if in_list:
                out.append("</ul>")
                in_list = False

        # Blank line
        if not stripped:
            flush_para()
            continue

        # Regular paragraph content
        para.append(inline(stripped))

    flush_para()
    if in_list:
        out.append("</ul>")
    if in_blockquote:
        out.append("</blockquote>")
    return "\n".join(out)


def save_to_reader(
    *,
    token: str,
    url: str,
    html: str,
    title: str,
    tags: list[str],
) -> dict:
    """POST to Readwise Reader. Returns parsed response dict or raises."""
    payload = {
        "url": url,
        "html": html,
        "title": title,
        "author": "Presidential Briefing",
        "category": "article",
        "location": "new",
        "saved_using": "presidential-briefing",
        "tags": tags,
        "should_clean_html": True,
    }
    req = urllib.request.Request(
        READER_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Token {token}",
            "Content-Type": "application/json",
            "User-Agent": "presidential-briefing/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Readwise API HTTP {e.code}: {body}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Readwise API network error: {e.reason}") from e

    if status not in (200, 201):
        raise RuntimeError(f"Readwise API HTTP {status}: {body}")

    return json.loads(body) if body else {}


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: send_readwise.py <brief.md path> <github blob url>", file=sys.stderr)
        sys.exit(2)

    brief_path = Path(sys.argv[1])
    github_url = sys.argv[2]

    token = os.environ.get("READWISE_TOKEN")
    if not token:
        print("[readwise] READWISE_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    if not brief_path.is_file():
        print(f"[readwise] brief not found: {brief_path}", file=sys.stderr)
        sys.exit(1)

    md = brief_path.read_text(encoding="utf-8")
    title = extract_title(md)
    html = md_to_html(md)

    # Derive date tag from the filename path (expects workspace/YYYY-MM-DD/brief.md)
    date_tag = ""
    for part in brief_path.parts:
        if re.match(r"^\d{4}-\d{2}-\d{2}$", part):
            date_tag = part
            break
    tags = ["ai-brief", "daily"]
    if date_tag:
        tags.append(date_tag)

    try:
        result = save_to_reader(
            token=token,
            url=github_url,
            html=html,
            title=title,
            tags=tags,
        )
    except RuntimeError as e:
        print(f"[readwise] send failed: {e}", file=sys.stderr)
        sys.exit(1)

    doc_id = result.get("id", "")
    doc_url = result.get("url", "")
    print(f"[readwise] saved: id={doc_id} url={doc_url} title='{title}'")


if __name__ == "__main__":
    main()
