# Presidential Briefing

Daily AI knowledge system. Scrapes 40 sources, builds a compounding knowledge brain, generates a presidential briefing delivered to Readwise Reader and a LinkedIn post delivered to Slack.

## What it does

Every morning at 5:30 AM:

1. **Intake** — Pulls from 40 sources (RSS feeds, X/Twitter via Grok, ArXiv, HN, GitHub trending)
2. **Filter** — Scores every item on 5 dimensions. Picks the lead story + 3-5 secondary items.
3. **Brain** — Ingests significant items into gbrain. Searches for connections to past knowledge.
4. **Briefing** — Writes a 5-7 minute presidential briefing that teaches AI concepts from first principles.
5. **Post** — Generates a LinkedIn post from the lead story with an original conviction (not a summary).
6. **Review** — Multi-model council reviews both outputs. Fact-checks, verifies concepts, checks voice, scores novelty.
7. **Deliver** — Briefing emailed to Readwise Reader. LinkedIn post sent to Slack for approve/edit/kill.

## Architecture

- **Orchestration**: n8n (self-hosted at n8n.atlan.com)
- **LLM routing**: LiteLLM proxy at llmproxy.atlan.dev (Claude Opus for writing, Sonnet for classification, Gemini for fact-checking, Grok for X data + adversarial review)
- **Knowledge layer**: gbrain (PGLite locally, upgradable to Supabase)
- **Delivery**: Email (Readwise Reader) + Slack DM

## Setup

```bash
# 1. Clone
git clone https://github.com/Aayushm24/presidential-briefing.git
cd presidential-briefing

# 2. Environment
cp config/.env.example .env
# Fill in: ANTHROPIC_AUTH_TOKEN, OPENAI_API_KEY, SLACK_BOT_TOKEN

# 3. Initialize gbrain
bun install -g gbrain
gbrain init

# 4. Import n8n workflow
# Import n8n/workflow.json into n8n.atlan.com
```

## Folder structure

```
config/          — sources.csv, council.json, env
skills/          — 7 self-contained skills (intake, filter, brain, briefing, post, review, feedback)
workspace/       — daily artifacts (YYYY-MM-DD directories)
brain/           — gbrain data (gitignored, managed by CLI)
n8n/             — exportable workflow definition
```

Each skill has its own SKILL.md with complete instructions. CLAUDE.md at root is the routing table.

## The compounding effect

Day 1: empty brain. The briefing teaches concepts. The post summarizes news.
Day 30: brain has 100+ pages. The briefing connects today's news to past reading. The post makes connections nobody else makes.
Day 100: brain has 500+ pages. The system writes posts that could only come from someone who has been tracking AI deeply for months.
