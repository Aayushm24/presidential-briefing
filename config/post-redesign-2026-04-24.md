# Post Redesign 2026-04-24 — GPT-5.5 voice realignment

**Purpose:** Realign `/write-posts` output to match the voice of the post Aayush wrote himself on 2026-04-24 about GPT-5.5. Pipeline's Option 2 ("$180 per million tokens.") was noticeably worse. Every change below is anchored to a line in one post or the other.

**Source of truth for voice-gaps diagnosed here:** `config/aayush-ai-post-examples/gpt-55-my-feed-is-doing-the-thing.md` + `history/feedback-log.jsonl` entry dated 2026-04-24 source=aayush-direct-write.

File paths referenced:
- `config/post-blueprint.md`
- `.claude/skills/write-posts/SKILL.md`
- `.claude/skills/write-posts/references/voice.md`
- `config/aayush-ai-post-examples/`
- `workspace/2026-04-24/posts.json`

---

## 1. Gap analysis — Aayush's post vs pipeline Option 2

### 1a. Paragraph length and visual breathing

**Aayush:** nearly every paragraph is one sentence. Often one fragment. Between ~90% of lines there's a blank line. Example run:

> `GPT-5.5.` \ (blank) \ `And my feed is already doing the thing it always does.` \ (blank) \ `Spreadsheets comparing price per million tokens.` \ (blank) \ `Threads weighing whether the capability bump justifies the cost.`

Four consecutive paragraphs, all under 12 words. Blueprint's "single-line paragraph fragments for sequences" rule exists but is treated as reach-for. Aayush treats it as default.

**Pipeline Option 2:** paragraphs run 2–4 sentences, packed.

> `Every week I watch teams hit the same inflection point. Their current model handles 80% of what they need. The new model handles 100% plus things they never thought possible.`

Three sentences in one block where Aayush would have given three lines.

### 1b. Observation-first pattern

**Aayush opens flat, then the feed's reaction, then the pivot:**

> `OpenAI released a new model.` \ `GPT-5.5.` \ `And my feed is already doing the thing it always does.` \ `Spreadsheets comparing price per million tokens.` \ `Threads weighing whether the capability bump justifies the cost.` \ `Teams publicly agonizing over this upgrade.` \ `Then Lenny Rachitsky tested it.`

Seven lines of setup before the claim. The claim is earned.

**Pipeline Option 2 leads with analysis-first punch:**

> `$180 per million tokens.` \ `That's what OpenAI thinks breakthrough AI is worth.`

Fine as a hook but there's no "here's what my feed is doing" beat. The hook pattern scoring in `hooks.md` rewards compression — actively pushing the model away from Aayush's cadence.

### 1c. The `↓` arrow device

Aayush uses a line I haven't seen before in any reference post:

> `His reaction ↓`
> (blank)
> `"Happy to pay $180 per million tokens."`

Arrow as a visual colon. Not in blueprint. Not banned. Pending Aayush's call on repeatability (see §6.Q1).

### 1d. "That's a tell." rhetorical beat

> `"Happy to pay $180 per million tokens."` \ (blank) \ `That's a tell.`

A 3-word standalone paragraph that names what the reader just heard. Similar to the "That's distribution." recap-tag pattern in blueprint but the object isn't a concept — it's a meta-observation. "That's a tell." / "That's a signal." are behavioral diagnostics. The blueprint's examples ("That's distribution." / "That's proprietary data.") name concepts, not diagnoses.

### 1e. Casual first-person voice

**Aayush:**

> `My take is teams with room in their AI budget just unlocked a new capability.`
> `Did you try GPT 5.5 yet? I haven't my I'm excited...`

Note the typo ("I haven't my I'm excited") left in. The vulnerability-in-closer here is personal uncertainty, not a rhetorical question.

**Pipeline Option 2 closer:**

> `What happens to your product roadmap if your competitor can afford capabilities you can't?`
> `p.s. At Atlan we've been building intelligent model routing for exactly this scenario, happy to compare notes with anyone facing the same stack decisions. 👇🏻`

A sharp rhetorical question plus an Atlan CTA. The Atlan CTA is blueprint-sanctioned. The question is aspirational/abstract. Aayush's closer is personal ("I haven't"), present ("excited"), conversational.

### 1f. Unicode-bold absent

Aayush uses zero unicode-bold numbers in this post. Pipeline Option 2 uses `𝟯𝟲` at "reversing 𝟯𝟲 months faster than anyone expected." The `𝟯𝟲` is **fabricated** — nothing in the brief justifies "36 months faster." The blueprint's reach-for checklist nudges the model toward the device even when the evidence doesn't warrant it.

### 1g. No hashtag-style markdown bold

Pipeline uses `**That's not pricing. That's access.**` and `**That's the new moat.**`. Aayush uses zero markdown bold anywhere in this post. On LinkedIn these asterisks render literally. Blueprint's "bold max 3-5 words per post" rule is being interpreted as "use markdown bold" — but LinkedIn strips it.

### 1h. "p.s." promo closer

