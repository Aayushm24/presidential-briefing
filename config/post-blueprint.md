# Post Blueprint

**Primary voice source for `/write-posts`.** Read this FIRST. Every other reference (voice.md, post-templates.md, hooks.md, kill-list.md) is secondary. When two sources conflict, this blueprint wins.

Updated from daily feedback in `history/feedback-log.jsonl`. Versioned in git.

---

## Who this is for

Aayush writing LinkedIn posts to founders and builders. Not a corporate newsletter. Not Atlan's voice. His voice — a practitioner sharing observations, not a teacher explaining frameworks.

His audience: founders in AI, operators thinking about how the game changes, builders on LinkedIn. They've seen every corporate thought-leadership post. They want signal.

---

## Reader awareness level — pre-flight question (2026-04-26, Paolo Trivellato)

**Before drafting any of the 3 options, decide which awareness level it targets.** Most pipeline failures around "this post sounds generic" come from defaulting to Level 2 every time. Every option in posts.json should declare its level in the conviction line.

| Level | Reader state | Hook needs to do | Voice register |
|---|---|---|---|
| **L1 — Unaware** | Hasn't noticed the problem yet | Show the problem with specifics — name a tool, price, person, behaviour — let the reader's gut react before any claim | Observation-first (Pattern E, GPT-5.5 anchor) |
| **L2 — Aware-unsure** | Sees the problem, doesn't know what works | Reframe the problem at a deeper level than the conventional take — dig 3-4 levels beneath the surface | Contrarian / two-line binary (Pattern A) |
| **L3 — Actively looking** | Wants a path or playbook | Name the meta-skill, give a specific signal of progress, make next step clear | Personal-I observer / data-point with named source |

**Sourcing:** Paolo Trivellato's anti-content-pillars approach (see `.claude/skills/write-posts/references/external-frameworks.md` §"Creator spotlight #3"). Reframed for Aayush's builder-to-builder context.

**How to use:** If the day's brief covers a topic readers haven't touched yet (an obscure tool, a sleeper trend), default to L1. If it covers the active debate everyone's having (model pricing, agent stacks), default to L2 — and dig deeper than the obvious take. If it covers a problem readers are actively trying to solve right now (Claude Code adoption, GTM engineering), L3 with the specific path.

**One option per level** when a story spans multiple awareness states. Three options on the same level → pipeline drift.

---

## Length — 1,400-1,800 chars sweet spot

**Floor: 1,300 chars** (posts-gate.sh rejects below this).
**Cap: 2,000 chars** (top-performer ceiling from data; 2,606c post dropped to 7 eng).
**Target: 1,400-1,800.**

Why 1,300 floor: top 5 performing posts (excluding the 83c job-change outlier that algorithm-boosted) average 1,368 chars. Below 1,300 there's no room for hook + proof + implication + closer in the structure that actually wins.

If a draft comes in at 1,000 chars, it's not finished. Add another specific beat from the brief, another named fact, or a deeper personal observation. Never pad with filler.

---

## Style tier system — pick based on data, not preference

**25-post performance data (2026-04-21):**
- Personal-story hooks: **83 avg engagement** (TIER 1)
- Personal-I hooks: **48 avg engagement** (TIER 2)
- Contrarian/data hooks: **35-37 avg engagement** (TIER 3)

Personal story is 3x contrarian. Always attempt TIER 1 first.

### TIER 1 — Vulnerable Victor (personal story)
Personal struggle at the peak. Success with hidden costs. Raw emotional honesty. Ends with empowerment.

**Performance: avg 83 eng. Top post: 305 eng ("I quit my job with zero backup plan.").**

Requires a verified entry in `config/aayush-experiences.md` matching today's theme. Never fabricate.

**Daily brief instruction:** Before writing 3 options, check `config/aayush-experiences.md`. If ANY entry connects to today's lead theme — even loosely (building AI at Atlan, managing a team, watching competitors, shipping a product, making a career bet) — one option MUST use TIER 1. Do not skip to contrarian because it's easier.

### TIER 2 — Personal-I Observer
First-person present-tense observation of the news. Not a story arc, but Aayush in the frame.

**Performance: avg 48 eng.** Signature phrases: "Every week I watch...", "Every team I talk to...", "I've been thinking about...", "Most people I know are...", "I see it across my network..."

Every option that isn't TIER 1 should have at least one TIER 2 moment — a sentence where Aayush is observing, not just describing.

**Note:** When using a two-line binary hook (Pattern A variant), the TIER 2 observer voice moves into the bridge sentence rather than the hook itself. Don't force "every team i talk to" as the hook when a sharper contrarian statement works better.

### TIER 3 — Contrarian Philosopher
Challenges conventional wisdom. Redefines what winning looks like. Paints an alternative reality.

**Performance: avg 37 eng.** Does NOT require personal experience — requires a sharp POV.

Top example: "every startup says they're 'ai-powered' now" (87 eng, 1,736c). Note: this is the ceiling for pure contrarian without personal story.

### Absurdist Truth-Teller
Normal setup → absurd reveal. Humor disarms defenses. Hidden truth in comedy.

### Relatable Human
"Average" positioning. Universal struggles. No-pretense honesty. Heart over metrics.

Top example (voice direction): "I'm the most average bloke ever."

