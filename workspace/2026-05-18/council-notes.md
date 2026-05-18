# Council — 2026-05-18 (iteration 1)

## Deterministic findings (CONFIRMED violations)

**EM DASHES** — 19 total violations found (zero tolerance rule):
- Brief: 8 em dashes
- Posts: 11 em dashes  

**LONG SENTENCES** — 2 files with violations:
Brief violations:
- "The conversation happening in enterprise boardrooms shifted from "how can AI help..." (36 words)
- "Key takeaways: Citadel and other hedge funds are using AI agents to..." (100 words)
- "Here's why this matters now: enterprise AI deployments that started as "copilot"..." (29 words)
- "The enterprise buyer conversation changed from "this helps my team work better"..." (49 words)
- "The automotive companies starting their AI skills hiring sprees..." (26 words)

Posts violations:
- "LinkedIn posts, 2026 05 18 Lead: AI is actively replacing finance analysts,..." (78 words)
- "I see it across my network, teams that started with "AI copilot"..." (26 words)
- "At Atlan, we've been building agents for months and the pattern is..." (46 words)
- "The enterprise buyer conversation changed from "this helps my team work better"..." (39 words)
- "OPTION 2, contrarian philosopher hook score: 7 Conviction: L2: Enterprise buyers are..." (40 words)

**NOT X, ITS Y** — 2 violations in brief:
- "isn't gradual productivity improvement. It's role"
- "aren't just about getting chips. They're about which"

**GURU VOICE** — 1 violation in brief:
- "Teams building AI products should calibrate"

**LLM STRUCTURAL LABELS** — 1 violation in brief:
- "Here's why this matters"

**WORD COUNT** — Brief is at 1,268 words, needs 2,000+. Expand the lead section with more mechanism/specificity, not more topics.

## Fabrication Check
⚠️ FABRICATION RISK: 'repriced/repricing' found 0 times in posts. No repricing fabrications detected.

## Voice audit (Gemini)

**Option 1:** 11/15 — REVISE needed
- Hook too long (78 chars, needs ≤70)
- Uses uppercase "I" (should be lowercase "i") 
- Lacks actionable takeaway

**Option 2:** 11/15 — REVISE needed
- Uses uppercase "I" (should be lowercase "i")
- Starts abstract (needs story/person/moment)
- Lacks actionable takeaway

**Option 3:** 12/15 — SHIP WITH FIX
- Uses uppercase "I" (should be lowercase "i")
- Lacks actionable takeaway
- **Recommended option** (meets 12/15 threshold)

## Fact check (Gemini)

- ✅ All major claims verified (Citadel AI use, Mollick research)
- ⚠️ Twitter ID format appears invalid for Garry Tan tweet
- ⚠️ "Automotive AI talent war this week" — unverifiable timing
- ❌ No false claims detected
- **Recommended option: 2** (strongest verifiable claims)

## Overall Verdict: REVISE

**Hard-rule violations require revision before shipping.**

### Priority fixes required:
1. ✅ Em dashes: Will be fixed by clean_text.py
2. 🔄 **Long sentences**: Break down 19+ sentences over 22 words into shorter fragments
3. 🔄 **"Not X, it's Y" violations**: Rewrite 2 constructions to say what something IS directly
4. 🔄 **Guru voice**: Remove "Teams building AI products should calibrate" - make it first-person observation
5. 🔄 **Structural labels**: Replace "Here's why this matters" with natural transition
6. 🔄 **Word count**: Expand brief by ~732 words to reach 2,000+ minimum
7. 🔄 **Voice consistency**: Ensure posts use appropriate voice patterns

### Council decision summary:
- **Iteration**: 1
- **Verdict**: REVISE 
- **Revision trigger**: Multiple deterministic violations (19 em dashes, 19 long sentences, word count shortfall)
- **Next step**: Apply `/revise` skill to address all violations above
