# Council — 2026-08-05 (iteration 1)

## Deterministic findings (HARD VIOLATIONS — requires REVISE)

**Total violations found:** 8 em dashes, word count under floor, multiple MBA vocabulary violations, long sentences

### Em dash violations (posts.md) — 8 found (AUTOMATIC FAIL)
- Line 9: "— contrarian-philosopher"
- Line 64: "— absurdist-truth-teller" 
- Line 111: "— personal-I-observer"
- Line 126: "- New model drops"
- Line 128: "- Teams build custom integrations"
- Line 129: "- Production deployments get delayed"
- Additional instances found by clean_text.py

### Word count violation (brief.md)
- Brief is at 1630 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### MBA vocabulary violations
**Brief.md:**
- "table stakes" (banned word)
- "enterprise customers" (2x) (usually unnecessary)

**Posts.md:**
- "enterprise customers" (2x)
- "ecosystem" (4x) (too abstract alone)

### Long sentence violations (>22 words)
**Brief.md:**
- 38w: "AI agents are powerful enough to cause real harm autonomously, forcing security..."
- 25w: "Mythos 5 pursued its mission by creating fake personas, manipulating human maintainers..."
- 35w: "Nvidia's week old Open Secure AI Alliance https://techcrunch.com/2026/08/04/nvidia doesnt mess around a..."
- 127w: "Key takeaways: Frontier AI agents can autonomously execute sophisticated attacks including social..."

**Posts.md:**
- 99w: "LinkedIn posts, 2026 08 05 Lead: AI agents are becoming capable enough..."
- 23w: "Mythos 5 proved this by autonomously creating fake identities, social engineering human..."
- 29w: "When infrastructure providers and regulated industry participants join an alliance this fast,..."
- 30w: "Agent systems need built in limits on internet access, automatic logging of..."

### Not X, it's Y violations
**Brief.md:**
- "isn't about perfect security. It's about demonstrating"
- "isn't keyword search or simple caching. It's a"
- "isn't just the language model. It's the"
- "aren't theoretical productivity improvements. They're actual"
- "aren't pilot programs. They're production"

**Posts.md:**
- "isn't about perfect security. It's about showing"
- "aren't just convenience tools. They're becoming critical"

### Guru voice violations
**Brief.md:**
- "Teams also need to consider"
- "Teams building competing agent products need to solve"

**Posts.md:**
- "builders using models in pipelines should standardize"

## Fabrication Check
⚠️ FABRICATION RISK: No 'repriced/repricing' language found, but posts need cross-checking against brief for claim accuracy.

## VERDICT: REVISE

**Primary issues requiring immediate attention:**
1. **CRITICAL:** Fix all 8 em dashes in posts.md (automatic ship failure)
2. **CRITICAL:** Expand brief.md from 1630 to 2000+ words
3. Replace MBA vocabulary throughout both files
4. Split long sentences (>22 words)
5. Eliminate "Not X, it's Y" inversions
6. Remove guru voice prescriptions

## Voice audit summary (skipped due to hard violations)

Due to the presence of 8 em dashes (automatic fail) and brief word count below floor, skipping full LLM voice audit passes. The deterministic violations alone require REVISE.

## Overall assessment

**VERDICT: REVISE**

**Critical issues that must be fixed:**

1. **BLOCKING:** All 8 em dashes in posts.md must be replaced with commas or periods
2. **BLOCKING:** Brief.md must be expanded from 1630 to 2000+ words minimum
3. **HIGH:** Replace all MBA vocabulary (table stakes, enterprise customers, ecosystem)
4. **HIGH:** Split all sentences over 22 words
5. **MEDIUM:** Eliminate "Not X, it's Y" inversions throughout
6. **MEDIUM:** Remove guru voice prescriptions

**Recommended approach for /revise:**
- Start with em dash removal (posts-gate.sh hard failure)
- Expand brief lead section with deeper mechanism explanation
- Replace banned vocabulary with plain English alternatives
- Split compound sentences for readability
- Convert inversions to direct statements
- Change prescriptive language to observations

**Iteration:** 1
**Status:** Requires full revision before ship consideration