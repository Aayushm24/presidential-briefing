# Council — 2026-04-21 (iteration 0)

## Deterministic findings (pre-flight)

**CONFIRMED violations from regex/format checks:**

### brief.md violations:
- em_dash found (U+2014 not allowed) — 3 instances
- audience_direct_address: "for founders" — 3 instances  
- word_count=1357 (expect 1500-2800) — too short
- not_x_its_y pattern: "isn't a demo or a benchmark. It's 100" — 1 instance
- guru_voice: ". for builders," — 1 instance
- long_sentences: 5 sentences exceeding 22 words including 125-word sentence

### posts.md violations:
- em_dash found (U+2014 not allowed) — 4 instances
- audience_direct_address: "for founders" — 1 instance
- not_x_its_y patterns: 3 instances including "isn't your competitive advantage. It's a"
- guru_voice: "for builders," — 1 instance
- long_sentences: 14+ sentences exceeding limits

## Voice audit (Opus)
- **Option 1:** 10/15 — REVISE (7 MBA vocabulary hits, multiple kill-list violations, 47-word sentence)
- **Option 2:** 10/15 — REVISE (7 MBA vocabulary hits, abstract noun stacks, stats jargon) 
- **Option 3:** 12/15 — SHIP WITH FIX (3 MBA hits, 28-word sentence needs splitting)

## Fact check (Gemini)
- Response truncated due to token limits, but key point: need to verify specific claims like "76% less variance"
- ✅ Intercom 2x velocity claim verified from research
- ⚠️ Need to check exact variance percentage from economics study

## Adversarial (Grok)
**Brief findings:**
- **Factual error:** Claims "OpenAI's Codex acquisition" when research shows "OpenAI acquiring via Skybysoftware"
- **Unsupported claim:** "Small teams outperform large orgs" not directly backed by research
- **Multiple "not X, it's Y" inversions** requiring fixes

**Posts freshness:**
- **Option 1:** SATURATED angle — X search found 5 similar "AI commoditization" takes in last 7 days
- **Option 2:** SATURATED angle — multiple posts on Claude Code vs human performance with Mollick's study
- **Option 3:** FRESH angle — unique "three stories connect" narrative not seen in recent posts

## Verdict: REVISE

**Revision priorities (iteration 0 → 1):**
1. **Fix deterministic violations:** Remove em dashes, eliminate "for founders/builders", break long sentences
2. **Fix factual error:** Correct Codex reference to Skybysoftware acquisition  
3. **Options 1 & 2:** Full regeneration needed due to <12/15 scores + saturated angles
4. **Option 3:** Ship with minor fixes (split long sentence, replace "churn" with "leave")
5. **Expand brief:** Add 200-400 words to meet minimum length requirement

Specific MBA vocabulary to eliminate: competitive advantage, commodity, coordination overhead, cost structure, velocity, workflows, pipeline, variance management, throughput, regression, metrics.