Aayush's closer: `Did you try GPT 5.5 yet? I haven't my I'm excited...` — zero p.s. No p.p.s. No 👇🏻. Blueprint's reach-for checklist drives the model toward p.s./p.p.s. on every post. This post shows it's optional.

### 1i. Vulnerability in closer

**Aayush closes with admission of not having tried the product:**

> `Did you try GPT 5.5 yet? I haven't my I'm excited...`

Even with the typo, the move is "I'm asking because I haven't done it either." This is vulnerability without a personal backstory. Blueprint only allows vulnerability in TIER 1 Vulnerable Victor style (requires verified experience). No vulnerability-in-closer pattern available for TIER 2/3 posts.

### 1j. "My take is" as explicit marker

> `My take is teams with room in their AI budget just unlocked a new capability.`

voice.md allows IMO / I think / I doubt as hedge markers. `My take is` is not listed. It should be. Exact register for committing to a thesis mid-post.

---

## 2. Changes to `config/post-blueprint.md`

### 2a. Clarify char-count math

Character count includes line breaks. A 1,400-char post with 40 blank lines is not the same as a 1,400-char post with 12. Top performers often land at 1,400c with more than a third of that budget in whitespace. Do not pad prose to hit 1,800 — pad rhythm via line breaks.

### 2b. Promote single-sentence paragraphs from reach-for to default

Default: one sentence per paragraph. Stack 2 only when tightly causally linked (A therefore B). Stack 3 only when the third is a wry closer the first two set up. Otherwise break. The 2026-04-24 GPT-5.5 post has ~30 paragraphs; 28 are single sentences. Option 2 has ~14 paragraphs; only 4 single sentences. Match Aayush's ratio.

### 2c. ADD: Observation-first opener pattern

```
[Company] released/shipped/raised [thing].

[Name of thing / price / number].

And my feed is already doing the thing it always does.

[Beat 1 of what the feed is doing — one line]
[Beat 2 of what the feed is doing — one line]
[Beat 3 of what the feed is doing — one line]

Then [named person] [did a specific thing].
```

Slower than a hook-punch. Earns the claim by showing the predictable discourse pattern first. Use when you want the reader to nod at every setup beat before the pivot. Not a replacement for Pattern A/B/C/D — equal-weight alternative (Pattern E).

### 2d. ADD `"my take is"` to allowed hedge markers

Insert after `**I think**`:

> - **My take is** — "My take is teams with room in their AI budget just unlocked a new capability." (2026-04-24) Commits to the thesis without claiming authority. Use at the pivot from setup to implication.

### 2e. Downgrade p.s. / p.p.s. from reach-for to conditional

Use p.s./p.p.s. when (a) you have a genuine confession or image worth pointing at, or (b) the post is a personal/vulnerable arc. Skip when the post is commentary-on-news and the closer is itself the payoff. The 2026-04-24 post skips p.s. entirely and closes on `Did you try GPT 5.5 yet? I haven't my I'm excited...` — the personal question is the closer. Forcing p.s. onto that post would deflate the arrow.

### 2f. Remove "reach for TWO per post" mandatory rule

Calibrate to post mode. News-commentary posts typically use 0–1 formatting devices, leaning on paragraph breaks, observation-first setup, and personal closer. Vulnerable-personal posts use 3–4. Count by mode.

### 2g. Downgrade unicode-bold to conditional-on-pivot-number

Use only when the number is the pivot. In the 2026-04-20 "I quit my job" post, `𝟰𝟬%` and `𝟵𝟬%` are the pivot. In 2026-04-24, Aayush uses zero unicode-bold — no single number is the pivot. $180/M is a reference anchor, not a reveal. The 2026-04-24 pipeline draft fabricated `𝟯𝟲` to hit the reach-for checklist. Rule: **if the post doesn't have a pivot number, don't hit unicode-bold.**

### 2h. ADD: No markdown bold in post body

LinkedIn strips `**bold**`. The asterisks render literally. If you want weight on a word, use unicode-bold (conditional per §2g) or a short fragment paragraph. Never asterisks.

### 2i. ADD: Vulnerability-in-closer for non-TIER-1 posts

Close with a present-tense admission of uncertainty, incompleteness, or not-yet-doing-the-thing. Does NOT require a verified past experience — only a present state. Examples:
- "Did you try GPT 5.5 yet? I haven't my I'm excited..." (2026-04-24)
- "What's the ugliest workaround in your current agent setup?" + implied "I have a few" (agent-stack-hardening)

Works even on contrarian-philosopher style posts. Distinct from TIER 1 Vulnerable Victor which requires a verified past arc.

### 2j. Pending — `↓` arrow

