#!/usr/bin/env python3
"""Ingest Aayush's LinkedIn performance CSV → structured JSONL + patterns summary.

Reads CSV exported from LinkedIn analytics (or the performance tracker sheet).
Produces:
  - history/engagement.jsonl — one line per post with derived style/hook/formula tags
  - config/linkedin-patterns.json — structured stats (top hooks/styles/CTAs by engagement)
  - config/aayush-linkedin-patterns.md — human-readable patterns for the writing prompt

Usage:
    python3 scripts/ingest_linkedin_csv.py <path-to-csv>

CSV schema (from LinkedIn export):
    Date posted, Time, URL, Post content, total_reactions:, like:, support:, love:,
    insight:, celebrate:, comments:, reposts:
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


# ============================================================
# Classification rules — mirror write-posts/SKILL.md taxonomy
# ============================================================

HOOK_PATTERNS = {
    # Pattern A: Contrarian Truth
    "A": [
        r"^\w+\s+(isn't|is\s+not|don't|doesn't)\s+\w+",  # "AI isn't your competitive advantage"
        r"but\s+\d+%?\s+are\s+just",  # "but 99% are just chatgpt wrappers"
        r"every\s+startup\s+says",
        r"\w+\s+is\s+a\s+commodity",
        r"your\s+.+\s+(isn't|is\s+not)\s+a",
    ],
    # Pattern B: Identity / Confession
    "B": [
        r"^[iI]['\u2019]ve\s+been",
        r"^[iI]\s+(don't|do\s+not)\s+celebrate",
        r"^[iI]\s+(finally|discovered|realized|found)",
        r"^[iI]['\u2019]m\s+(the\s+most|convinced|terrible|worse)",
        r"^[Ll]ast\s+week,?\s+(my|i)",
    ],
    # Pattern C: Absurd Comparison
    "C": [
        r"^[Mm]y\s+(mom|dad|kid|cat|dog)\s+",
        r"(cat|dog|kid|teenager)\s+with\s+(ChatGPT|Instagram|AI)",
        r"^[Ii]['\u2019]m\s+(too|really)\s+\w+\s+to\s+",
    ],
    # Pattern D: Time Bomb
    "D": [
        r"^[iI]\s+(quit|posted|was)\s+\d?\s?\w*",
        r"^\d+\s+(days?|weeks?|months?|years?)\s+(ago|later)",
        r"in\s+\d+\s+(days?|weeks?|months?)\s*,",
    ],
}

STYLE_INDICATORS = {
    "Vulnerable Victor": [
        "i quit", "i finally", "i discovered", "i['\u2019]m terrible",
        "broke me", "my savings", "rock bottom", "failed", "vipassana",
        "anxiety", "crying", "i was wrong", "humbled",
    ],
    "Contrarian Philosopher": [
        "isn't your", "is a commodity", "nobody says", "but 99%",
        "wrong approach", "uncomfortable truth", "optimizing the wrong",
        "ai first", "ai native", "competitive advantage",
    ],
    "Absurdist Truth-Teller": [
        "mom asked ai", "cat with instagram", "teenager with chatgpt",
        "my mom", "autocomplete", "regenerate response", "brewing ideas",
        "kindergarten", "goldfish math", "too attractive",
    ],
    "Relatable Human": [
        "i['\u2019]m the most average", "i don't have", "just this one thing",
        "we['\u2019]ve all", "honestly", "just me", "looking for a good paycheck",
    ],
}


CTA_STYLES = {
    "permission-giving": [
        r"take\s+this\s+(as\s+your\s+)?sign",
        r"if\s+you\s+can\s+afford",
        r"it's\s+okay\s+to",
    ],
    "direct-question": [
        r"\?\s*$",
        r"what\s+(would|percentage|weird|do)\s+you",
        r"what's\s+your",
        r"how\s+do\s+you\s+",
    ],
    "challenge": [
        r"try\s+this",
        r"start\s+building",
        r"i\s+challenge\s+you",
    ],
    "community": [
        r"to\s+anyone\s+who",
        r"if\s+you['\u2019]ve\s+been",
        r"we['\u2019]re\s+building",
    ],
    "soft-close": [
        r"p\.s\..*",
        r"p\.p\.s",
        r"btw",
    ],
}


def classify_hook(post: str) -> str:
    """Return the Blueprint hook pattern (A/B/C/D) or 'other'."""
    first_line = post.strip().split("\n")[0]
    for pattern_label, regexes in HOOK_PATTERNS.items():
        for rx in regexes:
            if re.search(rx, first_line, flags=re.IGNORECASE):
                return pattern_label
    return "other"


def classify_style(post: str) -> str:
    """Best-guess Blueprint style based on content signals."""
    lowered = post.lower()
    scores: dict[str, int] = {}
    for style, indicators in STYLE_INDICATORS.items():
        score = sum(1 for ind in indicators if re.search(ind, lowered))
        if score:
            scores[style] = score
    if not scores:
        return "Unclassified"
    return max(scores, key=scores.get)


def classify_cta(post: str) -> list[str]:
    """Return list of CTA types detected in post's last ~300 chars."""
    tail = post[-500:].lower()
    matches = []
    for cta_type, regexes in CTA_STYLES.items():
        for rx in regexes:
            if re.search(rx, tail):
                matches.append(cta_type)
                break
    return matches


