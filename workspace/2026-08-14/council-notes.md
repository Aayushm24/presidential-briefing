# Council — 2026-08-14 (iteration 1)

## Deterministic findings

**VERDICT: REVISE** — Hard rule violations found in pre-flight check.

**Violations summary:**
- Em dashes: 9 total (5 in brief.md, 4 in posts.md) — ZERO TOLERANCE
- MBA vocabulary: 2 hits ("table stakes")
- Guru voice: 2 hits ("companies raising at these valuations need to prove")
- Long sentences: 20 total with 2 violations
- Brief word count: 1518 words (needs 2000+ minimum)

**Specific violations from clean_text.py:**

**Brief violations:**
- guru_voice: "companies raising at these valuations need to prove"
- mba_vocabulary: "table stakes"
- long_sentences (5 over limit):
  - 27w: "AI observability merges with enterprise monitoring as OpenAI accelerates with 14x speed..."
  - 117w: "Key takeaways: Arize AI acquired by Dynatrace creates Dynarize, a $14B observability..."
  - 44w: "Instead of 'AI assistant that helps with code,' teams can build 'pair..."
  - 29w: "Capital supercycle validates the enterprise AI infrastructure thesis Databricks https://techcrunch.com/2026/08/13/databricks wanted to..."
  - 26w: "When VCs fight to put more money into a round than founders..."

**Posts violations:**
- guru_voice: "companies raising at these valuations need to prove"  
- mba_vocabulary: "table stakes"
- long_sentences (several over limit)

These violations must be fixed before ship. Running LLM passes to identify additional issues...

## Fabrication Check
Checking post claims against brief...

## Aayush voice score (10-point, gate at 8)

**Option 1: 8/10 — SHIP**
- Dimensions: first_person_observer=2, hedge_markers=0, contrast_labels=2, fragment_paragraphs=2, specific_named_details=2
- Missing: hedge markers (IMO, i think, tbh)
- Fix: Add one hedge marker to soften tone

**Option 2: 6/10 — REVISE** 
- Dimensions: first_person_observer=2, hedge_markers=0, contrast_labels=0, fragment_paragraphs=2, specific_named_details=2
- Missing: hedge markers, contrast labels
- Fix: Add hedge markers and "That's X." recap tags

**Option 3: 5/10 — REVISE**
- Dimensions: first_person_observer=1, hedge_markers=0, contrast_labels=0, fragment_paragraphs=2, specific_named_details=2  
- Missing: stronger first-person observation, hedge markers, contrast labels
- Fix: Upgrade observer voice, add hedges and contrast labels

## Writing audit (clean_text.py post-cleaning)

**Still failing after clean_text.py run:**
- Guru voice: 2 instances ("companies raising at these valuations need to prove")
- MBA vocabulary: 2 instances ("table stakes") 
- Long sentences: 20 total with 2 violations flagged
- Brief word count: 1518 words (needs 2000+ minimum)

## Fact check (Gemini)

*Note: LLM responses had issues - manual fact verification recommended*

Key claims to verify:
- Arize AI acquired by Dynatrace for $14B
- OpenAI GPT-5.6 Sol 14x speed via Cerebras
- Databricks $5B at $190B valuation
- IBM-OpenAI consultant training partnership

## Adversarial attack (Summary)

Based on voice audit findings:
- Option 1: Passes voice threshold (8/10) but needs hedge markers
- Options 2 & 3: Below voice threshold, need substantial revision
- All options need guru voice fixes ("companies need to prove" → observation style)
- "Table stakes" vocabulary needs replacement with plain English
- Brief needs expansion to meet 2000+ word minimum

## Verdict: REVISE

**Reasons for REVISE:**
1. **Voice gate failures**: Options 2 & 3 score below 8/10 threshold
2. **Hard rule violations**: MBA vocabulary ("table stakes"), guru voice patterns, long sentences
3. **Brief length**: 1518 words vs 2000+ requirement
4. **Multiple post options need substantial revision**

**Specific revision notes:**
- **brief.md**: Expand lead section by ~500 words with more mechanism/specificity, replace "table stakes" with "everyone has it", rewrite guru voice line about companies
- **posts.md Option 1**: Add hedge marker (tbh/IMO) to maintain 8/10 voice score, replace "table stakes"  
- **posts.md Option 2**: Add hedge markers + "That's X." recap tags, upgrade voice from 6/10 to 8/10
- **posts.md Option 3**: Strengthen first-person observer voice, add hedge markers and contrast labels, upgrade from 5/10 to 8/10