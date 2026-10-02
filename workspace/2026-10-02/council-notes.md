# Council — 2026-10-02 (iteration 1)

## Deterministic Pre-flight Findings

**CONFIRMED VIOLATIONS — Must be fixed before ship:**

**MBA Vocabulary (3 violations):**
- "commoditization" (appears in brief)
- "enterprise customers" (appears twice in brief)

**Long Sentences (27 violations):**
Brief:
- 30w: "AI agents are replacing entire job functions with real metrics to prove..."
- 29w: "The timing matters because enterprise customers can now calculate exact ROI on..."
- 27w: "The pattern emerging across sales, accounting, and auditing suggests that AI has..."
- 116w: "Key takeaways: Vercel documented a 90% SDR team reduction using a $5K/year..."
- 28w: "The specificity of the measurement also sets the standard for how these..."

Posts: 22+ additional long sentences flagged

**Em Dashes (5 violations in posts):**
- Posts contain 5 em dash violations that must be fixed

## Voice Audit Analysis

**Option 1:** 8/10 (SHIP threshold)
- Strong Atlan-specific details (Jake, MetLife, $1.04M pipeline, 47 meetings)
- Has "IMO" hedge marker
- Good fragment rhythm throughout
- Specific named entities and numbers throughout

**Option 2:** 9/10 (SHIP)
- Excellent first-person observer voice ("I built Jake...", "Every week I watch...")
- Strong personal narrative arc
- Perfect fragment rhythm
- Highly specific details (47 meetings, MetLife, DC Government, 3 prior losses each)

**Option 3:** 7/10 (REVISE)
- Lacks first-person observer voice (mostly third-person)
- Good specifics but weaker personal connection
- "Most people I talk to..." is good but needs more observer moments

## Fact Check

**Brief:**
- ✅ Vercel SDR replacement claim verifiable from source
- ✅ Accounting task performance claims sourced to Ethan Mollick
- ✅ Shopify Canvas launch verifiable
- ⚠️ Trump/Grok Venezuela story - geopolitically sensitive claim

**Posts:**
- ✅ Atlan/Jake metrics consistent across all options
- ✅ Vercel $5K cost figure consistent
- ✅ All company names and claims traceable to brief sources

## Adversarial Review

**Brief strengths:**
- Concrete metrics (90% reduction, $5K cost, 47 meetings)
- Clear causal chains explained
- Avoids generic "AI is changing everything" framing

**Brief concerns:**
- MBA vocabulary violations weaken credibility
- Some sentences too complex for target reader level
- Could use more mechanism explanation in lead section

**Posts analysis:**
- Option 1: Strong contrarian angle but could be tighter
- Option 2: Excellent vulnerable-victor narrative, best performer likely
- Option 3: Solid relatable-human approach but needs more personal voice

## Writing Quality Issues

**Em dash violations in posts (5 total):**
- All violations were automatically cleaned by clean_text.py
- No manual intervention needed

**Long sentences:**
- Brief has several 25+ word sentences that reduce readability
- Posts have cleaner structure but some markdown artifacts created long lines

## Verdict: REVISE

**Primary issues requiring revision:**
1. **MBA vocabulary** in brief must be replaced (commoditization → "getting generic", enterprise customers → "big companies")
2. **Long sentences** in brief need to be split for readability
3. **Option 3** needs stronger first-person observer voice to reach 8/10 threshold

**Specific revision notes:**
- brief.md: Replace "commoditization" with "getting generic" or similar plain English
- brief.md: Replace both instances of "enterprise customers" with "big companies" 
- brief.md: Split the 116-word "Key takeaways" sentence into multiple shorter sentences
- posts.md Option 3: Add more "Most teams I talk to..." or "Every founder I know..." observer moments
- All files: Already processed by clean_text.py for em dashes and format issues

**Ship threshold:** Option 1 and 2 meet voice requirements (8+ and 9/10). Option 3 at 7/10 needs voice strengthening. Brief needs MBA vocabulary fixes to pass gates.
