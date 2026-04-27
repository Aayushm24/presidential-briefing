# Post feedback design doc — 2026-04-27 (jagged frontier post)

**Source:** Aayush wrote and ran the post through me for refinement before posting. `source: aayush-direct-write` in feedback-log.

**Slug:** `jagged-frontier-the-20-percent`

---

## Gap analysis

There was no pipeline-generated version of this post — Aayush drafted it himself, then asked for refinement. The earlier draft and the finalized version differ on three structural axes:

| Axis | Earlier draft | Finalized version |
|---|---|---|
| Theses | Two: jagged frontier + regulatory timing | One: jagged frontier only |
| Bullet list | 2 items (Sales ops, Product) | 3 items (Marketing + Sales ops + Product) — matches blueprint hyphen-bullet 3-item rule |
| Hook | "It seems everybody these days..." (softened with "it seems") | "Everybody these days is an AI automation expert." (sharper, no "it seems") |
| Closer | "Your food for thought:" prefix + question | Question alone, no prefix |
| Meta-skill framing | Absent | "the question that matters more than 'what can AI do' is 'where should it stop'" added |

The finalized version applies four blueprint rules the earlier draft was violating:
1. **One Story Per Post** (cut the regulatory thesis)
2. **Hyphen-bullet 3-item list** (added third bullet)
3. **No softeners on hook** (cut "it seems" + ellipsis)
4. **Closing question without corporate prefix**

---

## Proposed blueprint edits — corpus-tagged

### HIGH CONFIDENCE — apply

**1. Promote two-line binary hook from "variant of Pattern A" to confirmed Pattern A.b.**

- Corpus evidence: `Everyone has Claude Code. Almost no one is using it right.` (Post 4) + `Everybody these days is an AI automation expert. / It's a great service to sell to founders.` (this post) = **2 of 5 finalized posts**.
- Threshold for promotion is 2+. Met.
- Edit target: `config/post-blueprint.md` §"The hook patterns" — promote the existing two-line binary annotation under Pattern A from "variant" to a separately-numbered Pattern A.b with explicit corpus count.

### LOW CONFIDENCE — annotate only, do not promote

**2. Dismissive-quote bullet list pattern.**

- Corpus evidence: 0/5 finalized posts use this. First sighting in this post.
- Format: `- [Role A] thinks [domain B] is "just [trivializing verb phrase]."` — exactly 3 items, parallel grammatical structure.
- Decision: park as annotated single-sighting. Watch for second appearance before promoting. Already documented in the few-shot anchor file.

**3. ALL CAPS one-word emphasis (`IS the product`).**

- Corpus evidence: grep on `\bIS\b` returned 0 matches in corpus. First word-boundary sighting.
- Caveat: voice.md already mentions ALL-CAPS one word per post is allowed for emphasis. This post is the first to actually use it. So the rule existed in the blueprint, but had zero corpus precedent.
- Decision: don't change the rule. Note that the corpus now has 1 confirmed usage. Watch for second.

**4. "The question that matters more than X is Y" meta-skill framing.**

- Corpus evidence: variations exist (multiple closing questions, "Ask the harder question first" in Post 2) but the explicit "more than X is Y" comparative form is novel.
- Decision: log in this design doc as worth tracking. No blueprint edit yet.

### NO EDIT REQUIRED

**5. Register B (observer-mode without Atlan, without p.s.) — second confirmed instance.**

The README in `config/aayush-ai-post-examples/` already names this register based on the GPT-5.5 post. With this post, Register B has 2 anchors. README's framing holds; no edit needed beyond linking the new anchor file.

**6. Awareness level L2.**

The blueprint's Reader Awareness Level section (added 2026-04-26 from the Kleo 5-3-1 PDF) is being used in practice — this post is a clean L2 (aware-unsure). Reinforces the framework, no edit needed.

**7. One Story Per Post.**

Not a new rule — already in `.claude/skills/write-posts/SKILL.md`. The fact that this post enforced it during refinement (cutting the regulatory thesis) is corroboration, not a new edit target.

---

## Hard-gate updates

None proposed. The post passes all 4 gates locally:
- kill-list-regex: clean
- golden-format: N/A (post, not brief)
- posts-gate: would pass (single-option, but format-equivalent — char count is ~1,500, 3-item bullets, no banned patterns)
- clean_text: 0 violations

---

## Open questions (flag for next 2-3 posts)

1. **Does the dismissive-quote bullet pattern recur?** If post #6 also uses `[Role] thinks [domain] is "just [trivializing thing]"`, promote it to a confirmed device.
2. **Does the "matters more than X is Y" meta-skill framing recur?** Watch for the explicit comparative form.
3. **Is Register B sustainable engagement-wise?** When 2026-04-27 + 2026-04-24 engagement data lands, compare against Register A posts (Atlan-stake) to see if the no-Atlan register holds attention.
4. **Two-thesis temptation in original drafts.** Both this post and the GPT-5.5 post had a second thesis in early drafts that got cut. This is a recurring writer behavior worth flagging proactively in `/write-posts` SKILL — when generating options, deliberately pick ONE thesis per option and reject the temptation to add a second one mid-post.

---

## Edits applied this commit

- `history/feedback-log.jsonl` — entry appended
- `config/aayush-ai-post-examples/jagged-frontier-the-20-percent.md` — new few-shot anchor
- `config/post-blueprint.md` — promoted two-line binary hook to Pattern A.b with 2/5 corpus citation
- `config/aayush-ai-post-examples/README.md` — note that Register B now has 2 anchors

## Edits parked

- Dismissive-quote bullet list (single-sighting)
- ALL CAPS "IS" emphasis (single-sighting in word-boundary form)
- "matters more than X is Y" meta-skill framing (single-sighting)
