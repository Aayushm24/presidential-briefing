---
name: revise
description: Apply council critique to posts. Fix fact errors, voice violations, stale angles. Preserves each option's core template/angle.
---

# /revise — Apply council fixes

Reads `workspace/${TODAY}/council-notes.md` + `.council-verdict.json`. Rewrites `workspace/${TODAY}/posts.md` with fixes applied. Preserves each option's template + core angle — only FIXES violations, doesn't re-pivot.

Also applies fact fixes to `brief.md` if council flagged any (e.g., "Cursor $1B → $900M").

Hard cap: 2 iterations total (controlled by orchestrator via `workspace/${TODAY}/.iter`).

## Inputs

- `workspace/${TODAY}/posts.md`
- `workspace/${TODAY}/brief.md`
- `workspace/${TODAY}/council-notes.md`
- `workspace/${TODAY}/.council-verdict.json`

## Outputs

- `workspace/${TODAY}/posts.md` — revised in place
- `workspace/${TODAY}/posts.md.iter-N.bak` — backup of pre-revision version
- `workspace/${TODAY}/brief.md` — revised in place ONLY if council flagged fact errors
- `workspace/${TODAY}/brief.md.iter-N.bak` — backup if revised

## Process

### Step 1: Back up pre-revision

```bash
ITER=$(cat workspace/${TODAY}/.iter)
cp workspace/${TODAY}/posts.md workspace/${TODAY}/posts.md.iter-${ITER}.bak
[ -f workspace/${TODAY}/brief.md ] && cp workspace/${TODAY}/brief.md workspace/${TODAY}/brief.md.iter-${ITER}.bak
```

### Step 2: Build revise prompt for posts

```
Apply council corrections to the 3 LinkedIn post options. Do NOT rewrite the briefing (separate step). Focus entirely on improving the posts.

RULES FOR REVISION:
- Keep each option's core template + angle (if it was personal-discovery, keep it personal-discovery)
- Fix ONLY what council flagged — don't re-write good parts
- NEVER use em dashes. Use commas, periods, or "..." instead.
- Preserve conviction statements unless council flagged them as false/unverifiable
- Hook revisions: new hook must still follow same hook pattern (A-J) unless council said pattern itself was wrong

Score 5 dimensions (1-10) per option after revision: novelty, insight_density, voice_match, hook_strength, teachability.

Output EXACTLY this format:

===OPTION 1===
template: [same as before, or NEW if council said pattern wrong]
hook_pattern: [A-J]
conviction: [preserved or tightened]
hook_score: [new 1-10]

[revised post body]

===OPTION 2===
[same structure]

===OPTION 3===
[same structure]

===SCORES===
option_1: novelty=N insight=N voice=N hook=N teach=N avg=N
option_2: novelty=N insight=N voice=N hook=N teach=N avg=N
option_3: novelty=N insight=N voice=N hook=N teach=N avg=N
best_option: N

=== CURRENT POSTS ===
<posts>
${POSTS_MD_CONTENTS}
</posts>

=== COUNCIL FEEDBACK ===

Voice audit:
<voice>
${VOICE_AUDIT_JSON}
</voice>

Fact check:
<facts>
${FACT_CHECK_JSON}
</facts>

Adversarial attack:
<attack>
${ATTACK_JSON}
</attack>

=== KILL LIST (do not reintroduce) ===
<kill_list>
${KILL_LIST_CONTENTS}
</kill_list>

Rewrite now.
```

### Step 3: Call Opus via proxy

```bash
curl -sS -X POST "${LLM_PROXY_BASE_URL}/v1/chat/completions" \
  -H "Authorization: Bearer ${ATLAN_LLM_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg model "claude-opus-4-6" --arg prompt "$REVISE_PROMPT" \
    '{model: $model, messages: [{role: "user", content: $prompt}], temperature: 0.4, max_tokens: 4000}')"
```

### Step 4: Parse + write revised posts.md

Extract 3 ===OPTION N=== blocks + ===SCORES=== block.

Validate:
- All 3 options present
- Each has template, hook_pattern, conviction, hook_score, post body
- Hook ≤70 chars
- No em dashes (hard regex)
- No kill-list regressions (compare against pre-revise version — flag if new violation introduced)

Rewrite `workspace/${TODAY}/posts.md` with revised options. Include revision metadata header:

```markdown
# LinkedIn posts — 2026-04-19 (iteration 2)

**Lead:** [lead title]
**Revision trigger:** council REVISE verdict at iter 1
**Best option:** 2 (revised score: 8.4/10 average)

---

## OPTION 1 — personal-discovery (hook score: 9, was 7)

**Conviction:** [...]

[post]

[...]
```

### Step 5: Revise brief.md if needed

If council flagged fact errors on brief (e.g., wrong funding amount, wrong company name):

```
Apply these fact corrections to the briefing. Do NOT rewrite any section. Edit ONLY the exact lines with issues.

Fact errors to fix:
<errors>
${FACT_ERRORS_JSON}
</errors>

Current brief:
<brief>
${BRIEF_CONTENTS}
</brief>

Output: full revised brief.md, with ONLY the flagged lines changed. Preserve every other word.
```

This is a surgical edit. Use Opus with temperature 0.2. Validate post-edit:
- Diff should be minimal (flagged lines only)
- Word count unchanged by more than 5%
- Structure preserved (all headers, sections intact)

### Step 6: Handoff back to orchestrator

Orchestrator's next step is re-running `/attack` on the revised content. Loop continues up to 2 iterations.

On iter 3 (the third attempt), orchestrator skips `/revise` and force-ships with `[UNREVIEWED]` tag injected at top of `posts.md`.

---

## Kill list

- NEVER re-pivot an option from personal-discovery to contrarian (or any template change) unless council explicitly flagged the template as wrong
- NEVER delete a conviction statement unless council flagged it false or unverifiable
- NEVER introduce a new em dash while fixing other issues
- NEVER regress voice audit score below pre-revise version
- NEVER rewrite the briefing — surgical line edits only, for flagged facts
- NEVER skip the .iter-N.bak backup step
