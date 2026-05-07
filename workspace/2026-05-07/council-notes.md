# Council — 2026-05-07 (iteration 1)

## Deterministic findings (pre-flight violations)

**CONFIRMED HARD-RULE FAILURES - VERDICT: REVISE**

### Em dashes (9 violations)
- Brief: 2 em dashes found
- Posts: 7 em dashes found  
**Fix:** Replace all em dashes with commas or periods

### [Not X, it's Y] inversions (5 violations)
- Brief: "aren't code generation use cases. They're business"
- Posts: "isn't coding speed. It's what"
- Posts: "isn't better prompts. It's persistent" 
- Posts: "aren't using Claude Code as better autocomplete. They're using"
- Posts: "isn't a nice-to-have anymore. It's headcount"
**Fix:** Rewrite each inversion as direct declarative statements

### Long sentences (21 violations - critical)
Multiple sentences exceed 22-word limit including:
- Brief: 42w sentence in opening
- Brief: 128w sentence in key takeaways (extremely long)
- Posts: Multiple sentences 24w-56w
**Fix:** Split all sentences over 22 words into shorter sentences

### MBA vocabulary (2 violations in brief)
- "Enterprise customers" — use "big companies" or skip
- "ecosystem" — name the specific thing
**Fix:** Replace with plain English alternatives

### Guru voice (1 violation in brief)  
- "team structure should reorganize" — third-person prescription
**Fix:** Rewrite as first-person observation

**Total violations: 38 confirmed rule violations**
**Verdict: REVISE required before any LLM passes**

---

## Voice audit (will run after revisions)
*Pending - requires fixes above first*

## Fact check (will run after revisions)  
*Pending - requires fixes above first*

## Adversarial (will run after revisions)
*Pending - requires fixes above first*

## Verdict: REVISE

**Priority revisions required:**
1. Replace all 9 em dashes with commas/periods
2. Rewrite all 5 [Not X, it's Y] inversions as direct statements
3. Split all 21 long sentences into sub-22-word sentences
4. Replace MBA vocabulary with plain English
5. Convert guru voice to first-person observation

Once these deterministic violations are fixed, full LLM council review will proceed.