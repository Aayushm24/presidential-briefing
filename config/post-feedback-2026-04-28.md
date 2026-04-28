# Post feedback design doc — 2026-04-28 (OpenAI $50B anywhere)

**Source:** `aayush-direct-write` — Aayush wrote and shipped this himself; no pipeline draft.

**Slug:** `openai-50b-anywhere`

---

## Gap analysis

No pipeline draft exists for this post. Aayush wrote it directly. Comparison happens against the corpus, not against pipeline output.

---

## Corpus counts — every candidate pattern

Counts: `corpus = /Users/aayush.maheshwari/Desktop/Aayush/all_posts.md` (4 finalized posts) + `config/aayush-ai-post-examples/*.md` (existing anchors). The new post's anchor file is excluded from the count of "prior corroborations."

| # | Candidate device | Corpus count (excl. new) | New post | TOTAL prior+new sightings | Verdict |
|---|---|---:|---:|---:|---|
| 1 | `"Read that again."` one-line meta-CTA | 0 | 1 | 1 | **LOW — single-sighting** |
| 2 | `"Wait what does this even mean?"` rhetorical reset | 0 | 1 | 1 | **LOW — single-sighting** |
| 3 | Three-blank-line paragraph spacing (4+ consecutive newlines) | **19 inside GPT-5.5 anchor**, 0 in main corpus | many | **2 corpus posts** | **HIGH — confirmed (GPT-5.5 + OpenAI-50B)** |
| 4 | Quote-as-paragraph-opener (standalone short quoted line) | 0 | 1 | 1 | **LOW — single-sighting** |
| 5a | `"by an order of magnitude"` intensifier | 0 | 1 | 1 | **LOW — single-sighting** |
| 5b | `"by a mile"` intensifier | 0 | 1 | 1 | **LOW — single-sighting** |
| 6 | Numeric-anchor lede (`$N` in first sentence + paradox) | 1 (Post 1: $9M Gitar) | 1 | **2** | **HIGH — confirmed (Gitar + OpenAI-50B)** |
| 7 | Two-line binary closer | 1 corpus post (Post 4 "Everyone has Claude Code") + 1 anchor (jagged-frontier) | 1 | **3** | **CONFIRMED — already in blueprint, reaffirmed** |
| 8 | Closing question ending in `?` | 2 of 4 main-corpus posts + 2 of 2 Register B anchors = 4/6 | 1 | 5/7 | **CONFIRMED — already in blueprint** |
| 9 | `Not because X. Because Y.` causal three-beat | 0 | 1 | 1 | **LOW — single-sighting** |

(Notes on count methodology: pattern 3 was not visible to a regex on `all_posts.md` directly because that file's posts use single-blank-line spacing. The triple-blank-line pattern shows up in the GPT-5.5 anchor's preserved verbatim post block, where Aayush actually wrote 4+ consecutive newlines between paragraphs. Two finalized posts use it — promotion threshold met.)

---

## Proposed blueprint edits — corpus-tagged

### HIGH CONFIDENCE — APPLY

**Edit 1. Promote three-blank-line spacing as an option for news-commentary posts.**

- Evidence: 2 corpus posts (GPT-5.5 + OpenAI-50B) use deliberate triple-blank-line spacing where the surrounding corpus uses single-blank.
- Threshold (2+) met.
- Edit target: `config/post-blueprint.md` §"Default cadence: one sentence per paragraph" — add a sub-section noting that for news-commentary in Register B, paragraph spacing can stretch to 2-3 blank lines deliberately (i.e. `\n\n\n` or `\n\n\n\n` between paragraphs in source). Do NOT promote as a default for all posts — single-blank is still the corpus norm in Register A (Posts 1-4 in main corpus all use single-blank).

**Edit 2. Document numeric-anchor lede as a confirmed opener variant.**

- Evidence: Post 1 (`Someone raised $9M just to babysit AI-generated code.`) + this post (`OpenAI just paid $50 billion to give up their biggest moat.`) = 2 corpus posts.
- Threshold (2+) met.
- Edit target: `config/post-blueprint.md` §"Hook patterns" — add as a noted variant under Pattern A (or as Pattern A.c). The lede is `[$ figure] [verb] [paradoxical purpose]`. Distinct from two-line binary because the punch is in line 1, not in the contrast between lines 1 and 2.

