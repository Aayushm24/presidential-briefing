# Aayush's Verified Experiences

**Purpose.** The ONLY source for first-person specific claims in LinkedIn posts. If a post wants to claim *"i built X"*, *"i advised Y"*, *"i deleted N lines"*, *"a 14-person team I worked with"* — it MUST trace to a verified entry in this file.

If no matching entry exists → the post MUST rewrite as a **take** (opinion on the news) instead of a **story** (personal experience).

This prevents the LLM from fabricating personal authority. Every example in the shipped 2026-04-18 posts was invented: "deleted 1,200 lines of Cursor code", "14-person team adopted Cursor in January", "tracking tokens per merged feature with a team I advise". None of it was true. All of it sounded plausible. That's the worst kind of AI failure — specific, plausible, totally fake, and published under Aayush's name.

**Rule:** if Aayush hasn't written it here, the LLM can't claim it.

---

## Format

Each entry contains:
- **Date** (real, approximate OK)
- **Specific claim** (what Aayush can truthfully say in first person)
- **Context** (why it's true — so the LLM can pick matching claims intelligently)
- **Tags** (topics/technologies this experience relates to)

---

## Verified Entries

### 2026-04-18 — Built a daily AI brief pipeline with Claude Code + GitHub Actions

- **Can claim:** "I built a daily AI brief pipeline using Claude Code"
- **Can claim:** "I migrated from n8n cloud to GitHub Actions for daily automation"
- **Can claim:** "I use an LLM council pattern — Opus writes, Gemini fact-checks, Grok attacks"
- **Can claim:** "I've been iterating on AI prompts in markdown, version-controlled"
- **Cannot claim:** specific dollar amounts, client names, team sizes of people Aayush doesn't lead
- **Tags:** AI pipelines, Claude Code, GitHub Actions, n8n, LLM council, automation

### 2026-04 — Running the Presidential Briefing daily knowledge system

- **Can claim:** "I read about 40 AI sources every morning"
- **Can claim:** "I maintain a memory layer with Supabase + pgvector for semantic search over past themes"
- **Can claim:** "I ran the pipeline in parallel with n8n for days to verify output quality"
- **Tags:** RAG, Supabase, semantic search, daily AI tracking, memory systems

---

## How the skill uses this file

When `/write-posts` generates the 3 options, it reads this file. For each option:

1. If the option includes a first-person specific claim (numbers, team sizes, specific code/clients), check this file
2. If a matching entry exists → use it verbatim in the post (no embellishment, no made-up context)
3. If no match → rewrite the option to be a **take**, not a story

A take says: *"Cursor raising at $50B reveals something about coding-tool valuations — the market is pricing distribution, not code quality."* (Opinion backed by source.)

A story says: *"I've been using Cursor for 6 months across 3 projects and here's what I learned."* (Requires verified entry.)

When no entries match the day's stories, ALL 3 options are takes. That's fine. Takes can be strong. Fabricated stories are never acceptable.

---

## Adding new entries

After Aayush ships something real, add it here. Example:

```markdown
### 2026-05-15 — Shipped v2 of X for Y customer

- Can claim: [what's true and specific]
- Can claim: [what's true and specific]
- Cannot claim: [things the LLM might extrapolate but shouldn't]
- Tags: [topics]
```

Weekly feedback (Sunday cron) can surface candidate entries from recent activity, but Aayush confirms each manually before it counts as verified.
