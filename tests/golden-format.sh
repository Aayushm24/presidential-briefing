#!/usr/bin/env bash
# Golden format test — validates structure of every workspace/*/brief.md
# Based on .claude/skills/write-briefing/references/section-order.md

set -uo pipefail

FAIL=0
CHECKED=0

check_brief() {
  local file="$1"
  local errors=()

  # H1 count: exactly 1
  local h1=$(grep -c '^# ' "$file" || true)
  [ "$h1" -eq 1 ] || errors+=("h1_count=$h1 (expect 1)")

  # H3 count: 3-8
  local h3=$(grep -c '^### ' "$file" || true)
  [ "$h3" -ge 3 ] && [ "$h3" -le 8 ] || errors+=("h3_count=$h3 (expect 3-8)")

  # Key takeaways present
  grep -q '\*\*Key takeaways:\*\*' "$file" || errors+=("missing_key_takeaways")

  # What to do this week
  grep -q '### What to do this week' "$file" || errors+=("missing_what_to_do_this_week")

  # Sources footer
  grep -q '^## Sources' "$file" || errors+=("missing_sources_footer")

  # Numbered sources (>=3)
  local sources=$(awk '/^## Sources/,0' "$file" | grep -cE '^[0-9]+\.' || true)
  [ "$sources" -ge 3 ] || errors+=("sources_count=$sources (expect >=3)")

  # No em dashes (U+2014)
  if grep -q $'\u2014' "$file"; then
    errors+=("em_dash_found")
  fi

  # No H2 outside Sources
  local bad_h2=$(awk '/^## Sources/{exit} /^## / && !/^## Sources/{print}' "$file" | wc -l)
  [ "$bad_h2" -eq 0 ] || errors+=("h2_in_body=$bad_h2")

  # Word count 800-2500
  local wc=$(wc -w < "$file")
  [ "$wc" -ge 600 ] && [ "$wc" -le 3000 ] || errors+=("word_count=$wc (expect 600-3000)")

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
