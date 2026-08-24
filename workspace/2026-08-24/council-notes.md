# Council — 2026-08-24 (iteration 1)

## Deterministic findings (pre-flight violations)

### Em dashes: 5 violations found in posts.md
**CONFIRMED hard-rule failures from clean_text.py scan:**
- Em dashes found: 5 instances in posts.md

### LLM structural violations: 1 violation found in posts.md 
**CONFIRMED from kill-list-regex:**
- "Here's the thing" (line 112 in posts.md) — banned LLM structural label

### MBA vocabulary violations: 2 instances found in brief.md
**CONFIRMED from clean_text.py scan:**
- "differentiation" (line 34 in brief.md) — banned MBA vocabulary 
- "ecosystem" (line 48 in brief.md) — banned MBA vocabulary

### Long sentence violations: 10+ violations found
**CONFIRMED from clean_text.py scan:**
- Brief contains multiple 42w, 133w, 36w, 31w, 39w sentences exceeding 22-word limit
- Posts contain multiple 43w, 27w, 24w sentences exceeding 22-word limit

### Word count violation: Brief under minimum
**CONFIRMED from word count check:**
- Brief is at 1325 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

---

## Voice audit (Gemini)

**Response truncated due to token limits, but key findings:**
- Option 1: Issues with lowercase "I" usage (should be uppercase per corpus evidence)
- Option 2: Personal fabrication concerns around Atlan specifics
- Option 3: Fabricated first-person claims without verification
- Multiple options show rhythm and structural issues

## Fact check (Gemini)

**Key findings (response truncated):**
- Anthropic "Fable" model name appears to be fabricated - Anthropic's actual models follow different naming conventions
- Revenue figures ($65B Anthropic, $40B OpenAI) unverifiable from provided sources
- Ramp as data source is real but specific 70,000 companies figure unverifiable
- Drew Breunig and Simon Willison are real people in AI space

## Adversarial review (Grok)

**Brief findings:**
- Logical gaps: Revenue figures appear without linkage to adoption data
- Unsupported claims: $65B/$47B Anthropic revenue, OpenAI growth figures
- Straw men: Quality vs economics framed as mutually exclusive
- Structural issues: "Key takeaways:", neat bow closers present
- Verdict: **REVISE**

**Post findings:**
- Option 1: Strongest option, relatable human style, but has guru voice and neat bow closers. **REVISE**
- Option 2: Heavy fabricated first-person specifics, "At Atlan" self-promotion, structural slop. **REJECT**
- Option 3: Most fabricated details, webinar voice ("here's the thing nobody talks about"). **REJECT**
- Freshness: All options marked as "saturated" - similar takes already exist
- Recommended: Option 1 (least problematic)

---

## Final Verdict: REVISE

**Critical issues requiring revision:**

### Brief.md:
1. **FABRICATED MODEL NAME**: "Fable" appears to be invented - Anthropic models don't use this naming
2. **MBA vocabulary**: Remove "differentiation" and "ecosystem" 
3. **Word count**: Expand from 1325 to 2000+ words with mechanism detail
4. **Long sentences**: Break 10+ sentences over 22 words
5. **Unsupported revenue claims**: Remove or source $65B/$47B figures

### Posts.md:
1. **Em dashes**: Remove all 5 instances
2. **LLM structural label**: Remove "Here's the thing" from Option 3
3. **Fabricated claims**: Verify or remove personal anecdotes in Options 2&3
4. **Guru voice**: Remove prescriptive language from all options
5. **Neat bow closers**: Rewrite ending structures

### Revision priority:
1. **Option 1**: Fix guru voice, neat bow - can be saved
2. **Options 2&3**: Require complete rewrite due to fabrication issues

**Ship threshold not met**: Multiple deterministic violations + fabricated content requires full revision before ship consideration.