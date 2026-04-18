# Conviction

**Purpose.** The through-line that makes the newsletter Aayush's. Not news. Not a summary. What he *believes* is happening in AI that others don't see. Every brief threads this through its synthesis and secondary sections.

**Update cadence.** Manually, weekly, on Sundays. The `/weekly-feedback` skill writes `workspace/YYYY-MM-DD/conviction-candidates.md` every Sunday with 2-3 through-lines extracted from top-performing posts — Aayush reviews and edits this file. No auto-rewrite until n ≥ 50 posts shipped (statistical confidence gate).

**Version history.** Rolling backups at `config/conviction.md.bak.1`, `.bak.2`, `.bak.3`. Max 20% text-delta per weekly update — the `/weekly-feedback` skill enforces this cap.

---

## This week's convictions (2026-04-18 → 2026-04-25)

### 1. Small teams with AI beat 50-person orgs in 2026

The cost of coordination is collapsing. A 3-person team with Claude Code + Cursor + n8n ships what took 25 engineers in 2022. Founders who get this early win. Founders who still hire like it's 2022 are building tomorrow's cost structure problem.

*Evidence to watch:* team sizes of recent YC W26 batch, agent-team startups raising Series A with <10 engineers, case studies of AI-native companies hitting $10M ARR with <5 people.

### 2. Most AI products will fail because they skip memory, not because of the model

The hard part is no longer the LLM. It's context — what the system remembers across sessions, how state persists between users, how lessons compound. Teams spending on model upgrades instead of memory architecture are optimizing the wrong axis.

*Evidence to watch:* Notion's 5 agent rebuilds (all memory-layer), gbrain-style local brains gaining traction, the gap between demos that work and products that stick.

### 3. Founders are underusing Claude Code

Treating Claude Code like an IDE plugin instead of an agent runtime. The ones who ship fastest treat it as the execution layer for their whole company — docs, marketing, CI, customer research, everything. Most founders still have it running in one terminal for coding only.

*Evidence to watch:* template repos like this one being forked, founder-built skills replacing SaaS categories, alphaclaw/openclaw adoption among non-engineers.

---

## How writers use this

- **Newsletter:** Thread this through synthesis sections. Reference specific convictions when stories align. Never say "as I believe" — demonstrate belief through what gets emphasized.
- **Posts:** One post should clearly express one of these convictions. The other two can be softer — discovery stories, specific numbers, contrarian takes — but at least one carries POV.
- **Brain:** When `/brain-connect` finds a past theme that matches a conviction, the connection becomes stronger evidence. Past brain connections don't just show "we covered this" — they show "this is the pattern we've been tracking."

---

## What this is NOT

- **Not a manifesto.** 2-3 short claims, not an essay.
- **Not predictions.** "Small teams win" is a claim about the present, not a guess about 2030.
- **Not evergreen.** These change weekly. Last week's conviction becomes this week's archive (bak files).
