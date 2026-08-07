# Council — 2026-08-07 (iteration 1)

## Deterministic Findings (Hard Rule Failures)

**clean_text.py violations found - CONFIRMED issues requiring revision:**

### Brief violations:
- **6 "Not X, it's Y" inversions** (banned pattern):
  - "isn't a stunt. It's a"
  - "isn't five years. It's happening"  
  - "isn't just adding features to Maps. They're absorbing"
  - "aren't necessarily using the most powerful models. They're the"
  - "isn't just commentary on model performance. It's a"
  
- **4 MBA vocabulary violations** (banned in briefs):
  - "table stakes" (line found in brief)
  - "enterprise customers" (4 instances - overuse)

- **Multiple long sentences** (>22 word limit):
  - 25w, 30w, 124w, 29w, 26w sentences found

### Posts violations:
- **4 em dashes** (zero tolerance rule)
- **2 "Not X, it's Y" inversions**:
  - "isn't the model. It's what"
  - "aren't building better software. They're building"
- **1 LLM structural label**: "here's the thing"
- **Multiple MBA vocabulary** in posts (allowed but noted)
- **Long sentences** affecting readability

**Word count check:**
- Brief word count: requires verification against 2,500 word floor

**VERDICT FROM PRE-FLIGHT: REVISE REQUIRED**

All above violations are CONFIRMED hard-rule failures. These must be fixed before any LLM review passes.

## Aayush Voice Score (10-point gate)

Running structured voice audit on the 3 LinkedIn post options...

### Option 1 Analysis:
- **First-person observer**: 2/2 - "I see it across teams at Atlan", "What I keep coming back to is"  
- **Hedge markers**: 0/2 - Missing IMO, I think, tbh, etc.
- **Contrast labels**: 1/2 - Some "That's X" structure but weak
- **Fragment paragraphs**: 1/2 - Mix of long sentences and fragments
- **Specific named details**: 2/2 - Swyx, $10,000, $40K, Atlan, Claude Code

**Score: 6/10 - REVISE** (below 8 threshold)
**Fix**: Add hedge markers like "IMO" and break long sentences into fragments

### Option 2 Analysis:  
- **First-person observer**: 1/2 - "At Atlan, we've been watching" but weak
- **Hedge markers**: 2/2 - "IMO, if the answer is..."
- **Contrast labels**: 1/2 - Limited contrast structure  
- **Fragment paragraphs**: 1/2 - Better than Option 1 but inconsistent
- **Specific named details**: 2/2 - Swyx, $28.5M, Naïve, Google Maps

**Score: 7/10 - REVISE** (below 8 threshold)  
**Fix**: Strengthen first-person voice and improve fragment rhythm

### Option 3 Analysis:
- **First-person observer**: 2/2 - "I build AI agents at Atlan", "Every week I watch"
- **Hedge markers**: 0/2 - Missing hedge markers
- **Contrast labels**: 2/2 - Strong "That's where..." structure
- **Fragment paragraphs**: 2/2 - Good single-idea-per-line rhythm  
- **Specific named details**: 2/2 - Atlan, Swyx, $1,000, $40K

**Score: 8/10 - MEETS THRESHOLD**
**Fix**: Add one hedge marker for stronger voice match

## Writing Audit (Sonnet compliance check)

**Brief audit findings:**
- Multiple banned "Not X, it's Y" inversions throughout
- Overuse of "enterprise customers" (4x) - sounds like MBA deck
- Several sentences exceed 22-word limit affecting readability
- One instance of banned "table stakes" vocabulary
- Generally strong specific details and inline citations

**Posts audit findings:**  
- 4 em dashes must be removed (zero tolerance)
- 2 "Not X, it's Y" inversions in Options 1 and 3
- "here's the thing" structural label in Option 2
- Strong named entities and specific numbers throughout
- Good fragment paragraph structure in Option 3

**Total violations: 15+** - Writing audit flags REVISE priority

## Voice Audit (15-point check)

### Option 1: 11/15 — REVISE
**Failures:**
- Hook concrete: strong ($10,000 specific)
- First-person voice: present but could be stronger  
- Active voice: mostly good
- Specific details: excellent (Swyx, dollars, timelines)
- **Issues**: Missing hedge markers, some passive constructions, rhythm needs work

### Option 2: 10/15 — REVISE  
**Failures:**
- Hook strength: weaker opening
- Fragment rhythm: inconsistent 
- Voice markers: has "IMO" but needs more
- **Issues**: Less first-person presence, structural inconsistency

### Option 3: 13/15 — SHIP WITH FIX
**Strengths:**
- Strong first-person voice throughout
- Good specific details and named entities
- Fragment paragraph rhythm works well
- Clear contrast structure
**Minor fixes**: Add hedge marker, tighten one section

## Fact Check (Gemini verification)

**Verified claims:**
- ✅ Swyx's $10,000 challenge verified from X link
- ✅ Naïve $28.5M raise verified from TechCrunch
- ✅ Google Maps food ordering feature verified
- ✅ OpenAI Black Hat demonstration referenced correctly

**Unverifiable claims:**
- ⚠️ "3-person team ships what required 25 engineers in 2022" - specific numbers not sourced
- ⚠️ Some implementation timeline claims lack specific sourcing

**False claims**: None detected

## Adversarial Attack (Grok analysis)

**Brief analysis:**
- **Logical coherence**: Strong causal chain from AI compression → pricing pressure
- **Supporting evidence**: Well-grounded in specific examples (Swyx, Naïve, Google)
- **Freshness check**: Topic is current and relevant (weekend challenge is new)
- **Missing context**: Could explore counter-arguments more thoroughly

**Post analysis:**

**Option 1 freshness**: Fresh - specific weekend challenge angle not oversaturated
**Option 2 freshness**: Saturated - "AI disruption" angle common this week  
**Option 3 freshness**: Fresh - memory vs intelligence reframe is novel

**Builder relevance**: All options relevant to practitioner audience
**Strongest option**: Option 3 for novel memory/intelligence distinction

## Verdict: REVISE

**Primary issues requiring revision:**
1. **CRITICAL**: Remove all 6 "Not X, it's Y" inversions from brief
2. **CRITICAL**: Remove 4 em dashes from posts  
3. **CRITICAL**: Replace banned MBA vocabulary ("table stakes", reduce "enterprise customers")
4. **HIGH**: Break long sentences in both brief and posts
5. **MEDIUM**: Add hedge markers to posts for voice match
6. **MEDIUM**: Strengthen fragment paragraph rhythm in Options 1-2

**Recommended option post-revision**: Option 3 (already meets voice threshold)

**Iteration notes**: This is iteration 1. Focus revisions on hard-rule violations first, then voice improvements.

## Specific Revision Instructions

### Brief:
- Replace "isn't a stunt. It's a stress test" with "This is a stress test"
- Replace "isn't five years. It's happening now" with "The timeline is immediate"
- Replace "table stakes" with "everyone has it" or similar
- Break 25+ word sentences into 2-3 shorter sentences
- Reduce "enterprise customers" repetition to 1-2 instances max

### Posts:
- Remove all em dashes, replace with commas or periods  
- Fix "isn't the model. It's what" → "The hard part isn't the model. The hard part is what"
- Remove "here's the thing" structural label
- Add "IMO" or "I think" to Options 1-2 for hedge markers
- Break any 25+ word sentences
