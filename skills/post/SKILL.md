# LinkedIn Post

Generate a LinkedIn post from the briefing's lead story. The post positions Aayush as someone who understands AI deeply — not by summarizing news, but by connecting dots nobody else connects.

## Trigger

Runs after briefing completes.

## Inputs

- `workspace/YYYY-MM-DD/briefing.md` — today's briefing
- `workspace/YYYY-MM-DD/selected-items.json` — lead story details
- `workspace/YYYY-MM-DD/connections.json` — brain connections
- `skills/post/format-selector.md` — story type to format routing
- `skills/post/voice-profile.md` — Aayush's writing patterns
- `skills/post/kill-list.md` — banned words and patterns
- `skills/post/hook-patterns.md` — proven hook structures
- Selected template from `skills/post/templates/`

## Process

### Step 1: Select format

Call LiteLLM proxy. Model: `claude-sonnet-4-6` (task: format_selection).

Read `skills/post/format-selector.md`. Based on the story type and connection types, select the right format template.

### Step 2: Form conviction

Call LiteLLM proxy. Model: `claude-opus-4-6` (task: conviction_formation).

```
You have:
- Today's lead story: {lead_story}
- Brain connections: {connections}
- The briefing you just wrote: {briefing}

Form a specific, falsifiable conviction about this story. Not a summary. A take.

It must be:
- Specific enough that someone could disagree with it
- Supported by 2+ data points from different time periods
- Not something any other AI newsletter would say
- Something Aayush would actually believe based on what he builds

Return: one conviction statement (1-2 sentences).
```

### Step 3: Write draft

Call LiteLLM proxy. Model: `claude-opus-4-6` (task: post_writing).

```
Write a LinkedIn post using:
- Conviction: {conviction}
- Format template: {selected_template}
- Voice profile: {voice-profile.md}
- Kill list: {kill-list.md}
- Brain connections: {connections}

Rules:
- Hook must fit in 80 characters (LinkedIn mobile fold)
- Total post: 900-1500 characters
- Active voice only
- No words from the kill list
- Burstiness: no 3+ consecutive sentences of similar length
- Perplexity: include at least 2 specific numbers/names/dates
- Success-oriented framing (talk to practitioners, not beginners)
- The post comes from the CONVICTION, not from summarizing the news
- Use brain connections to make points nobody else would make
- End with a genuine question that creates a binary choice

Do NOT:
- Start with "I" as the first word
- Use any form of "Here's what I learned" or "Let me share"
- List things with bullet points or numbered lists
- Use hashtags (we add 3-5 at the end separately)
- Include any external links in the body
```

### Step 4: Hook extraction

Call LiteLLM proxy. Model: `claude-sonnet-4-6` (task: hook_extraction).

```
Read this LinkedIn post draft:
{draft}

Find the single most surprising or provocative line in the post.
Propose it as an alternative hook (first line of the post).

Return:
{
  "original_hook": "...",
  "alternative_hook": "...",
  "recommendation": "original" or "alternative",
  "reason": "..."
}
```

If alternative is recommended, rewrite the post with the alternative hook.

### Step 5: Post council review

The post goes through the full review council. See `skills/review/SKILL.md`. Post-specific passes:

1. Structure + hook (Claude Sonnet)
2. Fact verification (Gemini with search grounding)
3. Voice + kill list (Claude Opus)
4. Adversarial novelty check (Grok)
5. 5-dimension scoring

Max 4 revision cycles.

## Output

- `workspace/YYYY-MM-DD/linkedin-draft.md` — the final post
- `workspace/YYYY-MM-DD/conviction.md` — the conviction statement
- `workspace/YYYY-MM-DD/format-selected.json` — which format was chosen and why
