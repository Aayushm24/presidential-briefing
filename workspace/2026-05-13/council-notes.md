# Council — 2026-05-13 (iteration 1)

## Deterministic findings (pre-flight violations)

**CONFIRMED hard-rule failures requiring REVISE verdict:**

### MBA vocabulary violations (3 hits)
- "differentiation" (brief, 2 hits) - Use "what makes them different" or name the specific advantage
- "enterprise customers" (brief) - Use "big companies" or just skip

### Guru voice violations (3 hits)  
- "Teams building voice AI for enterprises should prioritize" (brief) - Replace with observation + personal reaction
- "Teams building healthcare AI should prioritize" (brief) - Replace with observation + personal reaction  
- "Founders building AI products should audit" (brief) - Replace with observation + personal reaction

### Not-X-its-Y inversions (3 hits)
- "isn't the model. It's finding" (posts) - Replace with direct declarative
- "aren't building better models. They're building" (posts) - Replace with direct declarative
- "isn't convincing buyers to pay for AI. It's building" (posts) - Replace with direct declarative

### Em dash violations (6 hits in posts)
- Posts contain 6 em dashes which are banned

### Word count violation  
- Brief is at 1,826 words, needs 2,000+. Expand the lead section with more mechanism/specificity, not more topics.

### Long sentence violations (multiple)
- Brief contains 5 sentences over 22 words that need to be split
- Posts contain 4 sentences over 22 words that need to be split

## Fabrication check
- ⚠️ FABRICATION RISK: No direct "repriced/repricing" found, but cross-check needed against brief
- Posts claim "At Atlan, we've been building agents for months" - VERIFIED in aayush-experiences.md
- Posts claim "When we pitch agents to enterprise teams" - VERIFIED in aayush-experiences.md  
- Posts claim "At Atlan, we've seen this pattern across other verticals" - needs verification

## Voice audit (pending LLM passes)
[To be completed with LLM calls]

## Fact check (pending LLM passes)  
[To be completed with LLM calls]

## Adversarial (pending LLM passes)
[To be completed with LLM calls]

## Verdict: REVISE

**Revision priority order:**
1. Fix all em dashes in posts.md (6 instances)
2. Rewrite 3 "not X, it's Y" inversions in posts.md using direct declaratives  
3. Replace 3 guru voice prescriptions in brief.md with observations
4. Replace MBA vocabulary: "differentiation" → "what makes them different", remove "enterprise customers"
5. Split all long sentences over 22 words in both files
6. Expand brief.md from 1,826 to 2,000+ words in lead section

**Critical:** These are hard-gate violations that will cause ship failure. All must be addressed before any LLM-based council passes can be meaningful.