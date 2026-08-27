# Council — 2026-08-27 (iteration 1)

## Deterministic findings (regex pre-flight)

Based on scripts/clean_text.py output, the following violations require immediate revision:

### Brief violations:
- **Word count:** 1,547 words (below 2,500 floor). Expand the lead section with more mechanism/specificity, not more topics.
- **Guru voice:** 2 instances found:
  - "team hosting models" 
  - "Cybersecurity experts warn organizations must upgrade"
- **MBA vocabulary:** 1 instance - "infrastructure dependency"
- **Long sentences:** 5 over 22 words:
  - 37w: "NVIDIA's $12.9B HuggingFace buy centralizes AI infrastructure control NVIDIA https://techcrunch.com/2026/08/26/nvidia closes in..."
  - 32w: "Builders who rely on HuggingFace for model hosting, dataset access, and open..."
  - 135w: "Key takeaways: NVIDIA's HuggingFace acquisition creates rare vertical integration from training hardware..."
  - 28w: "Unlike traditional software where developers can easily switch hosting providers or databases..."
  - 26w: "Teams building on these cloud platforms still depend on HuggingFace for open..."

### Posts violations:
- **Em dashes:** 9 found in posts.md (zero tolerance - all must be removed)
- **Kill words:** 4 instances requiring replacement  
- **Guru voice:** 1 instance - "Teams shipping AI products need to understand"
- **Long sentences:** Multiple over-length sentences in metadata and content

**PRE-FLIGHT VERDICT:** REVISE REQUIRED due to word count violation, em dashes, and multiple long sentences.

## Fabrication Check

Checking post claims against brief...

✅ All major claims in posts trace back to brief content
⚠️ No "repriced/repricing" language found
✅ Posts stay grounded in brief facts and don't fabricate statistics

## Aayush Voice Score (10-point, gate at 8)

- **Option 1**: 8/10 - SHIP (first_person: 2, hedge_markers: 0, contrast_labels: 2, fragments: 2, specifics: 2)
  - Fix: Add one hedge marker (IMO, i think, etc.) for natural opinion signaling
- **Option 2**: 8/10 - SHIP (first_person: 2, hedge_markers: 0, contrast_labels: 2, fragments: 2, specifics: 2)  
  - Fix: Add hedge marker where personal opinion emerges
- **Option 3**: 7/10 - REVISE (first_person: 1, hedge_markers: 2, contrast_labels: 0, fragments: 2, specifics: 2)
  - Fix: Add "That's X." recap tag after a key insight to strengthen contrast labeling

## Writing Audit (Sonnet)

### Brief violations:
- ✅ EM DASHES: 0 found
- ❌ NOT X. Y. NEGATION: None found
- ✅ SENTENCE CASE: All sentences properly capitalized
- ❌ VAGUE GENERICS: "every team using open AI infrastructure" - should name specific teams or percentage
- ❌ UNSOURCED STATS: "400,000 models and 100,000 datasets" needs HuggingFace source link
- ❌ PASSIVE VOICE: Multiple instances - "is controlled", "are affected"
- ❌ PADDING: Some sentences restate prior content without new information
- ✅ CONVICTION: Sections end with clear takes

### Post violations:
- ❌ EM DASHES: 9 found across posts (CRITICAL - zero tolerance)
- ✅ NOT X. Y. NEGATION: Clean
- ❌ SENTENCE CASE: Several lowercase sentence starts in formatting
- ❌ VAGUE GENERICS: "Every team I talk to", "Most teams building AI products"
- ✅ UNSOURCED STATS: Numbers trace to brief sources
- ❌ PASSIVE VOICE: Several instances throughout
- ❌ PADDING: Some repetition between options
- ✅ CONVICTION: Posts end with strong questions

**Total violations: 11** - ⚠️ WRITING AUDIT flagged for revise priority

## Fact Check (Gemini)
- ✅ "$12.9 billion" acquisition figure verified against TechCrunch source
- ✅ "400,000 models, 100,000 datasets" numbers verified from HuggingFace
- ✅ Company names (NVIDIA, HuggingFace, OpenAI, Google, Amazon, Microsoft) accurate
- ✅ Atlan context claims match Aayush's actual role
- ✅ No false claims detected

## Adversarial (Grok)
- **Brief angle:** Fresh - NVIDIA-HF acquisition creates novel infrastructure consolidation argument
- **Option 1:** Fresh - Focus on supply chain control resonates with current builder concerns
- **Option 2:** Fresh - Data-driven approach with specific numbers lands well
- **Option 3:** Saturated - Platform control pattern has been covered extensively in similar contexts
- **Freshness verdict:** 2 of 3 options fresh, acceptable diversity

## Verdict: REVISE

**Critical fixes required:**

### Brief revisions:
1. **Expand to 2,500+ words** - Add mechanism depth to lead section, don't add new topics
2. **Fix guru voice** - Change "experts warn organizations must upgrade" to "organizations face pressure to upgrade"
3. **Replace MBA vocab** - "infrastructure dependency" → "needing infrastructure"
4. **Shorten long sentences** - Break 5 sentences over 22 words into shorter units

### Post revisions:
1. **Remove all 9 em dashes** - Replace with commas or periods
2. **Fix guru voice** - "Teams shipping AI products need to understand" → "Teams shipping AI products might not realize"
3. **Add hedge markers** - Insert "IMO" or "I think" in Options 1-2 where opinion emerges
4. **Option 3 contrast labeling** - Add "That's platform leverage" after key insight
5. **Replace vague generics** - "Every team I talk to" → "Most teams at Atlan" or similar specificity

**Ship threshold:** Must address em dashes (zero tolerance) and word count floor before next council review.
