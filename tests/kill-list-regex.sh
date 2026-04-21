#!/usr/bin/env bash
# Kill-list regex test — scans workspace/*/posts.md and brief.md for banned words/patterns.
# Source of truth: .claude/skills/write-posts/references/kill-list.md categories 1A–1F + 1G + 1K.

set -uo pipefail

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

  # Pattern 1H: "It's like ..." analogies
  if echo "$content" | grep -qiE "[Ii]t's like [A-Z]"; then
    errors+=('analogy_pattern: "It\'"'"'s like X" — turn into a question')
  fi

  # Pattern 1I: "Not X. Y." contrast-through-negation (the AI-tell we keep missing)
  # Catches: "Not the model.", "Not for the demos.", "Not because X.", "Not just X."
  # as standalone sentences (not mid-sentence negation which is fine)
  local not_x_y_count
  not_x_y_count=$(echo "$content" | grep -cE '(^|[.!?] )Not (the |a |for |because |just |one |in |at |by |an )' || true)
  if [ "$not_x_y_count" -gt 0 ]; then
    errors+=("not_x_y_negation_hits=${not_x_y_count} — 'Not X. Y.' sentences sound AI-generated. Say what it IS, not what it isn't.")
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
