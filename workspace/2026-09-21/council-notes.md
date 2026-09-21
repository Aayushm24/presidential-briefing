# Council — 2026-09-21 (iteration 1)

## Deterministic Findings (Pre-flight Violations)

**VERDICT: REVISE** — Hard rule violations found that must be fixed before ship:

### Em Dash Violations (13 total)
- brief.md: 3 em dashes found (zero tolerance rule)
- posts.md: 10 em dashes found (zero tolerance rule)
*Fix: Replace all em dashes (—) with regular hyphens (-) or rewrite sentences*

### "Not X, It's Y" Inversions (3 total)
**Brief violations:**
- "isn't that Waymo was always safe. It's that"
**Posts violations:**
- "aren't calibrated for your production data. They're calibrated"
- "isn't better models. It's better"
*Fix: Rewrite to state what something IS rather than what it ISN'T*

### Guru Voice Violation (1 total)
**Brief violation:**
- "builders shipping long-running AI systems must engineer"
*Fix: Change from third-person prescription to first-person observation*

### Word Count Violation
- Brief is at 1105 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### Long Sentence Violations (Multiple)
**Brief long sentences (>22 words):**
- 29w: "Agentic AI pipelines hit reliability walls that builders must engineer around today..."
- 93w: "Key takeaways: Language quality degrades in extended agent sessions as models drift..."
- 23w: "The model that opened with crisp, professional language ends the session generating..."
- 23w: "When a model says it's "70% confident" about something, that percentage only..."
- 24w: "If you're building an agent that needs to produce complete documents, you..."

**Posts long sentences:**
- Multiple sentences exceeding 22-word limit requiring breaking into shorter, punchier fragments

## LLM Review Results

### Voice Audit (Claude Opus 4.7)
**Option 1: 12/15** - Ship with fixes
- ❌ Hook lacks specificity (no proper noun/number/specific detail)
- ❌ Uses capital 'I' throughout (should be lowercase 'i')  
- ❌ Opens with generalization rather than story/person/moment
- ✅ Strong body with named examples (Ethan Mollick, Atlan, Claude, OpenAI)
- ✅ Concrete numbers (10-20 completions)

**Option 2: 13/15** - Ship with fixes
- ❌ Hook exceeds 70 characters (~108 chars)
- ❌ Uses capital 'I' throughout
- ✅ Opens with concrete Claude quote and specific percentage
- ✅ Names Sebastian Raschka and Atlan
- ✅ Sharp thesis on confidence calibration

**Option 3: 14/15** - Ship with fix
- ❌ Uses capital 'I' throughout (only violation)
- ✅ First-person build story as hook
- ✅ Names Mollick, Claude, OpenAI, Simon Willison, llm-keys-ui
- ✅ Specific 4-hour timeline
- ✅ Synthesizes three reliability walls with concrete actions

### Fact Check (Gemini 3.1 Pro Preview)
- Response truncated but indicated some verification issues
- Need to investigate specific Twitter status IDs mentioned in brief
- General technical claims about Claude/OpenAI capabilities appear accurate

## Final Verdict: REVISE

**REVISE triggered by multiple hard rule violations:**
1. **Deterministic violations** (13 em dashes, 3 "Not X, it's Y" inversions, 1 guru voice, word count deficit)
2. **Voice audit findings** (capital I usage across all options, hook issues in Options 1-2)
3. **Brief expansion required** (1105 words → 2000+ words needed)

### Specific Revision Instructions:

**Brief (brief.md):**
- Replace all 3 em dashes with regular hyphens or commas
- Fix "Not X, it's Y" inversion: "isn't that Waymo was always safe. It's that" → restate positively
- Change guru voice: "builders shipping long-running AI systems must engineer" → first-person observation
- Expand to reach 2000+ words with more mechanism/specificity in lead section
- Break long sentences into shorter fragments (5+ sentences need splitting)

**Posts (posts.md):**
- Replace all 10 em dashes with regular hyphens
- Fix 2 "Not X, it's Y" inversions in posts
- Change all capital 'I' to lowercase 'i' across all 3 options
- Option 1: Rewrite hook to lead with specific moment (Mollick observation or 4-hour degradation)
- Option 2: Trim hook to under 70 characters
- Break long sentences into shorter fragments

**Recommended option after revision: Option 3** (highest voice audit score, cleanest structure)
