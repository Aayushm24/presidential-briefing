#!/usr/bin/env bash
# Deterministic intake: RSS + Grok X search + merge into workspace/$TODAY/raw-intake.json.
# No LLM reasoning needed. Called from the intake job before any Claude Code step.
#
# Required env:
#   TODAY               YYYY-MM-DD (override) — default: today in Asia/Kolkata
#   ATLAN_LLM_KEY       LiteLLM virtual key for proxy (same for Grok + Claude via proxy)
#   LLM_PROXY_BASE_URL  https://llmproxy.atlan.dev (default)
#
# Writes (committed every run so main is the source of truth on scan health):
#   workspace/$TODAY/raw-intake.json      (full intake — what downstream reads)
#   workspace/$TODAY/scan-summary.json    (per-feed errors + stats — the dashboard)
#   workspace/$TODAY/.status              (scan-ok | scan-degraded | scan-quiet)
#
# Exit codes:
#   0  Success OR degraded OR quiet (orchestrator routes on .status)
#   1  Unrecoverable failure (missing env, parse_rss crash, etc.)
#
# 24h discipline: both RSS and Grok X posts post-filtered to the last 24 hours
# from NOW. Anything older is dropped — this pipeline runs daily, yesterday's
# content is already yesterday's brief.

set -euo pipefail

TODAY="${TODAY:-$(TZ=Asia/Kolkata date +%Y-%m-%d)}"
WS="workspace/${TODAY}"
mkdir -p "$WS"

LLM_PROXY_BASE_URL="${LLM_PROXY_BASE_URL:-https://llmproxy.atlan.dev}"

echo "[scan] TODAY=$TODAY" >&2

# =============================================================
# STEP 1: RSS via parse_rss.py — with structured stats JSON
# =============================================================
RSS_STATS="$WS/.rss-stats.json"
echo "[scan] running parse_rss.py --csv config/sources.csv" >&2
# parse_rss.py exits 2 if feedparser missing. Fail loud in that case.
# stdout = JSON items, stderr = human log. Never collapse them.
if ! python3 scripts/parse_rss.py --csv config/sources.csv --stats-json "$RSS_STATS" \
  > "$WS/.rss-items.jsonl" 2> "$WS/.rss-stderr.log"; then
  echo "::error::parse_rss.py failed — RSS unavailable. Check feedparser install." >&2
  cat "$WS/.rss-stderr.log" >&2 || true
  echo "scan-failed" > "$WS/.status"
  exit 1
fi
# Echo parse_rss stderr to the job log for visibility
cat "$WS/.rss-stderr.log" >&2 || true

RSS_COUNT=$(wc -l < "$WS/.rss-items.jsonl" | tr -d ' ')
FEEDS_FAILED=$(jq '.feeds_failed' "$RSS_STATS")
FEEDS_TOTAL=$(jq '.feeds_total' "$RSS_STATS")
echo "[scan] RSS: $RSS_COUNT items from $(jq '.feeds_processed' "$RSS_STATS")/$FEEDS_TOTAL feeds ($FEEDS_FAILED failed)" >&2

# =============================================================
# STEP 1b: Sitemap-scraped sources (CF-blocked newsletters)
# =============================================================
SITEMAP_STATS="$WS/.sitemap-stats.json"
SITEMAP_ITEMS_FILE="$WS/.sitemap-items.jsonl"
echo "[scan] running parse_sitemap_feed.py for sitemap sources" >&2
if ! python3 scripts/parse_sitemap_feed.py --csv config/sources.csv --stats-json "$SITEMAP_STATS" \
  > "$SITEMAP_ITEMS_FILE" 2> "$WS/.sitemap-stderr.log"; then
  echo "::warning::parse_sitemap_feed.py failed — continuing without sitemap sources" >&2
  echo "[]" > "$SITEMAP_STATS".fallback
  : > "$SITEMAP_ITEMS_FILE"