---

## The 4 formulas (matches to styles)

- **F1 Personal Crisis**: `I [did unexpected thing]. Everyone said [doubt]. [Time] later, [transformation]. The lesson: [wisdom].` — ONLY with matching entry in aayush-experiences.md.
- **F2 Hidden Truth**: `[What everyone believes]. [Why it's wrong]. The reality: [contrarian truth]. Here's what works: [alternative].` — works without personal experience.
- **F3 Absurd Mirror**: `[Relatable journey]. [Ridiculous comparison]. [What this reveals].` — works without personal experience.
- **F4 Vulnerable Share**: `I don't [what's expected]. Because [raw truth]. Instead, I [alternative action]. And that's okay.` — ONLY with matching entry.

---

## The 4 hook patterns

- **Pattern A — Contrarian Truth**: "Society's definition of wealth is expensive." / "AI isn't your competitive advantage. It's a commodity." / "every startup says they're 'ai-powered' now."
- **Pattern A.b — Two-line binary hook (CONFIRMED, 2026-04-26 — corpus 3/6 as of 2026-04-28):** Pair a universal claim with an immediate inversion on the next line. State the contrast and let the second line land it. No observer framing needed.
  - Examples (corpus): `Everyone has Claude Code.` / `Almost no one is using it right.` (Post 4); `Everybody these days is an AI automation expert.` / `It's a great service to sell to founders.` (jagged-frontier 2026-04-26); `That second question used to have one answer per cloud.` / `Now it has one answer, period.` (openai-50b-anywhere 2026-04-28, used as closer not opener).
  - Use when the gap between line 1 and line 2 IS the whole point. Promoted from "variant of Pattern A" after the second corpus instance landed. Works as opener AND closer (the 2026-04-28 post uses it to land the consequence, not to set up the post).
- **Pattern A.c — Numeric-anchor lede (CONFIRMED, 2026-04-28 — corpus 2/6):** Open with a specific dollar figure tied to a paradoxical purpose. The number is the hook; the paradox is the tension. Distinct from Pattern A.b because the punch is in line 1 alone.
  - Examples (corpus): `Someone raised $9M just to babysit AI-generated code.` (agent-stack-hardening, Post 1); `OpenAI just paid $50 billion to give up their biggest moat.` (openai-50b-anywhere 2026-04-28).
  - Pattern: `[Subject] [verb-paid/raised/spent] [$ figure] [paradoxical purpose].` Use when the dollar figure plus the paradox is the whole opening — no setup, no observer voice in the lede.
- **Pattern B — Identity Statement**: "97% of LinkedIn creators are men. I'm in the 3%." / "I'm the most average bloke ever." Requires a verified Aayush-side fact.
- **Pattern C — Absurd Comparison**: "A cat with Instagram makes more than your MBA."
- **Pattern D — Time Bomb**: "I posted my first LinkedIn post 3 years ago." / **Variant: ellipsis** — "AI startups have 12 months before they die…" (from today's shipped post, 2026-04-20). Trailing ellipsis adds stakes without a full sentence.
- **Pattern E — Observation-first setup (EXPERIMENTAL, 2026-04-24):** News reported flat, feed's predictable response, then pivot. Corpus evidence: **0 of 4 finalized Aayush posts use this pattern.** One single off-corpus post (2026-04-24 GPT-5.5) used it. Treat as experimental — reach for punch-first (Pattern A) or two-line binary first. Use Pattern E ONLY when the story is genuinely a hype-cycle moment where the discourse-first setup earns the claim.
  ```
  [Company] [released/shipped/raised] [thing].

  [Name of thing / price / number].

  And my feed is already doing the thing it always does.

  [Beat 1 of what the feed is doing — one line]
  [Beat 2 of what the feed is doing — one line]
  [Beat 3 of what the feed is doing — one line]

  Then [named person] [specific action].
  ```
  Anchor: `config/aayush-ai-post-examples/gpt-55-my-feed-is-doing-the-thing.md`. See `config/post-corpus-analysis-2026-04-24.md` §3.1 for the corpus counts that led to this demotion.

**Workhorse first:** 3 of 4 finalized posts use punch-first openers (named-specific stat → paradox, two-line binary, or time-bomb ellipsis). Reach for these before Pattern E.

- **Pattern F — Before → But → After (EXPERIMENTAL, 2026-04-26, Matt Barker):** A 3-word hook framework that contrasts the reader's problem state with their dream state and implies you have a proven path between the two. Corpus evidence: **0 of 5 finalized Aayush posts use this exact shape.** Source: external (Kleo's 5-3-1 newsletter, Matt Barker micro-playbook — see `references/external-frameworks.md`). Treat as experimental.
  ```
  [Specific Before — concrete past state with a stat or named tool/person].

  But [specific transition — what changed, what was learned].

  [Specific After — concrete present state with a stat or proof].
  ```
  Worked example from the source: "Last April, I had zero LinkedIn presence. But today, I hit 10,000 followers (and average 3 inbound leads a week)." Use only when Aayush has a real before/after arc to anchor (verified entry in `config/aayush-experiences.md`). Without that, the "After" reads as fabricated.

---

## Reframe depth — avoid surface-level complaints (2026-04-26)

