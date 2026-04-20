# Brief Blueprint

**Primary voice source for `/write-briefing`.** Read this FIRST, before any rule file or reference. Every other doc (plain-english-rules.md, section-order.md, anti-slop-checklist.md) is secondary and subordinate. When two sources conflict, this file wins.

Updated from daily feedback in `history/feedback-log.jsonl`. Versioned in git — if you want to see how voice has evolved, `git log config/brief-blueprint.md`.

---

## Who reads this brief

Aayush reads it every morning to learn about what happened in AI. He's an AI program manager at Atlan building agents. Smart, curious, not a beginner, but wants the WHY behind news, not just headlines. He's said explicitly: "optimize for my learning."

If a 16-year-old with no AI background can parse any sentence in one read, we're at the right level. If Aayush has to re-read a sentence to figure out what modifies what, we failed.

---

## Length — 2,500 words floor, no cap

**Target: 2,500-3,500 words. Go longer when the topic demands it.**

This is the most important rule in the blueprint. Do not optimize for brevity. Optimize for Aayush's learning. A thin 1,200-word brief is worse than a thorough 3,500-word brief even if the thorough one takes 15 minutes to read. He reads to level up, not to save time.

Below 2,500 = the mechanism isn't explained enough. Go back to the lead section, pick the claim with the least causal chain behind it, and TEACH the reader what's actually happening underneath.

