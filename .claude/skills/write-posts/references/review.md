# 15-Point Voice Audit

Every post must pass 12/15 to ship. The `/attack` skill runs this as part of council review.

Scoring: 1 = clean pass, 0 = violation. Total out of 15. Each violation requires a specific revision note.

---

## Hook (3 points)

1. **Hook earns the scroll.** First line creates curiosity or tension. A tired founder on mobile pauses. (Pass if hook score ≥7 per `hooks.md` rubric. Fail if it's a question, a cliche opener, or throat-clearing.)

2. **Hook fits under 70 characters.** One line on mobile. Hard count. (Pass = 1–70 chars. Fail = >70 OR ≤10 unless it's a Pattern F direct challenge.)

3. **Hook names something concrete.** Company, tool, number, or named experience. Not abstract ("the future of X") or meta ("here's a thought"). (Pass = contains a proper noun, a specific number, or a first-person observation. Fail = pure abstraction.)

---

## Voice (5 points)

4. **No corporate openers.** No "excited/thrilled/proud to announce", no "check out our latest". (Pass if neither phrase appears in first 2 lines.)

5. **Active voice throughout.** (Pass if ≤1 passive construction. Fail = ≥2 passive constructions or passive in the hook.)

6. **Lowercase i used consistently.** No uppercase "I" as the pronoun. (Pass = all "i" lowercase. Fail = any uppercase "I" pronoun. Uppercase "Atlan", "OpenAI", etc. is correct — check context.)

7. **Dashes, not bullets.** Uses `-` or line breaks. Never `•` or numbered lists for non-sequential content. (Pass if 0 `•` and no numbered listicles. Fail = any `•` or numbered list without story context.)

8. **No em dashes.** Hard regex check. Em dashes banned everywhere. (Pass = 0 em dashes. Fail = ≥1 em dash.)

---

## Content (4 points)

9. **Opens with a story, person, or moment.** Not a concept. Not a definition. (Pass = first 3 lines introduce a scene or named entity. Fail = starts with "AI is X" or "RAG stands for Y".)

10. **Named tools, repos, or companies.** At least 1 specific name. (Pass = ≥1 proper noun referring to a tool/company/repo. Fail = zero specificity.)

11. **Specific numbers.** At least 1 specific data point. Dollar amounts, time, percentages, team size, throughput. (Pass = ≥1 specific number with unit. Fail = zero numbers OR vague numbers like "a lot" / "many".)

12. **Reader finishes thinking "i should try this."** Actionable outcome or insight. (Pass = post ends with something the reader could DO within 24 hours. Fail = ends with vague reflection or generic positivity.)

---

## Kill list + format (3 points)

13. **Zero kill-list words.** Regex check against `kill-list.md` categories 1A–1F and 1K. (Pass = 0 violations. Fail = ≥1 banned phrase.)

14. **Rhythm variation.** No 3 consecutive sentences of similar length. Short-medium-short-long rhythm, not 4 same-length sentences in a row. (Pass = eyeball check — mixed sentence lengths. Fail = obvious monotone rhythm.)

15. **CTA works.** Not "Learn more." Not engagement bait ("Like if you agree"). Either a question that forces a stance, an invitation to try something specific, or an open-ended curiosity. (Pass = CTA is specific or invitational. Fail = generic engagement bait or "Learn more".)

---

## Scoring

- 15/15 — ship immediately
- 13–14/15 — ship with note on minor fix
- 12/15 — ship threshold. Fix one violation, re-check.
- <12/15 — revise. Return specific revision notes per failed dimension.

## Output format (for /attack)

```json
{
  "option_1": {
    "scores": {
      "hook_scroll": 1,
      "hook_length": 1,
      "hook_concrete": 1,
      "no_corporate": 1,
      "active_voice": 0,
      "lowercase_i": 1,
      "dashes_not_bullets": 1,
      "no_em_dashes": 1,
      "opens_with_story": 1,
      "named_tools": 1,
      "specific_numbers": 1,
      "actionable": 1,
      "no_kill_list": 1,
      "rhythm_variation": 1,
      "cta_works": 1
    },
    "total": 14,
    "violations": ["active_voice: Line 3 uses passive. Rewrite: 'teams ship' not 'it is shipped by teams'."],
    "verdict": "ship_with_fix"
  },
  "option_2": { "...": "..." },
  "option_3": { "...": "..." },
  "recommended": 1,
  "revision_needed": false
}
```

Revision triggered when ANY option scores <12, OR when all 3 options score identically (suggests model laziness — rewrite at least 2 with different angles).
