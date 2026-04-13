# Filter

Score every item from intake on 5 dimensions. Select the lead story and 3-5 secondary items.

## Trigger

Runs immediately after intake completes.

## Inputs

- `workspace/YYYY-MM-DD/raw-intake.json` — all scraped items
- `skills/filter/scoring-rubric.md` — the 5 dimensions with examples

## Process

### Step 1: Deduplicate

Many sources cover the same story. Group items by topic using Claude Sonnet. If 3 sources all cover "Meta releases Muse Spark," merge them into one item with all 3 URLs as sources. Keep the richest content_full.

### Step 2: Score

Batch items into groups of 15-20. For each batch, call LiteLLM proxy with model `claude-sonnet-4-6` (from council.json, task: significance_scoring).

Prompt:
```
Score each item on 5 dimensions (1-10). Read scoring-rubric.md for definitions and examples.

For each item return:
{
  "id": "...",
  "scores": {
    "significance": 7,
    "novelty": 8,
    "practitioner_impact": 6,
    "discussion_heat": 5,
    "connectability": 9
  },
  "combined_score": 35,
  "verdict": "breakthrough",
  "one_line_reason": "First evidence that top practitioners value AI for thinking over coding"
}

Verdicts:
- "breakthrough" (combined >= 35): genuine shift, must cover
- "notable" (combined 25-34): worth mentioning
- "incremental" (combined 15-24): skip
- "noise" (combined < 15): discard
```

### Step 3: Select

From scored items:

1. Lead story = highest combined score. If two items are within 3 points, prefer the one with the highest single-dimension spike. A 10/6/6/6/6 beats a 7/7/7/7/7.

2. Secondary items = next 3-5 by score. Diversity rule: no two secondary items from the same topic cluster. If three stories are about "new model releases," pick the highest-scoring one and drop the others.

3. Kill threshold: combined < 25. Don't include.

4. If nothing scores above 30, flag it: "Quiet day. Consider accumulating and skipping today's post." Write this to `workspace/YYYY-MM-DD/quiet-day-flag.json`.

## Output

- `workspace/YYYY-MM-DD/scored-items.json` — all items with scores
- `workspace/YYYY-MM-DD/selected-items.json` — lead + secondary items only