def count_specifics(post: str) -> dict[str, int]:
    """Count specific anchors in a post — numbers, named entities, etc."""
    return {
        "numbers_with_units": len(re.findall(r"\b\d+\s*(?:%|hours?|minutes?|days?|weeks?|months?|years?|\$|USD)\b", post, re.IGNORECASE)),
        "bare_numbers": len(re.findall(r"\b\d+\b", post)),
        "named_orgs": len(re.findall(r"\b(Atlan|OpenAI|Claude|ChatGPT|Anthropic|Google|Cursor|Cerebras|Khosla|Zerodha|Notion|Springworks|Stripe|Meta|NVIDIA|Apple|Amazon)\b", post)),
        "questions": post.count("?"),
        "ps_lines": len(re.findall(r"p\.s\.?", post, re.IGNORECASE)),
    }


def derive_metrics(row: dict[str, str]) -> dict[str, Any]:
    """Pull engagement numbers from CSV row, compute composite."""
    def g(key: str) -> int:
        try:
            return int(row.get(key, "0") or "0")
        except ValueError:
            return 0

    reactions = g("total_reactions:")
    likes = g("like:")
    support = g("support:")
    love = g("love:")
    insight = g("insight:")
    celebrate = g("celebrate:")
    comments = g("comments:")
    reposts = g("reposts:")

    # Weighted engagement score: comments worth more than likes (algorithm + intent signal)
    composite = reactions + (comments * 3) + (reposts * 5)

    return {
        "reactions": reactions,
        "likes": likes,
        "support": support,
        "love": love,
        "insight": insight,
        "celebrate": celebrate,
        "comments": comments,
        "reposts": reposts,
        "composite_engagement": composite,
    }


def process_row(row: dict[str, str]) -> dict[str, Any] | None:
    post = row.get("Post content", "").strip()
    if not post:
        return None

    metrics = derive_metrics(row)
    hook_pattern = classify_hook(post)
    style = classify_style(post)
    ctas = classify_cta(post)
    specifics = count_specifics(post)
    first_line = post.split("\n")[0][:120]

    return {
        "date": row.get("Date posted", "").strip(),
        "time": row.get("Time", "").strip(),
        "url": row.get("URL", "").strip(),
        "first_line": first_line,
        "length_chars": len(post),
        "hook_pattern": hook_pattern,
        "style": style,
        "ctas": ctas,
        "specifics": specifics,
        "metrics": metrics,
        "post_full": post,
    }


