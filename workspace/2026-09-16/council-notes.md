# Council — 2026-09-16 (iteration 1)

## Deterministic findings (clean_text.py violations)

**CONFIRMED violations found. Verdict: REVISE**

### Brief violations (workspace/2026-09-16/brief.md):
- **Em dashes**: 11 instances found — zero tolerance rule
- **MBA vocabulary**: 2 instances of "ecosystem" (banned in briefs)
- **Not X, it's Y inversion**: 1 instance — "isn't just a failure catalog. It's pattern"
- **LLM structural label**: 1 instance — "Here's why this matters"
- **Long sentences**: 2 violations over 22 words

### Posts violations (workspace/2026-09-16/posts.md):
- **Em dashes**: 9 instances found — zero tolerance rule
- **Not X, it's Y inversion**: 1 instance — "isn't the agent. It's the"
- **Guru voice**: 1 instance — "founders are still building AI demos when they should be"
- **MBA vocabulary**: 1 instance of "ecosystem" (posts allow "moat" but not "ecosystem")

### Word count check:
- **Brief word count**: 2,019 words (PASSES — above 2,000 floor)

These are regex-hard rules. All em dashes must be replaced with commas or periods. All MBA vocabulary must be replaced per plain-english-rules.md. All Not X, it's Y inversions must be rewritten as direct statements or parallel structure with different subjects.

## Verdict: REVISE

**Critical violations found in deterministic pre-flight:**
- 20 em dashes total (zero tolerance)
- 3 MBA vocabulary hits ("ecosystem")
- 2 Not X, it's Y inversions  
- 1 guru voice violation
- 1 LLM structural label

Specific revision notes:
- brief.md: Replace all 11 em dashes with commas or periods
- brief.md: Replace "ecosystem" with "tools built on Claude Code" or similar specific naming
- brief.md: Rewrite "isn't just a failure catalog. It's pattern" as direct statement
- brief.md: Remove/rewrite "Here's why this matters" structural label
- posts.md: Replace all 9 em dashes with commas or periods
- posts.md: Replace "ecosystem" with specific naming
- posts.md: Rewrite "isn't the agent. It's the" inversion
- posts.md: Rewrite guru voice "founders are still building AI demos when they should be" as observation
