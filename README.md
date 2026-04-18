# Presidential Briefing

Daily AI knowledge system. Runs on GitHub Actions. Scrapes ~40 sources at 5:30 AM IST, scores, clusters into themes, writes a full newsletter + 3 LinkedIn post options, runs a 4-pass council review with adversarial attack, and delivers to Readwise Reader + Slack.

All logic lives as composable Claude Code skills in `.claude/skills/`. Prompts are markdown — diffable, versionable, locally testable.

---

## What it does

**5:30 AM IST (daily cron)**
1. **Scan** — pulls 41 RSS feeds + 8 X/Twitter accounts via Grok
2. **Score** — Sonnet picks top 10 for business relevance + practitioner value
3. **Theme detect** — clusters stories into patterns (2+ stories per theme)
4. **Brain connect** — semantic search against Supabase memory of past themes
5. **Write briefing** — Opus writes 1,200–1,500 word newsletter with Helix 3-layer model (facts → synthesis → conviction)
6. **Write 3 posts** — Opus writes 3 LinkedIn options in different formats
7. **Council attack** — Grok adversarial review: find gaps, unsupported claims, voice violations
8. **Revise** — Opus applies fixes (hard cap: 2 iterations)
9. **Publish** — commits to `workspace/YYYY-MM-DD/`, emails brief to Readwise, Slack DMs the 3 posts

**07:00 AM IST (dead-man check)**
- If today's `workspace/` is empty, re-runs daily-brief. Mitigates GitHub Actions cron "best effort" SLA.

**Sunday 5:30 PM IST (weekly feedback)**
- Reads LinkedIn engagement via Sheets webhook
- Writes `workspace/YYYY-MM-DD/conviction-candidates.md` for manual review
- Auto-updates `hooks.md` scoring from 4-week engagement data
- Commits changes so Monday's brief reads the updates

---

## Architecture

- **Runtime:** Claude Code headless in GitHub Actions (`anthropics/claude-code-base-action`)
- **LLM gateway:** `llmproxy.atlan.dev` (LiteLLM proxy → Anthropic, Google, xAI)
- **Brain:** Supabase Postgres + pgvector
- **Delivery:** Gmail → Readwise + Slack webhook

See `CLAUDE.md` for the skill routing table, `config/council.json` for model routing per task, `config/conviction.md` for the weekly POV.

---

## Folder structure

```
.claude/skills/          # composable skills (markdown prompts)
.github/workflows/       # daily-brief.yml + dead-man.yml + weekly-feedback.yml + tests.yml
config/                  # sources.csv, council.json, conviction.md
workspace/YYYY-MM-DD/    # daily artifacts
history/                 # published.jsonl, engagement.jsonl, themes.jsonl
tests/                   # golden-format, kill-list-regex, voice-fixtures/
brain-engine/            # gbrain reference (not active — Supabase is the brain)
```

---

## Setup

```bash
# 1. Clone
git clone https://github.com/Aayushm24/presidential-briefing.git
cd presidential-briefing

# 2. Local .env (for dev runs)
cp .env.example .env
# Fill in required keys. ANTHROPIC_AUTH_TOKEN, XAI_API_KEY, SUPABASE_ANON_KEY minimum.

# 3. Test with dry run
DRY_RUN=1 claude -p '/daily-brief'

# 4. Wire GitHub Actions secrets
# Settings -> Secrets and variables -> Actions -> New repository secret
# Add the same keys as in .env.example.
```

---

## The compounding thesis

Day 1: empty brain. The newsletter teaches concepts.
Day 30: 100+ pages of theme history. The newsletter connects today's news to 2-week-old patterns.
Day 100: 500+ pages. The system writes posts that carry the specificity of someone who has tracked AI daily for months.

The learning loop updates `config/conviction.md` + `.claude/skills/write-posts/references/hooks.md` + `voice.md` from what actually gets engagement on LinkedIn. Auto-rewrite gated at n ≥ 50 posts — before that, Aayush edits manually.

---

## Status

Migrating from n8n workflow `9wfJC0I0I0j92r0N` to Claude Code + GitHub Actions. See `~/.gstack/projects/presidential-briefing/aayush-design-20260418.md` for the approved design doc.

**n8n workflow stays live during parallel-run period (days 6–10). Cutover only after 5 consecutive successful parallel runs with equivalent-or-better output.**
