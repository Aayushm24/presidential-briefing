#!/usr/bin/env bash
# Golden format test — validates structure of every workspace/*/brief.md
# Based on .claude/skills/write-briefing/references/section-order.md
#
# Grandfather clause: rules changed on 2026-04-20 (plain-English pass,
# inline citations, word-count raised to 1200-2800). Briefs before that
# date were shipped under the prior rules and are not reshipped, so we
# grandfather them with a permissive structural check.

set -uo pipefail

GRANDFATHER_DATE="2026-04-20"
FAIL=0
CHECKED=0

check_brief() {
  local file="$1"
  local errors=()

  # Extract brief date from path: workspace/YYYY-MM-DD/brief.md
  local brief_date
  brief_date=$(echo "$file" | sed -nE 's|.*workspace/([0-9]{4}-[0-9]{2}-[0-9]{2})/brief\.md|\1|p')
  local is_legacy="false"
  if [ -n "$brief_date" ] && [ "$brief_date" \< "$GRANDFATHER_DATE" ]; then
    is_legacy="true"
  fi

  # H1 count: exactly 1 (applies to all briefs, legacy or not)
  local h1=$(grep -c '^# ' "$file" || true)
  [ "$h1" -eq 1 ] || errors+=("h1_count=$h1 (expect 1)")

  # H3 count: 3-8 (applies to all)
  local h3=$(grep -c '^### ' "$file" || true)
  [ "$h3" -ge 3 ] && [ "$h3" -le 8 ] || errors+=("h3_count=$h3 (expect 3-8)")

  # Key takeaways present (applies to all)
  grep -q '\*\*Key takeaways:\*\*' "$file" || errors+=("missing_key_takeaways")

  # No em dashes — universal rule (applies to all)
  local em_dash
  em_dash=$(printf '\xe2\x80\x94')
  if grep -q "$em_dash" "$file"; then
    errors+=("em_dash_found")
  fi

  if [ "$is_legacy" = "true" ]; then
    # Legacy briefs (< GRANDFATHER_DATE): permissive check — H1, H3 count, key-takeaways, no em-dashes.
    # Skip inline-link / no-Sources-footer / word-count / no-H2 rules since they post-date the brief.
    if [ ${#errors[@]} -gt 0 ]; then
      echo "FAIL (legacy rules): $file"
      for e in "${errors[@]}"; do echo "  - $e"; done
      return 1
    fi
    echo "OK (legacy, grandfathered): $file"
    return 0
  fi

  # New-regime rules (briefs on/after GRANDFATHER_DATE)

  # What to do this week
  grep -q '### What to do this week' "$file" || errors+=("missing_what_to_do_this_week")

  # Inline citations: no "## Sources" footer
  if grep -q '^## Sources' "$file"; then
    errors+=("sources_footer_present_should_be_inline_only")
  fi
  local inline_links=$(grep -oE '\[[^]]+\]\(https?://[^)]+\)' "$file" | wc -l | tr -d ' ')
  [ "$inline_links" -ge 3 ] || errors+=("inline_links=$inline_links (expect >=3)")

  # No H2 anywhere
  local bad_h2=$(grep -cE '^## ' "$file" || true)
  [ "$bad_h2" -eq 0 ] || errors+=("h2_in_body=$bad_h2")

  # [Not X, it's Y] inversions — ZERO tolerance (2026-04-20 feedback: 4 in brief was unacceptable)
  # Matches "X isn't Y. It's/They're Z" pattern across sentence boundaries
  local not_x_its_y
  not_x_its_y=$(grep -cE "(isn'?t|aren'?t|is[[:space:]]+not|are[[:space:]]+not)[^.!?]*\.[[:space:]]*(It'?s|They'?re|It[[:space:]]+is|They[[:space:]]+are)[[:space:]]+(about|just|becoming|actually|the|changing|building|adding|really|where)" "$file" || true)
  [ "$not_x_its_y" -eq 0 ] || errors+=("not_x_its_y_hits=$not_x_its_y (expect 0)")

  # MBA vocabulary — ZERO tolerance for these specific words (2026-04-20 feedback: "moat" appeared 4x)
  # These words are banned in plain-english-rules.md. If they appear in shipped brief, something is broken.
  local mba_moat; mba_moat=$(grep -ciwE "moats?" "$file" || true)
  [ "$mba_moat" -eq 0 ] || errors+=("mba_vocab_moat_hits=$mba_moat (expect 0 — use 'the thing competitors can't copy' or name it concretely)")
  local mba_diff; mba_diff=$(grep -ciwE "differentiation|differentiator" "$file" || true)
  [ "$mba_diff" -eq 0 ] || errors+=("mba_vocab_differentiation_hits=$mba_diff (expect 0 — use 'what makes you different' or name the specific)")
  local mba_commod; mba_commod=$(grep -ciwE "commoditi[sz]ation|commoditi[sz]es?" "$file" || true)
  [ "$mba_commod" -eq 0 ] || errors+=("mba_vocab_commoditization_hits=$mba_commod (expect 0 — use 'gets cheap' / 'everyone has it')")
  local mba_stakes; mba_stakes=$(grep -ciwE "table\s+stakes" "$file" || true)
  [ "$mba_stakes" -eq 0 ] || errors+=("mba_vocab_table_stakes_hits=$mba_stakes (expect 0 — use 'everyone has it')")
  local mba_stack; mba_stack=$(grep -ciE "(up|move.*up|moves.*up|moving.*up|shift.*up)\s+the\s+stack" "$file" || true)
  [ "$mba_stack" -eq 0 ] || errors+=("mba_vocab_up_the_stack_hits=$mba_stack (expect 0 — use 'to apps' / 'to the product')")

  # Word count: FLOOR raised from 1200 to 1500 per 2026-04-20 feedback — brief at 1227 felt thin
  local wc=$(wc -w < "$file")
  [ "$wc" -ge 1500 ] && [ "$wc" -le 2800 ] || errors+=("word_count=$wc (expect 1500-2800)")

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

# Check all shipped briefs (workspace/*/brief.md)
shopt -s nullglob
for BRIEF in workspace/*/brief.md; do
  check_brief "$BRIEF" || FAIL=1
  CHECKED=$((CHECKED + 1))
done

# If called with an explicit file arg, check just that one
if [ $# -gt 0 ]; then
  CHECKED=0; FAIL=0
  check_brief "$1" || FAIL=1
  CHECKED=$((CHECKED + 1))
fi

if [ $CHECKED -eq 0 ]; then
  echo "NOTE: no brief.md files found to check — skipping (not a failure)"
  exit 0
fi

if [ $FAIL -eq 1 ]; then
  echo ""
  echo "golden-format: FAILED ($CHECKED files checked, >=1 failure)"
  exit 1
fi

echo ""
echo "golden-format: OK ($CHECKED files passed)"
exit 0
