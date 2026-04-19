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
# Broader coverage — matches ANY subject, not just "This/That/These".
# Examples caught: "the shift isn't about X. it's about Y" / "Claude stopped being X. it's becoming Y" /
# "the constraint isn't coding knowledge. it's knowing what to build" / "This isn't about X. It's about Y"
NOT_X_ITS_Y_PATTERNS: list[str] = [
    # "<anything> isn't/aren't/is not/are not <X>. It's/They're <Y>"
    r"\b(?:isn(?:'|\u2019)?t|aren(?:'|\u2019)?t|is\s+not|are\s+not)\s+(?:about\s+)?[\w\s'-]{1,60}?[.\n]+\s*(?:[Ii]t(?:'|\u2019)?s|[Tt]hey(?:'|\u2019)?re)\s+(?:about\s+|becoming\s+|actually\s+)?\w+",
    # "<anything> stopped being <X>. It's <Y>"  (e.g. "Claude Code stopped being a coding assistant. it's becoming...")
    r"stopped\s+being\s+[\w\s'-]{1,60}?[.\n]+\s*(?:[Ii]t(?:'|\u2019)?s|[Tt]hey(?:'|\u2019)?re)\s+\w+",
    # Explicit "The risk/difference/point is not X. The risk/difference/point is Y"
    r"[Tt]he\s+(?:risk|difference|point|challenge|problem|shift|constraint|answer)\s+is\s+not\s+[\w\s'-]{1,60}?[.\n]+\s*(?:[Tt]he\s+\w+\s+is|[Ii]t(?:'|\u2019)?s)\s+\w+",
    # Direct declarative contrast: "X is not Y. X is Z" (same-subject reframe)
    r"\b(\w+)\s+is\s+not\s+[\w\s'-]{1,40}?[.\n]+\s*\1\s+is\s+\w+",
    # "but correlation isn't strategy. accessibility creates..." — negation + contrasting abstract noun
    r"\bbut\s+\w+\s+(?:isn(?:'|\u2019)?t|is\s+not)\s+[\w\s'-]{1,40}?[.\n]+\s*\w+\s+(?:creates|requires|means|is|makes)",
]

# Winner/loser neat-bow closers — banned by Blueprint.
# "the founders who X ... the ones who don't Y" — the "the ones" pivot is the tell.
NEAT_BOW_PATTERNS: list[str] = [
    # "the founders/builders/teams/ones winning/who X (sentence). the ones losing/who don't/still Y"
    r"[Tt]he\s+(?:founders?|builders?|teams?|companies|startups?|engineers?|ones)\s+(?:who|that|winning|losing)\s+[\w\s,'-]{2,120}?\.\s*[Tt]he\s+ones\s+(?:who|still|losing|don(?:'|\u2019)?t|not)\s+",
    # Simpler: consecutive "the ones who/winning/losing" statements
    r"[Tt]he\s+ones\s+(?:winning|losing|who|still|don(?:'|\u2019)?t|not)\s+[\w\s,'-]{2,80}?(?:ship|will|retrofit|lose|miss|win)",
    # "winners X. losers Y."
    r"(?:winners|winning\s+teams|the\s+winners)\s+[\w\s,'-]{2,60}?[.\n]+\s*(?:losers|the\s+losers|the\s+ones\s+losing)\s+",
    # "X is/are where the real race is / X is where value accrues"
    r"\b(?:is|are)\s+where\s+the\s+(?:real\s+)?(?:race|value|game|opportunity|money)\s+(?:is|accrues|happens|lives|sits)\b",
    # "X will compound / X compounds productivity advantages" closures
    r"\b(?:compound(?:ing)?|stacked?|stacking)\s+(?:productivity\s+)?advantages?\s+(?:as|over|while)",
]

# Guru/advice voice — third-person prescriptions banned per user instructions.
# Allow up to 60 chars between the subject noun and the modal verb ("founders building X should plan...").
GURU_VOICE_PATTERNS: list[str] = [
    # "founders/builders/teams [any words] should/need to/must [verb]"
    r"\b(?:founders?|builders?|teams?|engineers?|companies|startups?|developers?)\s+[\w\s,'-]{0,60}?\s+(?:should|need\s+to|must|ought\s+to|have\s+to|want\s+to)\s+\w+",
    # "if you're a founder/builder/CTO..."
    r"\bif\s+you(?:'|\u2019)?re\s+(?:a|an)\s+(?:founder|builder|engineer|CTO|CEO|developer)\b",
    # "for founders/builders: ..." direct-address form
    r"(?:^|\.\s+)[Ff]or\s+(?:founders?|builders?|teams?|engineers?|CTOs?|CEOs?)\s*[,:]",
    # "X is a junior engineer. a very fast one." anthropomorphized advice setup
    r"\b(?:the\s+)?AI\s+is\s+a\s+junior\s+\w+",
    # "builders who X will compound returns" / "the ones who invest now"
    r"\b(?:builders?|founders?|teams?|engineers?)\s+who\s+(?:invest|use|build|adopt|ship)\s+[\w\s]{1,40}?\s+(?:now|today|early)\s+(?:will|get|compound|stack)",
]

# Trailing hashtag block — auto-strip (user said zero hashtags at end)
TRAILING_HASHTAG_PATTERN: str = r"\n*^#\w+(?:\s+#\w+)*\s*$"