**Edit 3. Reaffirm two-line binary closer (already promoted).**

- Already at Pattern A.b in blueprint with 2/5 corpus citation. This post adds a third instance (`That second question used to have one answer per cloud. / Now it has one answer, period.`).
- No new edit needed — bump the citation count from 2/5 to 3/6 in the blueprint annotation.

### LOW CONFIDENCE — PARK (do not edit blueprint)

**Edit 4. Quote-as-paragraph-opener (`"We run on Azure."` standalone).** 0 prior corpus, 1 sighting. Park.

**Edit 5. One-line meta-CTAs (`Read that again.` / `Wait what does this even mean?`).** Both 0 prior corpus, 1 sighting. Park. These are powerful when they work, but a single post is not enough evidence — they could be ornament that Aayush will not repeat.

**Edit 6. Conversational intensifiers (`by an order of magnitude`, `by a mile`).** Both 0 prior corpus, 1 sighting. Park. Risk: these are casual hyperbole that the kill-list could absorb if they become ornament-only.

**Edit 7. `Not because X. Because Y.` causal three-beat.** 0 prior corpus, 1 sighting. Park. Note proximity to existing `[Not X, it's Y]` AI-tell — this variant is causal not contrastive (different shape) and shouldn't trigger the kill-list. But until 2nd corpus instance, it's a single observation.

---

## Hard-gate updates

None proposed. Post passes existing gates locally. No new banned patterns surfaced. The `Not because X.` variant is causal, not contrastive — should not trigger `tests/posts-gate.sh`'s AI-tell inversion regex (which targets same-subject `not X, it's Y` constructions).

---

## Open questions (flag for next 2-3 posts)

1. **Will quote-as-paragraph-opener recur?** A standalone quoted phrase (`"We run on Azure."`) sitting between lede and bridge is a powerful opener. Watch for second sighting.
2. **Will meta-CTA one-liners (`Read that again.`, `Wait what does this even mean?`) recur?** These break the fourth wall. Worth tracking — could be a Register B device that earns its place over multiple posts.
3. **Are the conversational intensifiers (`by an order of magnitude`, `by a mile`) durable?** If Aayush keeps using these, they're voice; if they only appeared this once, they're ornament. Re-check on next post.
4. **Register A without Atlan name-drop.** This post has Aayush-as-operator-living-the-problem (`every conversation I've had for 3 months`) but no `at Atlan we…` beat. Is this a 3rd register, or a Register A variant? Watch.

---

## Edits applied this commit

- `history/feedback-log.jsonl` — entry appended (Phase 1)
- `config/aayush-ai-post-examples/openai-50b-anywhere.md` — new few-shot anchor (Phase 2)
- `config/post-blueprint.md` — three-blank-line spacing variant added under cadence section; numeric-anchor lede added under hook patterns; two-line binary citation bumped to 3/6
- `config/aayush-ai-post-examples/README.md` — note 6th anchor and Register A-without-Atlan variant

## Edits parked (single-sighting, do not apply)

- Quote-as-paragraph-opener (0 prior, 1 new = 1 total)
- `Read that again.` one-line meta-CTA (0 prior, 1 new = 1 total)
- `Wait what does this even mean?` rhetorical reset (0 prior, 1 new = 1 total)
- `by an order of magnitude` intensifier (0 prior, 1 new = 1 total)
- `by a mile` intensifier (0 prior, 1 new = 1 total)
- `Not because X. Because Y.` causal three-beat (0 prior, 1 new = 1 total)

## Anti-patterns avoided this iteration

- Did NOT promote the 5-6 single-sighting devices to first-class status (the 2026-04-24 mistake).
- Did NOT conflate "this post does X" with "X is a repeatable pattern" — only patterns with 2+ sightings made the blueprint.
- Counted before editing. The promotions (three-blank-line spacing, numeric-anchor lede) are both backed by a second corpus post each, not vibes.