def summarize_patterns(entries: list[dict[str, Any]]) -> dict[str, Any]:
    """Build stats JSON — which hooks/styles/CTAs win by engagement."""
    if not entries:
        return {}

    # Sort by composite engagement
    ranked = sorted(entries, key=lambda e: e["metrics"]["composite_engagement"], reverse=True)

    def avg_for(key_path: str, filter_fn) -> float:
        matching = [e for e in entries if filter_fn(e)]
        if not matching:
            return 0.0
        return sum(e["metrics"]["composite_engagement"] for e in matching) / len(matching)

    hook_stats = {}
    for pattern in list("ABCD") + ["other"]:
        hook_stats[pattern] = {
            "count": sum(1 for e in entries if e["hook_pattern"] == pattern),
            "avg_engagement": round(avg_for("hook_pattern", lambda e: e["hook_pattern"] == pattern), 1),
        }

    style_stats = {}
    for style in list(STYLE_INDICATORS.keys()) + ["Unclassified"]:
        style_stats[style] = {
            "count": sum(1 for e in entries if e["style"] == style),
            "avg_engagement": round(avg_for("style", lambda e: e["style"] == style), 1),
        }

    cta_stats: dict[str, Any] = {}
    for cta in CTA_STYLES.keys():
        matching = [e for e in entries if cta in e["ctas"]]
        cta_stats[cta] = {
            "count": len(matching),
            "avg_engagement": round(sum(e["metrics"]["composite_engagement"] for e in matching) / len(matching), 1) if matching else 0,
        }

    return {
        "total_posts": len(entries),
        "top_5_by_engagement": [
            {
                "date": e["date"],
                "first_line": e["first_line"],
                "hook_pattern": e["hook_pattern"],
                "style": e["style"],
                "ctas": e["ctas"],
                "composite_engagement": e["metrics"]["composite_engagement"],
                "reactions": e["metrics"]["reactions"],
                "comments": e["metrics"]["comments"],
            }
            for e in ranked[:5]
        ],
        "bottom_3_by_engagement": [
            {
                "date": e["date"],
                "first_line": e["first_line"],
                "hook_pattern": e["hook_pattern"],
                "style": e["style"],
                "composite_engagement": e["metrics"]["composite_engagement"],
            }
            for e in ranked[-3:]
        ],
        "hook_pattern_stats": hook_stats,
        "style_stats": style_stats,
        "cta_stats": cta_stats,
        "length_buckets": {
            "short (<1000 chars)": [e["metrics"]["composite_engagement"] for e in entries if e["length_chars"] < 1000],
            "medium (1000-2000)": [e["metrics"]["composite_engagement"] for e in entries if 1000 <= e["length_chars"] < 2000],
            "long (>=2000)": [e["metrics"]["composite_engagement"] for e in entries if e["length_chars"] >= 2000],
        },
    }


