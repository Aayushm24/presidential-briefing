# Briefing

Write the daily presidential briefing. 5-7 minute read. First-principles teaching. No section headers.

## Trigger

Runs after brain completes.

## Inputs

- `workspace/YYYY-MM-DD/selected-items.json` — lead + secondary items
- `workspace/YYYY-MM-DD/raw-intake.json` — full content of selected items
- `workspace/YYYY-MM-DD/connections.json` — brain connections for lead story
- Related brain pages' compiled_truth (fetched via `gbrain get {slug}` for top 3-5 connections)
- `skills/briefing/format.md` — the briefing writing prompt

## Process

### Step 1: Assemble context

n8n Function node assembles:
- Lead story full content
- 3-5 secondary items with summaries
- Brain connections + related pages' compiled_truth
- Past briefing topics from the last 7 days (from workspace/*/selected-items.json)

### Step 2: Generate briefing

Call LiteLLM proxy. Model: `claude-opus-4-6` (task: briefing_writing).

System prompt: contents of `skills/briefing/format.md`

User prompt:
```
Today's date: {YYYY-MM-DD}

LEAD STORY:
{lead_story.content_full}

BRAIN CONNECTIONS:
{connections with related_page_compiled_truth}

SECONDARY ITEMS:
{secondary_items with content_summary}

PAST WEEK'S TOPICS:
{list of lead story topics from last 7 briefings}

Write today's briefing following the format instructions.
```

### Step 3: Briefing council review

The briefing goes through 4 review passes before delivery. See `skills/review/SKILL.md` for the full review council process. The briefing-specific passes are:

1. Fact verification (Gemini 3.1 Pro with search grounding)
2. Concept accuracy (Claude Opus — are technical explanations correct?)
3. Teaching quality (Claude Sonnet — can a beginner follow this?)
4. Freshness check (Grok — is this actually new?)

If any pass flags issues, revise and re-check. Max 2 revision cycles for the briefing.

## Output

- `workspace/YYYY-MM-DD/briefing.md` — the final briefing
