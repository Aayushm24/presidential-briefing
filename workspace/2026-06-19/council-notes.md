# Council — 2026-06-19 (iteration 1)

## Deterministic findings (regex violations — confirmed hard failures)

**Pre-flight violations found: REVISE REQUIRED**

### Kill-list violations (posts.md):
- **analogy_pattern**: "It's like X" — turn into a question
  - Found in posts.md: "It's like the pizza delivery service being worth more than the pizza restaurant."

### Golden format violations (brief.md):
- **mba_vocabulary**: "table stakes" — use "everyone has it" 
- **word_count**: brief is at 1478 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### clean_text.py violations:
- **mba_vocabulary_violation**: 1 (CONFIRMED: "table stakes", "enterprise customers" 3x)
- **long_sentence_violation**: 2 (CONFIRMED: multiple sentences >22 words)
- **guru_voice_violation**: 0 (but flagged 2 instances: "teams who need to retrofit", "For builders,")
- **not_x_its_y_violation**: 0 (but flagged 1: "isn't about AI tooling. It's about who")
- **em_dash**: 4 found in posts.md

**VERDICT SO FAR: REVISE** (hard gate failures require fixing before LLM passes matter)

---

## Fabrication Check

✅ No "repriced/repricing" language found in posts.md
Cross-checking post claims against brief for factual accuracy...

---

## Aayush Voice Score (10-point audit, gate at 8/10)

### Option 1 (commentary-take): 6/10 — REVISE
- first_person_observer: 2/2 ✅
- hedge_markers: 0/2 ❌ (missing IMO/tbh/etc)
- contrast_labels: 2/2 ✅ ("That's not a model company. That's infrastructure.")  
- fragment_paragraphs: 1/2 ⚠️
- specific_named_details: 1/2 ⚠️
**Fix:** Add one natural hedge — e.g. 'tbh, most teams treat inference as an afterthought' or 'IMO the Baseten raise isn't about tooling' — to soften the declarative tone where opinion is being stated as fact.

### Option 2 (data-point): 8/10 — SHIP ✅
- first_person_observer: 2/2 ✅
- hedge_markers: 1/2 ⚠️
- contrast_labels: 2/2 ✅ ("That's distribution.")
- fragment_paragraphs: 2/2 ✅  
- specific_named_details: 1/2 ⚠️
**Improvement:** Replace 'one customer conversation' with a named customer type or real Atlan example (e.g. 'a mid-market data team running 500 queries/day') and add one concrete number to the Atlan agent observation to lift specificity from 1 to 2.

### Option 3 (pattern-observation): 7/10 — REVISE
- first_person_observer: 2/2 ✅  
- hedge_markers: 0/2 ❌ (missing IMO/tbh/etc)
- contrast_labels: 1/2 ⚠️
- fragment_paragraphs: 2/2 ✅
- specific_named_details: 2/2 ✅ (Jake, 47 meetings, $30K, month timelines)
**Fix:** Insert one hedge at the opinion pivot — e.g. change 'Your model choice matters less than your serving strategy' to 'IMO your model choice matters less than your serving strategy' — and sharpen the pizza analogy into a proper contrast label ('That's not a restaurant business. That's logistics.') to lift contrast_labels from 1 to 2.

**VOICE VERDICT: REVISE** (Options 1 & 3 < 8/10 threshold)

---

## Writing Audit (Sonnet)

⚠️ WRITING AUDIT: Multiple violations found
- **VAGUE GENERICS**: "every builder", "most AI model companies", "most teams" — replace with named entities or specific numbers
- **UNSOURCED STATS**: "60%" (GLM-5.2 claim), various percentages without named sources 
- **MBA VOCABULARY**: "table stakes" in brief, already flagged by pre-flight
- **SENTENCE CASE**: "for builders building generative video applications" starts lowercase in brief (line 74)

---

## Voice Audit (15-point, Sonnet)

### Option 1 (commentary-take): 10/15 — SHIP WITH FIX
- Hook: ✅ 3/3 (scroll-worthy, 67 chars, concrete)
- Voice: ❌ 3/5 (uppercase "I" throughout, otherwise clean)
- Content: ❌ 3/4 (no story opener, otherwise solid)
- Format: ✅ 3/3 (clean)
**Fix:** (1) Lowercase all "I" → "i", (2) Replace opener "Someone raised $1.5B..." with named moment before the stat

### Option 2 (data-point): 11/15 — SHIP WITH FIX ⭐ BEST
- Hook: ✅ 3/3 
- Voice: ❌ 3/5 (uppercase "I" issue only)
- Content: ❌ 3/4 (no story opener)
- Format: ✅ 3/3
**Fix:** (1) Lowercase "I" → "i", (2) Open with grounding scene (move the Atlan accounting moment to line 1)

### Option 3 (pattern-observation): 10/15 — REVISE
- Hook: ❌ 2/3 (79 chars = too long)
- Voice: ❌ 3/5 (uppercase "I")  
- Content: ❌ 3/4 (no story opener)
- Format: ❌ 2/3 (CTA is engagement bait)
**Issues:** Hook too long, question-CTA is generic engagement bait

**VOICE AUDIT VERDICT: REVISE** (only Option 2 hits 11/15 acceptable threshold)

---

## Fact Check (Gemini - attempted but model unavailable)

⚠️ **KEY CLAIMS TO VERIFY IN REVISE:**
- Baseten $1.5B raise at $13B valuation (verify exact amounts)
- "60%" memory reduction claim for GLM-5.2 (needs source)
- "$20-50 per million tokens" for GPT-4 level inference (verify current pricing)
- Snap/Dotmo spin-off for AI video costs (verify company name and details)

---

## Adversarial Attack (Grok - skipped, already have REVISE verdict)

Pre-flight and voice audits found sufficient violations to trigger REVISE without need for additional adversarial review.

---

## COUNCIL VERDICT: REVISE

**Multiple gate failures detected:**

### Hard Failures (pre-flight):
1. **Word count**: Brief at 1478 words, needs 2000+ (expand lead section)
2. **MBA vocabulary**: "table stakes" → use "everyone has it" 
3. **Em dashes**: 4 found in posts.md (must eliminate all)
4. **Analogy pattern**: "It's like the pizza delivery service..." → convert to question form
5. **Long sentences**: Multiple >22 words flagged

### Voice Failures (Aayush 10-point):
- Option 1: 6/10 (missing hedge markers)
- Option 2: 8/10 ✅ SHIP threshold
- Option 3: 7/10 (missing hedge markers)

### Format Failures (15-point): 
- Option 1: 10/15 (uppercase "I", no story opener)
- Option 2: 11/15 (uppercase "I", no story opener) 
- Option 3: 10/15 (hook too long, CTA engagement bait)

**REVISE PRIORITY ORDER:**
1. **CRITICAL**: Fix pre-flight violations (word count, MBA vocab, em dashes, analogy)
2. **HIGH**: Add hedge markers to Options 1 & 3 ("IMO", "tbh")
3. **MEDIUM**: Lowercase all "I" → "i" across all posts
4. **MEDIUM**: Add story openers to Options 1 & 2
5. **LOW**: Verify factual claims (Baseten amounts, GLM-5.2 60%, pricing)

**Recommended option after fixes: Option 2** (highest scores, most salvageable)