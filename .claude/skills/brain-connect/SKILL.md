---
name: brain-connect
description: Embed today's stories/themes + ingest into Supabase + search for connections to past themes. Output brain.md summary for writers.
---

# /brain-connect — Memory layer

Three responsibilities:
1. **Embed** today's lead story + top secondary stories using `text-embedding-3-small`
2. **Ingest** embeddings + metadata into Supabase `brain_pages` and `brain_themes` tables
3. **Search** for past stories/themes similar to today's — surface them as "accumulated context" for write-briefing and write-posts

Writes `workspace/${TODAY}/brain.md` — a human-readable summary the writing skills read from disk.

---

## Inputs

- `workspace/${TODAY}/scored.json`
- `workspace/${TODAY}/themes.json`
- Env: `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `ATLAN_LLM_KEY`

## Outputs

- Supabase rows inserted into `brain_pages` (one per story) and `brain_themes` (one per theme)
- `workspace/${TODAY}/brain.md`:

```markdown
# Brain connections — 2026-04-19

## Lead story embedding
"The agent knowledge moat is evaporating"
5 related past stories found (threshold 0.5):

### Related past themes
1. 2026-04-10 — "Agent-builder tools are commoditizing" (similarity 0.72)
   Conviction: The open-source agent stack is catching up to proprietary.
2. 2026-04-02 — "Context window isn't the moat" (similarity 0.64)
   Conviction: Memory and retrieval > raw context size for production agents.

### Related past stories
1. 2026-04-05 — "Notion adds agents to pro plan" (similarity 0.68) [lead]
2. 2026-04-01 — "LangGraph hits 1.0 with memory primitives" (similarity 0.61) [secondary]
...

## Brain size
487 pages | 42 themes
Growth this week: +18 pages | +3 themes
```

---

## Process

### Step 1: Embed top stories

Stories to embed: lead + all secondary (from scored.json top_10). Include theme title if pattern-day.

```bash
# Build embedding input: "title + one_line_reason" for each story
EMBED_INPUT=$(jq -r '.top_10[] | .title + " " + .one_line_reason' workspace/${TODAY}/scored.json)

curl -sS -X POST "${LLM_PROXY_BASE_URL}/v1/embeddings" \
  -H "Authorization: Bearer ${ATLAN_LLM_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -Rs --arg model "text-embedding-3-small" \
    '{model: $model, input: split("\n") | map(select(length > 0))}' <<< "$EMBED_INPUT")" \
  > workspace/${TODAY}/.embeddings.json
```

Result: `data[]` array with `.embedding` per input.

### Step 2: Ingest into Supabase

For each story + embedding pair, POST to `brain_pages`:

```bash
INDEX=0
jq -c '.top_10[]' workspace/${TODAY}/scored.json | while read STORY; do
  EMBEDDING=$(jq -c ".data[$INDEX].embedding | tostring" workspace/${TODAY}/.embeddings.json)
  
  SLUG=$(echo "$STORY" | jq -r '.title' | tr '[:upper:]' '[:lower:]' | tr -c '[:alnum:]' '-' | head -c 60)
  TYPE=$([ $INDEX -eq 0 ] && echo "lead" || echo "secondary")
  
  curl -sS -X POST "${SUPABASE_URL}/rest/v1/brain_pages" \
    -H "apikey: ${SUPABASE_ANON_KEY}" \
    -H "Authorization: Bearer ${SUPABASE_ANON_KEY}" \
    -H "Content-Type: application/json" \
    -H "Prefer: return=minimal" \
    -d "$(jq -n \
      --arg slug "$SLUG" \
      --arg title "$(echo "$STORY" | jq -r .title)" \
      --arg url "$(echo "$STORY" | jq -r .url)" \
      --arg reason "$(echo "$STORY" | jq -r .one_line_reason)" \
      --arg date "$TODAY" \
      --arg type "$TYPE" \
      --argjson score "$(echo "$STORY" | jq -r '(.combined_score * 10 | round)')" \
      --arg embedding "$EMBEDDING" \
      '{slug: $slug, title: $title, url: $url, reason: $reason, date: $date, type: $type, score: $score, embedding: $embedding}')" \
    || echo "[brain-ingest] page ingest failed for $SLUG" >&2
  
  INDEX=$((INDEX + 1))
