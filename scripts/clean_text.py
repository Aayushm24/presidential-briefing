#!/usr/bin/env python3
"""Deterministic text fixer — enforces hard voice rules that LLMs can't be trusted to apply 100%.

Reads each file, applies regex substitutions for the known kill-list, writes back in place.
Prints fix counts per category to stderr so callers can log what changed.

Usage:
    python3 scripts/clean_text.py workspace/2026-04-18/brief.md workspace/2026-04-18/posts.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


# Kill-list substitutions — source of truth is
# .claude/skills/write-posts/references/kill-list.md. Keep in sync when
# that file changes.
#
# Pattern → replacement. Patterns are compiled with re.IGNORECASE and
# use word boundaries (\b) unless otherwise noted.

WORD_SUBS: list[tuple[str, str]] = [
    # 1A classic AI buzzwords
    (r"\bdelve\b", "dig into"),
    (r"\btapestry\b", "mix"),
    (r"\bparadigm[- ]shift\b", "shift"),
    (r"\bsynergy\b", "overlap"),
    (r"\bsynergies\b", "overlaps"),
    (r"\bholistic\b", "complete"),
    (r"\bempower\b", "help"),
    (r"\bdemocratize\b", "open up"),
    (r"\bdisruption\b", "shift"),
    (r"\bdisrupting\b", "shifting"),

    # 1B corporate fluff
    (r"\bcutting[- ]edge\b", "leading"),
    (r"\bseamlessly\b", "smoothly"),
    (r"\bseamless\b", "smooth"),
    (r"\bleverage\b", "use"),
    (r"\butilize\b", "use"),
    (r"\bbest[- ]in[- ]class\b", "top"),
    (r"\bworld[- ]class\b", "top"),
    (r"\bnext[- ]generation\b", "next"),
    (r"\bstate[- ]of[- ]the[- ]art\b", "latest"),
    (r"\bmission[- ]critical\b", "essential"),
    (r"\bend[- ]to[- ]end\b", "full"),

    # 1D overwrought emotion
    (r"\bgame[- ]changing\b", "big"),
    (r"\bgame changer\b", "big shift"),
    (r"\bgroundbreaking\b", "notable"),
    (r"\bground[- ]breaking\b", "notable"),
    (r"\brevolutionary\b", "new"),
    (r"\btransformative\b", "big"),
    (r"\btransformational\b", "big"),
    (r"\bunprecedented\b", "rare"),
    (r"\bmonumental\b", "big"),
]

# Audience direct-address — 1L in the kill list. Rewrite founder-targeting phrases
# to builder-focused copy, or delete the greeting form outright.
AUDIENCE_SUBS: list[tuple[str, str]] = [
    (r"\bfor founders\b", "for builders"),
    (r"\bhey founders,?\s*", ""),
    (r"\bfellow founders\b", "fellow builders"),
    (r"\bif you.re a founder\b", "if you're building"),
]

# Transition crutches (1E) — safe to just delete with trailing comma/space.
# Only target when they appear at sentence start.
TRANSITION_PATTERNS: list[str] = [
    r"(^|\.\s+)In fact,\s*",
    r"(^|\.\s+)Indeed,\s*",
    r"(^|\.\s+)Additionally,\s*",
    r"(^|\.\s+)Furthermore,\s*",
    r"(^|\.\s+)Moreover,\s*",
    r"(^|\.\s+)Notably,\s*",
    r"(^|\.\s+)Interestingly,\s*",
    r"(^|\.\s+)Importantly,\s*",
    r"(^|\.\s+)Essentially,\s*",
    r"(^|\.\s+)Fundamentally,\s*",
    r"(^|\.\s+)Ultimately,\s*",
]

# Cliche openers (1F) — delete the whole phrase including trailing space.
OPENER_PATTERNS: list[str] = [
    r"\bHere's what I learned\b[,:.]?\s*",
    r"\bLet me share\b[,:.]?\s*",
    r"\bI've been thinking a lot about\b[,:.]?\s*",
    r"\bImagine if\b[,:.]?\s*",
    r"\bPicture this\b[,:.]?\s*",
    r"\bHot take:\s*",
    r"\bUnpopular opinion:\s*",
]


def fix_em_dashes(text: str) -> tuple[str, int]:
    """Replace U+2014 em dashes with commas + normalize spacing."""
    count = text.count("\u2014")
    if count == 0:
        return text, 0
    # ' — ' (mid-sentence) → ', '
    text = re.sub(r"\s*\u2014\s*", ", ", text)
    # Handle degenerate cases left behind
    text = re.sub(r",\s*\.", ".", text)       # ", ."  → "."
    text = re.sub(r",\s*,", ",", text)         # ", ,"  → ","
    text = re.sub(r"\s+([,.?!])", r"\1", text)  # " ,"  → ","
    return text, count


def fix_bullets(text: str) -> tuple[str, int]:
    count = text.count("•")
    if count == 0:
        return text, 0
    text = text.replace("•", "-")
    return text, count


def apply_patterns(
    text: str, patterns: list[tuple[str, str]] | list[str], replacement: str | None = None
) -> tuple[str, int]:
    """Apply a list of (pattern, replacement) substitutions. If given a
    bare list of patterns + a replacement, applies replacement to all.
    Returns (new_text, match_count)."""
    total = 0
    if isinstance(patterns[0], tuple):
        for pattern, repl in patterns:
            matches = re.findall(pattern, text, flags=re.IGNORECASE)
            total += len(matches)
            text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    else:
        for pattern in patterns:
            matches = re.findall(pattern, text, flags=re.IGNORECASE)
            total += len(matches)
            text = re.sub(
                pattern, replacement or "", text, flags=re.IGNORECASE
            )
    # Collapse whitespace artifacts
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text, total


def clean_file(path: Path) -> dict[str, int]:
    original = path.read_text(encoding="utf-8")
    text = original
    counts: dict[str, int] = {}

    text, counts["em_dash"] = fix_em_dashes(text)
    text, counts["bullet"] = fix_bullets(text)
    text, counts["kill_word"] = apply_patterns(text, WORD_SUBS)
    text, counts["audience_phrase"] = apply_patterns(text, AUDIENCE_SUBS)
    text, counts["transition"] = apply_patterns(
        text, TRANSITION_PATTERNS, replacement=r"\1"
    )
    text, counts["cliche_opener"] = apply_patterns(
        text, OPENER_PATTERNS, replacement=""
    )

    if text != original:
        path.write_text(text, encoding="utf-8")
        counts["file_changed"] = 1
    else:
        counts["file_changed"] = 0

    return counts


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: clean_text.py <file.md> [<file.md>...]", file=sys.stderr)
        sys.exit(2)

    grand_total: dict[str, int] = {}
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.is_file():
            print(f"[clean] skip (not a file): {arg}", file=sys.stderr)
            continue

        counts = clean_file(path)
        print(
            f"[clean] {path}: em_dash={counts['em_dash']} bullet={counts['bullet']} "
            f"kill_word={counts['kill_word']} audience_phrase={counts['audience_phrase']} "
            f"transition={counts['transition']} cliche_opener={counts['cliche_opener']} "
            f"changed={counts['file_changed']}",
            file=sys.stderr,
        )

        for k, v in counts.items():
            grand_total[k] = grand_total.get(k, 0) + v

    print(f"[clean] TOTAL: {grand_total}", file=sys.stderr)


if __name__ == "__main__":
    main()
