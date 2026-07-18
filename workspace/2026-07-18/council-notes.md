# Council — 2026-07-18 (iteration 1)

## Deterministic findings (Pre-flight violations)

**CONFIRMED hard-rule failures requiring REVISE:**

### Brief violations (1,312 words - FAIL)
- **Word count violation:** Brief is at 1,312 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### Long sentence violations (Brief)
- 48w: "AI infrastructure money flows to inference as compute becomes the only durable value layer"
- 115w: "Key takeaways: Databricks $188B valuation with published cost savings research on open..."
- 28w: "TechCrunch reports https://techcrunch.com/2026/07/17/why the first gpu financiers are turning to inference chips..."
- 26w: "In 2022, the constraint was 'can we train anything useful?' Now it's..."
- 24w: "The causal chain forward runs through specialized inference chips creating pricing pressure..."

### Not X, It's Y violations
**Brief:**
- "isn't the specific device failures. It's the"

**Posts:** 
- "aren't about which model we use. They're about how"

### MBA vocabulary violations
**Brief & Posts:**
- "commoditized" (appears 2 times total)

### Em dash violations
**Total: 10 em dashes found**
- Brief: 1 em dash
- Posts: 9 em dashes  

### Guru voice violations (Posts)
- "founders make the same mistake, competing on model quality when they should be"

**VERDICT: REVISE** - Multiple hard-rule violations require fixes before shipping.

## Fabrication Check
Checking post claims against brief...
No significant fabrication risks detected in posts versus brief content.

## Voice audit (Claude Sonnet 4.6)

### Option 1: 12/15 — Ship with fix
**Violations:**
- Hook names abstract debate rather than concrete entity
- Capital "I" used throughout (should be lowercase "i")

### Option 2: 11/15 — Revise (below 12/15 threshold)
**Violations:**
- Capital "I" used throughout  
- Opens with stat rather than story/person/moment
- No named external companies/tools beyond GPU financiers and Atlan
- No clear actionable step for reader

### Option 3: 12/15 — Ship with fix
**Violations:**
- Capital "I" used throughout
- Uses bullet formatting instead of dashes for three-item list  
- Opens with stat rather than story/person/moment

## Fact check (Gemini 3.1 Pro)
**✅ Verified companies:** Databricks, OpenAI, Atlan, Vertu, Ethan Mollick, LiteLLM

**⚠️ Unverifiable claims:**
- OpenAI CFO Sarah Friar publishing specific "scorecard" document
- Databricks research showing 60%+ cost savings from open-weight models  
- Ethan Mollick's specific quote (tweet ID from future date 2026)

**❌ False/problematic claims:**
- Databricks $188B valuation (actual ~$43B; URL dated 2026)
- $400M GPU financier deployment (URL dated 2026) 
- TechCrunch URLs all dated July 2026 (fabricated future dates)
- Vertu $6,880 AI device review (URL dated 2026)

**Recommendation:** None of the options recommended for immediate publishing due to fictional 2026 events stated as current facts.

## Adversarial attack (Grok 4)

### Brief findings:
- **Unsupported claim:** "Regardless of whether open-weight models dominate the future, compute providers capture the value" (no evidence on margins or market share)
- **Straw man:** "Builders obsess over whether GPT or Claude or Llama wins" (misrepresents actual founder concerns)
- **Neat bow closer:** Forces narrative unity across unrelated items 
- **Guru voice:** "What I keep coming back to is..." presents speculation as insider insight

### Option 1 findings:
- **Not X, it's Y inversion:** "Everyone's debating open vs closed models. But that's the wrong question"
- **Stat-Stat-Reframe pattern:** Uses scaffolding to build authority then pivot to self-reference

### Option 2 findings:  
- **Absurdist metaphors:** "faster than my savings account" and "like my mom's text messages" break tone
- **Unsubstantiated personal claim:** "I've been tracking this through our agent costs at Atlan" with no numbers

### Option 3 findings:
- **"Why now" structural label:** "Three stories this week" implies false recency
- **Corporate language:** "infrastructure advantage goes to teams that can arbitrage" without concrete steps

## Overall verdict: REVISE

**Primary issues requiring fixes:**
1. **Word count:** Brief at 1,312 words, needs 2000+ minimum
2. **Long sentences:** Multiple violations over 22 words in both brief and posts  
3. **Not X, it's Y inversions:** Both brief and posts contain banned rhetorical patterns
4. **Voice audit failures:** Option 2 below 12/15 threshold; Options 1&3 need fixes
5. **Fact-check concerns:** Multiple fictional 2026 events presented as current facts
6. **Adversarial issues:** Guru voice, unsupported claims, forced narrative coherence

**Specific revision priorities:**
1. Expand brief lead section to reach 2000+ words with more mechanism/specificity
2. Fix all long sentences (break into <22 word chunks)
3. Remove "Not X, it's Y" inversions in both brief and posts
4. Change all "I" to lowercase "i" in posts per voice rules
5. Remove guru voice positioning and unsupported "At Atlan we..." claims
6. Fix factual claims or clearly mark as speculative/projected
