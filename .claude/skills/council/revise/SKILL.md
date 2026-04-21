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

### Step 0: Back up pre-revision

```bash
ITER=$(cat workspace/${TODAY}/.iter 2>/dev/null || echo 0)
cp workspace/${TODAY}/posts.md workspace/${TODAY}/posts.md.iter-${ITER}.bak
[ -f workspace/${TODAY}/brief.md ] && cp workspace/${TODAY}/brief.md workspace/${TODAY}/brief.md.iter-${ITER}.bak
```

### Step 1: Deterministic clean (MUST run first)

LLMs cannot be trusted to apply 100% of hard rules (em dashes, kill-list words, audience direct-address). Run the regex fixer first — it substitutes every occurrence deterministically:

```bash
python3 scripts/clean_text.py workspace/${TODAY}/brief.md workspace/${TODAY}/posts.md 2>&1
```

This handles:
- em dashes (U+2014) → commas with spacing normalized
- Kill-list words → safe synonyms (leverage→use, cutting-edge→leading, etc.)
- Audience direct-address ("for founders" → "for builders", "hey founders" → removed)
- Bullets (•) → dashes (-)
- Transition crutches at sentence starts (Furthermore, In fact, etc.) → deleted
- Cliche openers (Let me share, Hot take:, etc.) → deleted

After clean, re-run kill-list regex to confirm hard rules are now clean:

```bash
BRIEF_CLEAN=0; POSTS_CLEAN=0
./tests/kill-list-regex.sh workspace/${TODAY}/brief.md > workspace/${TODAY}/.brief-killlist-post-clean.log 2>&1 && BRIEF_CLEAN=1
./tests/kill-list-regex.sh workspace/${TODAY}/posts.md > workspace/${TODAY}/.posts-killlist-post-clean.log 2>&1 && POSTS_CLEAN=1

if [ $BRIEF_CLEAN -eq 0 ] || [ $POSTS_CLEAN -eq 0 ]; then
  echo "[revise] kill-list violations remain after cleaner — LLM revise MUST remove them manually." >&2
  cat workspace/${TODAY}/.brief-killlist-post-clean.log workspace/${TODAY}/.posts-killlist-post-clean.log >&2
fi
```

**Do not exit here.** If violations remain, the LLM revise in Step 3+ is where they get fixed by hand. The ship step's final pre-delivery gate is the non-negotiable check; this one is a signal to the LLM to focus.

### Step 2: LLM revise (MANDATORY when pre-flight found violations)

**If council/attack flagged ANY deterministic violations (em dashes, kill-list words, analogy patterns, MBA vocab, long sentences, `[Not X, it's Y]` patterns, missing inline links, Sources footer, H2 in body), the LLM revise MUST remove every single one of them. No exceptions.**

When Step 3/4/5 builds the revise prompt, include the specific council-notes violations verbatim and tell the LLM:

> "The items below are DETERMINISTIC HARD BLOCKERS. The ship step runs the same regex checks at delivery time and will abort the whole run if ANY of these remain. Your job is to rewrite the specific sentences that contain them, preserving the post/brief's argument. Do NOT return the draft until every listed violation is gone. After your rewrite, re-check mentally against each rule."

Then re-run `kill-list-regex.sh` locally after the LLM finishes. **If it still fails, run a second LLM revision iteration** — the skill can iterate until clean, up to `max_iter=2`. If iter-2 still fails, mark `.status=rejected-kill-list` and let ship step abort — that's a surfacing mechanism so we know the pattern needs a clean_text.py fix.

### Step 3: Build revise prompt for posts

