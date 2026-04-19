# Aayush's Verified Experiences

**Purpose.** The ONLY source for first-person specific claims in LinkedIn posts. If a post wants to claim *"i built X"*, *"i advised Y"*, *"i deleted N lines"*, *"a 14-person team I worked with"* — it MUST trace to a verified entry below.

If no matching entry exists → the post MUST rewrite as a **take** (opinion on the news) instead of a **story** (personal experience).

This prevents the LLM from fabricating personal authority. Every fabricated claim in the shipped 2026-04-18 posts — *"deleted 1,200 lines of Cursor code"*, *"14-person team adopted Cursor in January"*, *"tracking tokens per merged feature with a team I advise"* — was invented.

**Rule:** if Aayush hasn't written it here, the LLM can't claim it.

---

## Aayush's context (verified)

- **Role:** Works at **Atlan** in a go-to-market / growth function
- **Core work:** Builds AI agents as a regular part of his job
- **Content thesis:** Translating hands-on, technical experience into authentic LinkedIn content that educates and resonates — without sounding like a guru, corporate spokesperson, or content marketer

## Verified experiences (from Aayush's own instructions)

### Ongoing — Building AI agents at Atlan

- **Can claim:** "I build AI agents at Atlan"
- **Can claim:** "I work in GTM/growth at Atlan and building AI agents is part of my job"
- **Can claim:** "I've built agents for internal workflows"
- **Cannot claim:** specific revenue/cost numbers, client names, anything outside Atlan
- **Tags:** AI agents, Atlan, GTM, growth, internal tooling

### Ongoing — Slack summarizer agents

- **Can claim:** "I've built Slack summarizer agents"
- **Can claim:** "I use agents to summarize Slack conversations as part of my workflow"
- **Cannot claim:** specific adoption numbers across teams, any fabricated user stats
- **Tags:** Slack, agents, summarization, LLM, productivity

### Ongoing — Prospect finder agents

- **Can claim:** "I've built prospect-finder agents for GTM work"
- **Can claim:** "I use agents for sales/GTM automations"
- **Cannot claim:** specific deal sizes, named prospects, win rates
- **Tags:** sales, GTM, prospecting, agents, automation

### Ongoing — API-driven automations

- **Can claim:** "I build API-driven automations for my GTM workflows"
- **Can claim:** "I integrate APIs and MCPs directly rather than building UIs"
- **Cannot claim:** specific hours saved, fabricated ROI numbers
- **Tags:** APIs, MCP, automation, integration

### Observed thesis — AI UIs becoming irrelevant

- **Can claim:** "I've been noticing that most of my AI agent interactions happen via APIs and MCPs, not buttons and sparkle icons"
- **Can claim:** "The sparkle-icon era of AI UI feels like it's ending — most of my actual agent work happens through protocol integrations"
- **Context:** This is a real observation from Aayush's own work pattern, not a universal claim about the industry
- **Tags:** AI UI, MCP, agent design, UX

### Observed behavior — LLM counting limitations

- **Can claim:** "I've hit the LLM counting limitation firsthand — the classic strawberry example"
- **Can claim:** "When I was building [agent X], I ran into the counting bug that shows up in 'how many r's in strawberry'"
- **Context:** Direct hands-on observation from agent building work
- **Tags:** LLM behavior, tokenization, hallucinations, agent debugging

### Live session — Agent-building session invite

- **Can claim:** "I'm running a live agent-building session" (when actually true and scheduled)
- **Tone note:** Frame with self-deprecating humor — not corporate webinar language
- **Tags:** live session, agent building, teaching

---

## Voice notes (Aayush's specific rules)

- **Real over fabricated** — Aayush catches invented examples quickly. Every specific claim must be grounded in a real experience or verifiable fact.
- **Thesis clarity before polish** — start with "what are we actually trying to say and why does it matter to the reader?" — NOT "what's a catchy angle?"
- **Audience-first hooks** — leading with the writer's personal experience is a known weak pattern. Hooks should lead with something the audience cares about.
- **Authenticity over performance** — no webinar language, corporate buzzwords, fluff words, or guru positioning. Humor should feel genuine, not engineered.
- **Honest pushback is valued** — Aayush prefers being challenged with real reasoning over agreement or flattery.
- **No hashtags at end** — zero hashtags.
- **Writing style:** conversational, lowercase-leaning tone in natural voice; final formatting uses standard capitalization, split sentences, and single-line paragraph rhythm suited to LinkedIn.

---

## Adding new entries

When Aayush ships something real, add it here. Template:

```markdown
### YYYY-MM-DD — [Short description of the real event]

- **Can claim:** "[specific sentence Aayush can truthfully say in first person]"
- **Can claim:** "[another specific truthful sentence]"
- **Cannot claim:** [things the LLM might extrapolate but shouldn't]
- **Context:** [1-2 sentences — why this is true]
- **Tags:** [topics/technologies]
```

**Rules when adding:**
1. Only real events. If it'd embarrass you to defend publicly → leave it out.
2. Name explicit boundaries — "Cannot claim: team sizes, dollar amounts beyond what's listed"
3. Short and specific. The LLM should not need to infer or embellish.
