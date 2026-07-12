# Council — 2026-07-12 (iteration 1)

## Deterministic findings (regex pre-flight)

**CONFIRMED violations requiring REVISE:**

### Not-X-Its-Y inversions (3 instances in brief.md)
- "isn't about making ChatGPT better at answering homework questions. It's about owning"
- "isn't just competing with workplace productivity tools anymore. It's positioning"
- "isn't a model upgrade. It's a"

**Fix:** Replace with direct declarative statements. Example: "OpenAI isn't building ChatGPT for families to make homework help friendlier. They're building it to own household coordination." → "OpenAI targets family coordination to own recurring daily touchpoints, not friendlier homework help."

### Guru voice violations (3 instances in brief.md)
- "Teams building AI-powered services need to proactively"
- Two "For builders," statements

**Fix:** Remove prescriptive "should/need to" language. Replace with observations. Example: "Teams building AI-powered services need to proactively address accountability gaps" → "Most teams building AI-powered services haven't addressed accountability gaps in their client contracts"

### MBA vocabulary (3 instances)
- "differentiation" (brief.md and posts.md)
- "platform dependency" (brief.md)

**Fix:** Replace with plain English per blueprint. "differentiation plans" → "plans to be different", "platform dependency risk" → "risk of needing ChatGPT"

### Long sentences (36+ instances across both files)
Notable violations include 36-word, 28-word, 24-word sentences that exceed the 22-word cap.

### Em dashes (6 instances in posts.md)
All em dashes must be removed per zero-tolerance rule.

## Aayush voice audit (10-point)

- **Option 1:** 6/10 — REVISE (missing hedge markers, lowest dimension)
- **Option 2:** 5/10 — REVISE (missing hedge markers, weak first-person observer)
- **Option 3:** 5/10 — REVISE (missing hedge markers, generic details)

**Gate failure:** ALL options scored below 8/10 threshold.

**Key fixes:**
- Option 1: Add hedge like "tbh, the gap is stickiness, not capability"
- Option 2: Add "imo this is a distribution play" + break compound paragraphs
- Option 3: Add "tbh" at pivot + name specific teams/numbers

## Writing audit (20 violations)

Major violations across brief and posts:
- **Unsourced statistics:** $2.3B market figure, "two years of usage data", retention claims
- **Vague generics:** "most teams", "every founder I talk to", "various founders"
- **Padding:** Sentences that restate without adding information
- **Brief violations:** 16 instances of unsourced stats, vague claims, padding
- **Posts violations:** 4 instances across options, mostly same patterns

## Fact check

⚠️ **CRITICAL:** Option 2 contains FALSE claim
- **$2.3 billion family management software market** — unverified and likely fabricated; no reliable public source found

**Other unverifiable claims:**
- "Two years of usage data" retention patterns (no public source)
- Claude Ultra subagents being "default" (unconfirmed product claim)
- Specific family coordination behavior patterns (no public data)

## Adversarial review (Grok with X search)

**Brief verdict:** REVISE
- Logical gaps: Links OpenAI family PM to Anthropic subagents with no evidence
- Fabricated usage data claims not supported by research.md
- Guru voice in key takeaways directing builders

**Post verdicts:**
- **Option 1:** REVISE (Contrarian Philosopher style, fresh angle, but fabricated Atlan examples)
- **Option 2:** REJECT (Corporate Analyst style, FALSE $2.3B claim, advisory tone)
- **Option 3:** REJECT (Corporate Analyst style, saturated angle, mismatches briefing lead)

**Angle diversity:** FAIL — Options 2&3 both Corporate Analyst style

## Verdict: REVISE

**Ship threshold failures:**
1. ✗ Aayush voice scores: All options < 8/10
2. ✗ Deterministic violations: Not-X-Its-Y, guru voice, MBA vocab, long sentences
3. ✗ Writing audit: 20 violations requiring fixes
4. ✗ Fact check: FALSE $2.3B claim in Option 2
5. ✗ Adversarial: Brief needs revision, only Option 1 viable

**Recommended focus for revision:**
- Fix deterministic violations first (Not-X-Its-Y, guru voice, sentence length)
- Remove/correct FALSE $2.3B market claim in Option 2
- Add hedge markers to all posts (tbh, imo, ngl)
- Replace fabricated examples with verified Aayush experiences
- Source all statistics or remove unsourced claims
- Break compound sentences under 22 words

**Revision notes count:** 8 major categories requiring fixes
