# Council — 2026-04-22 (iteration 0)

## Deterministic findings (pre-flight)

**CONFIRMED violations found via regex:**

### Brief violations (2):
- banned_phrase: "the future of" (line in brief.md)
- audience_direct_address: "for founders" (line in brief.md)

### Posts violations (3):
- em_dash found (U+2014 not allowed) - multiple instances in posts.md
- banned_word: "mission-critical" (line in posts.md) 
- banned_phrase: "Here's what I learned" (line in posts.md)

### Format violations (1):
- mba_vocab_moat_hits=1 (expect 0 — use 'the thing competitors can't copy' or name it concretely)

### Plain English violations:
- mba_vocabulary_violation: 0 (flag not triggered but hits found)
- long_sentence_violation: 2 (multiple long sentences over 22 words)

**VERDICT: REVISE** (pre-flight violations found)

Specific revision notes from deterministic scan:
- brief.md: Replace "for founders" with named specifics or remove audience direct address
- brief.md: Replace "the future of" with present-tense specific claim
- brief.md: Replace "moat" usage with "the thing competitors can't copy" or name the specific advantage
- posts.md: Remove all em dashes (U+2014) - use commas, periods, or ellipsis
- posts.md: Replace "mission-critical" with specific operational impact
- posts.md: Remove "Here's what I learned" opener
- Both files: Break long sentences (>22 words) into shorter sentences

LLM passes running...