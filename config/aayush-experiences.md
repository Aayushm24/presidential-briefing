# Aayush's Verified Experiences

**Purpose.** The ONLY source for first-person specific claims in LinkedIn posts. If a post wants to claim *"i built X"*, *"i advised Y"*, *"i deleted N lines"*, *"a 14-person team I worked with"* — it MUST trace to a verified entry in this file.

If no matching entry exists → the post MUST rewrite as a **take** (opinion on the news) instead of a **story** (personal experience).

This prevents the LLM from fabricating personal authority. Every example in the shipped 2026-04-18 posts was invented: *"deleted 1,200 lines of Cursor code"*, *"14-person team adopted Cursor in January"*, *"tracking tokens per merged feature with a team I advise"*. None of it was true. All of it sounded plausible. That's the worst kind of AI failure — specific, plausible, totally fake, and published under Aayush's name.

**Rule:** if Aayush hasn't written it here, the LLM can't claim it.

---

## Current state: EMPTY

**This file is intentionally empty.** Aayush fills it in manually when he has a real experience he wants the LLM to draw from.

Until entries exist, the `/write-posts` skill defaults ALL three options to **takes** (opinions on the news), never **stories** (personal experiences).

---

## How to add an entry

Copy the template below into the "Verified Entries" section when Aayush wants a specific experience to be available to the LLM:

```markdown
### YYYY-MM-DD — [Short description of the real event]

- **Can claim:** "[specific sentence Aayush can truthfully say in first person]"
- **Can claim:** "[another specific truthful sentence]"
- **Cannot claim:** [things the LLM might extrapolate but shouldn't — name them explicitly]
- **Context:** [why this is true, in 1-2 sentences]
- **Tags:** [topics/technologies — so the LLM can match today's story to relevant experiences]
```

**Rules when adding entries:**
1. Only add what actually happened. If it's a claim you'd be embarrassed to defend publicly, leave it out.
2. Name explicit boundaries — "Cannot claim: team sizes, dollar amounts beyond what's listed"
3. Keep entries short and specific. The LLM should not need to infer or embellish.

---

## Verified Entries

*(None yet. Aayush adds entries here as real experiences accumulate.)*

---

## How the skill uses this file

When `/write-posts` generates the 3 options, it reads this file. For each option:

1. If the option includes a first-person specific claim (numbers, team sizes, specific code/clients), check this file
2. If a matching entry exists → use it verbatim in the post (no embellishment, no made-up context)
3. If no match → rewrite the option to be a **take**, not a story

**A take says:** *"Cursor raising at $50B reveals something about coding-tool valuations — the market is pricing distribution, not code quality."* (Opinion backed by source.)

**A story says:** *"I've been using Cursor for 6 months across 3 projects and here's what I learned."* (Requires verified entry.)

When no entries match the day's stories, ALL 3 options are takes. That's fine. Takes can be strong. Fabricated stories are never acceptable.

---

## Weekly feedback loop (future)

The `/weekly-feedback` skill (Sunday cron, not yet active) can surface candidate entries from Aayush's recent commits + shipped posts + Slack notes. But every candidate must be manually reviewed and approved by Aayush before it counts as verified — no auto-add.
