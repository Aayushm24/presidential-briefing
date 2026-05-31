# Council — 2026-05-31 (iteration 1)

## Deterministic findings (CONFIRMED violations)

**WORD COUNT VIOLATION:**
- Brief is at 1734 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

**LONG SENTENCE VIOLATIONS:**
- Brief: "AI cost structures break as token based billing hits every team using..." (38 words)
- Brief: "Simon Willison warns that AI budgets set in 2025 will explode in..." (30 words)  
- Brief: "Key takeaways: GitHub Copilot's shift to token billing ends flat rate AI..." (117 words)
- Brief: "Teams with high Copilot usage report token costs spiking 5 10x..." (27 words)
- Brief: "A startup that budgeted $5,000 monthly for AI costs based on 2025..." (25 words)

**GURU VOICE VIOLATIONS:**
- Brief: "Teams spending 5x more on AI tools need to justify"
- Brief: "For builders,"

**EM DASH VIOLATIONS:**
- Posts: 7 em dashes found (zero tolerance policy)

**NOT X, ITS Y VIOLATIONS:**  
- Posts: "aren't broken because tools got expensive. They're broken"

## Fabrication Check
⚠️ FABRICATION RISK: Multiple specific dollar amounts and meeting counts claimed without clear sourcing in brief.

## Voice audit (Aayush 10-point scale)
- Option 1: 6/10 — REVISE (lacks hedge markers, contrast labels)
- Option 2: 6/10 — REVISE (lacks hedge markers, contrast labels) 
- Option 3: 6/10 — REVISE (lacks hedge markers, contrast labels)

**All options fail voice threshold (8/10 minimum).**

Fix needed for all: Add hedge markers like "tbh" or "IMO", include "That's X." contrast labels.

## Fact check (Gemini)
- ✅ Brief: AWS pricing evolution, Atlan is real company
- ❌ Brief: GitHub Copilot token billing is FALSE (currently flat-rate), SoftBank €75B investment is FALSE
- ❌ All posts: Based on false GitHub Copilot billing premise
- ❌ Option 3: Math error (359% increase claimed as 400%)

## Adversarial (Manual review - LLM proxy unavailable)
- Option 1: "Not X, it's Y" inversion detected: "aren't broken because tools got expensive. They're broken because..."
- All options: Rely on fabricated GitHub billing change
- All options: Specific Atlan claims (Jake, $3200-$14700) unverifiable  
- Freshness: Saturated (AI cost concerns widely discussed)

## Verdict: REVISE

**Critical failures:**
1. ALL posts score 6/10 on voice (below 8/10 threshold)
2. 7 em dashes in posts.md (zero tolerance)
3. 1734 words in brief (below 2000 minimum)
4. Long sentence violations (13 flagged)
5. Multiple false claims about GitHub Copilot
6. "Not X, it's Y" pattern violation

**Revision priorities:**
1. Expand brief to 2000+ words with mechanism detail
2. Remove all em dashes from posts
3. Add hedge markers ("tbh", "IMO") to all posts  
4. Add "That's X." contrast labels
5. Fix false GitHub Copilot claims or pivot to different angle
6. Break up long sentences