Section budget (floors, not ceilings):
- Title: ≤80 chars
- Hook + bottom line: 150-250 words
- Lead section: 1,200-1,800 words (the whole point of the brief)
- Each secondary section (#2, #3): 400-600 words
- "What to do this week": 250-350 words

---

## The mechanism rule (the most important content rule)

Every significant claim must answer THREE things beyond the headline:

### 1. Why is this happening NOW?

What changed? What precedent does it break or follow? Not "AI is growing" — instead: "Cerebras couldn't IPO for 2 years because GPU concentration made public-market investors skeptical. The OpenAI contract broke that gate because it turned speculative demand into contracted revenue. That's the precedent that unlocks capital markets for every specialized-chip startup waiting in queue."

### 2. Causal chain forward

What does this force next? For the ecosystem, for competitors, for builders? Trace 2-3 steps.

### 3. Mental-model shift for the reader

What belief should Aayush hold MORE strongly or LESS strongly after reading this section? A claim without all three is just news. A claim with all three compounds his understanding.

---

## Banned vocabulary in briefs — ZERO tolerance

Every word below is enforced by `tests/golden-format.sh` as a hard regex gate. If ANY appears in the brief, ship step aborts.

| Banned | Why | Use instead |
|---|---|---|
| **moat / moats** | MBA vocabulary. Makes the brief sound like a VC pitch deck. Note: allowed in posts (different audience). | Name the specific thing: "Canva's 100M user base", "Tesla's Texas-only focus". Or write "the thing competitors can't copy." |
| **differentiator / differentiation / differentiate** | Same. | "what makes them different" OR name the specific advantage |
| **commoditization / commoditize(s) / commoditized** | Business school word. | "everyone can buy it now" / "it's cheap now" / "gets generic" |
| **table stakes** | Poker jargon that sounds strategic but carries no meaning. | "everyone has it" / "it's not special anymore" |
| **up the stack** / **moves up the stack** | Insider metaphor. | "to apps" / "to the product" / "to what the user touches" |
| **underlying market** | Abstract. | "the market" / "customers" |
| **dependency (on a vendor)** | MBA phrasing. | "needing [vendor]" / "being stuck with [vendor]" |
| **generating real revenue** | Filler. | "charging customers" / "making $X" |
| **production workloads at scale** | Jargon soup. | "actual live systems" / "real daily use" |
| **enterprise customers** (when stating obvious) | Usually unnecessary. | "big companies" or just skip |
| **ecosystem** (bare) | Too abstract alone. | Name the specific thing ("tools built on Claude Code", "AI companies raising rounds") |
| **paradigm shift / disruption** | Hype words. | "this changes X" + the specific change |
| **leverage** (verb) | Jargon. | "use" |
| **utilize** | Jargon. | "use" |
| **seamless / seamlessly** | Delete. Never earned. | — |
| **revolutionary / game-changing / cutting-edge / groundbreaking** | Delete. If true, show don't tell. | — |
| **maturation / matures / maturity** (of markets) | Abstract. | "real companies pay real money for X" |
| **signals maturity / signals market maturation** | Meaningless. | "proves real money is moving" |

---

## `[Not X, it's Y]` inversions — ZERO tolerance

The #1 AI writing tell. Patterns:
- "This isn't X. It's Y."
- "X aren't about Y. They're about Z."
- "Stopped being X. Started becoming Y."

Example from today's failure: "Canva isn't adding AI image generation to their existing canvas. They're changing what it means to design." → FAILS. Replace with direct declarative: "Canva rebuilt the whole canvas around AI. That's a bigger bet than most design tools will make."

Use **parallel structure** instead: "Chips are cheap. Products aren't." — parallel structure with different subjects is fine.

---

## Sentence-level voice rules

### Rule 1 — Sentence length cap: 22 words

Count words. Anything over 22 gets split. The Signal newsletter (thesignal.club) averages 12-14 words per sentence. Aim for that.

Bad (29w): "When specialized AI hardware companies can justify public valuations, the underlying market has moved beyond experimental deployments into production workloads at scale."

Good (3 sentences, avg 13w): "Wall Street will now pay for AI chip companies. That means real businesses buy this stuff every day. We're past the experiment phase."

### Rule 2 — Max 2 abstract nouns per sentence

Abstract nouns name concepts you can't point at: maturation, commoditization, dependency, differentiation, adoption, transformation, deployment, scalability, optimization, integration.

Three or more in one sentence = rewrite.

### Rule 3 — Active voice, concrete verbs

Ban "is/are/was/were" as main verbs where possible. They're weakest-link verbs.

Bad: "The AWS partnership is the key detail."
Good: "The AWS deal matters most."

Bad: "Differentiation is moving up the stack."
Good: "Apps win now. Chips don't." (plus: neither word is in the banned list)

### Rule 4 — Name things

Instead of categories, name the specific company/tool/person/number. Specificity = credibility + clarity.

Bad: "Cloud providers don't integrate new chip architectures for experimental workloads."
Good: "AWS doesn't plug in a new chip unless customers will pay for it."

### Rule 5 — Concrete-first, abstract-earned

Abstract claims must IMMEDIATELY follow a concrete example. Never float alone.

Bad: "Infrastructure is becoming table stakes rather than competitive advantage." (banned words AND pure abstraction)
Good: "Cerebras just sold chips to OpenAI for $10 billion. AWS put them in its data centers. When everyone can buy the same chips, having them stops being special."

Pattern: **Fact · Fact · Claim** or **Number · Name · Rule**.

---

## Structure

```
# [Title — sentence case, one sharp claim, ≤80 chars]

[Hook — one specific, surprising detail. One line.]

[Bottom line — 2-3 sentences. State the thesis ONCE right here. Do NOT repeat at end.]

**Key takeaways:**
- [4-5 scannable bullets — a reader who stops here got 80% of the value]

### [Section 1 header — descriptive, sentence case]

[Content — short paragraphs, bold key phrases, inline-linked citations, NO dividers]

### [Section 2 header]

[Content — same]

### [Section 3 header — last section of lead piece]

[Content — flow into connections naturally. DO NOT create a "how these connect" header. End with a punchline that sticks, not a summary.]

---

### #2 [secondary post title]

[400-600 words — deep enough to teach, not just cite]

---

### #3 [secondary post title]

[400-600 words]

---

### What to do this week

[250-350 words. 1-3 concrete actions with named tools, links, and time estimates.]
```

**No `## Sources` footer.** Ever. Citations live inline with the claim.

---

## Inline citations — mandatory

Every named company, tool, or person on first mention gets a markdown link to a source.

Patterns:
- First mention: `[Cerebras](https://techcrunch.com/2026/04/18/ai-chip-startup-cerebras-files-for-ipo/) filed for IPO...`
- Quote attribution: `> "..." — [Cameron Adams](https://canva.com/blog/ai-2), Canva CPO`
- Article reference: `Simon Willison [analyzed the diff](https://simonwillison.net/2026/Apr/18/opus-system-prompt/)...`
- Number with source: `100M users will get AI in every workflow ([Canva announcement](https://canva.com/blog/ai-2))`

Minimum: 3 inline links. Aim for 7-10. Claims without a URL source get tagged `[UNGROUNDED]` and resolved or killed during `/attack`.

---

## Voice anchors (what Aayush's brief sounds like)

### First-person observer, at least once per section

"I noticed...", "What caught my eye...", "What I keep coming back to is...". Not constantly, but enough that the reader hears a person, not a magazine.

### Opinions signaled clearly

"I think...", "In my read...", "Here's where I disagree with the consensus..."

### Short paragraphs

2-4 sentences. Mix one-sentence paragraphs for punch. Front-load every paragraph — the first sentence IS the point.

### No hype vocabulary

groundbreaking, revolutionary, game-changing, cutting-edge, seamless, leverage, unlock, harness, robust, empower.

---

## Anti-patterns (regex-enforced or council-flagged)

- **"Why now?" structural labels** — "What's happening is...", "Here's why this matters...", "The parallel to the early cloud era is almost exact." ZERO.
- **Winner/loser neat bows** — "The founders who see this will build on these layers. The ones who don't will spend 2027 retrofitting." ZERO. End on open questions, honest uncertainty, or grounded observations.
- **Forced analogies** — "This is like the iPhone moment for AI." Unless the parallel is exact with specifics, drop it.
- **Stat-Stat-Reframe-Metaphor** — "X% of companies Y. Z% fail. Here's the reframe: [clever metaphor]." The #1 AI-tell scaffolding. Weave stats into arguments, never bullet-stack them.
- **Advice voice** — "Founders should...", "Builders need to plan for...". Replace with observation + personal reaction.
- **"It's like X" declarative analogies** — use a rhetorical question or direct parallel claim instead.

---

## The 5 tests — run on every paragraph

1. **Substitution test**: replace the named thing with generic. If the paragraph still works, it's too generic. Rewrite until it can ONLY be about this specific thing.
2. **Specificity count**: ≥3 named entities or concrete numbers per section. Zero specifics = rewrite.
3. **Jargon scan**: zero banned vocab hits.
4. **"So what?" test**: every sentence answers "so what for the reader?" in one sentence. If not, cut.
5. **5th-grade test**: could a smart 16-year-old with no AI background parse this in one read? If no, rewrite.

---

## Reference brief — today's v1 seeds from feedback

No shipped brief yet matches this blueprint. The closest directional goal:

**What a good brief sounds like (synthesized from Aayush's own "AI startups have 12 months" post — the voice he wants, scaled to brief length):**

- Stakes in the first sentence
- Named companies with dollar amounts in the first paragraph
- One sharp thesis stated ONCE
- Short declarative paragraphs
- "What I keep coming back to is..." first-person observer
- Mechanism explained in 3-4 paragraph chunks (why-now → causal chain → mental model)
- Inline `[Source](url)` on every named claim
- No Sources footer
- Ends on an open observation or honest question, NOT a recap

---

## Anti-reference — what failed today (2026-04-20)

Brief shipped with:
- "moat" 5x, "differentiator" 2x, "commoditizes" 1x (banned vocab)
- `[Not X, it's Y]` 4x including "Canva isn't adding AI image generation to their existing canvas. They're changing what it means to design."
- 1,227 words (below 2,500 floor — felt thin)
- Long sentences (7 over 22 words)
- `## Sources` footer (banned)

This blueprint exists BECAUSE of that failure. Every rule above traces to a specific piece of Aayush's feedback captured in `history/feedback-log.jsonl`.

---

## How this blueprint evolves

1. Every time Aayush reads a brief and shares feedback in chat, one line appends to `history/feedback-log.jsonl`.
2. Sunday's `/weekly-feedback` skill reads the week's feedback entries + shipped briefs + this blueprint. Proposes blueprint edits.
3. Aayush approves/rejects each proposal. Approved edits commit.
4. Week N+1 brief reflects updated blueprint.

Do not edit this file manually without also appending a feedback-log entry explaining why. The log is the audit trail.

---

## Hard-gate safety net (separate concern)

While this blueprint guides voice, five regex gates in `tests/golden-format.sh` catch universal failures at ship time:
1. No em dashes (U+2014)
2. No `## Sources` footer
3. No `[Not X, it's Y]` inversions
4. Word count 500-8000 (absurd-outlier only — real target 2,500+ lives here)
5. Exactly 1 H1, 3-8 H3s (structure only)

Plus banned-vocab regex: moat, differentiation, commoditization, table stakes, up-the-stack. These are belt-and-braces — the blueprint should keep them out at compose time.
