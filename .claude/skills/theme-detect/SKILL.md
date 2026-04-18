---
name: theme-detect
description: Cluster top 10 stories into themes. Return lead theme + standalone stories. Reject themes used >2x in past 4 weeks.
---

# /theme-detect — Pattern clustering

Reads top 10 stories from `/score`. Groups them into 2+ story themes. Outputs `workspace/${TODAY}/themes.json` with lead theme, supporting stories, and standalone items.

Also enforces **theme freshness**: rejects any theme title that has been used more than 2 times in the last 4 weeks (tracked in `history/themes.jsonl`).

## Inputs

- `workspace/${TODAY}/scored.json`
- `history/themes.jsonl` (for dedup check)
- `config/council.json` (task: `theme_detection` → model: `claude-sonnet-4-6`)

## Outputs

`workspace/${TODAY}/themes.json`:
```json
{
  "date": "2026-04-19",
  "briefing_type": "pattern",
  "lead_theme": {
    "theme_title": "Agent knowledge is going public in 24 hours",
    "conviction": "Frameworks and case studies for production agents are now freely available. The remaining differentiator is iteration speed.",
    "supporting_stories": ["Lenny's agent framework", "Notion 5 rebuilds", "RLHF free course"],
    "theme_strength": 24
  },
  "standalone_stories": ["OpenAI voice mode update", "Anthropic prompt caching"],
  "all_themes": [...]
}
```

If no theme has 2+ supporting stories:
```json
{
  "date": "2026-04-19",
  "briefing_type": "single_story",
  "lead_theme": null,
  "standalone_stories": [...top 5 by score],
  "all_themes": []
}
```

## Process

### Step 1: Call Sonnet via proxy

Prompt (ported from n8n `Find Themes`):

```
You are a pattern recognition system. You received the top 10 AI stories of the day with scores.

Your job: find THEMES. Which stories are about the same underlying shift? Group them.

For each theme:
- theme_title: one sentence describing the pattern (not any individual story)
- conviction: a specific claim about what this pattern means for builders
- supporting_stories: array of story titles that support this theme
- theme_strength: count of supporting stories multiplied by their average score

Rules:
- A theme needs at least 2 supporting stories to count
- Stories can only belong to one theme
- If no theme has 2+ stories, return empty themes array
- Look for: business model shifts, technology convergence, market signals, competitive moves pointing the same direction

Return JSON only, no markdown:
{
  "themes": [{"theme_title": "", "conviction": "", "supporting_stories": [], "theme_strength": 0}],
  "lead_theme_index": 0,
  "standalone_stories": ["titles that don't fit any theme"]
}

Scored stories:
<stories>
${SCORED_JSON}
</stories>
```

Call:

```bash
curl -sS -X POST "${LLM_PROXY_BASE_URL}/v1/chat/completions" \
  -H "Authorization: Bearer ${ATLAN_LLM_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg model "claude-sonnet-4-6" --arg prompt "$PROMPT" \
    '{model: $model, messages: [{role: "user", content: $prompt}], temperature: 0.3, max_tokens: 4000}')"
```

### Step 2: Parse + classify briefing type

Extract JSON from response. Validate structure.

- If `themes[].length > 0` AND lead theme has ≥2 supporting stories → `briefing_type = "pattern"`
- Else if top story has `combined_score ≥ 8` → `briefing_type = "single_story"`
- Else → `briefing_type = "quiet_day"` (but /score should have caught this)

### Step 3: Theme freshness check (dedup)

For each theme in output, check against `history/themes.jsonl`:

```bash
# Count occurrences of theme titles with >70% similarity in last 28 days
RECENT_THEMES=$(tail -n 100 history/themes.jsonl | \
  jq -r --arg d "$(date -u -d '28 days ago' +%Y-%m-%d)" \
  'select(.date >= $d) | .theme_title')

# For each new theme, compute title similarity. If >70% match appears >= 2 times, reject.
```

If lead theme is rejected for dedup, promote next strongest theme. If all themes rejected, fall back to `single_story` using top-scored item.

### Step 4: Write output

```bash
# themes.json — full theme data
cat > workspace/${TODAY}/themes.json <<EOF
{
  "date": "${TODAY}",
  "briefing_type": "${TYPE}",
  "lead_theme": ${LEAD_THEME_JSON},
  "supporting_stories": ${SUPPORTING_JSON},
  "standalone_stories": ${STANDALONE_JSON},
  "all_themes": ${ALL_THEMES_JSON},
  "dedup_rejected": ${DEDUP_REJECTED_JSON}
}
EOF

# Append lead theme to history
if [ "${TYPE}" == "pattern" ]; then
  cat >> history/themes.jsonl <<EOF
{"date":"${TODAY}","theme_title":"${LEAD_TITLE}","strength":${STRENGTH},"conviction":"${CONVICTION}"}
EOF
fi
```

---

## Kill list

- NEVER merge stories from different themes into one. Stories belong to ONE theme.
- NEVER invent a theme to fit stories that don't cluster. "single_story" is a valid outcome.
- NEVER use a theme title that's been used >2 times in the last 28 days. Dedup is enforced.
- NEVER base theme_strength on story count alone — factor in average score.
