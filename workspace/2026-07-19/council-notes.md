# Council — 2026-07-19 (iteration 1)

## Deterministic findings (PRE-FLIGHT HARD FAILURES)

**Verdict: REVISE** — Hard rule violations detected before LLM passes.

### Format violations (2 detected)
- mba_vocab_commoditization_hits=1 (expect 0 — use 'gets cheap' / 'everyone has it')  
- word_count=1661 (expect 2000+)

### Clean text violations
**Em dashes (7 total):** ZERO TOLERANCE violations in posts.md
**Not X. It's Y violations (5 total):**
- "isn't just computer use. It's workflow" (posts.md)
- "is not a simple app. It's a" (brief.md + posts.md)
- "isn't about capability anymore. It's about recognizing" (posts.md)
- "isn't just another model launch. It's the" (posts.md)

**Guru voice violations (5 total):**
- "Teams building customer-facing products need to run" (brief.md + posts.md)
- "Teams building on closed APIs need to model" (brief.md)
- ". For builders," (brief.md)
- "founders building on closed APIs should model" (posts.md)

**MBA vocabulary violations:**
- "commoditization" (brief.md + posts.md) — replace with "gets cheap" or "everyone has it"
- "ecosystem" (brief.md)

**Word count violation:**
Brief is at 1661 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

**Long sentence violations (22 total):**
Multiple sentences exceeding 22 words detected across both files.

## Fabrication Check
Checking post claims against brief...
⚠️ No repricing language detected.

## Verdict: REVISE

**Critical issues requiring revision:**

1. **Word count:** Brief at 1661 words, needs 2000+ minimum per blueprint
2. **Hard rule violations:** Multiple "Not X. It's Y" inversions across both files
3. **Voice violations:** Guru voice patterns ("Teams should", "Founders need to")  
4. **MBA vocabulary:** "commoditization" and "ecosystem" must be replaced
5. **Long sentences:** 22+ violations exceed blueprint limits

**Specific revision notes:**

### Brief.md fixes required:
- Line "is not a simple app. It's a" → "Blender has hundreds of tools, nested menus, and complex workflows."
- Replace "commoditization" with "gets cheap" or "everyone has it"
- Replace "ecosystem" with specific named examples
- "Teams building customer-facing products need to" → "Teams building customer products now"
- Expand word count by 350+ words in lead section mechanism explanation

### Posts.md fixes required:
- "isn't just computer use. It's workflow" → "Agents installing software autonomously signals workflow replacement."
- "isn't about capability anymore. It's about recognizing" → "The gap shifts from capability to recognition"  
- "isn't just another model launch. It's the" → "This model launch marks the moment"
- Remove "founders building on closed APIs should model" guru voice

**LLM passes would show additional issues but deterministic violations alone require REVISE verdict.**