# Council — 2026-08-03 (iteration 1)

## Deterministic findings (CONFIRMED hard-rule failures)

**VERDICT: REVISE** — Multiple hard-rule violations found in pre-flight check:

### Word count violation
- brief is at 1951 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### Format violations  
- golden-format.sh found 1 violation: word_count=1951 (expect 2000+)

### Plain English violations from clean_text.py:

**Em dash violations (14 total - ZERO TOLERANCE):**
- brief.md: 8 em dash violations found  
- posts.md: 6 em dash violations found
- All em dashes must be replaced with commas, periods, or ellipses

**Long sentence violations (28 total - SEVERE):**
- brief.md contains multiple sentences over 22-word limit:
  - 44w: "Karpathy's 1M token stress test reveals the new practical frontier for procedural..."
  - 28w: "The paradigm has shifted from "create an SVG of a pelican on..."
  - 133w: "Key takeaways: Karpathy's LLM stress tests collectively define a new practical frontier..." (EXTREME - needs immediate breaking)
  - 23w, 27w and more violations found
- posts.md contains 5 long sentences over 22-word limit

**Neat bow violations (3 instances):**
- brief.md: "The ones who understand it as a procedural content engine will" — generic winner/loser closer
- posts.md: "The founders who understand this will ship experiences that feel handcrafted but scale like templates. The ones still building chatbots will wonder why their demos feel generic." — classic winner/loser pivot closer
- posts.md: "The ones still building chatbots will" — another neat bow pattern

**Guru voice violations (3 instances):**
- brief.md: "Teams building products that depend on rapid capability scaling should model" — third-person prescription
- brief.md: "For builders, this means" — prescriptive language addressing builders directly  
- Additional prescriptive statements found

**LLM structural violations (1 instance):**
- posts.md: "here's the thing" — generic LLM structural label

**Not X, it's Y violations (1 instance):**
- posts.md: "isn't the generation. It's knowing" — rhetorical inversion pattern

## Fabrication Check
Checking post claims against brief...
⚠️ Posts contain first-person claims about Atlan that need verification against experience files

## Voice audit (Unable to complete - LLM proxy unavailable)
Could not execute real-time LLM calls for:
- Aayush voice score (5-dimension check)
- 15-point format audit  
- Fact-checking pass
- Adversarial review

## Council verdict: REVISE REQUIRED

**Primary failures (deterministic):**
1. **Em dashes**: 14 violations across both files - ZERO TOLERANCE rule
2. **Word count**: Brief at 1951 words, needs 2000+ minimum  
3. **Long sentences**: 28+ sentences over 22-word limit (worst: 133 words)
4. **Neat bow closers**: 3 instances of winner/loser pattern endings
5. **Guru voice**: 3+ prescriptive statements to imagined audience
6. **LLM tells**: Structural labels and rhetorical inversions

**Specific revision priorities:**
1. Replace ALL 14 em dashes with appropriate punctuation
2. Break down long sentences, especially the 133-word monster in Key Takeaways
3. Expand brief by ~100 words focused on mechanism explanation  
4. Rewrite neat bow endings as open questions or observations
5. Convert prescriptive "builders should..." to first-person observations
6. Remove "here's the thing" structural label
7. Rewrite "isn't X, it's Y" inversion positively

Due to deterministic hard-rule failures, revision is mandatory regardless of LLM review outcomes.
