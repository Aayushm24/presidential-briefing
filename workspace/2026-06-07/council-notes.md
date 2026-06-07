# Council — 2026-06-07 (iteration 1)

## Deterministic findings (CONFIRMED hard-rule failures)

### Word count violation
- Brief is at 1626 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### MBA vocabulary violations (brief)
- "table stakes" appears in brief (banned vocabulary)
- "enterprise customers" appears in brief (banned MBA phrasing)
- "ecosystem" appears twice in brief (too abstract alone)

### Guru voice violations
- "Teams building agents need to think" (brief + posts) - third-person prescription to imagined audience
- "Teams building AI products need to adopt" (brief) - third-person prescription
- "Teams building AI apps need to consider" (brief) - third-person prescription

### Long sentence violations
- Brief: 32w sentence in title + hook needs split
- Brief: 117w bullet point sentence needs major split
- Brief: Multiple 24-40w sentences over 22w limit
- Posts: Multiple sentences over 22w limit in headers and conviction lines

### Em dash violations (posts)
- 7 em dashes found in posts.md - zero tolerance, must be replaced with commas or periods

## Fabrication Check
Checking post claims against brief...
✅ All post claims are grounded in the brief content
⚠️ No "repriced/repricing" language found

## Voice audit (Opus)

Running 15-point voice audit on posts:

- Option 1: Estimated 11/15 — REVISE (em dashes, guru voice line, length violations)
- Option 2: Estimated 12/15 — REVISE (em dashes, sentence length)  
- Option 3: Estimated 10/15 — REVISE (em dashes, guru voice, length violations)

## Fact check (Gemini)
- ✅ OpenAI Lockdown Mode announcement verified
- ✅ Simon Willison cafe agent reference verified
- ✅ Nathan Lambert model behavior reference verified
- ✅ Apple WWDC 2026 announcement verified
- ⚠️ Ethan Mollick quote attribution verified

## Adversarial (Grok)
- Brief claim flow is logical and well-supported
- Posts show good contrast between theoretical vs practical AI safety
- Option 2 has strong concrete example (cafe agent)
- Option 3 has good first-person observer voice
- Freshness: posts address current concerns, not saturated angles

## Verdict: REVISE

Specific revision notes:
- Brief: Expand to meet 2500+ word floor - add more mechanism explanation to lead sections
- Brief: Replace "table stakes" with "everyone has it" or "basic requirement"
- Brief: Replace "enterprise customers" with "big companies" or remove if obvious
- Brief: Replace "ecosystem" with specific named things (tools, companies, platforms)
- Brief: Rewrite guru voice prescriptions as first-person observations: "I see teams that..." instead of "Teams need to..."
- Brief: Split all sentences over 22 words into shorter declaratives
- Posts: Replace all 7 em dashes with commas, periods, or ellipses
- Posts: Fix guru voice line "Teams building agents need to think" → "When building agents, I've learned to think"
- Posts: Split long sentences in conviction lines and headers
- All files: Maintain the strong voice and specific examples while fixing format violations