# Plain-English kill-list from .claude/skills/write-briefing/references/plain-english-rules.md
# These are MBA/VC jargon that make text hard to read. Any hit = REVISE.
MBA_VOCABULARY_PATTERNS: list[str] = [
    r"\bmaturation\b",
    r"\bmatures\b(?!\s+(?:in|over|through|around|at|on))",  # "markets mature into" but allow "matures in" = ages
    r"\b(?:market|ecosystem|industry)\s+maturity\b",
    r"\bcommoditi[sz]ation\b",
    r"\bcommoditi[sz]e[sd]?\b",
    r"\btable\s+stakes\b",
    r"\bmoat\b(?!\s+(?:castle|digging|wall))",  # let "digging a moat" etc through literal uses
    r"\bdifferentiation\b",
    r"\b(?:move|moves|moving|moved|shift|shifts|shifting|shifted)\s+up\s+the\s+stack\b",
    r"\bup\s+the\s+stack\b",
    r"\bunderlying\s+market\b",
    r"\b(?:vendor|infrastructure|model|platform)\s+dependency\b",
    r"\bsignals?\s+(?:market\s+)?maturi(?:ty|zation)\b",
    r"\bgenerating\s+(?:real|scale|commercial)\s+revenue\b",
    r"\bproduction\s+workloads?\s+at\s+scale\b",
    r"\benterprise\s+customers?\b",
    r"\becosystem\b(?!\s+of\s+\w)",  # allow "ecosystem of tools" (concrete), block bare "the ecosystem"
    r"\bparadigm\s+shift\b",
    r"\bdisruption\b",
    r"\bleverage(?:s|d|ing)?\b(?!\s+ratio)",  # block "leverage" verb, allow "leverage ratio" financial
    r"\butiliz(?:e|es|ed|ing|ation)\b",
    r"\bseamless(?:ly)?\b",
    r"\brevolutionary\b",
    r"\bgame[\s-]?changing\b",
    r"\bcutting[\s-]?edge\b",
    r"\bcompounds?\s+monthly\b",
]

# Sentence-length check: flag any sentence > 22 words
LONG_SENTENCE_THRESHOLD: int = 22

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


def strip_trailing_hashtags(text: str) -> tuple[str, int]:
    """Remove any trailing hashtag-only lines from a post or brief.
    User requirement: zero hashtags at end of post.
    Matches end-of-document lines like '#AI #infrastructure #startups'."""
    count = 0
    # Work on lines from the end backwards
    lines = text.rstrip().split("\n")
    while lines:
        last = lines[-1].strip()
        if re.fullmatch(r"#\w+(?:\s+#\w+)*", last):
            lines.pop()
            count += 1
            # Also strip any blank line immediately above
            while lines and not lines[-1].strip():
                lines.pop()
        else:
            break
    return "\n".join(lines) + "\n", count


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
    text, counts["trailing_hashtags"] = strip_trailing_hashtags(text)

    # Flag-only detections (not auto-rewritten — LLM must fix)
    flags["llm_structural_labels"] = count_matches(text, LLM_STRUCTURAL_LABEL_PATTERNS)
    flags["not_x_its_y"] = count_matches(text, NOT_X_ITS_Y_PATTERNS)
    flags["llm_connectives"] = count_matches(text, LLM_CONNECTIVE_PATTERNS)
    flags["fabrication_candidates"] = count_matches(text, FABRICATION_FLAG_PATTERNS)
    flags["neat_bows"] = count_matches(text, NEAT_BOW_PATTERNS)
    flags["guru_voice"] = count_matches(text, GURU_VOICE_PATTERNS)
    flags["mba_vocabulary"] = count_matches(text, MBA_VOCABULARY_PATTERNS)

    # Long-sentence detector (>22 words)
    long_sentences: list[str] = []
    for raw in re.split(r"(?<=[.!?])\s+", text):
        # strip markdown formatting before counting
        cleaned = re.sub(r"[*_#>\-\[\]()]", " ", raw).strip()
        words = cleaned.split()
        if len(words) > LONG_SENTENCE_THRESHOLD:
            long_sentences.append(f"{len(words)}w: {' '.join(words[:12])}...")
    flags["long_sentences"] = long_sentences

    counts["llm_structural_flags"] = len(flags["llm_structural_labels"])
    counts["not_x_its_y_count"] = len(flags["not_x_its_y"])
    counts["llm_connective_flags"] = len(flags["llm_connectives"])
    counts["fabrication_flags"] = len(flags["fabrication_candidates"])
    counts["neat_bow_flags"] = len(flags["neat_bows"])
    counts["guru_voice_flags"] = len(flags["guru_voice"])
    counts["mba_vocabulary_flags"] = len(flags["mba_vocabulary"])
    counts["long_sentence_flags"] = len(long_sentences)

    # Hard rule: >1 "[Not X, it's Y]" in a document = anti-slop violation
    counts["not_x_its_y_violation"] = 1 if len(flags["not_x_its_y"]) > 1 else 0
    # Hard rule: any neat-bow = violation (they're always closing clichés)
    counts["neat_bow_violation"] = 1 if counts["neat_bow_flags"] > 0 else 0
    # Hard rule: any guru voice > 0 (posts must be first-person take, not third-person advice)
    counts["guru_voice_violation"] = 1 if counts["guru_voice_flags"] > 2 else 0
    # Hard rule: >2 MBA-vocab hits = plain-english violation
    counts["mba_vocabulary_violation"] = 1 if counts["mba_vocabulary_flags"] > 2 else 0
    # Hard rule: >3 sentences over 22 words = plain-english violation
    counts["long_sentence_violation"] = 1 if counts["long_sentence_flags"] > 3 else 0

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
            f"trailing_hashtags={counts['trailing_hashtags']} "
            f"llm_structural={counts['llm_structural_flags']} "
            f"not_x_its_y={counts['not_x_its_y_count']} "
            f"neat_bows={counts['neat_bow_flags']} "
            f"guru_voice={counts['guru_voice_flags']} "
            f"llm_connectives={counts['llm_connective_flags']} "
            f"fabrications={counts['fabrication_flags']} "
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
