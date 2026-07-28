# Council — 2026-07-28 (iteration 1)

## Deterministic findings (CONFIRMED hard-rule failures)

**NOT_X_ITS_Y violations (2 instances):**
- "isn't your competitive advantage. It's a" (posts.md)
- "isn't a Claude problem. It's an" (posts.md)

**MBA_VOCABULARY violations (3 instances):**
- "maturation" (brief.md)
- "ecosystem" (brief.md) 
- "table stakes" (posts.md)

**LONG_SENTENCE violations (21 instances, showing key ones):**
Brief violations:
- 38w: "Claude's privacy failure exposes the risk hiding in every AI tool's share..."
- 28w: "Once a URL exists in a crawlable state, search engines will find..."
- 31w: "Legal teams at companies using Claude for sensitive work now need to..."

Posts violations:
- 69w: "LinkedIn posts, 2026-07-28 Lead: AI pricing and model selection is..."
- 37w: "The shift happened quietly: Task completion rates matter more than token costs..."
- 42w: "OPTION 2, personal-i-observer hook score: 9 Conviction: L1: The AI..."

**GURU_VOICE violation (1 instance):**
- "teams at companies using Claude for sensitive work now need to audit" (brief.md)

**EM_DASH violations (9 instances):**
- 2 in brief.md, 7 in posts.md

## Fabrication Check
Checking post claims against brief...
✅ No 'repriced/repricing' fabrication risks found.

## Voice Audit Summary (based on deterministic findings)

The deterministic pre-flight checks found CONFIRMED hard-rule failures that trigger automatic REVISE:

**Critical Issues Requiring Fix:**
1. **NOT_X_ITS_Y Pattern**: 2 instances in posts.md violate the zero-tolerance rule
   - "AI isn't your competitive advantage. It's a commodity."
   - "This isn't a Claude problem. It's an AI tool adoption problem."
   
2. **MBA Vocabulary**: 3 banned terms found
   - Brief: "maturation", "ecosystem" 
   - Posts: "table stakes"
   
3. **Long Sentences**: 21+ instances over 22-word limit across both files

4. **Guru Voice**: 1 instance in brief.md
   - "teams at companies using Claude for sensitive work now need to audit"

## Verdict: REVISE

**Total violations found**: 27+ confirmed hard-rule failures
**Ship threshold**: 0 violations required for SHIP

**Specific revision priorities** (in order):
1. **HIGH PRIORITY**: Fix NOT_X_ITS_Y inversions in posts.md - rewrite as direct statements
2. **HIGH PRIORITY**: Replace MBA vocabulary with plain English alternatives
3. **MEDIUM PRIORITY**: Break all 22+ word sentences into shorter declaratives
4. **LOW PRIORITY**: Rewrite guru voice as observation rather than prescription

**Revision notes**:
- Posts.md Option 1: Replace "AI isn't your competitive advantage. It's a commodity." with direct statement like "AI became a commodity. Every founder can buy the same models."
- Posts.md Option 3: Replace "This isn't a Claude problem. It's an AI tool adoption problem." with "This reveals the broader AI tool adoption challenge."
- Brief.md: Replace "maturation" with "real companies paying real money", "ecosystem" with specific named entities
- Posts.md: Replace "table stakes" with "everyone has it now" or "not special anymore"
