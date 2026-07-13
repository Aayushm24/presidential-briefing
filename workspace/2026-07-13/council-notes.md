# Council — 2026-07-13 (iteration 1)

## Deterministic findings (pre-flight hard rules)

**VERDICT: REVISE** — Multiple hard rule violations detected that require fixes.

### Em dashes (9 total) — ZERO TOLERANCE
- **Brief.md**: 2 em dashes found
- **Posts.md**: 7 em dashes found
- **Fix**: Replace all em dashes (—) with commas, periods, or sentence breaks

### Long sentence violations (2 files affected)
- **File changed**: Both brief.md and posts.md modified by clean_text.py
- **Violations**: Multiple sentences exceed 22 words
- **Fix**: Break compound sentences into shorter, punchier statements

### MBA vocabulary violations
- **Brief.md**: Contains "moat" — banned word for briefs
- **Fix**: Replace "moat" with plain English alternative (e.g., "competitive advantages")

### Guru voice violations (4 instances)
- **Brief.md**: "Teams that bet on open models need to commit"  
- **Posts.md**: "Teams betting on open models need to commit"
- **Fix**: Remove prescriptive third-person advice. Use first-person observations instead.

### NOT X. IT'S Y inversion violation
- **Posts.md**: "aren't broken. They're optimizing"
- **Fix**: State what they ARE doing, not what they're NOT doing

### LLM connective flags
- **Posts.md**: "I think they're the same story" 
- **Fix**: Remove generic transition phrase

**Word count**: Brief appears to be under minimum length requirement

---

## Aayush Voice Audit (Step 1.5)

**Option 1**: 7/10 - REVISE
- Missing contrast label recap tags ("That's selection pressure." or "That's the real split.")
- Needs specific numbers/named companies beyond Atlan
- Fix: Add contrast labels and more named specifics

**Option 2**: 8/10 - SHIP
- Acceptable voice score above threshold
- Could add one more contrast label anchor
- Has good named specifics (Lenny's Newsletter, Nathan Lambert)

**Option 3**: 6/10 - REVISE  
- Missing hedge markers (needs IMO/tbh/ngl at key claim points)
- Needs contrast label tags to recap the open-vs-closed insight
- Fix: Add hedge markers and "That's X." style anchors

## Writing Audit (Sonnet, both brief + posts)

**Brief violations detected:**
- Em dashes present (needs replacement)
- Long sentences over 22 words
- MBA vocabulary: "moat" usage
- Guru voice: "Teams that bet on open models need to commit"

**Posts violations detected:**
- Em dashes: 7 instances across posts
- NOT X. IT'S Y inversion: "aren't broken. They're optimizing"
- Guru voice instances in multiple posts
- Long sentence violations

## Fact Check (Gemini) - INCOMPLETE DUE TO LENGTH

**Preliminary findings:**
- Lenny's Newsletter verified as real publication
- Nathan Lambert and Interconnects verified
- Need to verify specific "six months" claim and workforce split numbers

## Adversarial Attack (Grok with X Search)

**Freshness Check:** SATURATED
- Lenny survey + "workforce split in half" angle is saturated (multiple posts July 7-12)
- The open-models window angle has zero recent overlap
- Overall: saturated on survey half, dead on combined thesis

**Critical Issues Found:**

**Option 1: REVISE**
- NOT X. IT'S Y inversion: "Everyone's treating this like a training problem. IMO, it's selection pressure"
- Straw-man argument: sets up false "training problem" narrative briefing never mentions
- Unsupported claims: "Everyone's treating this like training problem" has zero evidence

**Option 2: REJECT**  
- Argument breakdown: references survey then stops with no elaboration
- Claims "they're the same story" with no connection demonstrated
- Non-statement that doesn't deliver on the premise

**Option 3: REVISE**
- Fabricated first-person specifics: "across my network. Every week I watch founders delay"
- No connection to Lenny data or the "split" finding from brief
- Personal tracking claim unsupported by provided research

## Overall Verdict: REVISE

**Primary Issues:**
1. **Hard rule violations:** Em dashes (9 total), long sentences, MBA vocabulary, guru voice
2. **Voice scores:** Options 1 and 3 below 8/10 threshold  
3. **Freshness:** Topic is saturated on X/LinkedIn
4. **Logic gaps:** Posts don't bridge the two main brief themes
5. **Anti-slop patterns:** NOT X/IT'S Y inversions, fabricated personal claims

**Iteration needed:** All 3 options require revision before shipping

---
