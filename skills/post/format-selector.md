# Format Selector

Based on the story type, brain connections, and Aayush's performance data, select the right post format.

## Routing logic

Check in this order. First match wins.

### 1. Brain finds CONTRADICTS connection
Format: **contrarian-truth**
Template: `templates/contrarian.md`
When: The lead story challenges something we've believed or written before.
Hook style: Pattern A (Contrarian Truth)
Example: "think step by step" is making your AI worse.

### 2. Personal experience with the topic exists
Format: **personal-discovery**
Template: `templates/personal-discovery.md`
When: Aayush has built something related, or the topic connects to his real work.
Hook style: Pattern B (Identity/Confession)
Example: "i've been sabotaging my own AI pipelines for months."
Note: This is Aayush's top-performing style. Vulnerability + education.

### 3. Brain finds BRIDGE connection
Format: **dot-connecting**
Template: `templates/dot-connecting.md`
When: The lead story connects two previously unrelated topics.
Hook style: Two facts that don't fit together
Example: "Cursor raised $900M. Copilot loses money on every user."

### 4. Topic lends itself to humor
Format: **absurd-mirror**
Template: `templates/absurd-mirror.md`
When: The topic has an absurd angle that reveals truth through comedy.
Hook style: Pattern C (Absurd Comparison)
Example: "the term ARR is getting redefined. it used to mean annual recurring revenue."

### 5. Significance score = 9-10 (major news)
Format: **news-take**
Template: `templates/news-take.md`
When: Something genuinely big happened and we have an original angle.
Hook style: Pattern E (Specific Number + Surprise) or Pattern F (Direct Challenge)

### 6. Lead story extends a thread we've posted about before
Format: **evolution**
Template: `templates/evolution.md`
When: Our thinking has evolved on a topic.
Hook style: Pattern D (Time Bomb)

### 7. No single story dominates (all scores 5-7)
Format: **curation**
Template: `templates/curation.md`
When: Multiple interesting items, none dominant.

### 8. Brain finds a common misconception
Format: **hidden-truth**
Template: `templates/mistakes.md`
When: We can identify something people are getting wrong.
Hook style: Pattern A (Contrarian Truth)

### 9. Default
Format: **personal-discovery**
Why default to this: vulnerability + education is Aayush's highest-performing combination. When in doubt, make it personal.

## Output

```json
{
  "format": "personal-discovery",
  "template": "templates/personal-discovery.md",
  "reason": "Aayush has direct experience building multi-model pipelines where CoT was the default. Personal discovery angle will outperform pure contrarian."
}
```