fi
cat "$WS/.sitemap-stderr.log" >&2 || true
SITEMAP_COUNT=$(wc -l < "$SITEMAP_ITEMS_FILE" | tr -d ' ')
SITEMAP_SOURCES_OK=$(jq '.sources_ok // 0' "$SITEMAP_STATS" 2>/dev/null || echo 0)
SITEMAP_SOURCES_TOTAL=$(jq '.sources_total // 0' "$SITEMAP_STATS" 2>/dev/null || echo 0)
echo "[scan] Sitemap: $SITEMAP_COUNT items from $SITEMAP_SOURCES_OK/$SITEMAP_SOURCES_TOTAL sources" >&2

# =============================================================
# STEP 2: Grok X search via proxy /responses
# =============================================================
# Grok uses `since:YYYY-MM-DD` which is date-granular (up to 48h). We
# post-filter by date_of_post against NOW-24h below.
YESTERDAY=$(TZ=UTC date -u -d "yesterday" +%Y-%m-%d 2>/dev/null || TZ=UTC date -u -v-1d +%Y-%m-%d)
GROK_PROMPT="Today's date = ${TODAY}. Search X/Twitter for posts from the last 24 hours (since ${YESTERDAY}) by these X user handles: @karpathy, @rasbt, @natolambert, @simonw, @emollick, @garrytan, @swyx, @ttunguz. For each substantive post about AI technology, research, or industry, return a JSON array: [{author, date_of_post, text, full_post, url, key_claims}]. Include the exact timestamp in date_of_post if available. Skip personal/promotional content. Return ONLY the JSON array and nothing else."

GROK_STATUS="ok"
GROK_FAIL_REASON=""
GROK_REQUEST_BODY="$(jq -n --arg p "$GROK_PROMPT" '{
  model: "grok-4",
  input: [{role:"user", content:$p}],
  tools: [{type:"x_search"}],
  temperature: 0.2
}')"

# Retry loop: up to 2 attempts with 10s delay between retries.
# grok-4-1 via /responses with x_search can take 90-150s — use 180s timeout.
GROK_MAX_ATTEMPTS=2
GROK_ATTEMPT=0
GROK_SUCCESS=false
while [ $GROK_ATTEMPT -lt $GROK_MAX_ATTEMPTS ]; do
  GROK_ATTEMPT=$((GROK_ATTEMPT + 1))
  echo "[scan] Grok attempt $GROK_ATTEMPT/$GROK_MAX_ATTEMPTS via ${LLM_PROXY_BASE_URL}/responses (model=grok-4, timeout=180s)" >&2
  GROK_HTTP_CODE=0
  GROK_CURL_EXIT=0
  GROK_HTTP_CODE=$(curl -sS --max-time 180 -o "$WS/.grok-raw.json" -w "%{http_code}" \
    -X POST "${LLM_PROXY_BASE_URL}/responses" \
    -H "Authorization: Bearer ${ATLAN_LLM_KEY}" \
    -H "Content-Type: application/json" \
    -d "$GROK_REQUEST_BODY" 2>"$WS/.grok-curl-stderr.log") || GROK_CURL_EXIT=$?

  if [ $GROK_CURL_EXIT -eq 28 ]; then
    GROK_FAIL_REASON="connection_timeout (curl exit 28, attempt $GROK_ATTEMPT)"
    echo "::warning::Grok attempt $GROK_ATTEMPT timed out after 180s (curl exit 28)" >&2
  elif [ $GROK_CURL_EXIT -ne 0 ]; then
    GROK_FAIL_REASON="curl_error_$GROK_CURL_EXIT (attempt $GROK_ATTEMPT)"
    echo "::warning::Grok attempt $GROK_ATTEMPT curl error exit=$GROK_CURL_EXIT" >&2
    cat "$WS/.grok-curl-stderr.log" >&2 || true
  elif [ "$GROK_HTTP_CODE" = "401" ] || [ "$GROK_HTTP_CODE" = "403" ]; then
    GROK_FAIL_REASON="auth_error (HTTP $GROK_HTTP_CODE)"
    echo "::warning::Grok auth error HTTP $GROK_HTTP_CODE — check ATLAN_LLM_KEY. No retry." >&2
    break  # Auth errors won't be fixed by retrying
  elif [ "$GROK_HTTP_CODE" = "400" ]; then
    GROK_FAIL_REASON="format_error (HTTP 400)"
    echo "::warning::Grok HTTP 400 — bad request format. Response:" >&2
    cat "$WS/.grok-raw.json" >&2 || true
    break  # Format errors won't be fixed by retrying
  elif [ "$GROK_HTTP_CODE" = "200" ]; then
    GROK_SUCCESS=true
    echo "[scan] Grok attempt $GROK_ATTEMPT succeeded (HTTP 200)" >&2
    break
  else
    GROK_FAIL_REASON="http_error_$GROK_HTTP_CODE (attempt $GROK_ATTEMPT)"
    echo "::warning::Grok attempt $GROK_ATTEMPT unexpected HTTP $GROK_HTTP_CODE" >&2
    cat "$WS/.grok-raw.json" >&2 || true
  fi

  # Retry delay (only if more attempts remain)
  if [ $GROK_ATTEMPT -lt $GROK_MAX_ATTEMPTS ]; then
    echo "[scan] retrying Grok in 10s..." >&2
    sleep 10
  fi
