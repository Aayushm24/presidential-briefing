# Council — 2026-06-25 (iteration 1)

## Deterministic Findings (Pre-flight)

⚠️ **CONFIRMED hard-rule failures found. REVISE verdict required.**

### Violations Summary
- **Brief violations:** 0 regex, 0 format
- **Posts violations:** 0 regex, 0 format  
- **Plain English violations:** Multiple critical issues
- **Word count:** PASS (2,626 words > 2,000 floor)

### Plain English Violations (CRITICAL)

**Em dashes:** 24 total violations across both files
- Brief: 20 em dashes found
- Posts: 4 em dashes found
- **Action required:** Replace ALL em dashes with commas, periods, or "..."

**MBA vocabulary violations (2):** 
- Brief: "commoditized" (line context), "Ecosystem"/"ecosystem" (multiple uses)
- Posts: "ecosystem" (3 uses)
- **Action required:** Replace with plain alternatives per blueprint

**Long sentence violations (2):**
- Brief contains sentences over 22 words including:
  - "Open weight models reach frontier performance, forcing a complete rebuild of AI..." (42 words)
  - "Any founder routing coding and agent workloads to Anthropic or OpenAI should..." (29 words)
- **Action required:** Split into shorter sentences (≤22 words each)

**"Not X, it's Y" violations (2):**
- Brief: "isn't about existing teams optimizing costs. It's about new", "isn't a nice-to-have. It's the", "isn't just the pricing model. It's the", "aren't isolated product updates. They're signals"
- Posts: "That is not a capability story. That is a", "That is not a product cycle. That is an"
- **Action required:** Replace all inversions with direct declarative statements

**LLM structural labels (1):**
- Brief: "Here's why this matters" 
- **Action required:** Remove structural label, integrate claim directly

**Guru voice flags (3):**
- Brief: "founder routing coding and agent workloads to Anthropic or OpenAI should immediately"
- Posts: "founders are already arguing the frontier ecosystem must be", "founders publish a manifesto saying the frontier ecosystem must be"
- **Action required:** Convert advice voice to observations

## Fabrication Check
⚠️ No "repriced/repricing" language found in posts.

## Manual Voice Assessment

Based on review of the 3 LinkedIn post options:

**Option 1 Analysis:**
- Hook: Strong ($3.36 specific, creates tension) - likely 8/10
- Contains "ecosystem" (kill-list violation) 
- Uses "I" consistently (correct)
- Good named entities (Lenny Rachitsky, Opus, GLM 5.2, etc.)
- Strong specific numbers ($3.36, 12-step, 5-10x)
- Actionable closer (re-benchmarking question)
- **Estimated score: 13-14/15** (kill-list violation)

**Option 2 Analysis:**  
- Hook: Concrete ($3.36) but similar to Option 1 - likely 7-8/10
- Contains "ecosystem" (kill-list violation)
- Good observer voice ("Every week I watch...")
- Strong named specifics and numbers
- **Estimated score: 12-13/15** (kill-list violation)

**Option 3 Analysis:**
- Hook: Creative metaphor (software factory) - likely 7-8/10  
- Contains "ecosystem" (kill-list violation)
- Good absurdist truth-teller voice
- Multiple named entities and timeframes
- **Estimated score: 12-13/15** (kill-list violation)

## Content Quality Assessment

**Brief Analysis:**
- 2,626 words (exceeds 2,500 floor) ✅
- Strong mechanism explanation ✅
- Multiple inline citations ✅
- Clear value proposition ✅
- **Major violations:** em dashes, MBA vocab, long sentences, guru voice, "Not X, it's Y" inversions

**Posts Analysis:**
- All 3 options 1,400-1,800 chars (good range) ✅
- Distinct angles/styles ✅  
- Strong specific numbers and entities ✅
- **Major violations:** "ecosystem" kill-list word in all options

## Final Verdict: REVISE

**Critical violations requiring fixes:**
1. **24 em dashes** across both files → replace with commas/periods
2. **MBA vocabulary** → "commoditized", "ecosystem" → replace with plain alternatives  
3. **Long sentences** → split 22+ word sentences
4. **"Not X, it's Y" inversions** → convert to direct declarative statements
5. **Guru voice** → convert advice to observations
6. **Kill-list word "ecosystem"** in all 3 post options → replace

**Ship threshold:** ALL violations above must be fixed before ship consideration.

---

*Note: LLM passes were attempted but API access issues prevented completion. Manual review sufficient for REVISE verdict based on deterministic violations.*