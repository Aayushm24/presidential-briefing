# post-feedback — ingest a finalized Aayush post and update voice truth

Aayush shares a LinkedIn post he wrote or heavily edited himself. This skill runs the full learning loop: logs it as voice-truth feedback, creates a few-shot anchor, compares against the current blueprint, applies evidence-backed edits, and commits. Models the workflow from 2026-04-24 (GPT-5.5 post) as a repeatable skill.

This is the inverse of `/write-posts`. Write-posts produces candidates from a brief. Post-feedback ingests what Aayush actually shipped and uses it to re-calibrate the pipeline.

## Invocation

```
/post-feedback <file-path-or-pasted-text>
```

If the argument is a path (ends in `.md` / `.txt`), read it. Otherwise treat as the post text. Paths like `~/Desktop/Aayush/all_posts.md` containing multiple posts → ask which one.

## Inputs (read FIRST, always)

- The finalized post (the argument).
- `config/post-blueprint.md` — current voice rules, latest-of-latest.
- `config/aayush-ai-post-examples/` — existing few-shot anchors + README.
- `history/feedback-log.jsonl` — last ~10 entries so the new entry sits in context.
- `config/post-corpus-analysis-*.md` (if any exist) — prior corpus-wide analyses.
- `.claude/skills/write-posts/SKILL.md` + `references/voice.md` — so edits can flow into the SKILL if a rule needs softening or a hard-gate needs adding.

## The iron law — evidence over enthusiasm

A single post is **one data point**. Most of what feels like a new pattern in a single post is post-specific ornament, not a repeatable voice move. Before promoting anything to first-class status:

1. **Count across the corpus**, not just the new post. Use `config/aayush-ai-post-examples/` + `/Users/aayush.maheshwari/Desktop/Aayush/all_posts.md` when available.
2. **A pattern needs 2+ corroborating sightings** before it's promoted to "reach-for."
3. **Single-post devices are annotated with a count** (`0 of N corpus posts use this — single-sighting, experimental`) so future-you doesn't forget.
4. **If a new post contradicts a blueprint rule**, update the rule. Do not defend the rule against the evidence.

The 2026-04-24 session is a cautionary tale: I promoted Pattern E, the `↓` arrow, "That's a tell.", "My take is", and vulnerability-in-closer based on one post. The corpus-analysis pass caught that **none of these appeared in Aayush's 4 finalized corpus posts** and had to roll them back. The cost of over-promotion is a pipeline that drifts toward ornament with every new post. Run the corpus check on every ingest.

## Phase 1 — Log the post as feedback

Append a single JSON line to `history/feedback-log.jsonl`:

```jsonc
{
  "date": "YYYY-MM-DD",
  "surface": "posts",
  "what": "<1-2 sentence summary of what Aayush did different from pipeline, IF pipeline produced a version of this post>",
  "why": "<1-2 sentences on why his version works better — rhythm, observation, stakes>",
  "outcome": "<concrete voice directions extracted: 4-6 bullets of specific rules the pipeline should follow>",
  "source": "aayush-direct-write",   // or "aayush-edit" if it was a pipeline post Aayush rewrote
  "post_text": "<full post verbatim, preserve line breaks as \\n>"
}
```

**`source` taxonomy:**
- `aayush-direct-write` — Aayush wrote this himself, pipeline didn't contribute. **Highest weight.**
- `aayush-edit` — pipeline wrote a candidate, Aayush edited it before posting. High weight.
- `pipeline-shipped` — shipped exactly as pipeline wrote it. Lower weight (still useful for calibration).

## Phase 2 — Create a few-shot anchor

Write `config/aayush-ai-post-examples/<slug>.md`. Slug should be 3-6 words hyphenated, matching the post's hook or central image (e.g. `gpt-55-my-feed-is-doing-the-thing`, `every-saas-ai-button`).

