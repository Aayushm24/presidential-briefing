# Review Council

Multi-model review system for both the briefing and the LinkedIn post. Each output gets reviewed by different models checking different dimensions.

## Trigger

Runs after briefing is generated (for briefing review) and after post is generated (for post review).

## Inputs

- The draft to review (briefing.md or linkedin-draft.md)
- `config/council.json` — which model for which review pass
- `skills/review/scoring-dimensions.md` — the 5 scoring dimensions
- `skills/post/voice-profile.md` — for voice match review
- `skills/post/kill-list.md` — for kill list check

## Briefing Review (4 passes)

### Pass 1: Fact verification
Model: `gemini-3-1-pro-preview` (task: review_fact_check)
Google Search grounding enabled.

```
Read this AI briefing. Verify every specific claim:
- Numbers (funding amounts, user counts, install counts, percentages)
- Dates (when things happened)
- Attributions (who said what, who built what)
- Technical claims (how algorithms work, what architectures do)

For each claim, return:
{ claim, verdict: "verified" | "unverifiable" | "incorrect", source_if_found, correction_if_needed }

Do NOT flag opinions or interpretations. Only factual claims.
```

### Pass 2: Concept accuracy
Model: `claude-opus-4-6` (task: review_concept_accuracy)

```
Read this AI briefing. It teaches technical concepts to someone building AI systems.

Check:
- Are the technical explanations correct? Would an ML engineer find errors?
- Are the analogies valid? (e.g., "materialized views" analogy for pre-computed synthesis — is this actually the right comparison?)
- Are there oversimplifications that would give the reader a wrong mental model?
- Are there leaps in logic where a step is missing?

For each issue found, return:
{ location, issue, severity: "minor" | "major", suggested_fix }
```

### Pass 3: Teaching quality
Model: `claude-sonnet-4-6` (task: review_teaching_quality)

```
Read this AI briefing. It's designed to teach someone who builds with AI but hasn't studied the fundamentals formally.

Check:
- Could someone with no ML background follow the explanation?
- Are there terms used before they're defined?
- Are there jumps in reasoning where context is missing?
- Does it actually teach something new, or just describe what happened?
- Is the "one thing to go deeper on" a genuine recommendation?

For each issue found, return:
{ location, issue, suggested_fix }
```

### Pass 4: Freshness check
Model: `grok-4-1` (task: review_freshness)

```
Search X/Twitter and the web for the main topics in this briefing.

Check:
- Is this news actually new, or did it break 3+ days ago?
- Has someone already made the exact same connection or argument publicly?
- Are we late to this story?

Return:
{ topic, is_fresh: true/false, competing_takes: ["urls or descriptions of similar takes"], our_angle_is_unique: true/false }
```

After all 4 passes: if any major issues found, revise the briefing and re-run the failing pass. Max 2 revision cycles.

## LinkedIn Post Review (4 passes + scoring)

### Pass 1: Structure + hook
Model: `claude-sonnet-4-6` (task: review_structure)

```
Review this LinkedIn post draft:

1. Hook strength (1-10): Does the first line stop the scroll? Is it under 80 chars?
2. Flow: Does each paragraph lead naturally to the next?
3. Format compliance: Under 1500 chars? Short paragraphs? White space?
4. Closing: Does it end with engagement-worthy question or observation?

Return scores + specific suggestions.
```

### Pass 2: Fact verification
Same as briefing Pass 1.

### Pass 3: Voice + kill list
Model: `claude-opus-4-6` (task: review_voice_match)

```
Review this LinkedIn post against:

VOICE PROFILE:
{voice-profile.md}

KILL LIST:
{kill-list.md}

Check:
1. Voice match (1-10): Does this sound like Aayush or like ChatGPT?
2. Kill list violations: List every word/phrase/pattern from the kill list found in the draft.
3. Burstiness: Are there 3+ consecutive sentences of similar length?
4. Specificity: Does every paragraph have at least one specific number, name, or date?

For each violation, provide a specific fix (not just "fix this" but "replace X with Y").
```

### Pass 4: Adversarial novelty check
Model: `grok-4-1` (task: review_adversarial)

```
Search X/Twitter for takes similar to this LinkedIn post.

1. Has someone already made this exact argument this week?
2. Would anyone disagree with this take? If nobody would disagree, it's not a real take.
3. Is this genuinely Aayush's unique perspective, or could any AI newsletter have written this?

Novelty score (1-10). If below 6, explain what would make it more original.
```

### Scoring synthesis
Model: `claude-opus-4-6` (task: scoring_synthesis)

Read all 4 review outputs. Score 5 dimensions (1-10):

1. Novelty — does this say something new?
2. Insight density — how much do you learn per sentence?
3. Voice match — does it sound like Aayush?
4. Hook strength — would you stop scrolling?
5. Teach-ability — can someone walk away knowing something new?

Threshold: average >= 7 to ship. Any dimension below 5 = automatic revise with specific feedback on that dimension.

Max 4 revision cycles. After 4, output current best version with scores and flag for human review.

## Output

- `workspace/YYYY-MM-DD/reviews/` — all review pass outputs
- `workspace/YYYY-MM-DD/scores.json`:

```json
{
  "target": "linkedin-post",
  "dimensions": {
    "novelty": 8,
    "insight_density": 7,
    "voice_match": 8,
    "hook_strength": 9,
    "teachability": 7
  },
  "average": 7.8,
  "verdict": "ship",
  "revision_count": 1,
  "council_cost_estimate": "$0.45"
}
```
