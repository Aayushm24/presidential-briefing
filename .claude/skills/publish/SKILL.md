---
name: publish
description: Commit brief + posts to GitHub, email briefing to Readwise, Slack DM the 3 posts. Append to history/published.jsonl.
---

# /publish — Delivery

Final step. Commits workspace to GitHub (via path-allowlisted add+commit+push), emails brief to Readwise Reader, Slack webhook-DMs the 3 posts with a pick prompt. Writes final status `shipped` and appends to `history/published.jsonl`.

**Security:** All git operations strictly path-allowlisted (CLAUDE.md + `.claude/settings.json`). Attempts to commit outside allowed paths are rejected by the workflow's post-step check.

## Inputs

- `workspace/${TODAY}/brief.md`
- `workspace/${TODAY}/posts.md`
- `workspace/${TODAY}/.council-verdict.json`
- Env: `GMAIL_FROM_ADDRESS`, `GMAIL_APP_PASSWORD`, `READWISE_EMAIL`, `N8N_SLACK_WEBHOOK_URL` (optional), `DRY_RUN`, `GITHUB_REPO`

## Outputs

- Commit on `main`: `workspace/YYYY-MM-DD/brief.md` + `workspace/YYYY-MM-DD/posts.md`
- Email to Readwise Reader inbox
- Slack DM to U08G02QDEAG
- Append to `history/published.jsonl`
- `workspace/${TODAY}/.status` = `shipped`

## Process

### Step 0: Pre-publish hard-fail gate (MUST run first)

After /revise has run, final brief + posts MUST pass deterministic regex checks. No LLM interpretation — if anything dirty remains, the pipeline refuses to publish.

```bash
# Run the deterministic cleaner one more time as belt-and-braces (idempotent)
python3 scripts/clean_text.py workspace/${TODAY}/brief.md workspace/${TODAY}/posts.md 2>&1 || true

# Hard gate — must pass BOTH
./tests/kill-list-regex.sh workspace/${TODAY}/brief.md || {
  echo "[publish] REJECTED: brief.md has kill-list violations after revise+clean." >&2
  echo "rejected-kill-list" > workspace/${TODAY}/.status
  exit 1
}

./tests/kill-list-regex.sh workspace/${TODAY}/posts.md || {
  echo "[publish] REJECTED: posts.md has kill-list violations after revise+clean." >&2
  echo "rejected-kill-list" > workspace/${TODAY}/.status
  exit 1
}

# Golden format check — brief must have all required sections
./tests/golden-format.sh workspace/${TODAY}/brief.md || {
  echo "[publish] REJECTED: brief.md failed golden-format (missing sections or structure)." >&2
  echo "rejected-format" > workspace/${TODAY}/.status
  exit 1
}

echo "[publish] quality gates passed — proceeding to delivery"
```

If any gate fails, the pipeline aborts BEFORE any commit / email / Slack delivery. Upload the workspace as an artifact so the user can inspect what broke.

### Step 1: Build delivery payload

```bash
DATE=${TODAY}
LEAD_TITLE=$(head -1 workspace/${DATE}/brief.md | sed 's/^# //')
BEST_OPTION=$(jq -r '.best_option' workspace/${DATE}/.council-verdict.json)
BEST_SCORE=$(jq -r '.best_voice_score' workspace/${DATE}/.council-verdict.json)
VERDICT=$(jq -r '.verdict' workspace/${DATE}/.council-verdict.json)
ITER=$(cat workspace/${DATE}/.iter)

# If verdict was [UNREVIEWED], prepend the tag
if [ "$VERDICT" == "UNREVIEWED" ]; then
  sed -i '1i\\n**[UNREVIEWED — council hit 2-iteration cap, manual review recommended]**\n' workspace/${DATE}/posts.md
fi
```

### Step 2: Commit to GitHub

```bash
# Path allowlist check (defense in depth — workflow also enforces)
DIFF_FILES=$(git diff --name-only)
for FILE in $DIFF_FILES; do
  case "$FILE" in
    workspace/*) ;;
    history/*) ;;
    config/conviction.md) ;;
    .claude/skills/write-posts/references/voice.md) ;;
    .claude/skills/write-posts/references/hooks.md) ;;
    *)
      echo "[publish] REJECTED: attempted to commit outside allowlist: $FILE" >&2
      exit 1
      ;;
  esac
done

if [ "${DRY_RUN:-0}" != "1" ]; then
  git add workspace/${DATE}/brief.md workspace/${DATE}/posts.md
  git add history/published.jsonl 2>/dev/null || true
  git commit -m "daily brief: ${DATE} — ${LEAD_TITLE}"
  git push origin main
else
  echo "[DRY_RUN] would commit and push: workspace/${DATE}/brief.md, workspace/${DATE}/posts.md"
fi
```

### Step 3: Email brief to Readwise

The Readwise Reader inbox accepts emails at `${READWISE_EMAIL}`. Subject becomes the document title. Plain text body is the article.

```bash
SUBJECT="PDB — ${DATE}: ${LEAD_TITLE:0:60}"
BODY=$(cat workspace/${DATE}/brief.md)

if [ "${DRY_RUN:-0}" != "1" ]; then
  # Uses Gmail SMTP + App Password (simpler than OAuth for a daily cron)
  python3 scripts/send_gmail.py "${READWISE_EMAIL}" "${SUBJECT}" "${BODY}"
else
  echo "[DRY_RUN] would email to ${READWISE_EMAIL}: ${SUBJECT}"
fi
```

