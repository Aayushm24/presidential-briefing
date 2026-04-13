# Format Selector

Based on the story type and brain connections, select the right post format.

## Routing logic

Check in this order. First match wins.

### 1. Brain finds CONTRADICTS connection
Format: **contrarian**
Template: `templates/contrarian.md`
When: The lead story challenges something we've written or believed before.
Hook style: "[Consensus view] is wrong. Here's why."

### 2. Brain finds BRIDGE connection
Format: **dot-connecting**
Template: `templates/dot-connecting.md`
When: The lead story connects two previously unrelated topics.
Hook style: "Three things happened this week that nobody is connecting."

### 3. Significance score = 9-10 (major news)
Format: **news-take**
Template: `templates/news-take.md`
When: Something genuinely big happened and we have an original angle.
Hook style: "[Company] just [did thing]. Everyone is focused on the wrong part."

### 4. Lead story extends a thread we've posted about before
Format: **evolution**
Template: `templates/evolution.md`
When: We wrote about this topic in a past post. Our thinking has evolved.
Hook style: "I wrote about [X] in [month]. I was wrong about one thing."

### 5. No single story dominates (all scores 5-7)
Format: **curation**
Template: `templates/curation.md`
When: Multiple interesting items, none dominant.
Hook style: "Three things happened in AI this week that are worth your time."

### 6. Brain finds a common misconception
Format: **mistakes**
Template: `templates/mistakes.md`
When: We can identify a specific thing people are getting wrong.
Hook style: "Most people think [X]. The data says otherwise."

### 7. Default
Format: **news-take**
Template: `templates/news-take.md`
When: None of the above match.

## Output

```json
{
  "format": "contrarian",
  "template": "templates/contrarian.md",
  "reason": "Brain found CONTRADICTS connection between lead story and 'ai-coding-assistants' page"
}
```
