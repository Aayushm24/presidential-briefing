#!/usr/bin/env bash
# Hard gate for posts.json — validates:
#   1. Exactly 3 options present
#   2. Each option.post is >= MIN_CHARS (1,300), no upper cap
#   3. Zero "[Not X, it's Y]" patterns across all 3 options combined
#      (tight: same-subject inversion only — parallel comparisons with a
#      different subject are allowed. See regex below.)
#   4. Zero "It's like X" analogies
#   5. Zero trailing-hashtag blocks
#
# MBA-vocab ban (posts only): differentiation, commoditization, table stakes.
# "moat/moats" is ALLOWED in posts per 2026-04-20 voice calibration — Aayush
# uses it comfortably in his own posts. It stays BANNED in briefs via
# tests/golden-format.sh (different surface, different audience).
#
# Ship step calls this after revise. Fails = abort delivery.
# Runs against workspace/*/posts.json.

set -uo pipefail

MIN_CHARS=1300
MAX_CHARS=99999  # no cap — top posts go to 2,161c. content determines length.
FAIL=0
CHECKED=0

check_posts() {
  local file="$1"
  local errors=()

  if ! command -v jq >/dev/null 2>&1; then
    echo "::error::jq not installed" >&2
    return 1
  fi

  if ! jq empty "$file" 2>/dev/null; then
    errors+=("invalid_json")
    echo "FAIL: $file"
    for e in "${errors[@]}"; do echo "  - $e"; done
    return 1
  fi

  local count
  count=$(jq '.options | length' "$file")
  if [ "$count" -ne 3 ]; then
    errors+=("options_count=$count (expect 3)")
  fi

  # Per-option char count gate
  local i=1
  while [ $i -le "$count" ]; do
    local idx=$((i - 1))
    local post
    post=$(jq -r ".options[$idx].post // \"\"" "$file")
    local chars=${#post}
    if [ "$chars" -lt "$MIN_CHARS" ]; then
      errors+=("option_${i}_too_short=${chars}c (floor ${MIN_CHARS})")
    elif [ "$chars" -gt "$MAX_CHARS" ]; then
      errors+=("option_${i}_too_long=${chars}c (cap ${MAX_CHARS})")
    fi
    i=$((i + 1))
  done

  # [Not X, it's Y] — zero tolerance across all options combined
  # TIGHT pattern: only flag when the SECOND clause re-claims the SAME subject
  # with "It's/They're + abstract pivot word" (about/just/becoming/actually/the).
  # This catches AI-tells like:
  #   "The survivors aren't building better models. They're building better distribution."
  #   "This isn't about model access. It's about who owns the user."
  # But ALLOWS parallel comparisons where the subject changes, e.g.:
  #   "Customer support logs aren't a moat. Real-time workflow data is."
  # (Aayush uses this pattern — second sentence introduces a NEW noun subject,
  #  not "it's/they're" pointing back at the first.)
  local all_posts
  all_posts=$(jq -r '.options[].post' "$file")
  local not_x_its_y
  not_x_its_y=$(printf '%s' "$all_posts" | grep -ciE "(isn'?t|aren'?t|is\s+not|are\s+not)[^.!?]*\.[[:space:]]*(it'?s|they'?re)[[:space:]]+(about|just|becoming|actually|the)" || true)
  if [ "$not_x_its_y" -gt 0 ]; then
    errors+=("not_x_its_y_hits=${not_x_its_y} (expect 0)")
  fi

  # "It's like X" analogy — zero tolerance
  local its_like
  its_like=$(printf '%s' "$all_posts" | grep -ciE "(^|[[:space:]])it'?s\s+like\s+" || true)
  if [ "$its_like" -gt 0 ]; then
    errors+=("its_like_analogy_hits=${its_like} (expect 0)")
  fi

  # Trailing hashtag block
  local trailing_hashtags
  trailing_hashtags=$(printf '%s' "$all_posts" | grep -cE "^[[:space:]]*#[[:alnum:]]+(\s+#[[:alnum:]]+)*[[:space:]]*$" || true)
  if [ "$trailing_hashtags" -gt 0 ]; then
    errors+=("trailing_hashtag_block_hits=${trailing_hashtags} (expect 0)")
  fi

  # MBA vocabulary — ZERO tolerance in posts.
  # NOTE: "moats?" was REMOVED from this loop on 2026-04-20. Aayush uses
  # "moat" 4x in his own top-performing post (2026-04-20 "AI startups have
  # 12 months"). Posts can carry his industry vocab. Briefs cannot (see
  # tests/golden-format.sh — moat still banned there for a different audience).
  for word_pattern in "differentiation|differentiator" "commoditi[sz]ation|commoditi[sz]es?" "table\s+stakes"; do
    local hits
    hits=$(printf '%s' "$all_posts" | grep -ciwE "$word_pattern" || true)
    if [ "$hits" -gt 0 ]; then
      errors+=("mba_vocab_hits[${word_pattern}]=${hits} (expect 0)")
    fi
  done

  if [ ${#errors[@]} -gt 0 ]; then
    echo "FAIL: $file"
    for e in "${errors[@]}"; do echo "  - $e"; done
    return 1
  fi

  echo "OK: $file  (3 options, all ${MIN_CHARS}-${MAX_CHARS}c, 0 banned patterns)"
  return 0
}

# Check file arg if given, else all workspace/*/posts.json
if [ $# -gt 0 ]; then
  check_posts "$1" || FAIL=1
  CHECKED=1
else
  shopt -s nullglob
  for F in workspace/*/posts.json; do
    check_posts "$F" || FAIL=1
    CHECKED=$((CHECKED + 1))
  done
fi

if [ "$CHECKED" -eq 0 ]; then
  echo "NOTE: no posts.json files to check"
  exit 0
fi

if [ "$FAIL" -eq 1 ]; then
  echo ""
  echo "posts-gate: FAILED ($CHECKED checked, >=1 failed)"
  exit 1
fi

echo ""
echo "posts-gate: OK ($CHECKED checked)"
exit 0
