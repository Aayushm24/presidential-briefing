# Feedback

Capture performance data, edits, and kill decisions. Feed them back into the system.

## Three feedback signals

### 1. Edit capture (triggered by Slack reply)

When Aayush replies to the Slack DM with edited text:

- Diff the draft (linkedin-draft.md) against his version
- Extract patterns:
  - What he shortened (indicates wordiness)
  - What he rewrote (indicates wrong tone or framing)
  - What he deleted (indicates irrelevance)
  - What language he chose over what the system chose
- Append patterns to `skills/post/voice-profile.md` under "## Few-shot examples"
- Write full diff to `workspace/YYYY-MM-DD/edit-diff.md`

### 2. Kill capture (triggered by Slack reply "kill")

When Aayush replies "kill":
- n8n sends follow-up: "Why? boring topic / bad take / bad writing / not today"
- Record to `workspace/YYYY-MM-DD/kill-reason.md`
- If "boring topic": update brain page significance to "low"
- If "bad take": log the conviction that was wrong
- If "bad writing": flag for review council calibration

### 3. Performance capture (automated, 24h + 7d after publish)

When Aayush replies "approve" and publishes:

n8n cron fires 24 hours later:
- Record post URL (Aayush pastes it when approving)
- Capture metrics (manual entry via Slack for now, LinkedIn API later):
  - Impressions
  - Saves
  - Comments (count)
  - Shares
  - Engagement rate (engagement / impressions)
- Write to `workspace/YYYY-MM-DD/performance.json`
- Update brain page with performance data

n8n cron fires 7 days later:
- Capture final metrics + follower delta
- Update performance.json

### 4. Monthly retrospective (1st of each month)

n8n cron fires monthly:
- Read all performance.json from past 30 days
- Read all edit-diff.md files
- Read all kill-reason.md files

Generate analysis (Claude Opus):
```
Given 30 days of LinkedIn post data:
- Which formats performed best? (by engagement rate)
- Which hook patterns performed best?
- Which topics drove the most saves?
- What edit patterns are most common? (what does the system keep getting wrong?)
- What was killed and why?

Write a 200-word summary. Include:
- Top 3 format/topic/hook combinations by performance
- Top 3 recurring edit patterns to fix
- Recommended changes to voice-profile.md and scoring weights
```

Send to Slack DM. Also write to `workspace/monthly-retro-YYYY-MM.md`.

## Output

- `workspace/YYYY-MM-DD/edit-diff.md`
- `workspace/YYYY-MM-DD/kill-reason.md`
- `workspace/YYYY-MM-DD/performance.json`
- `workspace/YYYY-MM-DD/status.json` (approved / killed / edited)
- `workspace/monthly-retro-YYYY-MM.md`
- Updated `skills/post/voice-profile.md` (accumulated edit patterns)
