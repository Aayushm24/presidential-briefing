# Council — 2026-04-19 (iteration 1)

## Deterministic pre-flight findings

**CONFIRMED hard-rule violations (regex-detected):**
- **brief.md**: 1 em dash violation found (U+2014 not allowed)
- **posts.md**: 1 em dash violation found (U+2014 not allowed)  
- **brief.md format**: 2 em dash format violations detected

These are HARD FAILS requiring immediate fix before any ship consideration.

## Voice audit (Opus)

### Option 1 (Contrarian): 12/15 — ship_with_fix
**Violations:**
- Hook has no proper noun, specific number, or named experience; 'AI isn't your competitive advantage' is pure abstraction — Fix: 'Cerebras just filed for IPO. Your model isn't the moat.'
- First 3 lines are thesis statements, not a story, person, or moment — Fix: open with the Cerebras IPO filing or Tesla robotaxi week as a scene, then derive the thesis

### Option 2 (Dot-connecting): 15/15 — ship
**Clean pass** — no violations detected

### Option 3 (Personal-discovery): 12/15 — ship_with_fix
**Violations:**
- Hook has no proper noun, specific number, or named experience; 'the wrong layer' is abstract — Fix: 'i've been building Atlan's agents on the wrong layer for 4 months.'
- Contains em dash '—' in 'The AI was smart enough — it just couldn't remember.' — Fix: split into sentences: 'The AI was smart enough. It just couldn't remember.'
- No specific number with unit in the post; 'months' is vague — Fix: add concrete metric like 'lost context across 200+ sessions'

## Fact check (Gemini)

**CRITICAL FALSE CLAIMS DETECTED:**

### Brief & all posts:
- ❌ **"Cerebras filed for IPO with a $10+ billion OpenAI deal"** — FALSE. Deal is with G42 (UAE), not OpenAI
- ❌ **"Tesla expanded robotaxis to three Texas cities generating commercial revenue without safety drivers"** — FALSE. Tesla does not currently operate a commercial, driverless robotaxi network
- ❌ **"Cerebras announced agreement with AWS to use Cerebras chips in Amazon data centers"** — FALSE. AWS uses custom silicon; Cerebras' major cloud partner is G42

### Additional violations:
- **Em dashes found**: 1 in each of the 3 posts (automatic fail per rules)

**Recommended**: None are usable as-is due to core factual errors regarding Tesla and Cerebras.

## Adversarial (Grok)

### Brief analysis:
- **Logical gaps**: Assumes causation from correlation without evidence linking Cerebras and Tesla events
- **Unsupported claims**: "AI infrastructure layer is maturing" — no evidence of broader trend beyond two events
- **Guru voice**: "Builders should treat 2026 as..." — prescriptive advice violating first-person rule
- **Argument breakdowns**: Jumps from two events to prescriptive forecast without intermediate reasoning

### Option analysis:
- **Option 1**: Contrarian Philosopher style, fresh angle, BUT guru voice violations ("teams winning right now", "everyone obsesses")
- **Option 2**: CORPORATE ANALYST (reject) — fabricated claim about "Small teams with Claude Code ship what 50-person orgs used to build" not in experiences.md; generic AI thought-leader content
- **Option 3**: Vulnerable Victor style, BUT fabricated detailed narrative not in experiences.md ("spent weeks tweaking prompts", specific context loss scenarios)

### X search freshness: Fresh angle on infrastructure commoditization

## Verdict: REVISE

**Critical issues requiring revision:**
1. **FACTUAL ERRORS**: All Tesla robotaxi and Cerebras deal claims must be corrected or removed
2. **EM DASHES**: Multiple em dash violations across brief and posts  
3. **FABRICATED CLAIMS**: Option 2 and 3 contain unverified personal specifics
4. **GURU VOICE**: Multiple prescriptive statements violating first-person rule
5. **HOOK ISSUES**: Options 1 and 3 need concrete anchors

**Specific revision notes:**
- brief.md: Fix em dashes, remove or correct Tesla/Cerebras claims, convert guru voice to first-person observations
- posts.md option 1: Fix hook concreteness, remove guru voice
- posts.md option 2: **REJECT** — fabricated claims and corporate analyst tone  
- posts.md option 3: Fix em dash, limit to verified experiences only

**Ship threshold**: ALL factual errors must be corrected AND em dashes removed before any option can ship.