```
Apply council corrections to the 3 LinkedIn post options. Do NOT rewrite the briefing (separate step). Focus entirely on improving the posts.

RULES FOR REVISION:
- Keep each option's core template + angle (if it was personal-discovery, keep it personal-discovery)
- Fix ONLY what council flagged — don't re-write good parts
- NEVER use em dashes. Use commas, periods, or "..." instead.
- Preserve conviction statements unless council flagged them as false/unverifiable
- Hook revisions: new hook must still follow same hook pattern (A-J) unless council said pattern itself was wrong

**AAYUSH VOICE SCORE (check council-notes for per-option score and lowest_dimension)**
If any option scored < 8/10 on the Aayush voice score, the `lowest_dimension` field tells you exactly what to fix. Apply these fixes first, before any other revision:
- first_person_observer low → add "Every week i watch..." or "i've been thinking about..." or "Every team i talk to..." somewhere natural
- hedge_markers low → add one IMO, i think, or i doubt where Aayush shifts from fact to opinion
- contrast_labels low → add "That's X." after the key insight, or "That's not X. That's Y." to flip the frame
- fragment_paragraphs low → break compound sentences into one-idea-per-line rhythm
- specific_named_details low → replace any generic "companies" or "founders" with actual names and numbers from the brief

**PRIMARY SOURCES (read before fixing):**
- `config/brief-blueprint.md` — voice truth for briefs. Every rewrite serves a specific blueprint rule. Cite the rule when explaining the fix.
- `config/post-blueprint.md` — voice truth for posts. Same.
- `history/feedback-log.jsonl` — most recent feedback entries surface latest direction.

DETERMINISTIC HARD BLOCKERS — rewrite every sentence containing these, ZERO tolerance. The ship step's regex gates WILL reject the brief/posts if ANY remain:

- **em dashes (U+2014)** → use commas, periods, or "..."
- **"It's like X"** / "Think of it as Y" / any analogy-as-declaration → replace with a direct parallel claim ("Same sticker price. What you get for it changed.") or a rhetorical question ("what are you actually paying for?"). NEVER keep the analogy.
- **"moat" / "moats"** → name the specific thing ("Canva's 100M user base", "Tesla's Texas-only focus", "their distribution") or use "the thing competitors can't copy". If you can't name it specifically, the claim probably isn't defensible and should be cut.
- **"differentiator" / "differentiation" / "differentiate"** → "what makes you different" OR name the specific advantage ("owning the design tools", "having the users")
- **"commoditization" / "commoditize"** → "everyone can buy it now" / "it's cheap now"
- **"table stakes"** → "everyone has it" / "it's not special anymore"
- **"up the stack" / "moves up the stack"** → "to apps" / "to the product" / "to what the user touches"
- **"[Not X, it's Y]" inversions** — ZERO (not max 1). Patterns: "isn't X. It's Y" / "aren't A. They're B" / "stopped being X. It's becoming Y". Use direct declarative or parallel structure.
- **Long sentences (>22 words)** — split into 2+ sentences
- **Guru voice** ("founders should", "builders who", "teams who want to win") → first-person observation
- **Hashtags at end of post** → remove entirely
- **Uppercase "I" in posts** → lowercase "i" (voice rule)
- **Posts under 1,300 chars** — expand with one more specific fact, named number, or personal beat. NEVER pad with filler. If you can't add real substance, the post isn't ready. posts-gate.sh hard floor is 1,300 — under that, the run fails.

After rewriting, mentally re-check each deterministic finding. If you can't mark all as fixed, rewrite again before returning. The ship step runs the exact same regex tests and aborts delivery if any remain.

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

### Step 4: Call Opus via proxy

```bash
curl -sS -X POST "${LLM_PROXY_BASE_URL}/v1/chat/completions" \
  -H "Authorization: Bearer ${ATLAN_LLM_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg model "claude-opus-4-7" --arg prompt "$REVISE_PROMPT" \
    '{model: $model, messages: [{role: "user", content: $prompt}], temperature: 0.4, max_tokens: 4000}')"
```

### Step 5: Parse + write revised posts.md

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

### Step 6: Revise brief.md if needed

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

### Step 7: Handoff back to orchestrator

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
