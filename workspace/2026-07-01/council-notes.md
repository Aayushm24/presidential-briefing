# Council — 2026-07-01 (iteration 1)

## Deterministic findings

**CONFIRMED HARD-RULE FAILURES** - These MUST be fixed before shipping:

### Word count violation
- Brief is at 1,381 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### Guru voice violations (4 total)
- "Companies in other categories must either" (appears in both brief and posts)
- "Founders selling to enterprises should understand" (brief)
- "Companies building on frontier APIs should plan" (brief)

### Long sentence violations (17 total)
Including these examples:
- 27w: "Etched https://techcrunch.com/2026/06/30/nvidia competitor etched hits 5b valuation 1b in sales for ai..."
- 113w: "Key takeaways: Etched proves that enterprise AI infrastructure deals are massive and..."
- 34w: "This is the hardest milestone for any chip startup: moving from "we..."

### MBA vocabulary violations (2 total)
- "table stakes" (appears in both brief and posts)

### "Not X, it's Y" violations (2 total)
- "This is not a temporary belt-tightening. This is structural" (brief)
- "isn't the model. It's understanding" (posts)

### Em dash violations (posts only)
- 8 em dashes found in posts.md - all must be replaced with regular dashes or alternative phrasing

## Aayush Voice Score (5-point evaluation)

**Voice audit findings:**
- Option 1: 8/10 - **SHIP** (Strong first-person observer, good hedge markers, strong specifics, good fragments)
- Option 2: 5/10 - **REVISE** (Weak first-person, missing hedge markers, needs more specific present-tense observation)
- Option 3: 6/10 - **REVISE** (Good first-person, weak hedge markers, missing contrast labels)

**Lowest scoring dimensions needing fixes:**
- Option 2: Add natural hedge at opinion pivot (e.g. "IMO this is the hardest milestone") + replace vague "I see it across my network" with specific present-tense observation
- Option 3: Add contrast labels ("That's not a consulting problem. That's a forward-deployed engineering problem.")

## Fact Check (Verified via research.md)

**Brief**: All major claims verified from TechCrunch sources in research.md:
- ✅ Etched $5B valuation / $1B contracted sales (TechCrunch source)
- ✅ Tomasz Tunguz sector data +68.5% / +17.6% (X source)
- ✅ Amazon $1B FDE organization (TechCrunch source)
- ✅ Claude Sonnet 5 cost increase (Simon Willison X source)

**Posts**: Claims grounded in brief sources.

## Adversarial Attack (Grok with X search)

**Brief issues:**
- "Not X, it's Y" inversion violation: "This is not temporary belt-tightening. This is structural reallocation."
- Logical gap: "structural reallocation" asserted without evidence vs. cyclical spend shift

**Option 1 issues:**
- Unsupported leap: "creates two distinct go-to-market strategies" with no data or mechanism shown

**Option 2 issues:**
- Vague claim: "Teams shipping with identical tools getting different outcomes" needs examples/metrics
- Teaser without substance: "AI Native means transforming at 3 levels" (incomplete)

**Option 3 issues:**
- Anecdotal scope: "Every team I talk to this week" overstates personal network breadth

**Freshness**: All claims verified fresh on X - Etched, Amazon FDE, and market data confirmed current.

## Writing Audit

**Additional violations found:**
- Em dashes: 8 found in posts.md (must be replaced)
- Long sentences: 17 violations across brief + posts
- Not X, it's Y patterns: 2 violations identified

**OVERALL VERDICT: REVISE**

**Critical fixes required:**
1. Fix all deterministic hard-rule failures (word count, guru voice, long sentences, MBA vocab, em dashes)
2. Address voice score failures for Options 2 & 3
3. Fix "Not X, it's Y" inversions in brief and posts
4. Support unsupported strategy claims with data/mechanism