done

if [ "$GROK_SUCCESS" = "false" ]; then
  echo "::warning::Grok all attempts failed — reason: $GROK_FAIL_REASON. Falling back to RSS-only." >&2
  GROK_STATUS="failed"
  # Write empty raw so downstream parsing doesn't break
  echo '{}' > "$WS/.grok-raw.json"
fi

# Parse Grok: find the message item, extract content[0].text (Grok's JSON array)
GROK_TEXT=$(jq -r '.output[]? | select(.type=="message") | .content[0].text // empty' "$WS/.grok-raw.json" 2>/dev/null || echo "")

GROK_POSTS_ALL="[]"
if [ -n "$GROK_TEXT" ]; then
  GROK_POSTS_ALL=$(echo "$GROK_TEXT" | python3 -c "
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
fi

GROK_RAW_COUNT=$(echo "$GROK_POSTS_ALL" | jq 'length' 2>/dev/null || echo 0)

# Post-filter Grok posts to strict last-24h window
GROK_FILTER_RESULT=$(echo "$GROK_POSTS_ALL" | python3 -c "
import sys, json
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

now = datetime.now(timezone.utc)
cutoff = now - timedelta(hours=24)

def parse_date(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace('Z', '+00:00'))
    except Exception:
        pass
    try:
        dt = parsedate_to_datetime(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        pass
    # date-only: treat as end of that day UTC (permissive)
    try:
        d = datetime.fromisoformat(s[:10]).replace(tzinfo=timezone.utc)
        return d + timedelta(hours=23, minutes=59)
    except Exception:
        return None

posts = json.load(sys.stdin)
kept, dropped = [], []
for p in posts:
    dt = parse_date(p.get('date_of_post', ''))
    if dt is None:
        # No parseable date — drop (we can't verify freshness)
        dropped.append({'url': p.get('url', ''), 'reason': 'unparseable_date', 'date_of_post': p.get('date_of_post', '')})
        continue
    if dt < cutoff:
        dropped.append({'url': p.get('url', ''), 'reason': 'older_than_24h', 'date_of_post': p.get('date_of_post', '')})
        continue
    kept.append(p)

print(json.dumps({'kept': kept, 'dropped': dropped, 'cutoff_utc': cutoff.isoformat()}))
" 2>/dev/null || echo '{"kept":[],"dropped":[],"cutoff_utc":""}')

GROK_POSTS=$(echo "$GROK_FILTER_RESULT" | jq -c '.kept')
GROK_COUNT=$(echo "$GROK_POSTS" | jq 'length')
GROK_DROPPED=$(echo "$GROK_FILTER_RESULT" | jq '.dropped | length')
GROK_CUTOFF=$(echo "$GROK_FILTER_RESULT" | jq -r '.cutoff_utc')
echo "[scan] Grok: $GROK_COUNT posts within 24h ($GROK_DROPPED dropped as stale, $GROK_RAW_COUNT raw)" >&2

# =============================================================
# STEP 3: Combine RSS + Grok into raw-intake.json
# =============================================================
echo "$GROK_POSTS" | jq -c '[.[] | {
  title: (.key_claims // (.text // "")[:100]),
  url: (.url // ""),
  summary: (.full_post // .text // ""),
  source: ("x/" + ((.author // "unknown") | gsub("^@"; ""))),
  type: "x_post",
  date_posted: (.date_of_post // "")
}]' > "$WS/.grok-items.json" 2>/dev/null || echo "[]" > "$WS/.grok-items.json"

cat "$WS/.rss-items.jsonl" 2>/dev/null | jq -s '.' > "$WS/.rss-items.json" 2>/dev/null || echo "[]" > "$WS/.rss-items.json"
cat "$SITEMAP_ITEMS_FILE" 2>/dev/null | jq -s '.' > "$WS/.sitemap-items.json" 2>/dev/null || echo "[]" > "$WS/.sitemap-items.json"

# Combined RSS-shaped items — use --slurpfile to avoid "Argument list too long" on large feeds
jq -n \
  --arg date "$TODAY" \
  --slurpfile rss "$WS/.rss-items.json" \
  --slurpfile sitemap "$WS/.sitemap-items.json" \
  --slurpfile grok "$WS/.grok-items.json" \
  '{
    date: $date,
    items: ($rss[0] + $sitemap[0] + $grok[0]),
    stats: {
      rss_items: ($rss[0] | length),
      sitemap_items: ($sitemap[0] | length),
      x_posts: ($grok[0] | length),
      total: (($rss[0] + $sitemap[0] + $grok[0]) | length)
    }
  }' > "$WS/raw-intake.json"

TOTAL_COUNT=$(jq '.items | length' "$WS/raw-intake.json")
echo "[scan] combined items: $TOTAL_COUNT" >&2

# =============================================================
# STEP 4: scan-summary.json — the committed dashboard
# =============================================================
SITEMAP_STATS_JSON=$(cat "$SITEMAP_STATS" 2>/dev/null || echo '{"sources_total":0,"sources_ok":0,"sources_failed":0,"items_total":0,"per_source":[]}')

jq -n \
  --arg date "$TODAY" \
  --arg generated_at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --arg grok_status "$GROK_STATUS" \
  --arg grok_fail_reason "$GROK_FAIL_REASON" \
  --arg grok_cutoff "$GROK_CUTOFF" \
  --argjson rss_stats "$(cat "$RSS_STATS")" \
  --argjson sitemap_stats "$SITEMAP_STATS_JSON" \
  --argjson grok_raw_count "$GROK_RAW_COUNT" \
  --argjson grok_kept "$GROK_COUNT" \
  --argjson grok_dropped "$GROK_DROPPED" \
  --argjson grok_dropped_detail "$(echo "$GROK_FILTER_RESULT" | jq '.dropped')" \
  '{
    date: $date,
    generated_at: $generated_at,
    rss: {
      feeds_total: $rss_stats.feeds_total,
      feeds_processed: $rss_stats.feeds_processed,
      feeds_failed: $rss_stats.feeds_failed,
      items_returned: $rss_stats.items_returned,
      cutoff_utc: $rss_stats.cutoff_utc,
      failing_feeds: [$rss_stats.per_feed[] | select(.status != "ok") | {url, status, error}]
    },
    sitemap: {
      sources_total: $sitemap_stats.sources_total,
      sources_ok: $sitemap_stats.sources_ok,
      sources_failed: $sitemap_stats.sources_failed,
      items_total: $sitemap_stats.items_total,
      per_source: $sitemap_stats.per_source
    },
    x: {
      grok_status: $grok_status,
      grok_fail_reason: (if $grok_fail_reason == "" then null else $grok_fail_reason end),
      posts_returned_raw: $grok_raw_count,
      posts_within_24h: $grok_kept,
      posts_dropped_stale: $grok_dropped,
      cutoff_utc: $grok_cutoff,
      dropped_detail: $grok_dropped_detail
    },
    totals: {
      rss_items: $rss_stats.items_returned,
      sitemap_items: $sitemap_stats.items_total,
      x_posts: $grok_kept,
      total: ($rss_stats.items_returned + $sitemap_stats.items_total + $grok_kept)
    }
  }' > "$WS/scan-summary.json"

# =============================================================
# STEP 5: Health gates — write status
# =============================================================
# Three states:
#   scan-quiet     → <3 total items. Orchestrator skips write, sends "nothing new".
#   scan-degraded  → ship anyway but alarm (0 in a bucket, or many feed failures)
#   scan-ok        → green
REAL_ITEMS=$TOTAL_COUNT
STATUS="scan-ok"
REASONS=()
WEB_ITEMS=$((RSS_COUNT + SITEMAP_COUNT))  # RSS + sitemap share the "web content" bucket

if [ "$REAL_ITEMS" -lt 3 ]; then
  STATUS="scan-quiet"
  REASONS+=("total_items=$REAL_ITEMS (<3)")
else
  if [ "$WEB_ITEMS" -eq 0 ]; then
    STATUS="scan-degraded"
    REASONS+=("web_items=0 (rss=$RSS_COUNT, sitemap=$SITEMAP_COUNT)")
  fi
  if [ "$GROK_COUNT" -eq 0 ]; then
    STATUS="scan-degraded"
    REASONS+=("x_posts=0 (grok_status=$GROK_STATUS)")
  fi
  # Flag if >25% of RSS feeds failed
  if [ "$FEEDS_TOTAL" -gt 0 ] && [ "$((FEEDS_FAILED * 100 / FEEDS_TOTAL))" -ge 25 ]; then
    STATUS="scan-degraded"
    REASONS+=("rss_feeds_failed=$FEEDS_FAILED/$FEEDS_TOTAL ($((FEEDS_FAILED * 100 / FEEDS_TOTAL))%)")
  fi
  # Flag if any sitemap source failed (all 4 matter)
  SITEMAP_FAILED=$(jq '.sources_failed // 0' "$SITEMAP_STATS" 2>/dev/null || echo 0)
  if [ "$SITEMAP_FAILED" -gt 0 ]; then
    STATUS="scan-degraded"
    REASONS+=("sitemap_sources_failed=$SITEMAP_FAILED/$SITEMAP_SOURCES_TOTAL")
  fi
fi

REASONS_JSON=$(printf '%s\n' "${REASONS[@]:-}" | jq -R . | jq -s 'map(select(. != ""))')
# Append degraded reasons to scan-summary.json
jq --arg status "$STATUS" --argjson reasons "$REASONS_JSON" \
  '. + {status: $status, degraded_reasons: $reasons}' \
  "$WS/scan-summary.json" > "$WS/scan-summary.json.tmp" && mv "$WS/scan-summary.json.tmp" "$WS/scan-summary.json"

echo "$STATUS" > "$WS/.status"
echo "[scan] status=$STATUS reasons=${REASONS[*]:-none}" >&2

if [ "$STATUS" = "scan-ok" ]; then
  echo "[scan] SUCCESS: $TOTAL_COUNT items ($RSS_COUNT RSS + $SITEMAP_COUNT sitemap + $GROK_COUNT X, 24h window)"
elif [ "$STATUS" = "scan-degraded" ]; then
  echo "::warning::Scan degraded — shipping anyway. Reasons: ${REASONS[*]}"
else
  echo "[scan] QUIET DAY — orchestrator routes to nothing_new"
fi
