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

# LLM "Why now?" structural labels (Helix rule: real writers don't announce rhetorical moves).
# Match the full sentence containing them — flag via counting, don't auto-rewrite (LLM needed).
LLM_STRUCTURAL_LABEL_PATTERNS: list[str] = [
    r"[Ww]hat(?:'|\u2019)?s\s+happening\s+is\b",
    r"[Hh]ere(?:'|\u2019)?s\s+why\s+this\s+matters\b",
    r"[Hh]ere(?:'|\u2019)?s\s+the\s+thing\b",
    r"[Hh]ere(?:'|\u2019)?s\s+what\s+(?:i|I)(?:'|\u2019)?ve\s+seen\s+firsthand\b",
    r"[Hh]ere(?:'|\u2019)?s\s+what\s+that\s+looks\s+like\s+in\s+practice\b",
    r"[Tt]he\s+parallel\s+to\s+.{1,50}?\s+is\s+(?:almost\s+)?exact\b",
    r"[Tt]he\s+details\s+are\s+thin,?\s+but\s+the\s+direction\s+is\s+clear\b",
    r"[Tt]he\s+pattern\s+is\s+so\s+consistent\s+it(?:'|\u2019)?s\s+almost\s+boring\b",
]

# LLM "[Not X, it's Y]" inversion patterns (Helix rule: max 1 per document).
# Count occurrences, flag if > 1.
NOT_X_ITS_Y_PATTERNS: list[str] = [
    r"(?:[Tt]his|[Tt]hat|[Tt]hese)\s+(?:isn(?:'|\u2019)?t|aren(?:'|\u2019)?t)\s+\w+.{0,80}?[.—,]\s*(?:[Ii]t(?:'|\u2019)?s|[Tt]hey(?:'|\u2019)?re)\s+\w+",
    r"[Tt]he\s+\w+\s+is\s+not\s+\w+.{0,60}?\.\s*(?:[Tt]he\s+\w+\s+is|[Ii]t(?:'|\u2019)?s)\s+\w+",
    r"[Tt]he\s+risk\s+is\s+not\s+\w+.{0,60}?\.\s*[Tt]he\s+risk\s+is\s+\w+",
    r"[Tt]he\s+difference\s+is\s+not\s+\w+.{0,60}?\.\s*[Tt]he\s+difference\s+is\s+\w+",
]

# LLM connective tells (specific patterns from shipped output)
LLM_CONNECTIVE_PATTERNS: list[str] = [
    r"[Tt]hese\s+(?:two|three|several)\s+(?:numbers|facts|stories)\s+landed\s+in\s+the\s+same\s+(?:week|day|month)",
    r"everyone\s+treated\s+them\s+as\s+separate\s+stories",
    r"(?:i|I)\s+think\s+they(?:'|\u2019)?re\s+the\s+same\s+story",
    r"\btokenmaxxing\b",  # forced LLM coinage
    r"the\s+token\s+bill\s+says\s+you(?:'|\u2019)?re\s+working\s+hard",
]

# Fabricated first-person specifics — regex flag (don't auto-remove, flag for LLM review)
# Matches patterns like "i talked to an engineering lead last month", "a 14-person team I advise"
FABRICATION_FLAG_PATTERNS: list[str] = [
    r"\b(?:i|I)\s+(?:advise|work\s+with|coach|talked\s+to|reviewed|deleted|tracked|built)\s+(?:a|an|the|\d+)\s+(?:\d+[-\s]?person\s+team|team\s+of\s+\d+|engineering\s+lead|\d+,?\d*\s+lines)",
    r"\ba\s+\d+[-\s]?person\s+team\s+(?:i|I)\s+(?:advise|advised|work\s+with|worked\s+with)",
    r"(?:i|I)\s+deleted\s+(?:about\s+)?\d+%?\s+of",
    r"(?:i|I)(?:'|\u2019)?ve\s+been\s+(?:tracking|building|running)\s+(?:a|an|rough)\s+(?:metric|tool|system)\s+(?:with|for)\s+(?:one|a)\s+team",
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


def count_matches(text: str, patterns: list[str]) -> list[str]:
    """Return list of matched strings (for flag-only detection — no rewrite)."""
    matches = []
    for pattern in patterns:
        for m in re.finditer(pattern, text, flags=re.IGNORECASE):
            matches.append(m.group(0)[:120])
    return matches


def clean_file(path: Path) -> dict:
    original = path.read_text(encoding="utf-8")
    text = original
    counts: dict = {}
    flags: dict = {}

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

    # Flag-only detections (not auto-rewritten — LLM must fix)
    flags["llm_structural_labels"] = count_matches(text, LLM_STRUCTURAL_LABEL_PATTERNS)
    flags["not_x_its_y"] = count_matches(text, NOT_X_ITS_Y_PATTERNS)
    flags["llm_connectives"] = count_matches(text, LLM_CONNECTIVE_PATTERNS)
    flags["fabrication_candidates"] = count_matches(text, FABRICATION_FLAG_PATTERNS)

    counts["llm_structural_flags"] = len(flags["llm_structural_labels"])
    counts["not_x_its_y_count"] = len(flags["not_x_its_y"])
    counts["llm_connective_flags"] = len(flags["llm_connectives"])
    counts["fabrication_flags"] = len(flags["fabrication_candidates"])

    # Hard rule: >1 "[Not X, it's Y]" in a document = anti-slop violation
    counts["not_x_its_y_violation"] = 1 if len(flags["not_x_its_y"]) > 1 else 0

    if text != original:
        path.write_text(text, encoding="utf-8")
        counts["file_changed"] = 1
    else:
        counts["file_changed"] = 0

    counts["_flags"] = flags  # detailed flags for caller inspection
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
        flags = counts.pop("_flags", {})
        print(
            f"[clean] {path}: em_dash={counts['em_dash']} bullet={counts['bullet']} "
            f"kill_word={counts['kill_word']} audience_phrase={counts['audience_phrase']} "
            f"transition={counts['transition']} cliche_opener={counts['cliche_opener']} "
            f"llm_structural_flags={counts['llm_structural_flags']} "
            f"not_x_its_y_count={counts['not_x_its_y_count']} "
            f"llm_connective_flags={counts['llm_connective_flags']} "
            f"fabrication_flags={counts['fabrication_flags']} "
            f"changed={counts['file_changed']}",
            file=sys.stderr,
        )

        # Verbose flag output for human inspection
        for flag_type, matches in flags.items():
            if matches:
                print(f"[clean]   {flag_type}:", file=sys.stderr)
                for match in matches[:5]:
                    print(f"[clean]     - {match}", file=sys.stderr)

        for k, v in counts.items():
            if isinstance(v, int):
                grand_total[k] = grand_total.get(k, 0) + v

    print(f"[clean] TOTAL: {grand_total}", file=sys.stderr)


if __name__ == "__main__":
    main()