**File structure** (see existing examples for the format — don't deviate):

```markdown
# Example: <Title — short phrase from the post>

## Context

- **Date written:** YYYY-MM-DD
- **Theme:** <1-sentence topic>
- **Trigger:** <news event or observation that prompted the post>
- **Why this matters as an anchor:** <1-2 sentences on what the post proves about Aayush's voice>

## Post (verbatim, preserve line breaks)

```
<full post>
```

## Structural devices worth naming

Numbered list. For each device:
- Name it in 2-5 words (e.g. "Named-source pivot", "Unresolved closer").
- Give the exact line from this post that demonstrates it.
- Say when to reach for it (1 sentence).

## Things this post does NOT do (anti-patterns to avoid)

Bullet list of what this post explicitly skips (no p.s., no unicode bold, no Atlan mention, etc.) so the few-shot model knows which defaults to override.

## When to copy this post's structure

Bullet list of story types where this anchor applies. Be specific.

## Engagement (to be filled)

- **Posted:** TBD
- **Engagement:** TBD
- **Annotation:** <note anything worth measuring>
```

## Phase 3 — Corpus check (before proposing edits)

**Mandatory.** Run empirical counts before writing any blueprint edit.

```bash
# For each candidate "new pattern" the post seems to demonstrate,
# grep the corpus file and count.
grep -c "<pattern>" /Users/aayush.maheshwari/Desktop/Aayush/all_posts.md
# Also check existing few-shot anchors
grep -c "<pattern>" config/aayush-ai-post-examples/*.md
```

For each proposed new pattern, write one line of evidence:

> `"My take is"` — 0 hits in 4-post corpus, 1 hit in the new post. **Single-sighting. Annotate, do not promote.**

> `Hyphen-bullet 3-item list` — 4 of 4 corpus posts. **Already a core device. Promote.**

Only **2+ corroborating sightings** clear the bar for first-class status. Otherwise: annotate as experimental with the count.

## Phase 4 — Propose + apply edits

Write a short design doc (≤800 words) to `config/post-feedback-<DATE>.md` covering:

1. **Gap analysis** — if pipeline produced a version of this post, quote both and name the deltas.
2. **Proposed blueprint edits** — each one tagged with corpus-count evidence. HIGH CONFIDENCE (2+ corroborations): apply directly. LOW CONFIDENCE (single sighting): annotate only, do not edit.
3. **Hard-gate updates** — if the post reveals a rule that should be enforced by `tests/posts-gate.sh` (e.g. banned phrase, character cap), propose the regex/threshold.
4. **Open questions** — things that need 2-3 more posts before resolving.

Then **apply the HIGH CONFIDENCE edits** to:
- `config/post-blueprint.md`
- `.claude/skills/write-posts/SKILL.md`
- `.claude/skills/write-posts/references/voice.md`
- `tests/posts-gate.sh` (only if adding a deterministic gate)
- `config/aayush-ai-post-examples/README.md` if a new register or pattern class needs naming

Do NOT apply LOW CONFIDENCE edits. Park them in the design doc with the corpus count.

## Phase 5 — Verify + commit

```bash
# Gates still pass on known-good content
bash tests/posts-gate.sh workspace/*/posts.json
bash tests/kill-list-regex.sh workspace/*/brief.md
bash tests/golden-format.sh workspace/*/brief.md
```

Commit with a structured message:

```
feedback: ingest <slug> as voice-truth (source: aayush-direct-write)

- history/feedback-log.jsonl entry appended
- config/aayush-ai-post-examples/<slug>.md added as few-shot anchor
- blueprint edits applied: <list of patterns, with corpus counts>
- blueprint edits PARKED (single-sighting): <list>
- gate changes: <if any>

Full analysis: config/post-feedback-<DATE>.md
```

Push to main.

## Outputs — full list

- [ ] `history/feedback-log.jsonl` — 1 new line
- [ ] `config/aayush-ai-post-examples/<slug>.md` — new file
- [ ] `config/post-feedback-<DATE>.md` — design doc (keep all of them, they're the audit trail)
- [ ] `config/post-blueprint.md` — edited if corpus evidence supports it
- [ ] `.claude/skills/write-posts/SKILL.md` — edited if a rule in the SKILL needs softening or a worked example added
- [ ] `.claude/skills/write-posts/references/voice.md` — edited if a line contradicts the new evidence
- [ ] `tests/posts-gate.sh` — edited only to add deterministic gates
- [ ] `config/aayush-ai-post-examples/README.md` — edited only if a new register/pattern class emerged

## Anti-patterns (what went wrong on 2026-04-24)

1. **Promoted 5 devices from a single post.** All 5 failed the corpus check and had to be rolled back.
2. **Did not run the corpus check before writing blueprint edits.** Ran it after, via a separate agent. Invert that next time — count first, edit second.
3. **Conflated "this post uses X" with "this is a repeatable pattern."** A post can do something unique; that doesn't mean it's a pattern.
4. **Over-weighted ornament** (↓ arrow, "That's a tell.", unicode-bold fabrications) vs **under-weighted structure** (At Atlan mid-post beat, hyphen-bullet lists, closing-question rule). The structural stuff was in every corpus post — the ornament was in one.

## Invocation checklist (for future-me)

- [ ] Read the post. Read the current blueprint. Read last ~10 feedback entries.
- [ ] Phase 1: append feedback-log entry.
- [ ] Phase 2: write few-shot anchor.
- [ ] Phase 3: run corpus counts on every candidate pattern. **Do not skip.**
- [ ] Phase 4: design doc + apply HIGH CONFIDENCE edits only.
- [ ] Phase 5: verify gates + commit + push.
- [ ] Tell Aayush: what was applied, what was parked, any open questions.

## See also

- `config/post-corpus-analysis-2026-04-24.md` — example of a corpus-wide analysis run (read this before proposing any wide blueprint edits).
- `config/post-redesign-2026-04-24.md` — example of the single-post design doc (Phase 4 output).
- `/design-council` — the sibling skill that produces creatives for a post.
