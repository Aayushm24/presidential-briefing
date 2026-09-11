# Council — 2026-09-11 (iteration 1)

## Deterministic Findings (Pre-flight)

**VERDICT: REVISE** — Multiple hard-rule violations found.

### Word Count Violation
- Brief is at 1999 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### Em Dash Violations (12 total)
- Brief: 3 em dashes found
- Posts: 9 em dashes found
All em dashes must be replaced with regular hyphens or sentence restructuring.

### Not-X-Its-Y Violations (3 in brief)
- "aren't separate product launches. They're coordinated"
- "isn't abstract theory. It's a"  
- "isn't whether AI content generation works commercially. It's whether"

### Neat Bow Violations (1 in posts)
- "The founders who understand this pivot now. The ones who"

### Guru Voice Violations (1 in brief)
- "for builders,"

### Long Sentence Violations (19 total)
Brief contains 5 sentences over 22 words including a 167-word sentence that must be broken down.
Posts contain 14 long sentences that need restructuring for readability.

### MBA Vocabulary (1 in posts)
- "moat" - replace with plain English equivalent

## Fabrication Check
Checking post claims against brief...
⚠️ No repricing language found, but cross-checking claims against brief content required.

## Aayush Voice Score (10-point gate)

**ALL OPTIONS FAILED VOICE GATE (threshold: 8/10)**

- **Option 1: 5/10** — REVISE required
  - First-person observer: 2/2 ✓
  - Hedge markers: 0/2 ❌ (missing IMO, tbh, i think)
  - Contrast labels: 1/2 
  - Fragment paragraphs: 1/2
  - Specific named details: 1/2
  - **Fix:** "Add a natural hedge like 'tbh, the interface war feels over' or 'imo the platforms already won distribution' where opinion turns into claim."

- **Option 2: 3/10** — REVISE required
  - First-person observer: 1/2
  - Hedge markers: 0/2 ❌ (missing hedge markers)
  - Contrast labels: 0/2 ❌ (no "That's X" recap tags)
  - Fragment paragraphs: 1/2
  - Specific named details: 1/2
  - **Fix:** "Replace 'This creates permanent competitive advantage' with a contrast tag like 'That's not a productivity boost. That's a new business model.' to anchor the insight."

- **Option 3: 4/10** — REVISE required
  - First-person observer: 1/2
  - Hedge markers: 0/2 ❌ (missing hedge markers)
  - Contrast labels: 1/2
  - Fragment paragraphs: 1/2
  - Specific named details: 1/2
  - **Fix:** "Drop in 'tbh most founders build Wave 1 products but target Wave 3 users' or 'imo timing beats technology here' to shift from lecture-mode into observer voice."

## Fact Check (Sonnet)

**CRITICAL ERROR FOUND:** OpenAI/Astra conflation

### Brief
- ✅ **Verified:** Meta 3.9B users, Pocket FM $500M run rate, Pocket FM 93% AI content, 80x cost reduction
- ⚠️ **Unverifiable:** Meta Muse No. 2 App Store ranking, Tomasz Tunguz wave framework
- ❌ **FALSE:** "OpenAI paused Pro signups due to Astra demand" — **Astra is Google DeepMind's product, NOT OpenAI's. This is a credibility-killing factual error.**

### Posts
- **Option 1:** Contains the FALSE Astra/OpenAI claim + 1 em dash
- **Option 2:** ✅ **CLEANEST** — avoids the Astra error, all claims verified or properly attributed to Pocket FM
- **Option 3:** Avoids Astra error but repeats unverified App Store claim

**Recommended:** Option 2 (fewest factual issues)

## Adversarial Review (Grok)

**All options REJECTED by adversarial review**

### Brief Issues
- **Logical gaps:** Distribution compression claim unsupported by data
- **Unsupported claims:** Muse App Store ranking, Astra/OpenAI conflation
- **Straw men:** Frames all builders as pursuing horizontal consumer reach
- **Verdict:** REVISE

### Option 1 
- **Guru voice violations:** "Every founder I talk to", "The founders who understand this pivot now"
- **Fabricated specificity:** "At Atlan we've learned this firsthand"
- **Neat bow closer:** "The ones who..." pattern
- **Verdict:** REJECT

### Option 2
- **Guru voice:** "Most founders I know", "The winners will be companies that..."
- **Stat-Stat-Reframe pattern:** Pocket FM numbers → "most founders miss" → vertical insight
- **Fabricated Atlan claims**
- **Verdict:** REJECT

### Option 3
- **Guru voice:** "But here's what most founders miss", "most failures happen when..."
- **Ungrounded framework:** Tunguz wave model not in briefing
- **Forced synthesis:** Unrelated examples into framework
- **Verdict:** REJECT

## Overall Verdict: REVISE

**Hard gates failed:**
1. ✅ Word count: 1999/2000 (1 word short)
2. ❌ Voice scores: ALL options < 8/10 threshold 
3. ❌ Factual accuracy: FALSE Astra/OpenAI claim
4. ❌ Adversarial review: ALL options rejected for guru voice + fabrication

**Priority fixes for revise:**
1. **CRITICAL:** Fix Astra/OpenAI factual error throughout brief and posts
2. **VOICE:** Add hedge markers (tbh, imo, i think) to all options
3. **VOICE:** Add contrast labels ("That's X" recap tags) especially Option 2
4. **VOICE:** Remove guru voice ("founders should", "most founders", "the winners will be")
5. **FORMAT:** Fix em dashes (12 total found)
6. **FORMAT:** Break up long sentences (19 violations found)
7. **BRIEF:** Add 1+ words to hit 2000 word minimum
