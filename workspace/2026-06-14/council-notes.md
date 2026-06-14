# Council — 2026-06-14 (iteration 1)

## Deterministic findings (MANDATORY FIXES)

**CONFIRMED VIOLATIONS - VERDICT: REVISE**

### Em dashes (4 violations in posts.md)
- Em dashes found: 4 instances in posts.md
- Zero tolerance rule violated - all must be replaced with regular hyphens or rewritten

### Long sentences (17 violations total) 
**Brief.md (5 violations):**
- 34w: "AI models are now political assets controlled by governments, not companies Beijing..."
- 97w: "Key takeaways: Meta started dismantling its $2B Manus deal after Beijing ordered..."
- 34w: "Amazon triggered Anthropic's model shutdown through security concerns Andy Jassy https://techcrunch.com/2026/06/13/amazon ceo..."
- 46w: "Nathan Lambert captured https://x.com/natolambert/status/2065879789488250976 the new reality: 'Models are released when the...'"
- 35w: "India debates sovereign AI after losing Anthropic access Tech leaders in India..."

**Posts.md (12 violations):**
- 69w: "LinkedIn posts, 2026 06 14 Lead: Government and geopolitical forces are now..."
- 40w: "Character count: 1,456 OPTION 2, data point hook score: 8 Conviction: L1:..."
- 30w: "When $2 billion deals get killed by government phone calls, every AI..."
- 35w: "The supply chain looks like this: You build the product American labs..."
- 23w: "Every enterprise customer is about to start asking: 'what happens if the...'"
- Plus 7 more long sentences

### Not X, It's Y violations (6 violations total)
**Brief.md (5 violations):**
- "isn't technical failure. It's political"
- "isn't just about national pride. It's about business"  
- "aren't separate incidents. They're the"
- "isn't a technical failure. It's a"
- "isn't a toy model. It's production"

**Posts.md (1 violation):**
- "aren't just technical choices anymore. They're business"

### Guru voice violations (4 violations in brief.md)
- "builders building AI products, this is the cautionary tale you should show"
- "Companies buying AI tools need to audit"
- "Companies that want to avoid"
- "For builders,"

### Word count violation
- Brief is at 1703 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### MBA vocabulary (1 violation)
- "enterprise customer" in posts.md

## Fabrication Check
⚠️ Posts appear to fabricate specific first-person team experiences at Atlan that need verification against brief.

## Voice audit (Gemini)
- Option 1: 6/10 — REVISE (lacks contrast labels and specific details)
- Option 2: 7/10 — REVISE (no first-person observer, corporate tone)  
- Option 3: 8/10 — SHIP (strong first-person voice and specific details)

## Fact check (Gemini)
- ✅ All company names and deal amounts verified
- ✅ Timeline details match source dates
- ⚠️ "At Atlan, we've been testing" claims not grounded in brief - potential fabrication

## Adversarial (Grok)
- Brief: Strong causal chains, good mechanism explanation
- All options: Fresh angle, good specificity
- Option 1: Contrarian take is well-supported
- Option 2: Data-point approach works but could use more specificity
- Option 3: Pattern observation is solid

## VERDICT: REVISE

Priority fixes needed:
1. **CRITICAL - Em dashes removed** (clean_text already fixed)
2. **Long sentences broken up** - 15 violations across both files
3. **"Not X, It's Y" structures rewritten** - 6 violations total
4. **Guru voice removed** - 4 violations in brief ("For builders", "Companies should")
5. **Word count expansion** - Brief needs 300+ more words for 2000+ requirement
6. **MBA vocabulary** - Replace "enterprise customer" in posts

Specific revision notes:
- brief.md: Expand lead section with more mechanism/specificity detail
- brief.md: Rewrite "isn't X, it's Y" structures to positive statements
- brief.md: Remove prescriptive language targeting builders/companies
- posts.md: Replace "enterprise customer" with "large company"
- posts.md: Break up long sentences in metadata sections
