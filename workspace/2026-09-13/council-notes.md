# Council — 2026-09-13 (iteration 1)

## Deterministic findings (pre-flight violations)

**VERDICT: REVISE** - Multiple hard-rule violations found

### Plain English violations (clean_text.py):

**Brief.md violations:**
- not_x_its_y (2 violations): MUST rewrite as positive statements
  - "isn't that Perplexity built another AI feature. It's that"
  - "isn't a productivity tool anymore. It's an"
- guru_voice (4 violations): MUST remove prescriptive language
  - "Teams building agent systems need to think"
  - "builder will need to plan"
  - "Founders building on frontier models should treat"
  - "For builders,"
- mba_vocabulary (2 violations): MUST replace with specific terms
  - "Enterprise customers"
  - "ecosystem"
- long_sentences (5 violations): MUST break into shorter sentences

**Posts.md violations:**
- em_dash (5 violations): HARD FAIL - zero tolerance [FIXED by clean_text.py]
- not_x_its_y (2 violations):
  - "isn't about AI getting better. It's about oversight"
  - "aren't specialized AI capabilities. They're standard"
- neat_bows (2 violations):
  - "The builders who see this early will staff for it now. The ones who"
  - "The ones who don't will"
- guru_voice (1 violation):
  - "Teams building agent systems need to think"
- llm_connectives (1 violation):
  - "I think they're the same story"
- long_sentences (Multiple violations): MUST break sentences over 22 words

**Total deterministic violations after clean_text.py: 8**

Status: clean_text.py fixed em_dash and kill_word violations, but core voice violations remain requiring manual revision.

## Final Council Verdict: REVISE

Proceeding to revise step to address remaining hard-rule violations.