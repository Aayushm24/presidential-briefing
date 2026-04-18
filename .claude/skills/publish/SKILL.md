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
- Env: `GMAIL_FROM_ADDRESS`, `GMAIL_APP_PASSWORD`, `READWISE_EMAIL`, `SLACK_BOT_TOKEN` (optional), `SLACK_DM_USER_ID`, `DRY_RUN`, `GITHUB_REPO`

## Outputs

- Commit on `main`: `workspace/YYYY-MM-DD/brief.md` + `workspace/YYYY-MM-DD/posts.md`
- Email to Readwise Reader inbox
- Slack DM to U08G02QDEAG
- Append to `history/published.jsonl`
- `workspace/${TODAY}/.status` = `shipped`

## Process

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

### Step 4: Slack DM via chat.postMessage API

Uses the Slack bot token (`xoxb-...` from the "scout slack bot" credential). The bot must have `chat:write` scope + be able to DM the target user.

```bash
GITHUB_URL="https://github.com/${GITHUB_REPO}/blob/main/workspace/${DATE}/posts.md"

SLACK_TEXT="daily brief ready — ${LEAD_TITLE}
scores: avg ${BEST_SCORE}/15 | verdict: *${VERDICT}* | iterations: ${ITER}

read + pick an option: ${GITHUB_URL}

reply in thread: *1* / *2* / *3* / *edit* / *kill*"

if [ "${DRY_RUN:-0}" == "1" ]; then
  echo "[DRY_RUN] would slack to ${SLACK_DM_USER_ID}: ${SLACK_TEXT}"
elif [ -z "${SLACK_BOT_TOKEN:-}" ]; then
  echo "[publish] SLACK_BOT_TOKEN not set — skipping Slack DM (brief still delivered via email + Git)"
else
  curl -sS -X POST "https://slack.com/api/chat.postMessage" \
    -H "Authorization: Bearer ${SLACK_BOT_TOKEN}" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d "$(jq -n \
      --arg channel "${SLACK_DM_USER_ID}" \
      --arg text "$SLACK_TEXT" \
      '{channel: $channel, text: $text, unfurl_links: false}')" \
    > workspace/${DATE}/.slack-response.json

  # Verify success (non-fatal — log but don't fail pipeline)
  if [ "$(jq -r .ok workspace/${DATE}/.slack-response.json)" != "true" ]; then
    echo "[publish] Slack delivery failed (non-fatal):" >&2
    cat workspace/${DATE}/.slack-response.json >&2
  fi
fi
```

Why chat.postMessage not webhook:
- Uses the existing "scout slack bot" token from n8n (no new webhook to create)
- Slack MCP hits this same endpoint under the hood — so this is functionally identical
- Simpler than MCP in CI (no server to launch, no OAuth dance)

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

If quiet-day, skip the commit + email. Only Slack DM:

```bash
SLACK_TEXT="quiet day in AI. nothing above threshold. accumulating for tomorrow.
${DATE} — top score: ${TOP_SCORE}/10"

if [ -n "${SLACK_BOT_TOKEN:-}" ]; then
  curl -sS -X POST "https://slack.com/api/chat.postMessage" \
    -H "Authorization: Bearer ${SLACK_BOT_TOKEN}" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d "$(jq -n \
      --arg channel "${SLACK_DM_USER_ID}" \
      --arg text "$SLACK_TEXT" \
      '{channel: $channel, text: $text}')"
else
  echo "[publish] SLACK_BOT_TOKEN not set — quiet-day notice not delivered. Brain still ingested for tomorrow."
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
