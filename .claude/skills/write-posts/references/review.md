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
- <12/15 — **HARD REJECT** the whole option. Regenerate with a different template angle. Do NOT patch-revise below threshold.

## Anti-Slop 5 Tests (second pass — runs AFTER 15-point audit)

Every post MUST pass all 5 before ship. Council `/attack` checks via LLM + `scripts/clean_text.py` regex.

### Test 1: Substitution
Replace the specific named company/person in the hook with a generic one ("another AI tool"). If the post still works → it's too generic. Rewrite until it can only be about THIS specific thing.

### Test 2: Specificity Count
≥3 specific items per post: named companies, real numbers, named people, linked repos. Zero specifics = reject.

### Test 3: Jargon Scan
Zero matches for categories 1A–1F of kill-list.md. Auto-fixed by `clean_text.py` unless LLM introduced a new variant.

### Test 4: Stat-Stat-Reframe-Metaphor Check
No "X company did Y. Z company did W. The reframe is..." scaffolding. Stats must weave into the argument, not bullet-stack. If the post has this pattern → reject and rewrite with one clear argument line.

### Test 5: "So What?" Test
For every sentence, answer: "so what does this mean for the reader?" in one sentence. If can't answer → cut the sentence.

## Post-Specific Tests (additional)

### Test 6: First-Person Verification
Every `i [verb] [specific event/number/team/client]` claim must trace to a verified entry in `config/aayush-experiences.md`. If no match → the claim is fabricated → reject the whole post option and rewrite as a take (opinion), not a story (experience).

### Test 7: 3 Distinct Angles
The 3 shipped post options MUST use 3 different structures:
- Option 1: **Commentary take** — pure opinion on the news, zero personal story claimed
- Option 2: **Data-point expansion** — leads with ONE verifiable number from research.md, unpacks implication
- Option 3: **Pattern observation** — connects 2+ verified stories from research.md

If 2+ options use the same "problem → fake personal story → workflow list → CTA" mold → reject the whole set, regenerate.

### Test 8: Hook Gate (hard fail <7)
Hooks scored 1–10 per `hooks.md` rubric (scroll-stop + specificity + tension + voice-match). If ANY hook scores <7 → reject that option and regenerate with a different template, don't patch-revise the hook.

## Output format (for /attack)

```json
{
  "option_1": {
    "scores": { ...15 dimensions... },
    "voice_audit_total": 14,
    "anti_slop_tests": {
      "substitution": "pass" | "fail: quoted sentence",
      "specificity": "pass" | "fail: only 1 specific found",
      "jargon": "pass" | "fail: 'leverage' in line 7",
      "stat_stat_reframe": "pass" | "fail: paragraph 3 matches pattern",
      "so_what": "pass" | "fail: line 12 has no reader outcome"
    },
    "first_person_verification": "pass" | "fail: claim 'i deleted 1,200 lines' has no entry in aayush-experiences.md",
    "hook_score": 8,
    "hook_pattern": "B",
    "verdict": "ship" | "ship_with_fix" | "reject_and_regenerate"
  },
  "option_2": { ... },
  "option_3": { ... },
  "angles_distinct": true | false,
  "recommended_option": 1,
  "overall_verdict": "ship" | "regenerate"
}
```

If `angles_distinct` is false OR any option has `verdict: reject_and_regenerate` OR hook_score <7 → the council returns `overall_verdict: regenerate` and `/write-posts` runs again with a prompt noting which angles to avoid.

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