Tentative addition (see §6.Q1 for Aayush's decision on repeatability):

> Arrow `↓` as visual colon. Replace `said X:` or `reaction:` with a standalone line ending in `↓` followed by the quote on its own paragraph. Max 1 per post.

---

## 3. Changes to `.claude/skills/write-posts/SKILL.md`

### 3a. Rewrite "NEVER: three short sentences in a row"

Current rule contradicts 2026-04-24. Aayush has four+ short sentences in a row constantly. Replace with:

> NEVER: three short sentences CRAMMED into one paragraph. When you have a sequence of 3+ short sentences, break each onto its own paragraph. See post-blueprint.md "Default: one sentence per paragraph."

### 3b. Tighten emphasis guidance

> Emphasis: NEVER use markdown `**bold**` in the post body — LinkedIn renders the asterisks. Use unicode-bold (conditional per post-blueprint.md §2g) or short-fragment paragraphs for weight.

### 3c. Add Pattern E — Observation-first setup

> - **Pattern E — Observation-first setup:** News reported flat, feed's predictable response, then pivot. `[Company] [action] [thing]. / [Name]. / And my feed is already doing the thing it always does. / [3 beats of predictable discourse]. / Then [named person] [specific action].` — 2026-04-24 GPT-5.5 post. Earns the claim by showing the discourse pattern first.

### 3d. Soften observer-self-check

Not every post needs "every week I watch." Acceptable forms: "Every week I watch...", "I've been thinking about...", "My feed is already doing the thing it always does", "My take is...", "I haven't tried X yet."

### 3e. Slow the opener

The first 5–8 lines of a news-commentary post can all be "what I noticed." Only THEN pivot. Pipeline drafts tend to collapse setup + pivot into the hook. Don't.

### 3f. Add worked 2026-04-24 contrast

GOOD (Aayush):
```
OpenAI released a new model.

GPT-5.5.

And my feed is already doing the thing it always does.

Spreadsheets comparing price per million tokens.
```

BAD (pipeline Option 2):
```
$180 per million tokens.

That's what OpenAI thinks breakthrough AI is worth.

Every week I watch teams hit the same inflection point. Their current model handles 80% of what they need. The new model handles 100% plus things they never thought possible.
```

Both correct on facts. First earns the claim via patient setup. Second compresses into punch + packed paragraph. Prefer the first for news commentary.

---

## 4. Few-shot example already on disk

`config/aayush-ai-post-examples/gpt-55-my-feed-is-doing-the-thing.md` — created in the first pass of this commit chain. Covers the full post, structural devices, anti-patterns, when-to-use guidance.

Plan agent suggested filename `gpt-55-pricing-tell.md`. Keeping the existing filename — `my-feed-is-doing-the-thing` is Aayush's actual phrase and more evocative.

---

## 5. What to remove / deprecate

1. `NEVER: three short sentences in a row` — contradicted by 2026-04-24. Rewrite per §3a.
2. `Reach for TWO formatting devices per post` — pushed pipeline toward unicode-bold `𝟯𝟲` fabrication on a post that didn't need it. Replace with mode-calibrated rule per §2f.
3. Unicode-bold "use 1-2 per post" default — downgrade to conditional-on-pivot-number per §2g.
4. p.s./p.p.s. "worth reaching for" framing — 2026-04-24 explicitly skips. Rewrite to "when genuine confession or image available" per §2e.
5. voice.md I-case contradiction — lines 25 ("uppercase I") vs 170 ("lowercase i") directly contradict. 2026-04-24 uses uppercase "I" throughout. 2026-04-20 uses lowercase "i". **Pipeline is inconsistent because the config is inconsistent.** See §6.Q5.

---

## 6. Open questions for Aayush

1. **Arrow `↓` — one-off or repeatable?** Added tentative entry (§2j), not promoted to reach-for. Want 2–3 more uses before codifying?
2. **p.s. / p.p.s. — deprecate or keep as TIER-1-only?** 2026-04-24 skipped. 2026-04-20 used. Proposal: keep for personal/vulnerable arcs, drop from news-commentary reach-for.
3. **"my take is" as hedge marker — confirm adoption?**
4. **Vulnerability-in-closer without personal arc (§2i) — pattern or post-specific?** Was "I haven't" specific to this post, or a repeatable move for news-commentary?
5. **Uppercase `I` vs lowercase `i` — which is the rule?** voice.md lines 25 vs 170 directly contradict. Pipeline can't decide because config can't decide. Prior feedback-log entry says uppercase; voice.md says lowercase. Pick one.
6. **"That's a tell." vs "That's distribution." — one device or two?** Diagnostic beat vs concept-naming. I'll default to "one device with two surface forms" unless you want them distinct.
7. **Length floor — add a prose-char floor?** Current 1,300 is total chars. Aayush's 2026-04-24 post is ~1,480 with ~500 chars of whitespace. Want a prose-char floor (say 900) to prevent the pipeline from padding prose to hit 1,300 total?

---

## Implementation status (as of this doc)

- [x] `history/feedback-log.jsonl` entry appended with full post + voice directions
- [x] `config/aayush-ai-post-examples/gpt-55-my-feed-is-doing-the-thing.md` created
- [x] `config/aayush-ai-post-examples/README.md` updated with two-register framing
- [x] Safe edits (§2a–2i, §3a–3f) applied to blueprint + SKILL — see next commit
- [ ] §2j `↓` arrow — awaiting Q1 answer
- [ ] voice.md I/i contradiction resolution — awaiting Q5 answer
