#!/usr/bin/env bash
# Kill-list regex test — scans workspace/*/posts.md and brief.md for banned words/patterns.
# Source of truth: .claude/skills/write-posts/references/kill-list.md categories 1A–1F + 1G + 1K.
#
# Grandfather clause (matches tests/golden-format.sh): the "new regime" checks
# (repricing language, AI contemplation, "Not X. Y." negation) only apply to
# briefs/posts dated on/after 2026-04-23. Files before that date shipped under
# the prior rules and are not reshipped. Universal rules (em dashes, bullets,
# banned words, banned phrases, "It's like X" analogy, audience direct-address)
# still apply to every file.

set -uo pipefail

GRANDFATHER_DATE="2026-04-23"
FAIL=0
CHECKED=0

# Categories 1A-1F (words — case insensitive, whole-word match)
BANNED_WORDS=(
  # 1A classic AI buzzwords
  'delve' 'testament' 'tapestry' 'paradigm[- ]shift' 'synergy' 'synergies'
  'holistic' 'empower' 'democratize' 'disruption'
  # 1B corporate fluff
  'cutting[- ]edge' 'seamless' 'leverage' 'utilize' 'scalable'
  'best[- ]in[- ]class' 'world[- ]class' 'next[- ]generation' 'state[- ]of[- ]the[- ]art'
  'mission[- ]critical' 'end[- ]to[- ]end'
  # 1D overwrought
  'game[- ]changing' 'game changer' 'groundbreaking' 'ground[- ]breaking'
  'revolutionary' 'transformative' 'unprecedented' 'monumental'
)

# Categories 1C, 1E, 1F, 1K (phrases — case insensitive)
BANNED_PHRASES=(
  'at its core'
  'plays a significant role'
  "it's important to note"
  "it's worth noting"
  "in today's rapidly evolving"
  'the future of'
  'in an era of'
  'as we navigate'
  'the intersection of'
  'Here is what I learned'
  "Here's what I learned"
  "Let me share"
  "I've been thinking a lot about"
  "Let's talk about"
  "Hot take:"
  "Unpopular opinion:"
  "excited to announce"
  "thrilled to announce"
  "proud to announce"
  "honored to announce"
  "unlock the power of"
  "check out our latest"
  "Learn more"
)

check_file() {
  local file="$1"
  local content
  content=$(cat "$file")
  local errors=()

  # Determine legacy status from path: workspace/YYYY-MM-DD/*.md
  # BSD sed (macOS) and GNU sed (Linux) disagree on alternation, so match date only.
  local file_date
  file_date=$(echo "$file" | sed -nE 's|.*workspace/([0-9]{4}-[0-9]{2}-[0-9]{2})/.*|\1|p')
  local is_legacy="false"
  if [ -n "$file_date" ] && [ "$file_date" \< "$GRANDFATHER_DATE" ]; then
    is_legacy="true"
  fi

  # Em dashes (U+2014) — use UTF-8 byte sequence for portability across bash 3.2 + 4+
  local em_dash
  em_dash=$(printf '\xe2\x80\x94')
  if echo "$content" | grep -q "$em_dash"; then
    errors+=("em_dash found (U+2014 not allowed)")
  fi

  # Bullets (•)
  if echo "$content" | grep -q '•'; then
    errors+=("bullet (•) found — use dashes")
  fi

  # Banned words (case insensitive, word boundary)
  for word in "${BANNED_WORDS[@]}"; do
    if echo "$content" | grep -qiE "\\b${word}\\b"; then
      errors+=("banned_word: $word")
    fi
  done

  # Banned phrases (case insensitive, exact substring)
  for phrase in "${BANNED_PHRASES[@]}"; do
    if echo "$content" | grep -qi -- "$phrase"; then
      errors+=("banned_phrase: \"$phrase\"")
    fi
  done

  # Pattern 1H: "It's like ..." analogies (universal — applies to all files, legacy or new)
  if echo "$content" | grep -qiE "[Ii]t's like [A-Z]"; then
    errors+=('analogy_pattern: "It\'"'"'s like X" — turn into a question')
  fi

  # ── NEW-REGIME checks — only apply to files on/after GRANDFATHER_DATE ──
  # Files before that date shipped under the prior rules and are not reshipped.
  if [ "$is_legacy" = "false" ]; then
    # Fabricated repricing language — "repriced/repricing" applied to events that aren't price changes
    # e.g. "Three tools repriced this week" when they restricted access or got acquired
    local repricing_hits
    repricing_hits=$(printf '%s' "$content" | grep -ciE '(repriced|repricing)' || true)
    if [ "$repricing_hits" -gt 0 ]; then
      errors+=("repricing_language=${repricing_hits} — verify this actually happened. 'Repriced' is often fabricated when tools restricted access or were acquired.")
    fi

    # AI contemplation phrases — sound like AI trying to be thoughtful
    local ai_contemplation
    ai_contemplation=$(printf '%s' "$content" | grep -ciE "(here'?s what i keep coming back to|i want to sit with that|that'?s the part nobody wants to|the dangerous version of this story|it's worth sitting with|let that sink in|think about that for a moment)" || true)
    if [ "$ai_contemplation" -gt 0 ]; then
      errors+=("ai_contemplation_hits=${ai_contemplation} — phrases like 'Here\'s what I keep coming back to' and 'I want to sit with that' are AI tells")
    fi

    # Pattern 1I: "Not X. Y." contrast-through-negation (the AI-tell we keep missing)
    # Catches: "Not the model.", "Not for the demos.", "Not because X.", "Not just X."
    # as standalone sentences (not mid-sentence negation which is fine)
    local not_x_y_count
    not_x_y_count=$(echo "$content" | grep -cE '(^|[.!?] )Not (the |a |for |because |just |one |in |at |by |an )' || true)
    if [ "$not_x_y_count" -gt 0 ]; then
      errors+=("not_x_y_negation_hits=${not_x_y_count} — 'Not X. Y.' sentences sound AI-generated. Say what it IS, not what it isn't.")
    fi
  fi

  # Corporate direct-address
  for phrase in "for founders" "hey founders" "fellow founders" "if you're a founder"; do
    if echo "$content" | grep -qi -- "$phrase"; then
      errors+=("audience_direct_address: \"$phrase\"")
    fi
  done

  if [ ${#errors[@]} -gt 0 ]; then
    echo "FAIL: $file"
    for e in "${errors[@]}"; do
      echo "  - $e"
    done
    return 1
  fi

  echo "OK: $file"
  return 0
}

# If called with explicit file arg, just check that
if [ $# -gt 0 ]; then
  check_file "$1" || FAIL=1
  CHECKED=1
else
  shopt -s nullglob
  for FILE in workspace/*/posts.md workspace/*/brief.md; do
    check_file "$FILE" || FAIL=1
    CHECKED=$((CHECKED + 1))
  done
fi

if [ $CHECKED -eq 0 ]; then
  echo "NOTE: no files to check — skipping (not a failure)"
  exit 0
fi

if [ $FAIL -eq 1 ]; then
  echo ""
  echo "kill-list: FAILED ($CHECKED files, >=1 violation)"
  exit 1
fi

echo ""
echo "kill-list: OK ($CHECKED files clean)"
exit 0
