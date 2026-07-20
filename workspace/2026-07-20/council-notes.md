# Council — 2026-07-20 (iteration 1)

## Deterministic findings (pre-flight) — CONFIRMED hard-rule failures

**Verdict: REVISE (based on pre-flight violations)**

### Em dashes — 7 violations in posts.md (ZERO TOLERANCE)
All em dashes must be removed or replaced with commas/periods.

### Long sentences — 2 violations (>22 words)
- Brief: "China opens its frontier models and scales inference chip production to compete..." (31 words)
- Brief: "Key takeaways: Qwen3.8's open weight release signals China shifting policy from closed..." (97 words)
- Brief: "Lambert's read on the policy context rings true: imagine Xi deciding that..." (30 words)
- Brief: "When the government mandates that private labs open source their frontier work,..." (26 words)
- Brief: "Huawei gets government backing for inference chip scale up While Qwen opens..." (23 words)

### MBA vocabulary violations (banned words found)
- Brief: "ecosystem" (used 2 times) — replace with specific named entities

### "Not X, it's Y" inversions — 2 violations
- Brief: "aren't separate moves. They're connected" 
- Posts: "isn't desperation. It's asymmetric"

### Guru voice violations — 2 in brief.md
- "Companies that choose independence get freedom but have to build"
- "For builders,"

### LLM structural labels — 1 violation
- Brief: "Here's why this matters" (generic structural signpost)

## Fabrication Check
Checking post claims against brief...

⚠️ FABRICATION RISK: Posts make claims that need verification against brief content.

---

## Voice audit (Sonnet) — 15-point scores

**Option 1:** 11/15 — ship_with_fix
- Violations: lowercase_i throughout, hyphen-bullets instead of dashes, opens with claim not story
- Fix needed: convert "I" to "i", fix bullet format, add personal observer line earlier

**Option 2:** 11/15 — ship_with_fix
- Violations: lowercase_i throughout, opens with claim not story, lacks actionable close
- Fix needed: convert "I" to "i", add concrete next action instead of rhetorical question

**Option 3:** 13/15 — ship_with_fix (recommended by voice audit)
- Violations: lowercase_i throughout, hyphen-bullets instead of dashes
- Fix needed: convert "I" to "i", fix bullet format

## Fact check (Gemini) — TRUNCATED RESPONSE

Response was cut off but flagged:
- Brief: Qwen3.8 claims need verification — Qwen 1.5 is latest major release
- H100 pricing verified at $2/hour
- Huawei government funding confirmed

## Adversarial attack (Grok) — Critical findings

### Brief verdict: REVISE
- **Logical gaps:** Netflix CPTO and Apple-OpenAI bullets have "zero connection to China/Qwen/Huawei thesis"
- **Unsupported claims:** H100 pricing claim overstates certainty ("stabilizing" vs research saying "likely")
- **Not X, it's Y violations:** "Instead of trying to beat OpenAI at the API game, make frontier capability free"
- **Structural labels:** "What changed?", "The timing matters too", "The question is whether"

### Posts verdict analysis:
- **Option 1 (Contrarian Philosopher):** REVISE — guru voice + fabricated "tracking" claim + saturated angle
- **Option 2 (Absurdist Truth-Teller):** REVISE — single guru sentence, otherwise strong
- **Option 3 (Relatable Human):** SHIP — only fabricated budget claim needs removal

**Grok recommendation:** Option 3 (best of the three)

## Final council verdict: REVISE

**Ship threshold failures:**
1. **Pre-flight violations:** 7 em dashes, long sentences, MBA vocab, Not X/Y patterns, guru voice
2. **Voice scores:** All options below 12/15 threshold (11, 11, 13)
3. **Adversarial findings:** Brief logical gaps, fabricated claims in posts

**Specific revision priorities:**
1. Brief: Remove Netflix/Apple bullets, fix "Not X, it's Y" patterns, break up long sentences
2. Posts: Fix lowercase "i" across all options, remove fabricated claims
3. Option 1: Remove guru voice + tracking claim
4. Option 2: Remove guru sentence 
5. Option 3: Remove budget fabrication (cleanest option overall)

**Recommended focus:** Option 3 has strongest foundation — relatable human voice with genuine uncertainty. Fix the fabrication and formatting issues, and it ships.