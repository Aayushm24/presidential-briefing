---
name: daily-brief
description: Orchestrator for the full daily pipeline. Scans sources, scores, clusters, writes brief + 3 posts, runs council, commits + delivers.
---

# /daily-brief — Full pipeline orchestrator

Master recipe. Reads each sub-skill and executes it in sequence. Writes intermediate artifacts to `workspace/YYYY-MM-DD/` so steps are independently testable and failed runs can resume.

---

## Environment

Required environment variables (read from `.env` locally, GitHub secrets in CI):

```
ATLAN_LLM_KEY          # required — LiteLLM virtual key for llmproxy.atlan.dev (all models route through proxy)
SUPABASE_ANON_KEY      # required — brain read via RLS (NOT service key)
N8N_SLACK_WEBHOOK_URL  # optional — Slack Incoming Webhook URL. If empty, Slack is skipped.
READWISE_TOKEN         # required — Readwise Reader API token (from readwise.io/access_token)
DRY_RUN                # optional, when '1' skip Slack/Gmail/commit
TODAY                  # optional, override date for testing (YYYY-MM-DD)
```

Derived:
```
TODAY=${TODAY:-$(date -u +%Y-%m-%d)}
WORKSPACE="workspace/${TODAY}"
```

---

## Process

### Step 0: Initialize workspace

```bash
mkdir -p workspace/${TODAY}
echo "init" > workspace/${TODAY}/.status
echo "1" > workspace/${TODAY}/.iter
```

If `workspace/${TODAY}/.status` already shows `shipped`, abort — today's brief was already delivered.

If `.status` shows a partial state (e.g., `score-ok`), skip already-completed steps and resume. This makes failed runs idempotent.

### Step 1: Scan

Read `.claude/skills/scan/SKILL.md` and follow it. Writes to `workspace/${TODAY}/raw-intake.json`.

**Anti-fabrication gate:** if scan exits non-zero or writes `.status=scan-failed`:
- DO NOT continue with downstream skills
- DO NOT invent news items
- Jump directly to Step 9 (quiet-day path) and deliver `{"type":"nothing_new"}` via Slack
- Exit 0 (quiet day is a valid outcome, not a failure)

Update status: `echo "scan-ok" > workspace/${TODAY}/.status`

### Step 2: Score + select

Read `.claude/skills/score/SKILL.md` and follow it. Writes `workspace/${TODAY}/scored.json` with top 10 stories.

If scored.json has 0 items OR all scores <6 → write quiet-day marker and skip to Step 9. The day's Slack message is:
```
quiet day in AI. nothing above threshold. accumulating for tomorrow.
```

Update status: `echo "score-ok" > workspace/${TODAY}/.status`

### Step 3: Theme detect

Read `.claude/skills/theme-detect/SKILL.md`. Writes `workspace/${TODAY}/themes.json`.

Update status: `echo "theme-ok" > workspace/${TODAY}/.status`

### Step 4: Brain connect

Read `.claude/skills/brain-connect/SKILL.md`. Writes `workspace/${TODAY}/brain.md` + ingests today's stories/themes into Supabase.

Update status: `echo "brain-ok" > workspace/${TODAY}/.status`

### Step 5: Write briefing

Read `.claude/skills/write-briefing/SKILL.md`. Writes `workspace/${TODAY}/brief.md`.

Update status: `echo "brief-ok" > workspace/${TODAY}/.status`

### Step 6: Write 3 posts

Read `.claude/skills/write-posts/SKILL.md`. Writes `workspace/${TODAY}/posts.md`.

Update status: `echo "posts-ok" > workspace/${TODAY}/.status`

### Step 7: Council attack + revise loop

Iteration cap: 2. Check `workspace/${TODAY}/.iter` at start.

Loop:
1. Read `.claude/skills/council/attack/SKILL.md`. Writes `workspace/${TODAY}/council-notes.md`.
2. Parse council scores. If all options score ≥12/15 voice audit AND fact-check passes → break, ship.
3. Otherwise: read `.claude/skills/council/revise/SKILL.md`. Updates `posts.md` in place (backup saved as `posts.md.iter-N.bak`).
4. Increment iter: `echo $(($(cat workspace/${TODAY}/.iter) + 1)) > workspace/${TODAY}/.iter`
5. If iter > 2 → break anyway (force-ship with `[UNREVIEWED]` tag in publish.md).

Update status: `echo "council-ok" > workspace/${TODAY}/.status`

### Step 8: Publish

Read `.claude/skills/publish/SKILL.md`. Commits to GitHub, emails Readwise, posts to Slack.

Update status: `echo "shipped" > workspace/${TODAY}/.status`

Append to `history/published.jsonl`:
```json
{"date":"2026-04-19","status":"shipped","briefing_title":"...","best_option":1,"voice_score":14,"iterations":1,"theme":"...","brain_connections":3}
```

### Step 9: Quiet-day exit (if triggered)

If triggered from Step 2 quiet-day path:
- Slack webhook with the quiet-day message
- No commit, no email
- Append `{"date":"2026-04-19","status":"quiet_day"}` to `history/published.jsonl`
- Exit 0

---

## Error handling

- **Any step fails:** leave `.status` at last-good state. `DRY_RUN=0` exit 1. Actions alerts via failure notification.
- **Timeout (Actions 25-min cap):** `.status` tells us exactly where we stopped. Next manual re-run picks up from there.
- **Grok empty response:** scan writes placeholder item, continues. Score gracefully handles.
- **Supabase unreachable:** brain-connect writes empty `brain.md` with `[NO-BRAIN]` tag. Write-briefing proceeds without accumulated context.
- **Any kill-list violation after 2 iterations:** force-ship tagged `[UNREVIEWED]`. Slack message flags for manual edit before Aayush ships.

---

## Model routing

All LLM calls go through `${LLM_PROXY_BASE_URL}` (= `https://llmproxy.atlan.dev`) using OpenAI-compatible chat completions endpoint.

Per-task models defined in `config/council.json`. Each sub-skill names its task key explicitly. Example curl pattern:

```bash
curl -sS -X POST "${LLM_PROXY_BASE_URL}/v1/chat/completions" \
  -H "Authorization: Bearer ${ATLAN_LLM_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg model "claude-sonnet-4-6" --arg prompt "..." '{model: $model, messages: [{role: "user", content: $prompt}], temperature: 0.2, max_tokens: 4000}')"
```

Grok calls go through `https://llmproxy.atlan.dev/responses` (NOT `api.x.ai` — same key, different endpoint). The proxy passes through the `x_search` tool call to xAI internally and returns the xAI `/responses` format.

Gemini calls: via proxy model `gemini-3.1-pro-preview`.

---

## Dry run

When `DRY_RUN=1`:
- All curl/write/commit/Slack/Gmail steps DO write locally (so outputs are inspectable)
- But: skip `git commit/push`, skip Slack webhook, skip Gmail send
- Print "[DRY_RUN]" prefix on each side-effect step

Useful for local iteration + `tests.yml` CI checks.

---

## Status codes

Written to `workspace/${TODAY}/.status`:
- `init` — step 0 done
- `scan-ok` — step 1 done
- `score-ok` — step 2 done (may also be `quiet-day`)
- `theme-ok` — step 3 done
- `brain-ok` — step 4 done
- `brief-ok` — step 5 done
- `posts-ok` — step 6 done
- `council-ok` — step 7 done
- `shipped` — step 8 done

Dead-man monitor at 07:00 IST checks: `if status != shipped` → re-run `/daily-brief` (which resumes from last status).