See `scripts/send_gmail.py` — uses `GMAIL_APP_PASSWORD` + `GMAIL_FROM_ADDRESS`.

### Step 4: Slack delivery via n8n proxy webhook

Uses `N8N_SLACK_WEBHOOK_URL` — an n8n webhook at `https://atlanhq.app.n8n.cloud/webhook/presidential-briefing-slack` which:
- Accepts structured JSON payload
- Uses n8n's stored "scout slack bot" credential to DM `U08G02QDEAG`
- Keeps the Slack bot token inside n8n (one place to rotate)

**Payload contract:**
```json
{
  "type": "daily_brief",
  "briefing_url": "https://github.com/Aayushm24/presidential-briefing/blob/main/workspace/2026-04-19/posts.md",
  "posts": ["post 1 body text", "post 2 body text", "post 3 body text"]
}
```

For quiet days use `{"type":"nothing_new"}` (see Step 6).

```bash
GITHUB_URL="https://github.com/${GITHUB_REPO}/blob/main/workspace/${DATE}/posts.md"

# Build posts array from posts.json (structured output from /write-posts)
POSTS_JSON=$(jq -c '[.options[] | .post]' workspace/${DATE}/posts.json)

PAYLOAD=$(jq -n \
  --arg url "$GITHUB_URL" \
  --argjson posts "$POSTS_JSON" \
  '{type: "daily_brief", briefing_url: $url, posts: $posts}')

if [ "${DRY_RUN:-0}" == "1" ]; then
  echo "[DRY_RUN] would POST to n8n webhook:"
  echo "$PAYLOAD" | jq .
elif [ -z "${N8N_SLACK_WEBHOOK_URL:-}" ]; then
  echo "[publish] N8N_SLACK_WEBHOOK_URL not set — skipping Slack (brief still delivered via email + Git)"
else
  HTTP_CODE=$(curl -sS -o /tmp/slack-resp.txt -w "%{http_code}" \
    -X POST "${N8N_SLACK_WEBHOOK_URL}" \
    -H "Content-Type: application/json" \
    -d "$PAYLOAD")

  if [ "$HTTP_CODE" != "200" ]; then
    echo "[publish] n8n webhook returned HTTP $HTTP_CODE (non-fatal):" >&2
    cat /tmp/slack-resp.txt >&2
  fi
fi
```

Why n8n webhook proxy not direct Slack API:
- No Slack bot token in GitHub — token lives in n8n, one place to rotate
- n8n already has "scout slack bot" credential working from the old pipeline
- Structured payload lets n8n format the Slack message (emojis, blocks, etc.) centrally
- Verified working via `verify-secrets.yml` smoke test (HTTP 200, DM delivered)

### Step 5: Append to history

```bash
jq -n \
  --arg date "$DATE" \
  --arg lead_title "$LEAD_TITLE" \
  --arg best_option "$BEST_OPTION" \
  --arg voice_score "$BEST_SCORE" \
  --arg verdict "$VERDICT" \
  --arg iterations "$ITER" \
  --arg theme "$(jq -r '.lead_theme.theme_title // "single_story"' workspace/${DATE}/themes.json)" \
  --arg brain_connections "$(grep -c '^[0-9]\.' workspace/${DATE}/brain.md || echo 0)" \
  '{date: $date, lead_title: $lead_title, best_option: ($best_option | tonumber), voice_score: ($voice_score | tonumber), verdict: $verdict, iterations: ($iterations | tonumber), theme: $theme, brain_connections: ($brain_connections | tonumber), status: "shipped"}' \
  >> history/published.jsonl

echo "shipped" > workspace/${DATE}/.status
```

### Step 6: Quiet-day path (called from orchestrator Step 9)

Skip the commit + email. Send `{"type":"nothing_new"}` — n8n formats the quiet-day DM.

```bash
if [ -n "${N8N_SLACK_WEBHOOK_URL:-}" ] && [ "${DRY_RUN:-0}" != "1" ]; then
  curl -sS -X POST "${N8N_SLACK_WEBHOOK_URL}" \
    -H "Content-Type: application/json" \
    -d '{"type":"nothing_new"}'
elif [ "${DRY_RUN:-0}" == "1" ]; then
  echo '[DRY_RUN] would POST {"type":"nothing_new"} to n8n webhook'
else
  echo "[publish] N8N_SLACK_WEBHOOK_URL not set — quiet-day notice not delivered. Brain still ingested for tomorrow."
fi

echo "quiet_day" > workspace/${DATE}/.status

jq -n --arg date "$DATE" '{date: $date, status: "quiet_day"}' \
  >> history/published.jsonl
```

---

## Kill list

- NEVER commit files outside the allowlisted paths (workspace/, history/, config/conviction.md, write-posts references)
- NEVER push to any branch other than `main`
- NEVER send Slack/Gmail in DRY_RUN mode
- NEVER skip the path-allowlist check — it's the last line of defense against prompt-injection exfiltration
- NEVER retry a failed commit more than once — failed twice = exit with error, alert via Slack
- NEVER omit the `[UNREVIEWED]` tag when council force-shipped after iter 2
