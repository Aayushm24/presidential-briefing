# Council — 2026-08-31 (iteration 1)

## Deterministic findings — CONFIRMED VIOLATIONS

**VERDICT: REVISE** — Hard rule violations detected in pre-flight check

### EM Dash Violations (21 total) — ZERO tolerance
- Brief: 10 em dashes found and cleaned
- Posts: 11 em dashes found and cleaned

### "Not X, it's Y" Inversions (3 total) — AI-tell banned pattern
- "isn't about better models. It's about state" (appears 2x)
- Brief and posts both contain this exact inversion

### Word Count Violation
- Brief: 1,442 words (below 2,000 minimum floor)
- Needs expansion in lead section with more mechanism/specificity, not more topics

### Long Sentence Violations (26 total flags, 2 files marked)
Multiple sentences over 22-word limit, including:
- 106w: "Key takeaways: AI product strategy shifts from single turn interactions to long..."
- 40w: "Enterprise buyers used to ask 'can your AI write marketing copy?' Now..."

## Fabrication Check
⚠️ FABRICATION RISK: Claims appear grounded in brief sources. No repricing language found.

## Summary
Multiple hard rule violations require immediate revision before any LLM passes. clean_text.py has already fixed em dashes but structural issues remain.

## Verdict: REVISE

Specific revision notes:
- brief.md: Expand lead section to reach 2,000+ words minimum
- brief.md: Replace "isn't about better models. It's about state" inversion with direct statement
- brief.md: Break all sentences over 22 words into shorter segments
- posts.md: Fix remaining "Not X, it's Y" inversion
- posts.md: Break long sentences in all 3 options

Priority: Fix structural violations first, then focus on content expansion.