# Post feedback design doc — 2026-04-28 (20M Copilot, $0 inference)

**Source:** `aayush-direct-write` — Aayush wrote and shipped this himself; no pipeline draft.

**Slug:** `20m-copilot-zero-cost`

**Companion design doc:** `config/post-feedback-2026-04-28.md` (earlier ingest of `openai-50b-anywhere` from the same day).

---

## Gap analysis

No pipeline draft exists. Comparison happens against the corpus, not against pipeline output. The post is the second Aayush-direct-write of 2026-04-28 — a rare two-in-a-day cadence — and it shares a register with `openai-50b-anywhere` (Register A-without-Atlan, observer-mode, single-blank spacing, no p.s., no unicode-bold).

The structural significance of this post: it stacks **four single-sighting devices** ("Two narratives died in that sentence." / "The first: ... / The second: ..." / period-separated 3-noun-phrase fragment ("The wrapper layer. The orchestration layer. The thin agent on top of GPT.") / "All of it.") in one ship. None of these had any prior corpus instance. The 2026-04-24 cautionary tale (promoted 5 devices from one post, all failed corpus check) means we annotate, do not promote, until a 2nd sighting lands.

The post also does work that has 2+ corpus sightings — and those promote.

---

## Corpus counts — every candidate pattern

Counts: corpus = `/Users/aayush.maheshwari/Desktop/Aayush/all_posts.md` (4 finalized main-corpus posts) + `config/aayush-ai-post-examples/*.md` (existing anchors). The new anchor file is excluded from the count of "prior corroborations." Total prior corpus = 6 anchors. Including this post = 7.

| # | Candidate device | Corpus prior | This post | TOTAL | Verdict |
|---|---|---:|---:|---:|---|
| 1 | Two-line binary opener (Pattern A.b) | 3 (Post 4, jagged-frontier, openai-50b-as-closer) | 1 (opener) | **4/7** | **CONFIRMED — already promoted; bump citation 3/6 → 4/7** |
| 2 | Quote-as-paragraph-opener | 1 (openai-50b `"We run on Azure."`) | 1 (`"We fully plan to exploit it"`) | **2/7** | **PROMOTE — graduates from single-sighting to confirmed** |
| 3 | Hyphen-bullet 3-item list | 5 of 6 prior corpus | 2 lists (3-item each) | **6/7 posts use** | **CONFIRMED — already core; reaffirm** |
| 4 | Two hyphen-bullet 3-item lists in same post | 2 prior (agent-stack-hardening, every-saas-ai-button-stacks-multiple) | 1 (this post) | **3/7** | **CONFIRMED as a workhorse pairing — covered by existing rule, no new edit needed** |
| 5 | "Two narratives died in that sentence." meta-thesis-naming reset | 0 | 1 | **1/7** | **LOW — single-sighting. ANNOTATE.** |
| 6 | "The first: ... / The second: ..." enumerated-thesis split | 0 | 1 | **1/7** | **LOW — single-sighting. ANNOTATE.** |
| 7 | Period-separated 3-noun-phrase fragment stack ("The wrapper layer. The orchestration layer. The thin agent on top of GPT.") | 0 | 1 | **1/7** | **LOW — single-sighting. ANNOTATE.** |
| 8 | "All of it." 3-word recap-tag | 0 | 1 | **1/7** | **LOW — single-sighting. ANNOTATE.** |
| 9 | Numeric-anchor lede (Pattern A.c) — non-dollar variant ("20 million people") | 0 (A.c is $-figure-only in 2 prior posts) | 1 | **1/7** non-$ | **LOW — do not broaden A.c yet. ANNOTATE on anchor.** |
| 10 | Wider paragraph spacing (Register B variant) | 2 (GPT-5.5, openai-50b) | 0 (single-blank throughout) | **2/7** | **No bump — count unchanged** |
| 11 | Specific present-tense closing question | 6 of 6 prior | 1 | **7/7** | **CONFIRMED — already core, no edit** |
| 12 | Operator-living-the-problem voice WITHOUT Atlan name-drop | 1 (openai-50b) | 1 | **2/7** | **NOTABLE — already flagged in README as "track" register; second instance bumps it** |

---

## Proposed blueprint edits — corpus-tagged

### HIGH CONFIDENCE — APPLY

**Edit A — Bump Pattern A.b citation count (3/6 → 4/7).**

- Evidence: this post is the 4th corpus instance of two-line binary. Already a confirmed pattern.
- Propagation map (hook sub-pattern citation):
  - `config/post-blueprint.md` §"Pattern A.b" — citation count + new example
  - `.claude/skills/write-posts/SKILL.md` §"5 hook patterns" — bump count + add example
  - `.claude/skills/write-posts/references/hooks.md` §"Pattern A.b" — bump count + add example
  - `.claude/skills/write-posts/references/post-templates.md` §"news-take" — note A.b can OPEN (not just close) when the news has a paid-vs-free / someone-pays-someone-doesn't asymmetry

**Edit B — Promote quote-as-paragraph-opener from single-sighting to confirmed device (2/7).**

