# Post Blueprint

**Primary voice source for `/write-posts`.** Read this FIRST. Every other reference (voice.md, post-templates.md, hooks.md, kill-list.md) is secondary. When two sources conflict, this blueprint wins.

Updated from daily feedback in `history/feedback-log.jsonl`. Versioned in git.

---

## Who this is for

Aayush writing LinkedIn posts to founders and builders. Not a corporate newsletter. Not Atlan's voice. His voice — a practitioner sharing observations, not a teacher explaining frameworks.

His audience: founders in AI, operators thinking about how the game changes, builders on LinkedIn. They've seen every corporate thought-leadership post. They want signal.

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
  - **Two-line binary variant (2026-04-21)**: Pair a universal claim with an immediate inversion on the next line. Example: "Everyone has Claude Code. / Almost no one is using it right." Works better than a single declaration when the gap IS the whole point. No observer framing needed — just state the contrast and let the next line land it.
- **Pattern B — Identity Statement**: "97% of LinkedIn creators are men. I'm in the 3%." / "I'm the most average bloke ever." Requires a verified Aayush-side fact.
- **Pattern C — Absurd Comparison**: "A cat with Instagram makes more than your MBA."
- **Pattern D — Time Bomb**: "I posted my first LinkedIn post 3 years ago." / **Variant: ellipsis** — "AI startups have 12 months before they die…" (from today's shipped post, 2026-04-20). Trailing ellipsis adds stakes without a full sentence.

---

## Voice — what Aayush sounds like

### Sentence case — with one exception

Every sentence starts with a capital letter. Proper nouns capitalized (Claude Code, Intercom, OpenAI, Atlan).

**One exception: `i` is always lowercase.** Never "I". That's Aayush's signature. Everything else follows normal sentence case.

Closing rhetorical questions: sentence case too. "What does your team's AI memory look like after 12 months?" — not "what does your team's...".

**What changed:** earlier posts used all-lowercase throughout ("every team i talk to..."). That was performing casualness, not being casual. Sentence case with lowercase `i` reads more natural.

### Allowed hedge markers (first-person voice anchors)

- **IMO** — "IMO, it's about who owns the user when the feature becomes commodity." (from today's post)
- **I doubt** — "I doubt current stakes are about model access anymore."
- **I think** — "I think [specific claim]"
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

### Parenthetical personality aside

Inject a casual, self-aware observation mid-post as an inline parenthetical + 1 emoji. Signals the author knows what the reader is thinking. Pre-empts an obvious objection without a full disclaimer sentence.

**Format:** `(observation 🤷🏻‍♂️)` — inline, attached to the sentence that prompted it. Use once per post max.

Example: "The tools were identical (using claude code is not a moat 🤷🏻‍♂️). The infrastructure was completely different."

This is distinct from a standalone body emoji. It's a wink mid-sentence.

### Single-line paragraph fragments for sequences

When listing consequences, actions, or observations in sequence, break each into its own paragraph line. Never stack 3+ short sentences (under 12 words each) in a single paragraph block.

**Pipeline fail:** "He built telemetry that logs every Claude Code interaction. Every pattern analyzed. Every skill saved to a shared repository."
**Aayush edit:** Each sentence on its own line.

Rule: if you have 3+ sentences that are each under 12 words, break them one-per-line. They land harder as separate beats.

---

## Rhythm devices (performance-data-derived, 2026-04-20 calibration)

### Unicode-bold signature (the Aayush formatting)

LinkedIn strips markdown. Aayush uses **Mathematical Bold block** (U+1D400-U+1D7FF) to make specific words render bold in the feed. This survives copy-paste.

Examples from top-1 post (392 eng):
- "My savings dropped 𝟰𝟬%. But, my anxiety dropped 𝟵𝟬%."
- "Sometimes not knowing 𝗜𝗦 the plan."

Rules:
- 1-2 unicode-bold hits per post maximum
- Apply to: the pivot number, the thesis word, a key verb
- Never entire sentences
- Numbers: use Bold Digit block (U+1D7CE-U+1D7FF). Example: `40` → `𝟰𝟬`, `90` → `𝟵𝟬`
- Letters: use Mathematical Sans-Serif Bold (U+1D5D4-U+1D607). Example: `IS` → `𝗜𝗦`

### P.S. / P.P.S. closer with 👇🏻 image pointer

Top-1 and top-5 posts both end with this pattern:

```
p.s. Take this post as your sign to take a break from work :)
p.p.s First day at the Vipassana center 👇🏻
```

- **p.s.** = friendly directive, personal confession, or one new concrete detail that reframes what the reader just read. Lowercase. Do NOT use p.s. to repeat a stat already covered in the body — use it to land something specific and surprising that the body didn't have room for.
- **p.p.s.** = image/asset pointer using 👇🏻 emoji — OR — personal Atlan context CTA (see below). Lowercase.

Reach for this on vulnerable or contrarian posts. 2 of top 5 posts used it.

### Atlan context p.p.s. (2026-04-21)

When the post topic overlaps with what Atlan is building (AI infrastructure, agent ops, data systems, institutional memory, workflow automation), add a p.p.s. that ties the post back to Aayush's actual work:

```
p.p.s. at Atlan we've been building this layer for a while. happy to compare notes with anyone doing the same. 👇🏻
```

**When to use:** Post theme = something Atlan builds or has shipped. Not a sales pitch — a genuine "we're in this too" signal. Makes the post feel less theoretical and more grounded in real work.

**Tone:** Lowercase. Casual. "happy to compare notes" not "let's connect". "we've been building" not "we've built a solution".

### Short fragment paragraphs

Top performers use 2-8 word standalone paragraphs for emphasis:
- "That's distribution." (1,595c post)
- "That's proprietary data."
- "Just... nothing." (392 eng post)
- "Don't get me WRONG, the 99% aren't dumb." (1,736c post, mid-paragraph)

These break rhythm and carry weight. Use sparingly — 2-3 per post max.

### "That's X." recap-tag pattern

After making a concrete point, close with a tag naming what you just showed:
- "Canva has 100 million users. When they decide your AI feature belongs in their workflow, you're not competing against their product. You're competing against their audience. **That's distribution.**"

Posts using this pattern read as structured and deliberate. From today's 1,595c post.

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
- [ ] Sentence case throughout — every sentence starts with capital letter
- [ ] Lowercase "i" everywhere (the one exception to sentence case)
- [ ] No em dashes
- [ ] 1,300c floor, no cap — write as long as the content earns
- [ ] At least 3 specific numbers OR named tools/companies
- [ ] CTA is not "Learn more" or engagement bait
- [ ] Max 1 emoji in body (👇🏻 in p.p.s. pointer doesn't count)
- [ ] 0 hashtags
- [ ] Passes posts-gate.sh: no "It's like X", no AI-tell inversion, no trailing hashtags, no banned MBA-vocab (differentiation, commoditization, table stakes)

## Reach-for checklist — at least TWO per post (top-performer patterns)

- [ ] Unicode-bold on 1-2 specific words/numbers (𝟰𝟬%, 𝗜𝗦)
- [ ] P.S. closer (lowercase, new concrete detail — not a repeat of body stats)
- [ ] P.P.S. with 👇🏻 image pointer when an image is attached
- [ ] Atlan context p.p.s. when post topic overlaps Atlan's work ("at Atlan we've been building this layer...")
- [ ] Bridge sentence after hook (observer placement + mechanism named)
- [ ] Parenthetical personality aside mid-post (one-liner + emoji, inline)
- [ ] Single-line paragraph breaks on 3+ short sequential sentences
- [ ] Parallel-imperative rhythm
- [ ] Contrast labels (short binary pair + payoff)
- [ ] Named specifics with $/scale ($15Bn, 100M users, $10B deal)
- [ ] Two-question close OR poetic line-break close
- [ ] ALL-CAPS one-word emphasis (once/post max)
- [ ] Negative-space paragraphs (2-8 word standalone for emphasis)
- [ ] "That's X." recap-tag rhythm
- [ ] Era-reframe ("2023 strategy on 2026 timelines")
- [ ] Ellipsis hook ("…" at end of first line)
- [ ] Two-line binary hook ("Everyone has X. / Almost no one is using it right.")

Zero per post = probably generic. Four+ per post = probably overworked. Aim for 2-3.

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
