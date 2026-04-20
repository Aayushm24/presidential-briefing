# Council — 2026-04-20 (iteration 1)

## Deterministic findings (pre-flight)

**CONFIRMED violations (no LLM interpretation needed):**

### Brief violations (1):
- em_dash found (U+2014 not allowed)

### Posts violations (2):
- em_dash found (U+2014 not allowed)  
- analogy_pattern: "It's like X" — turn into a question

### Format violations (4):
- em_dash_found
- inline_links=0 (expect >=3)
- em_dash_found (duplicate)
- inline_links=0 (expect >=3) (duplicate)

### MBA vocabulary violations (1):
- MBA vocabulary detected: "moat" (3 instances), "Enterprise customers" (1 instance)

### Long sentence violations (1):  
- Long sentences detected:
  - Brief: "AI startups have 12 months before platform providers absorb their categories Notion..." (28w)
  - Brief: "Key takeaways: Claude 4.7 costs 46% more tokens than 4.6 for text,..." (109w)
  - Brief: "Many AI startups exist partly because foundation models haven't expanded into their..." (44w)
  - Brief: "A three person team with better AI can't overcome a platform with..." (26w)
  - Brief: "Nikhyl Singhal from Meta and Google https://www.lennysnewsletter.com/p/why half of product managers are..." (24w)
  - Posts: "LinkedIn posts, 2026 04 20 Lead: AI startups have 12 months before..." (45w)
  - Posts: "The first question our security team asks now isn't 'how does the..." (38w)

### "not X, it's Y" violations (4):
- Brief: "isn't adding AI image generation to their existing canvas. They're changing"
- Brief: "isn't just the new features. It's the"  
- Posts: "aren't building better models. They're building"
- Posts: "isn't about model access anymore. It's about who"

**Deterministic verdict: REVISE** (due to violations found in pre-flight checks)

---

## Voice audit (Opus)

**Option 1: 13/15 — ship_with_fix**
- Violations: Uppercase "I" throughout (must be lowercase "i")
- Overall strong post with concrete hook and specific numbers
- Fix needed: Change all "I believe it", "I talk to" → "i believe it", "i talk to"

**Option 2: 15/15 — ship immediately** 
- Clean pass on all dimensions
- Strong hook with specific numbers (46%, Claude 4.7)
- No violations found

**Option 3: 9/15 — HARD REJECT**
- Multiple passive constructions ("got breached", "got hit", "got compromised") 
- Kill-list violations: "stack" x2, "Enterprise"
- No specific numbers anywhere
- Must regenerate with different template

## Fact check (Gemini)

**Critical FALSE findings:**
- Claude 4.7 does not exist (current version is 3.5)
- TechCrunch article dated 2026-04-19 is fabricated (future date)
- Simon Willison's Claude 4.7 token comparison tool is fabricated

**Verified claims:**
- Canva has 100 million users ✅
- o1 proved reasoning could scale with compute ✅

**Unverifiable claims:**
- Notion rebuilt agent system five times
- Half of product managers face displacement
- Vercel security incident via Context.ai

**Recommended:** Option 3 (fewest false claims)

## Adversarial review (Grok)

**Brief verdict: REVISE**
- Guru voice in "What to do this week" section (prescriptive advice)
- Unsupported Notion claim not in research.md
- Multiple "not X, it's Y" violations (≥4 instances)
- Structural labels instead of narrative flow

**Post verdicts: All REVISE**
- Option 1: Fabricated Notion claim, mild guru voice 
- Option 2: Guru voice in winner/loser framing ("teams that audit... beat teams that...")
- Option 3: Guru voice prescribing to "teams" instead of first-person

**Style diversity:** ✅ All 3 use different Blueprint styles
**Freshness:** All fresh angles based on X search
**Builder relevance:** All would be forwarded by practitioners

## Final Verdict: REVISE

**Critical issues requiring fixes:**
1. **FALSE claims:** All references to Claude 4.7, 2026 dates, and fabricated tools must be corrected
2. **Guru voice:** Multiple prescriptive statements to imagined audiences must be rewritten as first-person observations
3. **Fabricated specifics:** Notion "five times" claim has no source - remove or replace
4. **Kill-list violations:** MBA vocabulary ("moat", "enterprise", "stack") must be replaced
5. **Voice audit:** Option 3 needs complete regeneration; Options 1-2 need targeted fixes

**Iteration: 1**
**Best salvageable option:** Option 2 (after fact corrections and guru voice fixes)