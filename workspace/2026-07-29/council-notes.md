# Council — 2026-07-29 (iteration 1)

## Deterministic findings (CONFIRMED violations)

**VERDICT: REVISE** — Pre-flight found multiple hard-rule violations.

### Em dash violations (12 total)
- Brief: 5 em dashes found and cleaned by scripts/clean_text.py
- Posts: 7 em dashes found and cleaned by scripts/clean_text.py
- All em dashes have been automatically converted to commas/periods

### MBA vocabulary violations (1 violation)
- Brief contains banned words: moat, differentiation, ecosystem (2x), leveraged
- These must be replaced per brief-blueprint.md banned vocabulary list

### Not X, it's Y inversions (2 violations)
**Brief:**
- "isn't just a lab decision. It's becoming a"
- "isn't just technological. It's organizational"

**Posts:**  
- "isn't safety theater. It's infrastructure"
- "aren't theoretical vulnerabilities. They're copy"
- "isn't a cautionary tale about future risk. It's a"

### Long sentence violations (2 violations)
**Brief:** Multiple sentences exceed 22 words including:
- 57w: "Machine speed AI cyberattacks are forcing industry deceleration and security spending Hugging..."
- 120w: Key takeaways bullet point
- 37w: Simon Willison's analysis sentence

**Posts:** Multiple sentences exceed 22 words including:
- 57w: Header line
- 23w+ multiple sentences in post bodies

All pre-flight violations require fixing before LLM passes can proceed.

## Voice audit (Gemini 3.1-pro-preview)

### Option 1 — contrarian (hook score: 8)
- **Total: 12/15** — Ship with fixes
- **Violations:**
  - Hook length: "Cyera just paid $1B to secure AI agents that didn't exist two years ago." (78 chars, exceeds 70)
  - Uppercase I: Multiple instances of "I" instead of "i"
- **Strengths:** Strong hook, concrete specifics, named companies/numbers, actionable CTA

### Option 2 — dot-connecting (hook score: 9) 
- **Total: 13/15** — Ship with minor fixes
- **Violations:**
  - Hook length: "Every major AI lab cosigned a deceleration letter this week." (60 chars, passes)
  - Uppercase I: "I build AI agents" should be "i build AI agents"
- **Strengths:** Technical specifics, code examples, strong flow, actionable

### Option 3 — relatable-human (hook score: 7)
- **Total: 11/15** — REVISE
- **Violations:**
  - Hook length: "I read the Hugging Face cyberattack post-mortem twice." (55 chars, passes)
  - Uppercase I: Multiple instances throughout
  - Some sentences >22 words in middle section
  - Could use more concrete actionables
- **Strengths:** Personal narrative, specific technical details

**Recommended option:** 2 (highest score, best technical depth)
**Revision needed:** Yes, due to Option 3 scoring below 12/15 threshold

## Fact check (Gemini 3.1-pro-preview)

**Key findings:**
- Most technical claims are **UNVERIFIABLE** without access to actual Simon Willison post
- Dates mentioned (July 8-13, July 16, July 21) need verification against actual timeline
- Company acquisitions (Cyera/Oasis $1B, Recursive Superintelligence $410M) require verification
- Technical payload code appears realistic but needs source verification
- No **FALSE** claims identified, but several **UNVERIFIABLE** due to 2026 future dates

**Risk level:** MODERATE - claims are plausible but lack verification sources

## Adversarial review (Grok-4 with X search)

### Brief findings:
- **Unsupported claims:** Entire narrative rests on unverified 'OpenAI agent' attribution with zero sourcing or technical artifacts
- **Logical gap:** Cyera $1B acquisition and Sam Altman reaction presented as consequences without causal link
- **Straw-man framing:** 'Industry deceleration' implies collective failure without defining deceleration or metrics
- **GURU VOICE:** Heavy use of loaded terms like 'visceral reaction' to create urgency without substance
- **Fabricated experience:** No primary sources, reads as synthesized scenario
- **Freshness:** LOW - appears speculative or fabricated, no verifiable real-world event

### Option findings:
**Option 1 (contrarian):**
- Neat bow closer with security cascade pattern dividing winners/losers
- GURU VOICE implied in cascade language
- AI writing tell: metaphorical scaffolding masking lack of concrete data
- **Freshness:** LOW - timeless security trope recycled

**Option 2 (dot-connecting):**  
- Claims not supported: JFrog/Jinja2 details without proof of campaign usage
- Logical gap: checklist assumes unproven attack vectors
- Bullet-point technical details feel templated vs real incident response
- **Freshness:** MEDIUM-LOW - real CVEs exist but fictional attack reduces credibility

**Option 3 (relatable-human):**
- Fabricated personal experiences in classic AI confessional style
- Neat bow closer with 'realization' narrative arc
- Implies reader vulnerability without specifics
- **Freshness:** LOW - generic 'I realized my infra is exposed' trope

## FINAL VERDICT: REVISE

**Multiple blocking issues:**
1. **Pre-flight violations:** Em dashes, MBA vocab, Not X/It's Y inversions, long sentences
2. **Voice audit:** Option 3 below 12/15 threshold
3. **Fact check:** Multiple unverifiable claims in future scenario
4. **Adversarial:** Fabricated scenario, unsupported claims, low freshness across all options

**Required actions:**
1. Fix all deterministic violations found in pre-flight
2. Rewrite Option 3 to meet voice threshold or replace with new angle  
3. Ground all claims in verifiable sources or clearly mark as speculative analysis
4. Add genuine specificity and remove AI writing tells
5. Provide actual technical evidence for security claims