- Evidence: `"We run on Azure."` (openai-50b, 2026-04-28) + `"We fully plan to exploit it"` (this post, 2026-04-28). Both Register B / Register-A-without-Atlan posts. Both load-bearing — the quote does work the prose can't.
- This is a structural / voice device, not a hook sub-pattern. Propagation map (cadence + voice rule):
  - `config/post-blueprint.md` — new sub-section under structural devices, before "Wider paragraph spacing"
  - `config/post-blueprint.md` §"Available devices (pick per mode)" list — add an entry
  - `.claude/skills/write-posts/references/voice.md` — new "Rhythm device: quote-as-paragraph-opener" sub-section
  - `.claude/skills/write-posts/references/post-templates.md` §"news-take" — add as a "Reach-for device" line because news-take is the template most likely to surface a load-bearing executive quote
  - `config/aayush-ai-post-examples/README.md` — note the device under Register A-without-Atlan as a shared marker between the two anchors

### LOW CONFIDENCE — PARK (do not edit blueprint)

These all sit at 1/7. Annotate on the anchor file (already done in `20m-copilot-zero-cost.md` §"Structural devices worth naming"). Do not promote.

| Device | Sightings | Action |
|---|---:|---|
| "Two narratives died in that sentence." meta-thesis-naming reset | 1/7 | Park. Watch for 2nd. |
| "The first: ... / The second: ..." enumerated-thesis split | 1/7 | Park. Watch for 2nd. |
| Period-separated 3-noun-phrase fragment stack | 1/7 | Park. Watch for 2nd. |
| "All of it." 3-word recap-tag | 1/7 | Park. Distinct from concept-naming "That's X." pattern. |
| Numeric-anchor lede with NON-dollar number | 1/7 | Park. Pattern A.c stays $-figure-only until 2nd non-$ instance lands. |

If two of these recur in the next 2-3 posts, revisit and promote whichever clears the 2-sighting bar first.

---

## Hard-gate updates

None proposed. Post passes existing gates locally (no em dashes, no markdown bold, no `[Not X, it's Y]` inversion, no "It's like X" analogy, no hashtags). The single-sighting devices that we parked (period-separated noun-phrase fragments, "All of it." recap-tag) are NOT close enough to existing AI-tells that the gate would mistakenly fire on them. No regex changes required.

One observation worth flagging for future hard-gate consideration: **"All of it." as a 3-word standalone paragraph** is a rhetorical sweep-up move. If pipelines start over-using it as a 4th-or-5th "That's X." substitute, it could become an AI-tell. For now, single corpus instance → no gate.

---

## Open questions (flag for next 2-3 posts)

1. **Will the meta-thesis-naming reset ("Two narratives died in that sentence.") recur?** It's a powerful structural beat — naming the rhetorical move ABOUT to happen — but it's also very specific. Post-specific ornament or repeatable device?
2. **Will "The first: / The second:" enumerated-thesis split recur?** Distinct from 3-pillar lists with "That's X." tags. Watch.
3. **Will "All of it." earn a 2nd sighting?** It functions like "That's X." but sweeps rather than names. Worth tracking.
4. **Numeric-anchor lede generalization.** Pattern A.c is currently $-figure-only. The 20M-Copilot opener uses a non-$ count ("20 million people"). If a 2nd non-$ numeric opener lands, broaden A.c to "specific-number lede with paradoxical line 2."
5. **Register A-without-Atlan promotion to its own register?** Now 2 anchors (openai-50b + this). The README still flags it as "track / a Register A variant." A 3rd anchor would graduate it.
6. **Quote-as-paragraph-opener — same-day clustering coincidence?** Both 2/7 instances dropped on the same date. Watch whether this device persists into next week's posts or whether it was a same-news-cycle artefact.

---

## Edits applied this commit

- `history/feedback-log.jsonl` — entry appended (Phase 1)
- `config/aayush-ai-post-examples/20m-copilot-zero-cost.md` — new few-shot anchor (Phase 2)
- `config/post-blueprint.md` — Pattern A.b citation bumped (3/6 → 4/7) with new example; new "Quote-as-paragraph-opener" sub-section under structural devices; "Available devices" list updated
- `config/aayush-ai-post-examples/README.md` — Register A-without-Atlan section updated to 2 anchors with shared device list
- `.claude/skills/write-posts/SKILL.md` — Pattern A.b list bumped to 4/7 with new example
- `.claude/skills/write-posts/references/hooks.md` — Pattern A.b citation bumped to 4/7 with new example
- `.claude/skills/write-posts/references/voice.md` — new "Rhythm device: quote-as-paragraph-opener" sub-section
- `.claude/skills/write-posts/references/post-templates.md` — news-take template updated; A.b noted as opener variant; quote-as-paragraph-opener added as Reach-for device

## Edits parked (single-sighting, do not apply)

- "Two narratives died in that sentence." meta-thesis-naming reset (1/7)
- "The first: ... / The second: ..." enumerated-thesis split (1/7)
- Period-separated 3-noun-phrase fragment stack (1/7)
- "All of it." 3-word recap-tag (1/7)
- Numeric-anchor lede with non-dollar number — pattern A.c broadening (1/7 non-$)

## Anti-patterns avoided this iteration

- Did NOT promote the 4 single-sighting structural devices to first-class status (the 2026-04-24 mistake repeated would have been: promoting "Two narratives died", "The first/The second", noun-phrase fragments, and "All of it." all at once based on this single post).
- Did NOT broaden Pattern A.c just because the new opener is "numeric-anchor + paradoxical line 2." The shape is similar, but the corpus has only 1 non-$ instance; A.c stays $-figure-only.
- Counted before editing. Quote-as-paragraph-opener earned promotion because it now has 2 corpus sightings on 2 separate finalized posts (openai-50b + this), not 1+ "this feels like a pattern" vibes.
- Walked the propagation map for both HIGH CONFIDENCE edits across blueprint, SKILL.md, hooks.md, voice.md, post-templates.md, and README.md.
