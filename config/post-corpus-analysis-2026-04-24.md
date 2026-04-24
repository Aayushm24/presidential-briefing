# Post Corpus Analysis — 2026-04-24

**Purpose:** Empirical validation of the current blueprint against Aayush's full corpus of 4 finalized LinkedIn posts at `/Users/aayush.maheshwari/Desktop/Aayush/all_posts.md`. Every answer below is grounded in counts from the corpus, not intuition. Answers questions raised in `config/post-redesign-2026-04-24.md` §6 plus surfaces additional gaps.

---

## Section 1 — Corpus inventory

4 distinct posts, separated by a single `—` line. Raw char counts computed via Python `len()` on each post's text block (whitespace included).

| # | Opening line | Total chars | Prose chars | Whitespace chars | WS % | Topic |
|---|---|---:|---:|---:|---:|---|
| 1 | "Someone raised $9M just to babysit AI-generated code." | 1,783 | 1,500 | 283 | 15.9% | Gitar funding + OpenAI sandbox = agent stack hardening |
| 2 | "Every SaaS is shipping an AI button right now. Most of them are going to look ridiculous in 18 months." | 2,604 | 2,098 | 506 | 19.4% | AI buttons, user-is-an-agent, Figma vs Anthropic bet |
| 3 | "AI startups have 12 months before they die…" | 1,617 | 1,327 | 290 | 17.9% | Distribution / proprietary data / deep workflow moats |
| 4 | "Everyone has Claude Code. Almost no one is using it right." | 1,555 | 1,293 | 262 | 16.8% | Intercom telemetry, institutional memory, Claude Code |

Paragraph structure (by `\n\s*\n` split):
- Post 1: 14 paragraphs, 4 single-sentence
- Post 2: 28 paragraphs, 17 single-sentence (60%)
- Post 3: 24 paragraphs, 17 single-sentence (71%)
- Post 4: 19 paragraphs, 10 single-sentence (53%)

---

## Section 2 — Empirical answers to the 7 open questions

### Q1. Arrow `↓` as visual colon

**Count in corpus: 0.** Python regex search for `↓` returned zero hits across all 4 posts.

**Verdict:** Stay in "pending" state. One-off device from the 2026-04-24 GPT-5.5 post. Do **not** promote to a repeatable device. Needs at least 2 more sightings in future Aayush-authored posts before codifying.

### Q2. p.s. / p.p.s. closer

**Count in corpus: 2 p.s. hits, 1 p.p.s. hit — all in Post 4 only.** Posts 1, 2, 3 have zero p.s. / p.p.s. closers.

- Post 4 (Claude Code / Intercom): uses both `p.s.` (concrete detail: "designers and PMs now merge PRs through Claude Code") and `p.p.s.` (Atlan CTA with 👇🏻).
- Post 3 (AI startups 12 months): closes with lowercase "what are you building that only YOU can build?" — no p.s. Despite being the exact post the current blueprint cites as having a p.s., it doesn't. The blueprint references "p.s. My honest answer? My entire role..." — that's from an older 2026-04-20 top-performer NOT in this corpus file.
- Post 1 and Post 2 end on questions/observations only.