Aayush's posts consistently work because they dig 3-4 levels beneath the surface complaint. **Surface-level posts read as generic; basement-level posts read as Aayush.** This is a quality criterion, not a hard gate — but it should be checked at council pre-flight.

**Surface vs basement (corpus evidence):**

| Surface complaint | Basement reframe (Aayush's actual posts) |
|---|---|
| "AI tools are getting expensive" | "The debate only exists when the gains are marginal. When a jump like this lands, the advantage almost always outweighs the cost" (2026-04-24) |
| "Companies are buying more AI tokens" | "The budget anxiety is doing more damage than the budget itself. Your usage graph is the shape of your rationing, not your demand" (2026-04-23) |
| "Coding tools are getting consolidated" | "The category just graduated from software expense to strategic infrastructure" (2026-04-22, pre-rewrite) |
| "Every SaaS is shipping AI buttons" | "The button isn't the problem. The user it's designed for is" (every-saas-ai-button.md) |
| "AI startups will struggle in 2026" | Surface = market timing; basement = "12 months to find distribution before incumbents copy the feature" (ai-startups-12-months.md) |

**The check (for council pre-flight):** read each option's hook + first paragraph. Ask:

1. Does the post identify a *faulty belief* the reader is holding, or just describe an event?
2. Does it *redefine* the problem at a deeper level (a posture, a measurement error, a category shift) — or stop at the surface description?
3. Could you swap out "AI" for any other tech topic and the post would still read as generic? If yes, the post is surface-level — push for the reframe.

**Where it lives:** add to `.claude/skills/council/attack/SKILL.md` Step 1 voice audit as a numbered question: "Does this post reframe the surface complaint at a deeper level, or does it describe the surface event only?" — if surface only, flag REVISE.

**Sourcing:** Nicolas Cole's "Generic Content Trap" template (see `references/external-frameworks.md` §"Template 2"). The principle, not the template — Aayush's voice already does this naturally; this rule keeps the pipeline from drifting toward surface-level summaries when the writer is tired.

---

## Voice — what Aayush sounds like

### Sentence case throughout

Every sentence starts with a capital letter. Proper nouns capitalized (Claude Code, Intercom, OpenAI, Atlan). Standard English — including "I" for the first-person pronoun.

Closing rhetorical questions: sentence case. "What does your team remember from last sprint?" not "what does your team remember...".

### Allowed hedge markers (first-person voice anchors)

- **IMO** — "IMO, it's about who owns the user when the feature becomes commodity." (from today's post)
- **I doubt** — "I doubt current stakes are about model access anymore."
- **I think** — "I think [specific claim]"
- **My take is** (OCCASIONAL, 2026-04-24) — "My take is teams with room in their AI budget just unlocked a new capability." **Corpus count: 0 hits in 4 finalized posts.** IMO (3 hits) and I doubt (2 hits) are the proven defaults — reach for those first. Treat "My take is" as an allowed variant, not a first-class marker.
- **tbh, fwiw, ngl** — occasional, informal, not every post

These are NOT guru-speak. They're the opposite — they signal humility and conviction at the same time. Use them.

### First-person observer

Every post has Aayush IN it. "Every week I watch a category shrink." "Most people I talk to are building the exact thing OpenAI will ship next quarter." "I build AI agents at Atlan."

### Present tense for observations

"Every week I watch a category shrink." NOT "I have been watching categories shrink." Present tense makes it feel like now, not a retrospective.

### Specific named entities with numbers

Every post has ≥3 named things. Examples from top performers:
- "Canva has 100 million users" (1,595c post)
- "Cerebras filed for IPO with a $10+ billion OpenAI deal" (1,595c post)
- "Khosla Ventures (the $15 Bn VC)" (1,736c post)
- "At Atlan, we realized going AI Native means..." (1,736c post)

Unnamed "some companies" or "many founders" = rewrite until named.

---

## Structural devices (2026-04-21 additions)

### Bridge sentence — between hook and story

After a strong hook, add one sentence that (a) grounds the claim in Aayush's own observation and (b) names the specific gap or mechanism. Without the bridge, the reader goes from claim to proof without feeling the problem.

**Structure:** `[Observer placement] + [mechanism or gap named]`

Examples:
- "I see it across my network, teams shipping with identical tools, but getting wildly different outcomes."
- "The difference lies in what happens when your Claude conversation ends."
- "Every founder I've talked to this week is asking the same question."

The bridge keeps the post grounded and prevents the jump from hook to case study feeling abrupt.

### Parenthetical personality aside — three variants (3 of 4 corpus posts)

Inject a casual, self-aware observation mid-post as an inline parenthetical. Corpus evidence: Post 2 alone uses all three variants below. Use **one per post max**, picking the variant that matches the moment.

**Variant 1 — self-aware wink (with emoji).** Pre-empts an obvious objection without a full disclaimer sentence.
- Format: `(observation 🤷🏻‍♂️)` — inline, attached to the sentence that prompted it.
- Example: "The tools were identical (using claude code is not a moat 🤷🏻‍♂️). The infrastructure was completely different." (Post 4)

**Variant 2 — explanatory (no emoji).** Unpacks a technical term or detail in one beat, so the sentence can keep moving.
- Format: `(one-line unpacking of the term just used)`
- Example: "OpenAI's Codex update shipped computer use (the agent literally sees your screen and operates your apps for you) which changes everything." (Post 2)

**Variant 3 — tonal (single word or short phrase).** Adds voice without adding content. Rare but punchy.
- Format: `(quietly)` or similar short adverb/phrase in parens.
- Example: "(quietly)" as a tag on a sentence about a major shift happening below the surface (Post 2).

This is distinct from a standalone body emoji. It's a wink or a beat inside the sentence, never a standalone paragraph.

### Default cadence: one sentence per paragraph (2026-04-24)

**Single-sentence paragraphs are the default, not the reach-for exception.** Stack 2 sentences in one paragraph ONLY when tightly causally linked (A therefore B). Stack 3 ONLY when the third is a wry closer the first two set up. Otherwise break.

Anchor: the 2026-04-24 GPT-5.5 post has ~30 paragraphs; 28 are single sentences. Pipeline's Option 2 draft had ~14 paragraphs, only 4 single-sentence. Match Aayush's ratio.

**Pipeline fail:** "He built telemetry that logs every Claude Code interaction. Every pattern analyzed. Every skill saved to a shared repository."
**Aayush edit:** Each sentence on its own line.

Rule: if you have 3+ sentences that are each under 12 words, break them one-per-line. They land harder as separate beats.

**Character-count math:** character count includes line breaks. A 1,400-char post with 40 blank lines is not the same as a 1,400-char post with 12. Top performers often budget more than a third of char count to whitespace. Never pad prose to hit 1,800 — pad rhythm via line breaks.

### Wider paragraph spacing — Register B variant (2026-04-28, corpus 2/6)

Register B news-commentary posts can stretch paragraph spacing from single-blank to double or triple-blank between paragraphs (`\n\n\n` or `\n\n\n\n` in source). The wider gap slows reading deliberately and gives each beat its own breath.

**Corpus evidence:**
- 2026-04-24 GPT-5.5 anchor (`gpt-55-my-feed-is-doing-the-thing.md`): 19 instances of triple-blank-line spacing within the post.
- 2026-04-28 OpenAI $50B post (`openai-50b-anywhere.md`): triple-blank-line spacing throughout.

**When to use:** Register B observer-mode posts where the cadence IS the rhythm — news-commentary, frontier-shift posts. Single-blank remains the default for Register A (operator-stake) posts (Posts 1-4 in the main corpus all use single-blank).

**Don't:** stretch spacing in posts that already lean heavy on hyphen-bullet lists or "That's X." recap rhythm — those devices need single-blank tightness to land. The wider spacing is for fragment-paragraph runs, not for structured prose.

---

## Rhythm devices (performance-data-derived, 2026-04-20 calibration)

### Unicode-bold signature — conditional on pivot-number (2026-04-24 update)

LinkedIn strips markdown. Aayush uses **Mathematical Bold block** (U+1D400-U+1D7FF) when a specific number or word IS the pivot of the post. Not on every post.

**Use only when the number is the pivot.** In the 2026-04-20 "I quit my job" post, `𝟰𝟬%` and `𝟵𝟬%` ARE the pivot — savings down, anxiety down. Without them the post has no beat. In the 2026-04-24 GPT-5.5 post, Aayush uses zero unicode-bold — because no single number is the pivot. $180/M is a reference anchor, not a reveal.

Examples from top-1 post (392 eng):
- "My savings dropped 𝟰𝟬%. But, my anxiety dropped 𝟵𝟬%."
- "Sometimes not knowing 𝗜𝗦 the plan."

Rules:
- **If the post doesn't have a pivot number/word, don't hit unicode-bold at all.** Do not fabricate a number to justify the device. 2026-04-24 pipeline Option 2 fabricated `𝟯𝟲` at "reversing 𝟯𝟲 months faster" to satisfy the reach-for checklist — that number was not in the brief.
- When used: 1-2 unicode-bold hits per post maximum
- Apply to: the pivot number, the thesis word, a key verb
- Never entire sentences
- Numbers: use Bold Digit block (U+1D7CE-U+1D7FF). Example: `40` → `𝟰𝟬`, `90` → `𝟵𝟬`
- Letters: use Mathematical Sans-Serif Bold (U+1D5D4-U+1D607). Example: `IS` → `𝗜𝗦`

### NO markdown bold in post body (2026-04-24)

LinkedIn strips `**bold**`. The asterisks render literally to readers. If you want weight on a word, use unicode-bold (conditional per above) or a short fragment paragraph. **Never use markdown asterisks.** 2026-04-24 pipeline Option 2 shipped `**That's not pricing. That's access.**` and `**That's the new moat.**` — these would have rendered with stars visible on LinkedIn.

### P.S. / P.P.S. closer — conditional (2026-04-24 downgrade)

**Use p.s./p.p.s. when** (a) you have a genuine confession or image worth pointing at, or (b) the post is a personal/vulnerable arc. **Skip when** the post is news-commentary and the closer is itself the payoff.

The 2026-04-24 GPT-5.5 post closed on `Did you try GPT 5.5 yet? I haven't my I'm excited...` — a present-tense personal question. Forcing p.s. onto that post would deflate the arrow. For news-commentary mode, the unresolved closer IS the p.s. equivalent.

Top-1 and top-5 posts ended with this pattern:

```
p.s. Take this post as your sign to take a break from work :)
p.p.s First day at the Vipassana center 👇🏻
```

- **p.s.** = friendly directive, personal confession, or one new concrete detail that reframes what the reader just read. Lowercase. Do NOT use p.s. to repeat a stat already covered in the body — use it to land something specific and surprising that the body didn't have room for.
- **p.p.s.** = image/asset pointer using 👇🏻 emoji — OR — personal Atlan context CTA (see below). Lowercase.

**NOT a reach-for.** Not every post needs one. Count by mode: vulnerable-personal posts often use 3-4 formatting devices (p.s., unicode-bold, 👇🏻). News-commentary posts typically use 0-1.

### At Atlan grounding beat — mid-post (3 of 4 corpus posts, 2026-04-24 addition)

**The workhorse Atlan placement is MID-POST, not in the p.p.s.** 3 of 4 finalized posts have a single-line "At Atlan, we..." grounding beat in the body of the post. Only Post 4 uses the Atlan CTA in a p.p.s. The blueprint has been under-representing the mid-post form.

**What it does:** converts an abstract argument into a concrete one-liner of lived experience. Signals "I'm not theorizing — I'm in it too."

**Format:** one sentence, mid-post, after a general claim. Not a CTA. Not a disclaimer. A proof beat.
- Post 1: "At Atlan, we've been building agents for months and this tracks."
- Post 2: "When we build agents at Atlan, we don't have them click buttons."
- Post 4 (mid-post, separate from p.p.s.): "At Atlan we've learned shipping agents fast and fixing them publicly beats shipping perfectly."

**Rules:**
- One per post max (either the mid-post beat OR the p.p.s., never both unless the post earns it — Post 4 is the edge case).
- Must come AFTER you've made the general point, not before. The beat CONVERTS the abstraction; it does not introduce it.
- Lowercase "at Atlan" (not "At Atlan,") in informal posts; sentence case at sentence start.
- Never used as a setup — always as a proof.

### Atlan context p.p.s. (2026-04-21)

When the post topic overlaps with what Atlan is building (AI infrastructure, agent ops, data systems, institutional memory, workflow automation), add a p.p.s. that ties the post back to Aayush's actual work:

```
p.p.s. at Atlan we've been building this layer for a while. happy to compare notes with anyone doing the same. 👇🏻
```

**When to use:** Post theme = something Atlan builds or has shipped. Not a sales pitch — a genuine "we're in this too" signal. Makes the post feel less theoretical and more grounded in real work.

**Tone:** Lowercase. Casual. "happy to compare notes" not "let's connect". "we've been building" not "we've built a solution".

### Hyphen-bullet 3-item list (4 of 4 corpus posts, 2026-04-24 addition)

**Every single finalized corpus post uses hyphen-bulleted sub-lists.** This is Aayush's most reliable parallel structure. The blueprint has been treating this as incidental; it's core.

**Format:** one-line setup ending with `:` followed by 2-4 bulleted items, each on its own line, each under 12 words, each starting with `- `.

**Count distribution in the corpus:** Post 1 has 6 hyphen-bullet lines, Post 2 has 16, Post 3 has 3, Post 4 has 2.

**Examples from the corpus:**

Post 1 (3-item, explanatory):
```
This is multiple layers of the agent stack hardening at once:
- runtime primitives becoming first-class
- orchestration getting native support
- security tools catching up to output volume
```

Post 1 (3-item, actionable):
```
Here's why IMO that cost should drop now:
- native sandboxed execution = stop building infra
- long-running support = stop managing state yourself
- security tooling = stop manually auditing agent output
```

**Rules:**
- 3-item is the dominant length. 2 or 4 items OK.
- Each line starts with `- ` (hyphen + space).
- Each line under 12 words.
- Parallel grammatical structure within the list (all noun phrases, all imperatives, all `= ` equations — pick one pattern per list).
- No nested bullets. No sub-bullets.
- Use 1-2 lists per post max; more than that fragments the post.

### Short fragment paragraphs

Top performers use 2-8 word standalone paragraphs for emphasis:
- "That's distribution." (1,595c post)
- "That's proprietary data."
- "Just... nothing." (392 eng post)
- "Don't get me WRONG, the 99% aren't dumb." (1,736c post, mid-paragraph)

These break rhythm and carry weight. Use sparingly — 2-3 per post max.

### "That's X." recap-tag pattern (two variants)

After making a concrete point, close with a 3-word tag naming what you just showed.

**Variant 1 — concept-naming.** The tag names the underlying concept:
- "Canva has 100 million users. When they decide your AI feature belongs in their workflow, you're not competing against their product. You're competing against their audience. That's distribution."

**Variant 2 — diagnostic beat (UNCONFIRMED, 2026-04-24).** The tag names a *behavioral observation* about what you just quoted. **Corpus count: 0 of 4 finalized posts use this variant.** Single off-corpus sighting in the 2026-04-24 GPT-5.5 post: `"Happy to pay $180 per million tokens." / That's a tell.` Do NOT reach for this variant until it shows up in 2+ more finalized posts.

**Corpus-proven form is Variant 1 (concept-naming).** All 4 corpus "That's X." uses name a concept: `That's distribution.` / `That's proprietary data.` / `That's the third.` / `That's the gap.` Reach for Variant 1 by default. Use Variant 2 only if the moment genuinely requires it and you're ready to defend the choice.

Posts using this pattern read as structured and deliberate.

### Vulnerability-in-closer — RARE (1 of 4 corpus posts)

Close with a present-tense admission of uncertainty, incompleteness, or not-yet-doing-the-thing. Does NOT require a verified past experience — only a present state.

**Corpus evidence: 1 of 4 finalized posts uses this** (Post 1 / agent-stack-hardening: `What's the ugliest workaround in your current agent setup? 👀` — implied "I have a few"). Do NOT treat as a standard reach-for. The dominant corpus closer is a **specific present-tense question to the reader** (see §"Closing move" below), not a confession about the writer.

Examples (sparingly):
- `Did you try GPT 5.5 yet? I haven't my I'm excited...` (2026-04-24 GPT-5.5, off-corpus)
- `What's the ugliest workaround in your current agent setup?` (Post 1)

When you use this, typos or typo-like flow ("I haven't my I'm excited") are allowed if they keep the rhythm of thought. Do not sanitize into "I haven't tried it yet, but I'm excited." — the run-on IS the signal.

**Don't default to vulnerability-in-closer for news-commentary.** Default to a specific present-tense question like `What does your team remember from last sprint?` instead.

### Parallel-imperative rhythm

Two short imperatives, same structure, different object:
- "Kill the constraint. Kill the process." (1,736c post)
- "One optimizes. One eliminates."
- "Smart companies. Great founders. Wrong approach." (3-beat variant)

Punches delivered with zero filler. 1-2 per post max, in the implication section.

### Contrast labels

Short labels for opposing concepts, colon-separated:
```
AI First: "How can we add AI to improve X?"
AI Native: "Why does X exist at all?"
```

Works for any binary framing. 2-4 words per label. Follow with a one-sentence payoff: "One optimizes. One eliminates."

From 1,736c post — top-5 performer.

### Era-reframe (naming a strategy by its vintage year)

Today's post (1,595c) uses: "'build the feature, they'll come' is a 2023 strategy running on 2026 timelines."

Pattern: `[quoted strategy] is a [OLD YEAR] [term] on [CURRENT YEAR] [timeline-word]`.

Implies the strategy is outdated without calling it stupid. Codified as a rhetorical device.

### Two-question close / poetic line-break close

Top performers end with TWO questions OR a line-broken poetic question:

Two-question (1,736c post):
- "What would you delete if AI had always existed?"
- (paragraph break + p.s. reveals Aayush's own answer)

Poetic line-break (1,100c post, #3 performer):
```
What does it say about us
when our machines can't dream
of anything but nightmares?
```

Use sparingly — 1 post per week can do this.

### Closing question specificity (2026-04-21)

Closing questions should be present-tense and specific, not future-abstract. Make the question answerable right now.

**Pipeline fail:** "what does your team's AI memory look like after 12 months of compounding?" → aspirational, hypothetical, 12 months away.

**Aayush edit:** "What does your team remember from last sprint's Claude Code usage?" → specific timeframe (last sprint), specific tool (Claude Code), answerable today.

**Rule:** Default to "last [week/sprint/quarter]" or "right now" over "in 12 months" or "next year". Readers engage with questions about what they've already done, not what they plan to do.

### ALL-CAPS one-word emphasis

Once per post maximum:
- "Don't get me WRONG, the 99% aren't dumb." (1,736c post)
- "what are you building that only YOU can build?" (1,595c post — today)

Reserve for the beat that deserves a vocal stress. Never on function words.

### Lowercase rhetorical openers

"what are you building that only YOU can build?" — today's post closer opens with lowercase "what". Deliberate voice choice for personal/rhetorical questions.

Also works for: "what's actually changing here?" / "how do you even measure that?" / "why does any of this matter?"

### Ellipsis hook

"AI startups have 12 months before they die…" (2026-04-20 post).

Trailing `…` (unicode) or `...` (three periods) on the hook adds stakes without a full sentence. Do NOT use ellipsis mid-sentence — that's AI-tell.

---

## Banned patterns — ZERO tolerance (hard-gate enforced)

### Em dashes (U+2014)
Use commas, periods, or "..." instead. Regex enforced in `tests/kill-list-regex.sh`.

### "It's like X" analogies
The #1 LLM tell. "It's like buying a coffee for $5, but they use a smaller cup" (today's failure) = REJECTED.
Replace with direct parallel claim ("Same pricing. Less per token.") or rhetorical question ("what are you actually paying for?").

### `[Not X, it's Y]` AI-tell inversion
"The survivors aren't building better models. They're building better distribution." = REJECTED.
"This isn't about X. It's about Y." = REJECTED.

BUT — parallel comparisons with DIFFERENT subjects are allowed:
- "Customer support logs from 2023 aren't a moat. Real-time workflow data from power users who can't leave is." ← Aayush uses this. Subject changes from "logs" to "data". ALLOWED.

The regex in `tests/posts-gate.sh` tightened 2026-04-20 to catch only the same-subject AI-tell inversion.

### Trailing hashtag blocks
Zero hashtags anywhere in the post. Top performers have zero. Bottom performers often have blocks.

### Fabricated personal experience
Every "i [verb] [specific past event]" must trace to `config/aayush-experiences.md`. If no match, use F2 (Hidden Truth) or F3 (Absurd Mirror), which don't require personal experience. Never invent numbers, team sizes, client names, or specific past events.

### Guru positioning
No "here's what I've learned", no "the framework I use", no "what separates X from Y". Aayush is a practitioner sharing observations, not a teacher.

### Advice voice
Zero "founders should...", "builders who invest now get...", "teams need to plan for...", "the ones who X will Y" closers.
Replace with: personal observation + open question.

### Winner/loser neat bows
"The founders winning this wave X. The ones losing Y." — banned. End on open questions, honest uncertainty, or grounded observations.

---

## What's ALLOWED in posts that's banned in briefs

Briefs are for Aayush's learning (broad-audience newsletter voice). Posts are Aayush's own voice to founders. Different surfaces, different rules.

- **moat / moats** — ALLOWED. He uses it 4× in today's shipped post. Part of his vocabulary. (Banned in brief.)
- **thesis, conviction** — ALLOWED.
- **10x, 100x, 3x multipliers** — ALLOWED if attached to a named thing.

---

## Format checklist (all templates)

- [ ] Hook under 70 chars, fits before the "see more" fold
- [ ] Sentence case throughout — every sentence starts with capital letter, including "I"
- [ ] Uppercase `I` pronoun (not `i`). **Corpus evidence: 6 of 7 first-person pronoun uses are uppercase; the 1 lowercase is inside quoted AI-chatbot dialogue.**
- [ ] No em dashes
- [ ] No markdown `**bold**` (LinkedIn renders the asterisks literally)
- [ ] 1,300c total floor, **1,100 prose-char floor** (prose = total minus whitespace), soft cap at 2,000 total, hard cap at 2,700
- [ ] At least 3 specific numbers OR named tools/companies
- [ ] CTA is not "Learn more" or engagement bait
- [ ] Max 1 emoji in body (👇🏻 in p.p.s. pointer doesn't count)
- [ ] 0 hashtags
- [ ] Passes posts-gate.sh: no "It's like X", no AI-tell inversion, no trailing hashtags, no banned MBA-vocab (differentiation, commoditization, table stakes)
- [ ] **Closes with a question OR unresolved pivot to the reader.** Corpus evidence: 4 of 4 finalized posts do this. Options: (a) direct question with specific present-tense framing ("What does your team remember from last sprint?"), (b) unresolved statement pointed at reader ("Because they might not be who you think."), (c) rare — self-admitting question ("I haven't tried X yet").

## Formatting devices — calibrate to post mode (2026-04-24 rewrite)

These are OPTIONS, not a checklist. Count by mode, not by quantity.

**News-commentary / observer-mode posts** (like 2026-04-24 GPT-5.5, using Pattern E observation-first):
Typically use **0-1** formatting devices. Rely on paragraph breaks, observation-first setup, and a personal closer. Do not force additional devices in.

**Vulnerable-personal posts** (like 2026-04-20 "I quit my job", TIER 1):
Use **3-4** formatting devices. p.s., p.p.s., unicode-bold on the pivot number, 👇🏻 pointer to image, etc.

**Contrarian-philosopher posts** (like 2026-04-20 "every startup says they're 'ai-powered'"):
Use **1-2** formatting devices. Typically contrast labels or a "That's X." recap plus one emphasis device.

### Available devices (pick per mode, do not stack mandatorily)

- Unicode-bold on pivot words/numbers — **ONLY when a specific number/word IS the pivot** (2026-04-24 §g). Do not fabricate a number to justify the device.
- Markdown asterisks `**bold**` — **NEVER** (LinkedIn renders the stars, 2026-04-24 §h).
- P.S. closer — lowercase, new concrete detail. Skip when the post's natural closer is a genuine question or admission.
- P.P.S. with 👇🏻 image pointer — only when an image is actually attached.
- Atlan context p.p.s. — only when post topic overlaps Atlan's actual work. Not a default closer.
- Bridge sentence after hook (observer placement + mechanism named).
- Parenthetical personality aside mid-post (one-liner + emoji, inline).
- Single-line paragraph breaks — **default cadence now, not a reach-for** (see "Default cadence: one sentence per paragraph").
- Parallel-imperative rhythm.
- Contrast labels (short binary pair + payoff).
- Named specifics with $/scale ($15Bn, 100M users, $10B deal).
- Two-question close OR poetic line-break close OR unresolved-admission close (2026-04-24 §i).
- ALL-CAPS one-word emphasis (once per post max).
- Negative-space paragraphs (2-8 word standalone for emphasis).
- "That's X." recap-tag rhythm (concept-naming or diagnostic beat — two variants).
- Era-reframe ("2023 strategy on 2026 timelines").
- Ellipsis hook ("…" at end of first line).
- Two-line binary hook.
- Arrow `↓` as visual colon before a quote — **0 corpus uses (single off-corpus sighting).** Do NOT use until 2+ more uses appear in finalized posts. Resolved per `config/post-corpus-analysis-2026-04-24.md` §Q1.

**Old rule (removed 2026-04-24):** "aim for 2-3 devices per post." This rule was pushing the pipeline toward fabricated `𝟯𝟲`-style unicode-bold hits on posts that didn't need any formatting. The correct count depends on which mode you're writing in, not a constant minimum.

---

## Top 5 performers — quoted with annotations

### #1 — 392 engagement, 1,497 chars

**Style**: Vulnerable Victor · **Hook**: D Time Bomb · **Formula**: F1 Personal Crisis

> I quit my job with zero backup plan.
>
> Everyone said I was insane.
>
> 3 months later, I realized they were wrong about everything.
>
> See, by January 2025, I was done:
> - Mentally fried
> - Living on autopilot
> - Couldn't give 100% at Springworks
>
> So I did what "responsible adults" never do.
>
> I walked away.
>
> - No next job lined up.
> - No 12-month runway saved.
> - No side hustle to fall back on.
>
> Just... nothing.
>
> My savings dropped 𝟰𝟬%. But, my anxiety dropped 𝟵𝟬%.
>
> [...continues...]
>
> Sometimes not knowing 𝗜𝗦 the plan.
>
> [...]
>
> p.s. Take this post as your sign to take a break from work :)
>
> p.p.s First day at the Vipassana center 👇🏻

**What worked**: unicode-bold (𝟰𝟬%, 𝟵𝟬%, 𝗜𝗦), hyphen-bullet sub-lists, "Just... nothing." negative-space paragraph, P.S./P.P.S. with 👇🏻 image pointer, vulnerable first-person with a time-bomb hook.

### #5 — 87 engagement, 1,736 chars

**Style**: Contrarian Philosopher · **Hook**: A Contrarian Truth · **Formula**: F2 Hidden Truth

> every startup says they're "ai-powered" now.
>
> but 99% are just chatgpt wrappers with extra steps.
>
> the 1% though? they're terrifying.
>
> Don't get me WRONG, the 99% aren't dumb.
> Smart companies. Great founders. Wrong approach.
>
> Here's why:
>
> They're still thinking AI First when winners are going AI Native.
>
> [...]
>
> AI First: "How can we add AI to improve X?"
> AI Native: "Why does X exist at all?"
>
> One optimizes. One eliminates.
>
> [...]
>
> Kill the constraint. Kill the process.
>
> [...]
>
> What would you delete if AI had always existed?
>
> p.s. My honest answer? My entire role. That's why I'm learning to build what replaces me.
> p.p.s This is me drooling over our new N8N setup 👇🏻

**What worked**: all-lowercase hook, contrast labels (AI First: / AI Native:), parallel imperatives (Kill X. Kill Y.), ALL-CAPS WRONG, two-question close structure, p.s./p.p.s. with image.

---

## Today's post (2026-04-20) — voice reference

Full text lives in `config/aayush-reference-posts/2026-04-20-ai-startups-12-months.md`. Summary of what it did:

- Ellipsis hook ("AI startups have 12 months before they die…")
- Uses "moats" 4× naturally (his word, his surface)
- Present-tense first-person observer ("Every week I watch a category shrink")
- Inline 3-pillar list with hyphens (Distribution / Proprietary data / Deep workflow integration)
- "That's X." recap tags after each pillar's proof
- Named specifics: Canva 100M users, Notion rebuilt 5 times, Anthropic/OpenAI
- Hedge markers: "I doubt", "IMO"
- Era-reframe: "a 2023 strategy running on 2026 timelines"
- Lowercase rhetorical closer with ALL-CAPS YOU: "what are you building that only YOU can build?"
- 1,595 chars — in the sweet spot

Match THIS voice.

---

## Anti-reference — what failed in shipped posts

### 2026-04-20 morning cron — Option 2 (pre-edit)
Had "It's like buying a coffee for $5, but they use a smaller cup and don't tell you." → failed the analogy gate.

### Bottom performer (7 engagement, 2,606 chars)
Well-structured post about AI buttons. But 2,606c was too long — LinkedIn readers dropped off mid-scroll. Brilliant closer never got seen.

Lesson: discipline on length matters more than length ambition.

### Bottom performer (1 engagement, 289 chars) — Obsidian plugin
"Any obsidian users in my network? I'm working on a plugin..." + hashtag block.

Lesson: broad stakes beat niche technical asks. Hashtag blocks correlate with dead posts.

---

## How this blueprint evolves

1. Aayush reads the Slack-delivered posts and shares feedback in chat.
2. One JSONL line appends to `history/feedback-log.jsonl`.
3. Sunday `/weekly-feedback` reads the log + week's shipped posts + attribution data (which option was picked/edited/posted). Proposes blueprint edits.
4. Aayush approves/rejects. Approved edits commit.
5. Week N+1 posts reflect updated blueprint.

Also: every new top-performing post (engagement > prior #5) gets annotated in the "Top 5 performers" section of this file. Performance data drives evolution.

---

## Hard-gate safety net (separate from this blueprint)

`tests/posts-gate.sh` enforces at ship time:
1. Length bounds: 1,300-2,000 chars per option (post 2026-04-20 update)
2. No "It's like X" / "Think of it as" analogies
3. No `[Not X, it's Y]` AI-tell inversions (same-subject only)
4. No trailing hashtag blocks
5. No em dashes

The blueprint handles everything else.
