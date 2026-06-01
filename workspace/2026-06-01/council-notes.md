# Council — 2026-06-01 (iteration 1)

## Deterministic findings (pre-flight failures — CONFIRMED violations)

**VERDICT ALERT: Multiple hard-rule violations detected. REVISE required.**

### Word count violation
- Brief is at 1,948 words, needs 2,000+ minimum per blueprint. Expand the lead section with more mechanism/specificity, not more topics.

### Em dash violations (17 found)
- Em dashes banned everywhere - replace with commas or periods throughout brief and posts

### MBA vocabulary violations (2 found)
- "matures" in brief.md - banned, replace with "real companies pay real money for X"
- "ecosystem" in brief.md - banned, name the specific thing (tools, people, products)

### Long sentence violations (19 found)
Multiple sentences over 22-word limit across both files:
- Brief line: "Local AI crosses the viability threshold as 74% of real workloads run..." (47 words)
- Brief line: "Key takeaways: Local models crossed the 75% capability threshold for real workloads,..." (129 words) 
- Brief line: "The brain connections show this has been building, we covered local AI..." (26 words)
- Brief line: "Instead of 'how do we optimize prompts to reduce tokens?' they ask..." (32 words)
- Brief line: "The creator class goes local first as PewDiePie ships agents Shawn Wang..." (33 words)
- Posts line: "LinkedIn posts, 2026 06 01 Lead: Local AI crosses the viability threshold..." (66 words)
- Posts line: "From: 'how do we optimize prompts to reduce tokens?' To: 'which 25%..." (30 words)
- Posts line: "OPTION 2, data point hook score: 8 Conviction: L3: Teams need a..." (25 words)
- Posts line: "If your use case runs 1,000 times per day, you pay frontier..." (24 words)
- Posts line: "OPTION 3, pattern observation hook score: 8 Conviction: L1: The creator class..." (32 words)

### Not X, it's Y violations (2 found)
- Brief: "isn't just other startups. It's every"
- Posts: "isn't just other startups. It's every"

### Guru voice violation (1 found)
- Brief: "for builders," - banned advice voice pattern

**These deterministic violations must be fixed before any LLM passes can be evaluated. Proceeding with voice audit...**

## Fabrication Check
Checking post claims against brief...
⚠️ FABRICATION RISK: Claims in posts cross-checked against brief sources - no repricing language detected but claims need verification.

## Voice audit (Gemini - Aayush 10-point system)

**Option 1 — contrarian-philosopher**: 8/10 — SHIP
- First-person observer: 2/2 (Strong: "Every team I talk to is asking the wrong question")
- Hedge markers: 2/2 (Natural: "I doubt the cost math is what matters most here")  
- Contrast labels: 0/2 (Missing "That's X." recap tags)
- Fragment paragraphs: 2/2 (Clear one-idea-per-line rhythm)
- Specific named details: 2/2 (Tunguz, 74.5%, $50K, GPT-4, $100M ARR)
- Fix: Add a punchy 'That's X.' contrast label (e.g., 'That's leverage.') to maximize the score

**Option 2 — data-point**: 6/10 — REVISE (below 8/10 threshold)
- First-person observer: 2/2 (Strong: "I've been thinking about the teams burning serious cash", "Most teams I see")
- Hedge markers: 0/2 (No IMO, i think, i doubt, tbh, fwiw, ngl)
- Contrast labels: 0/2 (Missing "That's X." recap tags)
- Fragment paragraphs: 2/2 (Good rhythm)
- Specific named details: 2/2 (Tunguz, 15, 100%, $50K, 1,000 times, 365,000)
- Fix: Include a hedge marker like 'tbh' or 'IMO' and a short 'That's X.' recap tag to sound more authentic to the voice

**Option 3 — pattern-observation**: 4/10 — REVISE (below 8/10 threshold)
- First-person observer: 0/2 (No present-tense observer perspective)
- Hedge markers: 0/2 (No hedge markers)
- Contrast labels: 0/2 (Missing "That's X." recap tags)
- Fragment paragraphs: 2/2 (Good rhythm)
- Specific named details: 2/2 (PewDiePie, February 2025, Soumith Chintala, Nine months, SOC 2, 500-person company)
- Fix: Needs a first-person observer perspective ('I see startups...'), hedge markers ('tbh'), and a contrast label to fit the voice profile

## Fact check (Gemini)
✅ Key numbers appear accurate from sources
- Tunguz 74.5% local model data — verified against source post
- PewDiePie AI productivity suite — verified against source post  
- Cost figures ($10-15 per user, $2-3 local) — reasonable estimates
- No fabricated numbers detected

## Adversarial attack (Manual assessment)
- Brief wordcount insufficient (1,948 vs 2,500 minimum)
- Multiple long sentences impact readability
- MBA vocabulary reduces accessibility
- Overall quality strong but needs revision for compliance

## Verdict: REVISE

**Multiple hard violations require fixes:**
1. **Primary blocker**: Options 2 and 3 score below 8/10 voice threshold
2. **Secondary blockers**: Word count, long sentences, MBA vocab, "Not X, it's Y" patterns, guru voice

**Specific revision notes:**
- Brief.md: Expand by 500+ words, fix long sentences, replace "matures"→"real companies pay real money", replace "ecosystem"→name specific things, fix "for builders"→"for builders who...", fix "isn't just other startups. It's every"→direct statement
- Posts.md: Option 2 needs hedge markers and contrast labels, Option 3 needs first-person observer voice, hedge markers, and contrast labels
- Both: Fix long sentences under 22 words each

**Iteration count**: 1 (first pass)
**Best performing option**: Option 1 (8/10 voice score)
**Options requiring regeneration**: Options 2 and 3