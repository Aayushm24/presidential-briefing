## Fabrication Check
Checking post claims against brief...

# Council — 2026-09-09 (iteration 1)

## Deterministic Findings

**MBA Vocabulary Violations (1):** commoditized, differentiation

**Long Sentence Violations (1):** Multiple sentences exceed 22 words, including:
- 169w: Key takeaways: Cognition's $48B valuation proves AI coding agents can command frontier...
- 46w: Massive capital flows into specialized AI companies signal the market is far...

**Not X Its Y Violations (2):**
- "aren't betting on potential. They're betting"
- "isn't just the 25 million professional developers. It's every"
- "isn't about the math. It's about attribution"

**Em Dash Violations:** FIXED by clean_text.py (previously 14 total em dashes, now 0)

**VERDICT: REVISE** - Multiple deterministic violations found requiring fixes.

## Specific Revision Notes

**Brief.md revisions needed:**
- Fix MBA vocabulary: replace "commoditized" with "everyone can buy it now" or "it's cheap now"
- Fix MBA vocabulary: replace "differentiation" with "what makes them different" or name the specific advantage
- Break long sentences: 169w sentence starting "Key takeaways:" needs to be split into multiple shorter sentences
- Fix "Not X Its Y" patterns: rewrite "aren't betting on potential. They're betting" as direct statement
- Fix "Not X Its Y" patterns: rewrite "isn't just the 25 million professional developers. It's every" as direct statement

**Posts.md revisions needed:**
- Fix MBA vocabulary: replace instances of "commoditized" and "differentiation" with simpler alternatives
- Fix "Not X Its Y" patterns: rewrite "aren't betting on potential. They're betting" and "isn't about the math. It's about attribution" as direct statements
- Break metadata long sentences in headers

