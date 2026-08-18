# Council — 2026-08-18 (iteration 1)

## Deterministic findings (pre-flight)

**CONFIRMED violations found by regex/clean_text.py:**

### MBA vocabulary violations (6 total)
- **differentiation** (2 hits in brief) — banned per brief-blueprint.md
- **enterprise customers** (2 hits in brief) — usually unnecessary  
- **ecosystem** (1 hit in brief) — too abstract alone
- **moat** (2 hits in posts) — ALLOWED in posts (different surface than brief)
- **leveraged** (1 hit in posts) — jargon, use "used"

### Long sentences (22 violations, need splitting)
**Brief violations:**
- 119w: "Key takeaways: Stripe's $7B OpenRouter acquisition signals..." — way too long
- 32w: "The distribution layer captured $7 billion this week Stripe..."
- 29w: "OpenAI, Anthropic, and Google all want placement in aggregation layers..."
- 27w: "This usage telemetry reveals which models perform best for specific tasks..."
- 25w: "Stripe now controls both the distribution layer and the monetization layer..."

**Posts violations:**
- Multiple over 22-word sentences need breaking

### Not X, It's Y violations (1 hit)
- "isn't picking the best model. It's managing" — AI-tell inversion, needs rewrite

### Guru voice violations (1 hit)
- "Teams shipping agents need to audit" — prescriptive voice, not Aayush's observational style

### Word count check
- **Brief at 1,667 words** — Above 2,500-word floor requirement: FAIL. Brief needs expansion.

**VERDICT from pre-flight: REVISE** — Multiple hard-rule violations must be fixed.

## Fabrication Check
Checking post claims against brief...
✅ Most post claims verified against brief content
⚠️ **FABRICATION FOUND**: Option 1 claims "OpenAI just paid $50 billion" - not in brief, appears fabricated

## Aayush Voice Score (10-point check)

### Option 1: 8/10 — SHIP threshold met
- First-person observer: 2/2 ("Every week I watch")
- Hedge markers: 0/2 (missing IMO, I think, etc.)
- Contrast labels: 2/2 ("That's not a technology play. That's distribution.")
- Fragment paragraphs: 2/2
- Specific named details: 2/2

### Option 2: 7/10 — BELOW SHIP threshold  
- First-person observer: 2/2 ("I build AI agents at Atlan")
- Hedge markers: 0/2 (missing)
- Contrast labels: 1/2 (weak)
- Fragment paragraphs: 2/2
- Specific named details: 2/2

### Option 3: 8/10 — SHIP threshold met
- First-person observer: 2/2 ("Every team I talk to")
- Hedge markers: 2/2 ("IMO, this signals")
- Contrast labels: 0/2 (missing)
- Fragment paragraphs: 2/2
- Specific named details: 2/2

## Writing Audit Findings
**Brief violations:**
- 5 sentences over 22 words need splitting
- 2 MBA vocabulary hits: "differentiation", "enterprise customers", "ecosystem"  
- Word count at 1,667 — needs 800+ more words to reach 2,500 floor

**Posts violations:**
- Option 1: Fabricated $50B claim, missing hedge markers
- Option 2: "Not X, It's Y" inversion, MBA vocab ("leveraged", "differentiation") 
- Option 3: Guru voice ("Teams shipping agents need to audit")

## VERDICT: REVISE

**Priority fixes:**
1. **Brief**: Expand to 2,500+ words, split long sentences, remove MBA vocab
2. **Option 1**: Remove fabricated $50B claim, add hedge markers  
3. **Option 2**: Fix AI-tell inversion, clean MBA vocabulary, add hedge markers
4. **Option 3**: Convert guru voice to observational, add contrast labels

**Recommended option after revision**: Option 3 (strongest voice score)
