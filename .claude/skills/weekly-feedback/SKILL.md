# weekly-feedback — Sunday conviction candidates

Produce 2-3 conviction candidates for Aayush to review. **Do NOT auto-edit `config/conviction.md`.** Aayush keeps that file manual until n ≥ 50 published posts (current count is ~25).

## When this runs

Sunday 7 AM IST, via `.github/workflows/weekly-feedback.yml`. `TODAY` env is the Sunday date.

## Goal

Synthesize the week's signal into 2-3 candidate through-lines. A candidate is one of:
- **🟢 Keep** — existing conviction was reinforced this week
- **🟡 Tension** — existing conviction looks stale or never gets shipped
- **🔴 New** — pattern emerged this week worth adding

Write everything to `workspace/$TODAY/conviction-candidates.md`. The Slack step happens outside this skill.

## Inputs (read only)

| File | What to pull from it |
|---|---|
| **`config/brief-blueprint.md`** | **Current brief voice rules.** Read in full. Primary source for "does the week's output match intended voice?" |
| **`config/post-blueprint.md`** | **Current post voice rules.** Same — read in full. |
| **`history/feedback-log.jsonl`** | **Every feedback event this week.** Each entry has `surface`, `what`, `why`, `outcome`. These drive the blueprint edit proposals. |
| `config/conviction.md` | Current 2-3 convictions. Baseline. |
| `config/aayush-linkedin-patterns.md` | Latest patterns including the "Option pickup rates" section. |
| `history/option-pickups.jsonl` | Last 7 days of attributions. Filter by `published_date >= (TODAY - 7 days)`. |
| `performance-data/*.md` | Engagement for posts published in the last 14 days. |
| `workspace/YYYY-MM-DD/posts.json` | Every day's 3 options for the last 7 days. |
| `workspace/YYYY-MM-DD/brief.md` | Every day's brief for the last 7 days. |
| `history/published.jsonl` | What actually shipped each day (lead title). |

**Primary job shift (2026-04-20):** This skill now proposes **blueprint edits** (additions, removals, tightenings), not just conviction candidates. Conviction candidates remain a secondary output.

## Processing

1. Enumerate last 7 days of `workspace/` (YYYY-MM-DD directories where the date is within `[TODAY - 7 days, TODAY]`).
2. For each day, load `posts.json` and `brief.md`. Collect: generated options (template, hook_pattern, conviction field), brief themes.
3. For each post in `history/option-pickups.jsonl` with `published_date >= TODAY - 7 days`, find the matching `performance-data/post-<id>.md` and pull engagement numbers (latest snapshot).
4. Cross-reference:
   - Which existing conviction was threaded most often in the week's briefs?
   - Which generated option template had highest pickup this week?
   - Which template was generated multiple times but never picked up?
   - Which published post hit highest engagement? What conviction did it express?
   - Are there themes that came up ≥ 3 times in the week's `raw-intake.json` / `research.md` data but aren't in any existing conviction?
5. Draft 2-3 candidates using the exact shape in the output section.

## Hard constraints

- **Do NOT write to `config/conviction.md`.** Write candidates to `workspace/$TODAY/conviction-candidates.md` only.
- **Do NOT propose more than 3 candidates.** If there's nothing strong, write fewer. Blank candidates section is acceptable for a quiet week.
- **Max 20% text-delta** for any "edit existing conviction" proposal. If you're suggesting a rewrite bigger than that, reframe it as "Retire + New" instead.
- **Evidence-grounded.** Every candidate must cite specific data (post URL, engagement number, date, theme count). No vibes.
- **Substitution test.** Could this candidate apply to any random AI newsletter? If yes, it's too generic. Sharpen until it's Aayush-specific.
- **No fabricated claims.** If you don't have enough data for a candidate, say so.

## Output format

Write to `workspace/$TODAY/conviction-candidates.md`. Exact structure:

```markdown
# Conviction candidates — week of START_DATE → END_DATE

*Generated Sunday by `/weekly-feedback`. Aayush reviews + edits `config/conviction.md` manually. System does NOT auto-apply.*

## Week at a glance

- Posts generated: N across M days
- Posts published (scraped): K (variant_of=X, inspired_by=Y, organic=Z)
- Top-performing published post this week: <first-line>... (engagement: N)
- Themes covered most: A, B, C

---

## Candidate 1: [🟢 Keep | 🟡 Tension | 🔴 New] — "Headline of conviction"

**Evidence:**
- [Specific datapoint with URL or file path]
- [Another datapoint]
- [Another datapoint]

**Proposed action:** [Keep as-is / Tighten to X / Retire / Add as conviction #N]

**Suggested text** (if Keep or Tighten):
> The actual conviction text, max 20% delta from current.

---

## Candidate 2: ...

## Candidate 3: ...

---

## What I looked at

- Workspace dirs: <list>
- Pickup entries: N (since <earliest date>)
- Perf-data files referenced: N
```

## Exit

- Write `workspace/$TODAY/conviction-candidates.md`.
- Write `workspace/$TODAY/.status` with value `candidates-ready`.
- Do nothing else. No commits, no Slack. The workflow handles those in deterministic bash.