def render_markdown(summary: dict[str, Any], entries: list[dict[str, Any]]) -> str:
    """Render a markdown patterns file for the writing prompt to read."""
    lines = [
        "# Aayush's LinkedIn Performance Patterns",
        "",
        "**Auto-generated from `history/linkedin-posts-history.jsonl`. Do not edit by hand.**",
        "",
        "Read by `/write-posts` when generating the 3 daily options. Use this to weight which Blueprint style/hook/CTA to pick for today's content based on what's actually worked for Aayush.",
        "",
        f"**Total posts analyzed:** {summary['total_posts']}",
        "",
        "---",
        "",
        "## Top 5 posts by composite engagement",
        "",
    ]
    for i, post in enumerate(summary["top_5_by_engagement"], 1):
        lines.append(f"### #{i} — {post['date']}  (engagement: {post['composite_engagement']})")
        lines.append(f"- Hook pattern: **{post['hook_pattern']}** | Style: **{post['style']}** | CTAs: {', '.join(post['ctas']) or 'none'}")
        lines.append(f"- Reactions: {post['reactions']}, Comments: {post['comments']}")
        lines.append(f"- First line: *\"{post['first_line']}\"*")
        lines.append("")

    lines.extend([
        "## Bottom 3 (what underperforms)",
        "",
    ])
    for post in summary["bottom_3_by_engagement"]:
        lines.append(f"- {post['date']} | Hook: **{post['hook_pattern']}** | Style: **{post['style']}** | Engagement: {post['composite_engagement']}")
        lines.append(f"  *\"{post['first_line']}\"*")
    lines.append("")

    lines.extend([
        "## Hook pattern performance",
        "",
        "| Pattern | Count | Avg engagement |",
        "|---|---|---|",
    ])
    for label, stats in sorted(summary["hook_pattern_stats"].items(), key=lambda x: -x[1]["avg_engagement"]):
        pattern_name = {
            "A": "Contrarian Truth",
            "B": "Identity / Confession",
            "C": "Absurd Comparison",
            "D": "Time Bomb",
            "other": "Other/Unclassified",
        }.get(label, label)
        lines.append(f"| **{label}** {pattern_name} | {stats['count']} | {stats['avg_engagement']} |")
    lines.append("")

    lines.extend([
        "## Style performance",
        "",
        "| Style | Count | Avg engagement |",
        "|---|---|---|",
    ])
    for style, stats in sorted(summary["style_stats"].items(), key=lambda x: -x[1]["avg_engagement"]):
        lines.append(f"| **{style}** | {stats['count']} | {stats['avg_engagement']} |")
    lines.append("")

    lines.extend([
        "## CTA type performance",
        "",
        "| CTA | Count | Avg engagement |",
        "|---|---|---|",
    ])
    for cta, stats in sorted(summary["cta_stats"].items(), key=lambda x: -x[1]["avg_engagement"]):
        lines.append(f"| {cta} | {stats['count']} | {stats['avg_engagement']} |")
    lines.append("")

    # Pick a few-shot example: the top 1 post, shown in full
    if summary["top_5_by_engagement"]:
        top_url = summary["top_5_by_engagement"][0]["date"]
        top_post = next((e for e in entries if e["date"] == top_url), entries[0])
        lines.extend([
            "## Reference post (Aayush's top performer — use as voice-matching anchor)",
            "",
            f"Date: {top_post['date']} | Engagement: {top_post['metrics']['composite_engagement']}",
            "",
            "```",
            top_post["post_full"][:2500],
            "```",
            "",
            "---",
            "",
            "## Rules for using this data in /write-posts",
            "",
            "1. **Bias toward the top 3 hook patterns by avg engagement** — write at least 1 option in that style per day.",
            "2. **Avoid bottom-3 patterns** — unless today's content strongly demands it, skip the underperforming angles.",
            "3. **Match Aayush's top CTA styles** — permission-giving + direct-question win for him. Challenges win less.",
            "4. **Length:** medium (1000-2000 chars) is Aayush's sweet spot based on the data.",
            "5. **Voice anchor:** read the reference post above. Match that rhythm + vulnerability + specificity. Do NOT copy specific claims — copy the structure + tone.",
            "",
        ])

    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ingest_linkedin_csv.py <path-to-csv>", file=sys.stderr)
        sys.exit(2)

    csv_path = Path(sys.argv[1])
    if not csv_path.is_file():
        print(f"CSV not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    # Repo root
    repo = Path(__file__).parent.parent
    history_dir = repo / "history"
    config_dir = repo / "config"
    history_dir.mkdir(exist_ok=True)

    entries: list[dict[str, Any]] = []
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            entry = process_row(row)
            if entry:
                entries.append(entry)

    # Write engagement.jsonl (one line per post, canonical history)
    jsonl_path = history_dir / "linkedin-posts-history.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as out:
        for e in entries:
            out.write(json.dumps(e, ensure_ascii=False) + "\n")

    # Write patterns summary JSON
    summary = summarize_patterns(entries)
    json_path = config_dir / "linkedin-patterns.json"
    json_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    # Write human-readable patterns (for /write-posts prompt)
    md_path = config_dir / "aayush-linkedin-patterns.md"
    md_path.write_text(render_markdown(summary, entries), encoding="utf-8")

    print(f"[ingest] processed {len(entries)} posts")
    print(f"[ingest] wrote {jsonl_path}")
    print(f"[ingest] wrote {json_path}")
    print(f"[ingest] wrote {md_path}")
    print()
    print("Top 3 posts:")
    for e in sorted(entries, key=lambda x: -x["metrics"]["composite_engagement"])[:3]:
        print(f"  {e['date']} | {e['hook_pattern']} | {e['style']} | engagement={e['metrics']['composite_engagement']}")
        print(f"    {e['first_line'][:80]}")


if __name__ == "__main__":
    main()
