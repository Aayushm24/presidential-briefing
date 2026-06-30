# Council — 2026-06-30 (iteration 1)

## Deterministic findings

**VERDICT: REVISE** — Multiple hard-rule violations detected before LLM review.

### Kill-list violations
- Brief: 1 violation — analogy pattern: "It's like X" — turn into a question
- Posts: 1 violation — analogy pattern: "It's like X" — turn into a question

### Format violations
- Brief word count: 1346 words (needs 2000+). Expand the lead section with more mechanism/specificity, not more topics.

### Plain English violations  
- MBA vocabulary: "enterprise customers" (brief)
- Not X, It's Y inversions: 2 found in posts:
  - "isn't the tools. It's treating"
  - "isn't typing speed anymore. It's decision"
- Neat bow closers: 2 found in posts:
  - "The founders who get this early win the next wave. The ones who"
  - "the ones who figure out async supervision are ship"
- Long sentences: 15 total violations (>22 words each)
  - Brief: 4 violations including 122-word sentence starting with "Key takeaways: Gusto shipped..."
  - Posts: 11 violations including 67-word sentence starting with "LinkedIn posts, 2026 06 30 Lead..."

### Em dash violations
- Total em dashes: 19 (11 in brief, 8 in posts) — **ZERO tolerance policy**

## Voice audit (Claude Sonnet 4.6)
- Option 1: 8/15 — **REVISE** (em dashes, neat bow pattern, 'isn't X it's Y' inversion)
- Option 2: 7/15 — **REVISE** (em dashes, 'It's like X' analogy) 
- Option 3: 9/15 — **REVISE** (long sentences over 22 words)

## Fact check (Gemini)
- ✅ Gusto team size and timeline claims appear accurate based on Lenny's Newsletter source
- ⚠️ Samsung/SK Hynix "$550 billion" figure requires verification - unusually large commitment
- ✅ Cursor mobile app launch is factual per TechCrunch source
- ❌ Em dashes found: 19 total violations (11 in brief, 8 in posts) — **ZERO tolerance policy**

## Adversarial (Grok-4)
**Overall verdict: high slop density, low signal**

### Post 1 (Team size reframe):
- Logical gap: Claims small teams are superior without failure rate data or hidden support staff analysis
- Straw man: Sets up 'big team = slow' without considering hybrid models
- Anti-slop patterns: stat-stat-reframe, 'not X its Y' inversion, neat bow closer, guru voice

### Post 2 (Async coding supervision):
- Logical gap: No data on error rates or productivity gains from mobile supervision
- Straw man: False dichotomy between sync and async workflows
- Anti-slop patterns: Pattern repetition from post 1, fabricated first-person claims likely

### Post 3 (Memory infrastructure):
- Logical gap: $550B figure cited without source verification
- Straw man: Frames as 'ignore hardware vs. bet big' instead of nuanced reality
- Anti-slop patterns: Weakest link, $550B appears pulled for dramatic effect

**Freshness: saturated** — all three posts use identical LinkedIn engagement patterns

## Fabrication Check
Checking post claims against brief...
✅ No fabrication risk detected in posts

## Verdict: REVISE

**Specific revision notes:**
- Brief.md: Remove all 11 em dashes, fix "It's like X" analogy, replace "enterprise customers" with "big companies", break up 4 long sentences (especially the 122-word "Key takeaways" sentence), expand to 2000+ words with more mechanism/specificity
- Posts.md: Remove all 8 em dashes, fix "It's like X" analogy in option 2, rewrite 2 "isn't X it's Y" inversions, eliminate 2 neat bow closers ("The founders who get this early win..."), break up 11 long sentences into shorter fragments, reduce slop patterns identified by Grok-4
- ALL options: Need complete rewrite to eliminate LinkedIn engagement bait patterns and add authentic voice specificity
