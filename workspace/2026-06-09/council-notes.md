# Council — 2026-06-09 (iteration 1)

## Deterministic findings (pre-flight regex checks)

**Total violations found: 7 major violations requiring REVISE**

### Brief violations (brief.md):
- **MBA vocabulary violations (2):** "differentiation" appears twice, "ecosystem" appears once
- **Long sentence violations (24):** Multiple sentences over 22 words including 152-word sentence in Key takeaways
- **"Not X, it's Y" inversion (1):** "aren't isolated trends. They're creating"
- **Neat bow violation (1):** "The ones who figured out AI automation first will"
- **Em dash violations (1):** One em dash found

### Post violations (posts.md):
- **Em dash violations (8):** Multiple em dashes throughout posts
- **Long sentence violations:** Multiple sentences over 22 words
- **"Not X, it's Y" inversion (1):** "isn't about features. It's about runway"
- **Neat bow violation (1):** "The ones who figure out AI automation now will"

### Word count check:
- **Brief word count: 2,319 words** — PASSES minimum 2,000 requirement

**VERDICT SO FAR: REVISE** (due to deterministic violations)

---

## Voice audit (Gemini)

- **Option 1:** 14/15 — ship with fix (lowercase_i violation: uses uppercase 'I' in multiple places)
- **Option 2:** 14/15 — ship with fix (lowercase_i violation: uses uppercase 'I' in 'I see this pattern everywhere')
- **Option 3:** 14/15 — ship with fix (lowercase_i violation: uses uppercase 'I' in 'I've been thinking')

All options pass the 12/15 ship threshold but need lowercase 'i' fixes.

## Fact check (Gemini)

**Brief violations:**
- ❌ **FALSE:** "Apple waives cloud API costs for developers under 2M downloads" — Apple has not announced any such developer API pricing tier
- ❌ **FALSE:** "Siri AI upgrades at WWDC 2026" — WWDC 2026 is future; Apple Intelligence was announced at WWDC 2024
- ❌ **FALSE:** "2024 false-advertising history" — Apple does not have a 2024 false-advertising settlement regarding AI demos
- ⚠️ **UNVERIFIABLE:** "100,000 AI requests monthly costs $200-400 for GPT-4" — Plausible but highly dependent on tokens per request

**Post violations:**
- **All 3 options:** Repeat the fabricated "2M downloads" pricing tier and false advertising settlement claims
- **Options 1 & 3:** Include fabricated Atlan team experiences not verified in aayush-experiences.md

## Adversarial attack (Grok)

**Brief verdict:** REVISE
- Multiple unsupported claims beyond the core research item #4
- Logical gaps between key takeaways and available research
- Claims about Siri upgrades, WWDC 2026, coordinated rollout not supported by research

**Post verdicts:**
- **Option 1:** REVISE (fabricated Atlan experience)
- **Option 2:** REVISE (neat-bow closer violates voice rules)
- **Option 3:** REJECT (multiple guru/advice prescriptions + fabricated claims)

**Freshness check:** All angles are fresh - no similar takes found on X in past 7 days
**Builder relevance:** High - practitioners would share content about API costs and platform lock-in

## Overall Verdict: REVISE

**Critical issues requiring fixes:**
1. **FALSE CLAIMS:** Remove all references to:
   - Apple's "2M downloads" API pricing tier (fabricated)
   - 2024 false-advertising settlement (fabricated)  
   - Siri upgrades at WWDC 2026 (wrong timeline)
   - Coordinated rollout claims not in research

2. **VOICE VIOLATIONS:**
   - Fix all uppercase 'I' to lowercase 'i' in all posts
   - Remove neat-bow closer from Option 2
   - Remove guru/advice voice from Option 3
   - Remove fabricated Atlan experiences from Options 1 & 3

3. **DETERMINISTIC VIOLATIONS (still need fixing):**
   - Fix "Not X, it's Y" inversions in both brief and posts
   - Fix neat bow patterns
   - Split long sentences over 22 words
   - Replace MBA vocabulary terms

**Recommended approach:** Focus revision on Option 2 (absurdist-truth-teller) as it has the fewest violations and strongest blueprint style match.