done
```

If today is a pattern day, also ingest the lead theme into `brain_themes`:

```bash
if [ "$(jq -r .briefing_type workspace/${TODAY}/themes.json)" == "pattern" ]; then
  # Use lead story's embedding for the theme (closest proxy)
  LEAD_EMBEDDING=$(jq -c '.data[0].embedding | tostring' workspace/${TODAY}/.embeddings.json)
  
  curl -sS -X POST "${SUPABASE_URL}/rest/v1/brain_themes" \
    -H "apikey: ${SUPABASE_ANON_KEY}" \
    -H "Authorization: Bearer ${SUPABASE_ANON_KEY}" \
    -H "Content-Type: application/json" \
    -H "Prefer: return=minimal" \
    -d "$(jq -n \
      --arg date "$TODAY" \
      --arg title "$(jq -r .lead_theme.theme_title workspace/${TODAY}/themes.json)" \
      --arg conviction "$(jq -r .lead_theme.conviction workspace/${TODAY}/themes.json)" \
      --argjson supporting "$(jq '.lead_theme.supporting_stories' workspace/${TODAY}/themes.json)" \
      --argjson strength "$(jq -r .lead_theme.theme_strength workspace/${TODAY}/themes.json)" \
      --arg embedding "$LEAD_EMBEDDING" \
      '{date: $date, theme_title: $title, conviction: $conviction, supporting_stories: $supporting, theme_strength: $strength, embedding: $embedding}')" \
    || echo "[brain-ingest] theme ingest failed" >&2
fi
```

### Step 3: Search for past connections

Use Supabase RPC `search_brain` (cosine similarity on embedding):

```bash
QUERY_EMBEDDING=$(jq -c '.data[0].embedding | tostring' workspace/${TODAY}/.embeddings.json)

curl -sS -X POST "${SUPABASE_URL}/rest/v1/rpc/search_brain" \
  -H "apikey: ${SUPABASE_ANON_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_ANON_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg q "$QUERY_EMBEDDING" --arg excl "$TODAY" \
    '{query_embedding: $q, match_threshold: 0.5, match_count: 5, exclude_date: $excl}')" \
  > workspace/${TODAY}/.story-connections.json
```

Also pull recent themes from `brain_themes`:

```bash
curl -sS -X GET "${SUPABASE_URL}/rest/v1/brain_themes?select=theme_title,date,conviction,supporting_stories&order=date.desc&limit=10" \
  -H "apikey: ${SUPABASE_ANON_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_ANON_KEY}" \
  > workspace/${TODAY}/.recent-themes.json
```

Keyword-match today's lead title + theme against past theme titles. Surface top 3 matching themes.

### Step 4: Get brain size

```bash
TOTAL_PAGES=$(curl -sS -I -X GET "${SUPABASE_URL}/rest/v1/brain_pages?select=id" \
  -H "apikey: ${SUPABASE_ANON_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_ANON_KEY}" \
  -H "Prefer: count=exact" | grep -i 'content-range' | awk -F'/' '{print $2}' | tr -d '\r')
```

Same for `brain_themes`.

### Step 5: Write brain.md

Format output per the Outputs spec above. Include:
- Lead story title
- Top 3 past themes (similarity + conviction)
- Top 5 past stories (similarity, date, type)
- Brain size stats (total pages, themes, growth this week)

If Supabase was unreachable (connection failure):
- Write `brain.md` with single line: `[NO-BRAIN] Supabase unreachable. Proceeding without accumulated context.`
- Log error to `.brain-errors.log`
- Continue — write-briefing gracefully handles empty brain

---

## Kill list

- NEVER use `SUPABASE_SERVICE_KEY` in this skill. Daily pipeline is read/write via ANON_KEY + RLS. Service key lives ONLY in weekly-feedback.
- NEVER ingest full article text — only title + one_line_reason. Full articles are for writing, not memory.
- NEVER fail the pipeline on Supabase errors. Graceful degradation to `[NO-BRAIN]` mode.
- NEVER embed items whose source isn't in `config/sources.csv`.