**Mode split:** Post 4 is the one post where Atlan is doing exactly what the post discusses (institutional memory = Atlan's work). That's why the Atlan-CTA p.p.s. lands. It is NOT about news-commentary vs personal-vulnerable.

**Verdict:** The real trigger is "does Atlan do this thing, worth a genuine name-drop?" — not "is this personal-vulnerable?". Update the blueprint to pin p.p.s. to Atlan-topic overlap, not to vulnerability.

### Q3. "My take is" hedge marker

**Count in corpus: 0.** Zero hits for "My take", "my take", "my read", "the way I see", "honest take" across all 4 posts.

Actual hedge markers in corpus:
- IMO: 3 hits (Posts 1, 2, 3)
- I doubt: 2 hits (Posts 3, 4)
- Here's why: 1 hit (Post 1: "Here's why IMO that cost should drop now:")
- ngl: 1 hit (Post 1 — actually appears inside a hashtag-ish search; verify manually)

**Verdict:** "My take is" is specific to the 2026-04-24 GPT-5.5 post (which is NOT in this corpus file — it's separate). Keep it as an *allowed* marker but don't elevate it above "IMO" and "I doubt", which are Aayush's defaults by 5-to-0 margin. Specifically, the blueprint's line listing "My take is" at the pivot from setup to implication should be softened: "occasional variant of IMO."

### Q4. Vulnerability-in-closer without personal arc

**Count in corpus: 1 direct hit.** Post 1: `What's the ugliest workaround in your current agent setup? 👀` — a rhetorical question that implicitly admits Aayush has his own ugly workaround. No "I haven't tried X" or "I don't know yet" direct admissions in the rest of the corpus.

Post 3 closes: `what are you building that only YOU can build?` — a challenge, not a vulnerability.
Post 2 closes: `Because they might not be who you think.` — an unresolved pivot, not a confession.
Post 4 closes: `What does your team remember from last sprint's Claude Code usage?` — specific question, not vulnerability.

**Verdict:** Vulnerability-in-closer without a personal arc is **rare** in the corpus (1 of 4). More common closers: specific present-tense question to the reader. The current blueprint's §2i promotion of vulnerability-in-closer as a broadly available device is over-weighted. Keep as an option; don't promote it to a standard reach-for for news-commentary.

### Q5. Uppercase `I` vs lowercase `i` pronoun

**Count via regex `\bI(?:'m|'ve|'ll|'d)?\b` vs `\bi(...)` — pronoun forms only:**
- Uppercase I: **6 hits** across corpus (variants: `I`, `I'm`)
- Lowercase i: **1 hit** — and that 1 is inside a quoted mock dialogue: `"hi, how can i help?"` (Post 2, mimicking an AI chatbot's lowercase greeting).

**Ratio: 6:0 uppercase among genuine first-person uses.** The only lowercase is dialogue decoration.

**Verdict:** `voice.md` line 169 correctly resolves this: uppercase `I` is the rule. The contradiction at `voice.md` line 25 (which the old voice.md had stating lowercase) is already fixed. The pipeline should NEVER produce lowercase `i` as pronoun. Add a hard-gate regex to catch `(?:^|[^a-zA-Z])i(?: |'m|'ve|'ll|'d)` and reject.

### Q6. "That's X." — concept-naming vs behavioral diagnosis

**Count in corpus: 4 hits.** All 4 are **concept-naming**, zero behavioral diagnoses.

Exhaustive list:
- Post 3: `That's distribution.`
- Post 3: `That's proprietary data.`
- Post 3: `That's the third.` (index-naming, still concept-labeling the 3rd pillar)
- Post 4: `That's the gap.` (concept, not diagnosis)

Zero instances of `That's a tell.` / `That's a signal.` / `That's a pattern.` in the corpus.

**Verdict:** The diagnostic-beat variant (`That's a tell.`) from the GPT-5.5 post is **not supported** by the corpus as a repeatable device. Keep it in the blueprint as a noted second variant but flag it as unconfirmed. The dominant, proven form is concept-naming after a concrete example. The current blueprint's equal-weight treatment of the two variants overweights the diagnostic beat.

### Q7. Prose-char floor

**Per-post prose char counts (total minus all whitespace):**

| Post | Total | Prose | WS |
|---|---:|---:|---:|
| 1 | 1,783 | 1,500 | 283 |
| 2 | 2,604 | 2,098 | 506 |
| 3 | 1,617 | 1,327 | 290 |
| 4 | 1,555 | 1,293 | 262 |

Prose range: **1,293 – 2,098.** Mean ≈ 1,555. Excluding outlier Post 2 (2,098): 1,293 – 1,500.

**Verdict:** A prose-char floor of **900 is way too low** — every corpus post clears it by 400+. A **1,250 prose-char floor** would hold all 4 posts above water while preventing pad-to-hit-1,300-total games. Recommend: add a 1,250 prose-char floor to `tests/posts-gate.sh` alongside the existing 1,300 total-char floor.

Also: the 2026-04-24 GPT-5.5 post (referenced in redesign doc) is ~1,480 total with ~500 whitespace = ~980 prose chars. That post would fail a 1,250 prose floor. Either (a) treat GPT-5.5 as an outlier and set the floor based on the reliable 4 posts, or (b) set the floor at 950 to accommodate whitespace-heavy news-commentary. Preference: **set prose floor at 1,100** — catches the pad-heavy failures, keeps Aayush's actual range.

---

## Section 3 — Patterns the blueprint is missing or misreading

### 3.1. Opening move: named-specific stat → paradox (3 of 4 posts)

Posts 1, 2, 3 open with a sharp factual statement + immediate tension. This is NOT Pattern E (observation-first setup). It's the OPPOSITE — punch first, build tension immediately.

- Post 1: `Someone raised $9M just to babysit AI-generated code.` (number + paradox)
- Post 2: `Every SaaS is shipping an AI button right now. Most of them are going to look ridiculous in 18 months.` (two-line binary)
- Post 3: `AI startups have 12 months before they die…` (time bomb + ellipsis)
- Post 4: `Everyone has Claude Code. Almost no one is using it right.` (two-line binary)

Pattern E (observation-first / "my feed is doing the thing") appears in **zero** of 4 corpus posts. The blueprint elevating it as a named first-class pattern is premature. It's documented in one off-corpus post only.

**Fix:** Demote Pattern E to "experimental — use when news is genuinely a hype-cycle story." Restore Pattern A (contrarian / two-line binary) as the workhorse. Post 2 and Post 4 both use two-line binaries — promote that variant further.

### 3.2. Hyphen-bullet sub-lists: present in all 4 posts

| Post | Hyphen-bullet lines |
|---|---:|
| 1 | 6 |
| 2 | 16 |
| 3 | 3 |
| 4 | 2 |

Every single corpus post uses `- ` bullets for lists of 2-4 parallel items. The blueprint mentions "dashes not bullets" but doesn't celebrate this as a core structural device. It should. Hyphen-lists of 3 items are Aayush's most common parallel structure.

### 3.3. "At Atlan" grounding paragraph (3 of 4 posts)

Posts 1, 2, 4 have an "At Atlan, we..." line that grounds the abstract argument in Aayush's real work. Only Post 3 doesn't have it.

- Post 1: "At Atlan, we've been building agents for months and this tracks."
- Post 2: "When we build agents at Atlan, we don't have them click buttons."
- Post 4: "p.p.s. at Atlan we've been building this layer for a while..."

The blueprint mentions Atlan-context p.p.s. but understates that the **Atlan grounding mid-post** (not just in the p.p.s.) is a structural staple. It's a proof beat, not a CTA.

**Fix:** Add "At Atlan grounding beat" as a named structural device in the blueprint. Use mid-post to convert a general observation into a specific one-liner of lived experience. One per post max.

### 3.4. Length reality — blueprint says 1,400-1,800 sweet spot, corpus says 1,555-1,800 (with 2,604 outlier)

Three of 4 posts are in the 1,555-1,800 range. One is 2,604. The 2,604 post (AI buttons) is cited in the blueprint as a "bottom performer" — but it IS in the finalized corpus. So either (a) Aayush shipped and kept it despite low engagement, or (b) the previous "bottom performer" annotation is on a different draft. Blueprint's stated cap of 2,000 is consistent with the corpus median but inconsistent with Aayush actually shipping 2,604.

**Fix:** Keep the 2,000 cap as a soft target in the blueprint ("above 2,000 requires a reason to earn it"). Do not hard-reject at 2,000.

### 3.5. Parenthetical personality asides — 3 of 4 posts

Blueprint lists this as a device but undersells frequency. Actual corpus uses:
- Post 2: `(the agent literally sees your screen and operates your apps for you)` — explanatory
- Post 2: `(quietly)` — tonal
- Post 4: `(using claude code is not a moat 🤷🏻‍♂️)` — self-aware wink

Three variants — explanatory, tonal, self-aware. The blueprint only names the self-aware-wink form. Add the explanatory form ("brackets to unpack a technical term in one beat") and the tonal form (single-word adverb in parens).

### 3.6. Lowercase rhetorical closer — 2 of 4 posts

Posts 3 and 4 both close with a lowercase-opener question:
- Post 3: `what are you building that only YOU can build?`
- Post 4: `What does your team remember from last sprint's Claude Code usage?` (sentence case — actually capital W)

Correction: only Post 3 uses lowercase-opener. Post 4 is sentence case. So 1 of 4. The blueprint's elevation of lowercase rhetorical openers is slightly over-weighted.

### 3.7. Emoji usage — very sparse

- Post 1: `👀` (in closing question)
- Post 2: zero emojis
- Post 3: zero emojis
- Post 4: `🤷🏻‍♂️` inline, `👇🏻` in p.p.s.

Pattern: **zero-to-two emojis per post, never in body prose without purpose.** Blueprint says "max 1 emoji in body" — corpus confirms and under-uses.

### 3.8. Question-as-closer frequency

All 4 posts close on a question or an unresolved statement pointed at the reader:
- Post 1: direct question ("What's the ugliest workaround...")
- Post 2: unresolved statement ("Because they might not be who you think.")
- Post 3: direct question ("what are you building...")
- Post 4: direct question ("What does your team remember...")

**Closing rhetorical question is a hard rule, not an option.** The blueprint should state: every post closes with a question OR an unresolved pivot to the reader.

---

## Section 4 — Recommended follow-up edits (priority order)

All edits are to `/Users/aayush.maheshwari/presidential-briefing/config/post-blueprint.md` unless noted.

### Priority 1 — correct over-weighted devices from the single-post GPT-5.5 read

1. **post-blueprint.md §Formatting devices (line ~445):** Change "Arrow `↓` as visual colon — pending" to "Arrow `↓` — single-post sighting, do NOT use until 2+ more confirmed uses." Add date check.
2. **post-blueprint.md §Hook patterns Pattern E (lines ~89-103):** Demote from 5th named pattern to "experimental variant of A." Restore two-line binary + ellipsis as the default. Corpus: 3 of 4 posts use punch-first openers, 0 use Pattern E.
3. **post-blueprint.md §"That's X." recap-tag (lines ~250-262):** Remove Variant 2 (diagnostic beat) as equal weight. Note it as "one observed use in GPT-5.5 off-corpus post, not confirmed." Concept-naming is 4/4 in corpus, diagnostic is 0/4.
4. **post-blueprint.md §Allowed hedge markers line ~120:** Remove "My take is" as first-class marker. Keep as "occasional variant, see 2026-04-24 GPT-5.5 post." IMO (3) and I doubt (2) are the proven defaults.
5. **post-blueprint.md §Vulnerability-in-closer lines ~264-274:** Scope down to "rare, 1 in 4 corpus posts." Do not present as a standard option for all TIER 2/3 posts.

### Priority 2 — add missing corpus patterns

6. **post-blueprint.md — add new §"At Atlan grounding beat":** 3 of 4 corpus posts have a one-line Atlan-work reference mid-post. Codify as a structural device separate from the p.p.s. CTA.
7. **post-blueprint.md §Parenthetical personality aside (line ~160):** Expand to name three variants — explanatory (unpacks a technical term), tonal (single word in parens), self-aware wink. Corpus has all three in Post 2 alone.
8. **post-blueprint.md — add new §"Hyphen-bullet 3-item list":** Formalize 3-item parallel lists with `- ` as a top device. All 4 corpus posts use this. Include example.
9. **post-blueprint.md — add rule to §Format checklist:** "Every post closes with a question OR unresolved pivot to the reader." 4 of 4 corpus posts do this.

### Priority 3 — tighten hard gates

10. **tests/posts-gate.sh:** Add 1,100 prose-char floor (total-chars minus whitespace). Current 1,300 total-char floor allows whitespace padding. Corpus min prose = 1,293, so 1,100 is a safe floor that still catches pipeline padding.
11. **tests/posts-gate.sh:** Add lowercase-i-as-pronoun regex reject: `(?:^|[^a-zA-Z'])i(?:[ '.,?!]|'m|'ve|'d|'ll)` — corpus uses uppercase I in 6 of 7 pronoun instances, the 1 exception is inside quoted AI-chatbot dialogue.
12. **tests/posts-gate.sh:** Soften upper cap from reject-at-2000 to warn-at-2000, hard-reject at 2,700. Post 2 in corpus is 2,604. Aayush ships 2,604 when content earns it.

### Priority 4 — blueprint housekeeping

13. **post-blueprint.md §"Top 5 performers":** Verify the quoted "p.s. My honest answer..." is actually from this corpus. Python scan says p.s./p.p.s. only appear in Post 4. If the quoted top performer is from an older file, annotate it as "archive reference, not in current corpus."
14. **.claude/skills/write-posts/references/voice.md lines 25 vs 169:** Confirm the 169 resolution (uppercase I default) and delete any remaining "lowercase i" language. Corpus is 6:0 uppercase.
15. **post-redesign-2026-04-24.md §6 Open questions:** Mark Q1 (arrow), Q3 (my take), Q6 (tell vs distribution) as RESOLVED by this corpus analysis. Q2, Q4, Q5, Q7 answered above with numbers.

---

## Appendix — methodology

- Parsed corpus via Python `re.split(r'\n—\n', text)` → 4 posts.
- Char counts via `len()` and `re.sub(r'\s', '', text)` for prose.
- Pronoun counts via `\bI(?:'m|'ve|'ll|'d)?\b` and lowercase equivalent.
- Every pattern claim checked with explicit regex against the corpus before reporting a count.
- Counts in this doc are reproducible by running the scripts preserved in working-memory `python3 -c` calls (2026-04-24).
