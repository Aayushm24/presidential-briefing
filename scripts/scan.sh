#!/usr/bin/env bash
# Deterministic intake: RSS + Grok X search + merge into workspace/$TODAY/raw-intake.json.
# No LLM reasoning needed. Called from the intake job before any Claude Code step.
#
# Required env:
#   TODAY               YYYY-MM-DD (override) — default: today in Asia/Kolkata
#   ATLAN_LLM_KEY       LiteLLM virtual key for proxy (same for Grok + Claude via proxy)
#   LLM_PROXY_BASE_URL  https://llmproxy.atlan.dev (default)
#
# Writes:
#   workspace/$TODAY/raw-intake.json
#   workspace/$TODAY/.rss-stats.log
#   workspace/$TODAY/.grok-raw.json
#   workspace/$TODAY/.status  (scan-ok or scan-failed)
#
# Exit 0 on success. Exit 1 if fewer than 3 items collected (triggers quiet-day).

set -euo pipefail

TODAY="${TODAY:-$(TZ=Asia/Kolkata date +%Y-%m-%d)}"
WS="workspace/${TODAY}"
mkdir -p "$WS"

LLM_PROXY_BASE_URL="${LLM_PROXY_BASE_URL:-https://llmproxy.atlan.dev}"

echo "[scan] TODAY=$TODAY" >&2

# =============================================================
# STEP 1: RSS via parse_rss.py (all 44 feeds, single invocation)
# =============================================================
echo "[scan] running parse_rss.py --csv config/sources.csv" >&2
python3 scripts/parse_rss.py --csv config/sources.csv \
  > "$WS/.rss-items.jsonl" \
  2> "$WS/.rss-stats.log" || echo "[scan] parse_rss exited non-zero, continuing" >&2

RSS_COUNT=$(wc -l < "$WS/.rss-items.jsonl" | tr -d ' ')
echo "[scan] RSS items: $RSS_COUNT" >&2

# =============================================================
# STEP 2: Grok X search via proxy /responses
# =============================================================
GROK_PROMPT="Today's date = ${TODAY}. Search X/Twitter for posts from the last 24 hours by these X user handles: @karpathy, @rasbt, @natolambert, @simonw, @emollick, @garrytan, @swyx, @ttunguz. For each substantive post about AI technology, research, or industry, return a JSON array: [{author, date_of_post, text, full_post, url, key_claims}]. Skip personal/promotional content. Return ONLY the JSON array and nothing else."

echo "[scan] calling Grok via ${LLM_PROXY_BASE_URL}/responses" >&2
curl -sS --max-time 120 -X POST "${LLM_PROXY_BASE_URL}/responses" \
  -H "Authorization: Bearer ${ATLAN_LLM_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg p "$GROK_PROMPT" '{
    model: "grok-4",
    input: [{role:"user", content:$p}],
    tools: [{type:"x_search"}],
    temperature: 0.2
  }')" > "$WS/.grok-raw.json" || {
    echo "[scan] Grok call failed (non-fatal, RSS-only fallback)" >&2
  }

# Parse Grok — xAI /responses format: output[] array, find item with type=message, extract content[0].text
GROK_TEXT=$(jq -r '.output[]? | select(.type=="message") | .content[0].text // empty' "$WS/.grok-raw.json" 2>/dev/null || echo "")

# Try to extract the JSON array from Grok's text response
GROK_POSTS="[]"
if [ -n "$GROK_TEXT" ]; then
  # Pull the first [...] JSON array out of the text
  EXTRACTED=$(echo "$GROK_TEXT" | python3 -c "
import sys, re, json
text = sys.stdin.read()
m = re.search(r'\[[\s\S]*\]', text)
if not m:
    print('[]')
    sys.exit(0)
try:
    parsed = json.loads(m.group(0))
    print(json.dumps(parsed))
except Exception:
    print('[]')
" 2>/dev/null || echo "[]")
  GROK_POSTS="$EXTRACTED"
fi

GROK_COUNT=$(echo "$GROK_POSTS" | jq 'length' 2>/dev/null || echo 0)
echo "[scan] Grok X posts: $GROK_COUNT" >&2

# =============================================================
# STEP 3: Combine RSS + Grok into raw-intake.json
# =============================================================
# Convert Grok posts to the common item shape
GROK_ITEMS=$(echo "$GROK_POSTS" | jq -c '[.[] | {
  title: (.key_claims // (.text // "")[:100]),
  url: (.url // ""),
  summary: (.full_post // .text // ""),
  source: ("x/" + ((.author // "unknown") | gsub("^@"; ""))),
  type: "x_post",
  date_posted: (.date_of_post // "")
}]' 2>/dev/null || echo "[]")

# If Grok returned nothing, add a placeholder so downstream doesn't choke on empty
if [ "$GROK_COUNT" -eq 0 ]; then
  GROK_ITEMS='[{"title":"[grok-empty]","url":"","summary":"","source":"x/unknown","type":"x_empty"}]'
fi

# Convert RSS JSONL to array
RSS_ITEMS=$(cat "$WS/.rss-items.jsonl" 2>/dev/null | jq -s '.' 2>/dev/null || echo "[]")

# Stats from RSS stderr log
RSS_TOTAL=$(grep -oE 'feeds_total=[0-9]+' "$WS/.rss-stats.log" 2>/dev/null | head -1 | sed 's/feeds_total=//' || echo 0)
RSS_PROCESSED=$(grep -oE 'feeds_processed=[0-9]+' "$WS/.rss-stats.log" 2>/dev/null | head -1 | sed 's/feeds_processed=//' || echo 0)
RSS_FAILED=$(grep -oE 'feeds_failed=[0-9]+' "$WS/.rss-stats.log" 2>/dev/null | head -1 | sed 's/feeds_failed=//' || echo 0)

jq -n \
  --arg date "$TODAY" \
  --argjson rss "$RSS_ITEMS" \
  --argjson grok "$GROK_ITEMS" \
  --argjson rss_total "$RSS_TOTAL" \
  --argjson rss_processed "$RSS_PROCESSED" \
  --argjson rss_failed "$RSS_FAILED" \
  '{
    date: $date,
    items: ($rss + $grok),
    stats: {
      rss_feeds_total: $rss_total,
      rss_feeds_processed: $rss_processed,
      rss_feeds_failed: $rss_failed,
      rss_items: ($rss | length),
      x_posts: ($grok | map(select(.type != "x_empty")) | length),
      total: (($rss + $grok) | length)
    }
  }' > "$WS/raw-intake.json"

ITEM_COUNT=$(jq '.items | length' "$WS/raw-intake.json")
echo "[scan] combined items: $ITEM_COUNT" >&2

# =============================================================
# STEP 4: Hard gate — fail rather than fabricate
# =============================================================
# Need at least 3 REAL items (excluding x_empty placeholder)
REAL_COUNT=$(jq '[.items[] | select(.type != "x_empty")] | length' "$WS/raw-intake.json")
echo "[scan] real items (excl x_empty): $REAL_COUNT" >&2

if [ "$REAL_COUNT" -lt 3 ]; then
  echo "[scan] FAILED: only $REAL_COUNT real items — quiet-day signal" >&2
  echo "scan-failed" > "$WS/.status"
  # Don't hard exit — let the orchestrator route to quiet-day
  # But signal via status file so intake job can classify
  exit 0
fi

echo "scan-ok" > "$WS/.status"
echo "[scan] SUCCESS: $ITEM_COUNT items ($RSS_COUNT RSS + $GROK_COUNT X posts)"
