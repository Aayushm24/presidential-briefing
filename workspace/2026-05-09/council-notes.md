# Council — 2026-05-09 (iteration 1)

## Deterministic findings (pre-flight violations)

**EM DASHES** — CONFIRMED hard rule violations:
- Total: 10 em dashes found (2 in brief, 8 in posts)
- Must be converted to hyphens or comma splices

**MBA VOCABULARY** — CONFIRMED banned word violations:
- "commoditized" (brief)
- "moat" (brief) 
- "enterprise customers" (brief)

**LONG SENTENCES** — CONFIRMED violations (24 sentences over 22 words):
Brief violations:
- 36w: "AI splits the workforce while companies that ship fast pull ahead Anthropic..."
- 114w: "Key takeaways: Anthropic's hypergrowth versus widespread tech layoffs reveals where AI value..."
- 26w: "Anthropic https://www.latent.space/p/ainews anthropic growing 10xyear is growing 10x year over year while..."
- 29w: "When Anthropic designs customer service, they architect systems where AI handles 90%..."
- 25w: "Cloudflare https://techcrunch.com/2026/05/08/cloudflare says ai made 1100 jobs obsolete even as revenue hit..."

**NOT X ITS Y INVERSIONS** — CONFIRMED violation:
Posts violation:
- "isn't adding AI to human workflows. It's rebuilding" (Option 1)

**NEAT BOW CLOSERS** — CONFIRMED violation:
Brief violation:
- "compounding advantages over" (neat bow language)

**GURU VOICE** — CONFIRMED violation:
Brief violation:
- "Founders building consumer AI products should review" (third-person prescription to imagined audience)

**VERDICT SO FAR:** REVISE required based on deterministic findings alone

## Fabrication Check
Checking post claims against brief...
⚠️ FABRICATION RISK: No direct "repriced/repricing" language found, but checking Jake (AI SDR) claims against brief content.

## Voice Audit (Opus) — Aayush Voice Scoring (out of 10)

**Option 1: 5/10 — REVISE**
- First-person observer: 0/2 (no present-tense observer voice)
- Hedge markers: 0/2 (no IMO/tbh/i think hedges)
- Contrast labels: 1/2 (weak "That's infrastructure, not a feature")
- Fragment paragraphs: 1/2 (mixed rhythm)  
- Specific named details: 2/2 (good company names and numbers)
- **Fix needed:** Add present-tense observer line like "Every week I watch founders panic about AI layoffs"

**Option 2: 7/10 — REVISE**
- First-person observer: 2/2 (strong "I see it at Atlan", "Every week I watch")
- Hedge markers: 0/2 (no hedges)
- Contrast labels: 2/2 (excellent "That's not X, That's Y" pattern)
- Fragment paragraphs: 2/2 (clear fragment rhythm)
- Specific named details: 1/2 (some specifics but could be stronger)
- **Fix needed:** Drop natural hedge like "tbh" before coordination overhead claim

**Option 3: 8/10 — SHIP** (meets 8+ threshold)
- First-person observer: 2/2 (strong "Every week I watch", specific Atlan context)
- Hedge markers: 0/2 (no hedges)
- Contrast labels: 1/2 (weak contrast labels)
- Fragment paragraphs: 2/2 (excellent rhythm)
- Specific named details: 2/2 (Jake details, specific numbers)
- **Could improve to 10/10:** Add hedge near AI-native operations claim

## Fact Check (Gemini)

**CRITICAL FALSE CLAIM FOUND:**
- ❌ **Cloudflare eliminated 1,100 customer support roles via AI** — FALSE. This appears to be confusion with Klarna's AI assistant story (700 support agents). Cloudflare has not reported eliminating 1,100 support roles due to AI.

**Brief:**
- ✅ Anthropic 10x year-over-year growth (Revenue ~$100M to ~$1B ARR) 
- ✅ OpenAI reasoning gap closure in voice agents
- ⚠️ "Tech companies lay off >10% workforce" (broad generalization, true for specific companies)

**Option 1:**
- ✅ All layoff numbers verified (Meta 21k, Amazon 18k, Google 12k)
- ❌ Carries false Cloudflare claim from brief

**Option 2:**
- ✅ Twitter 7,500 to 1,500 employees confirmed
- ⚠️ "Twitter runs better than before" (highly subjective/debated)

**Option 3:**
- ✅ Jake SDR claims match aayush-experiences.md (47 meetings, $1.04M pipeline, closed-lost accounts)
- ❌ Repeats false Cloudflare claim

**Recommended by fact-checker:** Option 1 (fewest unverifiable claims)

## Adversarial Attack (Grok) — TIMED OUT
*Grok analysis incomplete due to API timeout*

## Overall Council Verdict: **REVISE**

**Blocking Issues (must fix before ship):**
1. **CRITICAL:** False Cloudflare claim appears in brief + Options 1&3 — must correct or remove entirely
2. **Voice Quality Gate:** Only Option 3 meets 8/10 voice threshold. Options 1&2 need voice improvements.
3. **Format Violations:** Multiple deterministic violations (em dashes, MBA vocab, long sentences, guru voice)

## Required Revisions:

**Brief:**
- Fix/remove fabricated Cloudflare 1,100 layoffs claim (use Klarna example instead, or remove)
- Replace MBA vocabulary: "commoditized", "moat", "enterprise customers"
- Fix guru voice: "Founders building consumer AI products should review"
- Shorten 5+ sentences over 22 words
- Convert em dashes to hyphens

**Posts:**
- **Option 1:** Add first-person observer voice + fix Cloudflare claim
- **Option 2:** Add hedge markers + strengthen specific details  
- **Option 3:** Fix false Cloudflare claim (otherwise ships)
- **All options:** Fix "Not X its Y" inversion in Option 1
