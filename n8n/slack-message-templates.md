# slack-message-templates

n8n workflow: daily-brief → Slack (inbound from presidential-briefing CI).

This doc is the contract between the pipeline and n8n. When the pipeline POSTs one of these shapes to `N8N_SLACK_WEBHOOK_URL`, the n8n workflow should render it as a Slack DM to U08G02QDEAG.

## Routing

All payloads arrive at a single webhook. Discriminate on `type`:

```
switch (type):
  "daily_brief"    → render daily brief + 3 post options + scan health
  "nothing_new"    → render quiet-day message
  "scan_degraded"  → render early warning (fires during intake, ~5 min into run)
  "weekly_feedback" → render Sunday conviction candidates pointer
```

---

## Type 1: `daily_brief` (existing, now with scan_health block)

Fires from the `ship` job after the brief is committed + Readwise delivered.

Payload:
```json
{
  "type": "daily_brief",
  "title": "Cerebras validates the AI chip wave with a $10 billion OpenAI deal before IPO",
  "briefing_url": "https://github.com/.../workspace/2026-04-19/brief.md",
  "posts_url":    "https://github.com/.../workspace/2026-04-19/posts.md",
  "posts": ["[option 1 post text]", "[option 2 post text]", "[option 3 post text]"],
  "scan_health": {
    "status": "scan-ok | scan-degraded | unknown",
    "rss_items": 8,
    "rss_feeds_ok": 36,
    "rss_feeds_total": 36,
    "rss_feeds_failed": 0,
    "sitemap_items": 2,
    "sitemap_sources_ok": 4,
    "sitemap_sources_total": 4,
    "x_posts": 14,
    "x_dropped_stale": 6,
    "degraded_reasons": []
  }
}
```

Render (Slack Block Kit):
```
*{title}*

📰 <{briefing_url}|Full brief on GitHub>
✍️ <{posts_url}|3 LinkedIn post options>

──────────────
*Option 1:*
{posts[0]}

*Option 2:*
{posts[1]}

*Option 3:*
{posts[2]}

──────────────
_Scan: {scan_health.rss_items} RSS + {scan_health.sitemap_items} newsletters + {scan_health.x_posts} X posts · {scan_health.rss_feeds_ok}/{scan_health.rss_feeds_total} RSS feeds ok_
```

If `scan_health.status == "scan-degraded"`, prepend a warning banner:
```
⚠️ *Brief shipped on degraded scan.* Reasons: {scan_health.degraded_reasons | join(", ")}
```

Reply `1`, `2`, `3` to pick; any longer text = edited version; `kill` = skip. (Existing behavior, handled by daily-brief-replies workflow.)

---

## Type 2: `nothing_new` (existing)

Fires on quiet days (`<3` total items).

Payload:
```json
{ "type": "nothing_new" }
```

Render:
```
🤫 Quiet day across 41 sources. No brief today.
```

---

## Type 3: `scan_degraded` (NEW — early warning)

Fires from the `intake` job right after classify, ~5 min into the run. This gives you heads-up while the write + ship jobs are still running (~15 more min). Brief will still ship unless another gate trips.

Payload:
```json
{
  "type": "scan_degraded",
  "date": "2026-04-19",
  "message": "Scan degraded — brief will still ship",
  "rss_summary": "36/36 feeds ok",
  "x_summary": "0 X posts (24h)",
  "reasons": ["x_posts=0 (grok_status=ok)"],
  "scan_summary_url": "https://github.com/.../workspace/2026-04-19/scan-summary.json"
}
```

Render:
```
⚠️ *Scan degraded today ({date})*
{message}

· RSS: {rss_summary}
· X: {x_summary}
· Reasons: {reasons | join(", ")}

<{scan_summary_url}|View full scan-summary.json>
```

No reply handling needed. Pure alert.

---

## Type 4: `weekly_feedback` (NEW — Sunday)

Fires Sundays at 7 AM IST from the `weekly-feedback.yml` workflow. Links to conviction candidates for Aayush to review + manually edit conviction.md.

Payload:
```json
{
  "type": "weekly_feedback",
  "date": "2026-04-26",
  "candidates_url":  "https://github.com/.../workspace/2026-04-26/conviction-candidates.md",
  "conviction_url":  "https://github.com/.../config/conviction.md",
  "message": "Sunday review: conviction candidates ready. Edit conviction.md if you want to apply any."
}
```

Render:
```
🧭 *Sunday conviction review — week ending {date}*
{message}

📋 <{candidates_url}|Conviction candidates for this week>
✏️ <{conviction_url}|Edit conviction.md>
```

No reply handling (human loops through GitHub, not Slack).

---

## Implementation notes for n8n

1. One webhook endpoint covers all 4 types. Route via a `Switch` node on `{{$json.type}}`.
2. Use Slack's `chat.postMessage` with Block Kit for richer rendering. Plain text fallback in the `text` field for notifications.
3. All payloads include a URL pointing to the canonical GitHub artifact. If n8n wants to show inline content, it can HTTP GET the URL. Not required.
4. For `daily_brief`, the existing workflow (`daily-brief-replies.md`) handles reply parsing. Only the inbound rendering needs update for the new `scan_health` block.
5. `scan_degraded` and `weekly_feedback` are one-way pings — no reply handling.

## Testing

Manually POST each shape to the webhook to verify rendering:

```bash
curl -X POST "$N8N_SLACK_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"type":"scan_degraded","date":"2026-04-19","message":"test","rss_summary":"36/36 ok","x_summary":"0 posts","reasons":["x_posts=0"],"scan_summary_url":"https://example.com"}'
```
