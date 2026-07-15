# Council — 2026-07-15 (iteration 1)

## Deterministic findings (Pre-flight)

**CONFIRMED VIOLATIONS found by clean_text.py - these require fixes before ship:**

### Brief violations:
- **NOT X. ITS Y violations (5):**
  - "aren't building the best models. They're building"
  - "aren't piloting AI coding tools anymore. They're standardizing"
  - "aren't just using Codex for individual coding tasks. They're building"
  - "aren't treating AI as a helper tool anymore. They're treating"
  - "isn't just about user acquisition. It's about workflow"

- **GURU VOICE violations (3):**
  - "companies will need to hit"
  - "developers who learned to code alongside AI, product managers who want to prototype"
  - "companies will need to cap"

- **MBA VOCABULARY (2):**
  - "market maturity"
  - "enterprise customers"

- **LONG SENTENCES (5):**
  - 32w: "Agentic coding tools reach platform scale as hundreds of millions in ARR..."
  - 34w: "When Codex adds 1 million users daily https://www.latent.space/p/ainews not much happened today..."
  - 135w: "Key takeaways: Cognition's hundreds of millions in ARR post Windsurf acquisition proves..."
  - 37w: "Since then, the combined company has 'shipped dozens of new features, added..."
  - 23w: "One year from acquisition to hundreds of millions in ARR means Cognition..."

### Posts violations:
- **EM DASHES (6 total) - HARD FAIL**
- **NOT X. ITS Y violations (1):**
  - "aren't building better models. They're building"

- **GURU VOICE violations (1):**
  - "developer on a team uses AI coding effectively, the rest have to adapt"

- **MBA VOCABULARY (2):**
  - "moat"
  - "enterprise customers"

**PRE-FLIGHT VERDICT: REVISE** - Multiple hard-rule violations detected

## Aayush Voice Score (10-point gate)

**Option 1: 9/10 - SHIP** (lowest dimension: hedge_markers)
- first_person_observer: 2 (Strong: "Every founder I talk to", present-tense observer placement)
- hedge_markers: 1 (Single IMO feels bolted on rather than natural opinion pivot)
- contrast_labels: 2 (Clear: "That's not the question anymore")
- fragment_paragraphs: 2 (Good rhythm throughout)
- specific_named_details: 2 (Cognition, Windsurf, specific dollar amounts)

**Option 2: 6/10 - REVISE** (lowest dimension: hedge_markers)
- first_person_observer: 2 (Strong: "I've been tracking", "Every week I watch")
- hedge_markers: 0 (ZERO hedge markers - reads like press release)
- contrast_labels: 1 (Weak contrast labels)
- fragment_paragraphs: 2 (Good rhythm)
- specific_named_details: 1 (Too generic: "my network", "smaller tools")

**Option 3: 6/10 - REVISE** (lowest dimension: hedge_markers)
- first_person_observer: 1 (Weak: only "I see this pattern", buried mid-post)
- hedge_markers: 0 (ZERO hedge markers - sounds like strategy memo)
- contrast_labels: 2 (Strong: "That's the software playbook flipped upside down")
- fragment_paragraphs: 2 (Good rhythm)
- specific_named_details: 1 (Vague: "50-person orgs", "dozens of features")

**VOICE VERDICT: REVISE** - 2 of 3 options failed the 8/10 threshold

## Fact Check (Claude Sonnet)

**MAJOR FACTUAL ERROR IDENTIFIED:**

**Brief & Posts contain FALSE claim:** "Cognition acquired Windsurf" 
- **CORRECT:** OpenAI acquired Windsurf for ~$3 billion in May 2025 (The Verge, Bloomberg)
- **CONFUSION:** Cognition builds Devin (different company). This is a core factual error that undermines the entire narrative in Options 1 & 3

**Brief fact issues:**
- ❌ FALSE: "Cognition acquired Windsurf" (Actually OpenAI acquired Windsurf)
- ❌ FALSE: Math calculations based on false acquisition premise
- ⚠️ UNVERIFIABLE: "hundreds of millions in ARR" (single swyx tweet, no verification)
- ⚠️ UNVERIFIABLE: "Codex 1M daily users" (newsletter source, not official OpenAI)
- ⚠️ Em dashes found: 3

**Option 1 fact issues:**
- ❌ FALSE: Central Cognition/Windsurf acquisition claim
- ⚠️ UNVERIFIABLE: "$500K enterprise deals" figures (illustrative)
- ✅ VERIFIED: ChatGPT 1M users in 5 days

**Option 2 fact issues:** 
- ✅ VERIFIED: ChatGPT 1M users, GitHub Copilot 2021 launch
- ⚠️ UNVERIFIABLE: Codex 1M daily (newsletter source)
- ✅ No false claims flagged

**Option 3 fact issues:**
- ❌ FALSE: "Cognition paid hundreds of millions for Windsurf" 
- ❌ FALSE: Deal value (~$3B actual, not "hundreds of millions")
- ⚠️ Em dashes found: 1

**FACT CHECK VERDICT:** REVISE - Core factual error must be fixed before ship

## Adversarial Attack (Grok with X Search)

**Brief issues identified:**
- **LOGICAL GAPS:** Key takeaways claim "Codex 1M daily users" and "OpenAI ChatGPT repositioning" but research.md contains ZERO data on either - only Cognition ARR sourced
- **UNSUPPORTED CLAIMS:** Both Codex and OpenAI claims need deletion - no research basis
- **ARGUMENT BREAKDOWN:** "Companies winning aren't building best models, they're building distribution" - unsupported leap from single company ARR data

**All 3 posts FAILED Blueprint style check:**
- **Option 1:** Corporate Analyst (REJECT) - generic market summary, saturated angle
- **Option 2:** Corporate Analyst (REJECT) - same market-summary voice, already covered on X July 14  
- **Option 3:** Corporate Analyst (REJECT) - identical framing to other options

**DIVERSITY CHECK:** FAIL - all 3 use Corporate Analyst style instead of different Blueprint styles
- **FRESHNESS:** All 3 flagged as "saturated" - angle already covered by multiple X posts 
- **BUILDER RELEVANCE:** All 3 flagged as NOT builder-relevant

**ADVERSARIAL VERDICT:** REJECT ALL 3 - No personal experience, contrarian angle, or differentiation

## FINAL COUNCIL VERDICT: REVISE

**Revision required on ALL fronts:**

1. **FACTUAL ERRORS (CRITICAL):**
   - Fix "Cognition acquired Windsurf" → "OpenAI acquired Windsurf" 
   - Remove unsourced Codex 1M daily users claim
   - Remove unsourced OpenAI ChatGPT repositioning claim

2. **CLEAN_TEXT VIOLATIONS (MANDATORY):**
   - Fix 6 em dashes in posts (hard fail)
   - Fix 6 "not X, it's Y" inversions in brief + posts
   - Fix 4 guru voice violations
   - Fix MBA vocabulary ("moat", "enterprise customers")

3. **VOICE ISSUES (QUALITY GATE):**
   - Options 2 & 3 failed 8/10 Aayush voice score (missing hedge markers)
   - All 3 posts rejected by adversarial review as "Corporate Analyst" style
   - Need Blueprint style diversity: Contrarian Philosopher, Vulnerable Victor, Relatable Human

4. **CONTENT GAPS:**
   - Posts lack first-person observer moments
   - Missing contrarian/personal angles 
   - Saturated take already covered on X

**ITERATION 1 VERDICT: REVISE** 
**BEST SALVAGEABLE OPTION:** Option 2 (cleanest facts, no Cognition error)
**REVISION PRIORITY:** Fix factual errors first, then voice/style issues
