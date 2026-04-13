# Presidential Briefing System

Daily AI knowledge system. Scrapes 40 sources, synthesizes into a presidential briefing delivered to Readwise Reader, generates a LinkedIn post delivered to Slack.

## Routing

| Task | Read this |
|------|-----------|
| Run full pipeline | This file, then each skill in order below |
| Intake (scrape sources) | `skills/intake/SKILL.md` |
| Filter (score significance) | `skills/filter/SKILL.md` |
| Brain (ingest + connect) | `skills/brain/SKILL.md` |
| Write briefing | `skills/briefing/SKILL.md` |
| Write LinkedIn post | `skills/post/SKILL.md` |
| Review council | `skills/review/SKILL.md` |
| Process feedback | `skills/feedback/SKILL.md` |

## Config

- Sources: `config/sources.csv`
- LLM council routing: `config/council.json`
- Kill list: `skills/post/kill-list.md`
- Voice profile: `skills/post/voice-profile.md`

## Daily workspace

All artifacts for a given day: `workspace/YYYY-MM-DD/`

## Pipeline order

```
intake → filter → brain → briefing → review(briefing) → post → review(post) → deliver
```

## Infrastructure

- n8n: n8n.atlan.com (self-hosted)
- LLM proxy: llmproxy.atlan.dev (LiteLLM, routes to all models)
- Brain: gbrain with PGLite (local, upgradable to Supabase)
- Delivery: Email to aayushm24@library.readwise.io (briefing) + Slack DM to U08G02QDEAG (LinkedIn post)
