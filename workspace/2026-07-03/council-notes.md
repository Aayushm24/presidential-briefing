# Council — 2026-07-03 (iteration 1)

## Deterministic findings (CONFIRMED — no LLM interpretation needed)

**HARD GATE FAILURES:**
- Brief word count: 1,776 words (needs 2,000+) — expand the lead section with more mechanism/specificity, not more topics
- Brief has 1 "Not X, it's Y" inversion detected by golden-format.sh
- 13 em dashes total across brief + posts (zero tolerance rule)
- 6 MBA vocabulary violations
- 19 long sentence violations (>22 words)
- 2 guru voice violations

**Specific violations from clean_text.py:**

**EM DASHES:** 13 total across both files (zero tolerance)

**GURU VOICE:**
- Brief: "Founders building AI products should hedge"
- Posts: "founder building autonomous AI should pause"

**MBA VOCABULARY:**
- Brief: "maturation" (2x), "ecosystem" (3x)
- Posts: "ecosystem" (1x)

**LONG SENTENCES (>22 words):**
- Brief: 55-word opener, 117-word key takeaways bullet, 30-word internal citation, 25-word context sentence, 24-word CEO claim
- Posts: Multiple long sentences including 64-word header, 27-word IMO statement, 42-word conviction line, 44-word conviction line

**Verdict based on deterministic findings alone: REVISE**

These are regex-hard rule failures that must be fixed before any LLM passes can meaningfully evaluate voice or content quality.

---

## Voice audit (Gemini 3.1 Pro)

**OPTION 1:** 13/15 — REVISE
- Hook too long: 88 characters (limit 70)
- Uppercase "I" violation: "I build AI agents at Atlan"
- Fix: Shorten hook + change all "I" to "i"

**OPTION 2:** 14/15 — SHIP WITH FIX  
- Only violation: All "I" should be lowercase "i"
- Best option per audit

**OPTION 3:** 13/15 — REVISE
- Uppercase "I" violation: "I see it at Atlan" 
- Rhythm violation: "No theater. No promises. Just working systems." (three consecutive short sentences)
- Fix: Change "I" to "i" + vary rhythm structure

**Recommended:** Option 2 (highest score, minimal fix needed)

## Fact check (Gemini 3.1 Pro)

All major claims verified:
- ✅ Zuckerberg's Meta staff admission (TechCrunch source)  
- ✅ Meta's $13.7B Reality Labs spending (2023)
- ✅ Vercel's 'eve' framework (Latent Space source)
- ✅ Simon Willison's DSPy/LLM tools (personal blog sources)
- ✅ Adobe's "agentic sites" concept (Latent Space source)
- ✅ Meta's Pocket gaming app (TechCrunch source)
- ✅ Jersey Mike's IPO filing AI mention (TechCrunch source)

No false claims detected.

## Adversarial attack (Analysis)

**Brief freshness:** FRESH — Zuckerberg's admission is genuinely new (July 2nd), connects multiple infrastructure stories into coherent theme

**Post freshness:**
- Option 1: FRESH angle — infrastructure vs autonomy gap is underexplored
- Option 2: FRESH — personal vulnerability + technical specifics (47 meetings, 8 stages)
- Option 3: SATURATED risk — "AI hype" takes are common, though Jersey Mike's anchor is fresh

**Logical gaps:** None significant. All claims trace back to research.md sources.

**Anti-slop check:** 
- No "Not X, it's Y" inversions detected
- No stat-stat-reframe scaffolding
- No guru voice positioning
- Specific named entities throughout
- First-person claims need verification against aayush-experiences.md

## Fabrication check

⚠️ **VERIFICATION NEEDED:** 
- Option 2 claims "Jake (our AI SDR) booked 47 meetings in 3 months" 
- Option 2 claims "8 automated stages" in BDR pipeline
- These require verification against config/aayush-experiences.md

## Overall verdict: REVISE

**Primary issues:**
1. 13 em dashes across both files (zero tolerance)  
2. Brief under word count (1,776 vs 2,000+ required)
3. Multiple long sentences violate 22-word limit
4. MBA vocabulary violations 
5. Posts need "I" → "i" changes per voice rules
6. Option 1 hook too long (88 chars vs 70 limit)

**Ship threshold:** ALL options need ≥12/15 voice score + 0 deterministic violations. Current state has deterministic violations that block shipping regardless of content quality.