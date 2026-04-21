# Voice-matching fixture — 2026-04-20

**Status:** Published by Aayush. Use as the primary voice anchor for every
`/write-posts` generation from 2026-04-20 onward. Read this BEFORE composing
the 3 daily options. Match its rhythm, not its claims.

**CRITICAL — CONTENT EMBARGO:** The specific examples in this post (Notion, Canva, Anthropic/OpenAI, "12 months", Distribution/Proprietary data/Deep workflow integration) are ALREADY PUBLISHED and must NEVER appear in generated posts. Using them would make Aayush look like he's repeating himself.

Extract DEVICES only (ellipsis hook, "That's X." recap tags, three-pillar list, "I doubt"/"IMO" markers, era-reframe, lowercase closer). Apply to TODAY'S news, not yesterday's examples.

**Length:** ~1,900 characters
**Template:** three-pillar (see `.claude/skills/write-posts/references/post-templates.md`)
**Style (Blueprint):** Contrarian Philosopher
**Hook pattern:** D-ellipsis (Time Bomb + trailing "…")

---

## The post

```
AI startups have 12 months before they die…
Every week I watch a category shrink.
The pattern is always the same.
Small team ships a clever AI wrapper.
Founders raise a round.
Six months later, Anthropic or OpenAI ships the same thing natively.
The startup pivots or dies quietly.
Most people I talk to are building the exact thing OpenAI will ship next quarter. They just don't see it yet.
The ones who survive are building moats the platforms can't copy.
There are only three that still hold:

- Distribution
- Proprietary data
- Deep workflow integration

Canva has 100 million users. When they decide your AI feature belongs in their workflow, you're not competing against their product. You're competing against their audience.
That's distribution.
Customer support logs from 2023 aren't a moat. Real-time workflow data from power users who can't leave is.
That's proprietary data.
And deep integration isn't "we added AI to our app." It's going so far into the job that switching means rebuilding the whole workflow from scratch.
That's the third.
Everything else is a feature waiting to be absorbed.
Notion rebuilt their agent system five times before shipping.
Every time they got close, a platform provider shipped the feature underneath them.
They only won by going deeper, not wider.
I doubt current stakes are about model access anymore. That war is over.
IMO, it's about who owns the user when the feature becomes commodity.
Small teams can still win.
But "build the feature, they'll come" is a 2023 strategy running on 2026 timelines.
what are you building that only YOU can build?
```

---

## Rhythm devices used (annotated)

1. **Ellipsis hook** — "AI startups have 12 months before they die…" (Pattern D-ellipsis). Trailing "…" builds suspense.

2. **Short fragment paragraphs** — "The pattern is always the same.", "That's distribution.", "That's proprietary data.", "That's the third.", "Small teams can still win." Each stands alone, each lands a beat.

3. **Inline 3-pillar list** with `-` hyphens:
   ```
   - Distribution
   - Proprietary data
   - Deep workflow integration
   ```
   Never `•`. Hyphens only.

4. **"That's X." recap-tag pattern** — used 3 times ("That's distribution.", "That's proprietary data.", "That's the third."). Each lands AFTER a concrete named example (Canva, support-logs, deep-integration). The recap tag names the abstract concept the example just proved.

5. **Named companies as proof** — Canva (100M users), Anthropic, OpenAI, Notion (rebuilt agent system 5 times). Every abstract claim sits next to a specific named thing.

6. **Personal-voice markers** — "I doubt" once, "IMO" once. Two total, both marking opinion vs fact. Reads as him thinking aloud, not positioning as expert.

7. **Era-reframe** — "'build the feature, they'll come' is a 2023 strategy running on 2026 timelines." One-line implication that compresses a full argument into a dated label.

8. **Word "moat" used 4 times** — Aayush's own vocabulary. Posts-gate allows this; briefs do not.

9. **Lowercase rhetorical question as closer** — "what are you building that only YOU can build?" Lowercase "what" + ALL-CAPS "YOU" (emphasis used once, max). Closer is a personal challenge, not a CTA.

10. **Parallel-structure comparison, not AI-tell inversion** — "Customer support logs from 2023 aren't a moat. Real-time workflow data from power users who can't leave is." Second sentence introduces a NEW subject ("real-time workflow data") rather than bouncing "it's/they're" back at the first. The posts-gate regex must NOT flag this.

---

## How /write-posts should use this fixture

1. Read this file at the top of the prompt, alongside `config/aayush-linkedin-patterns.md`.
2. Pick at least 1 of the 3 daily options to mirror this rhythm (even if the topic differs).
3. Match the DEVICES, not the CLAIMS. Never copy "12 months", "Anthropic/OpenAI", etc. — pick today's equivalent from today's brief.
4. A generated post that hits 5+ of the 10 rhythm devices above is on-voice. A post that hits 2 or fewer needs a rewrite.
