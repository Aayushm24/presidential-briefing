# Council — 2026-07-11 (iteration 1)

## Deterministic findings (pre-flight)

**CONFIRMED hard-rule violations found. Verdict: REVISE required.**

- **NOT X, ITS Y violations (2 hits)**: 
  - Brief: "isn't a feature update. It's OpenAI"  
  - Brief: "aren't separate product updates. They're evidence"

- **GURU VOICE violations (2 hits)**:
  - Brief: "Builders who plan around current chip economics should update"
  - Brief: "For builders,"

- **EM DASHES (10 hits in posts.md)**: All em dashes must be converted to commas, periods, or ellipsis

- **LONG SENTENCE violations (Brief: 5 hits, Posts: 5+ hits)**:
  - Brief 37w: "Work mode is the new chat mode: AI just shifted from conversation..."
  - Brief 29w: "The interface paradigm is moving from "ask and answer" to "delegate and..."
  - Brief 111w: "Key takeaways: ChatGPT's Work vs Chat mode split proves task execution drives..."
  - Brief 24w: "The marketing language shifted from "chat with AI" to "AI does your..."
  - Brief 28w: "A tool that can fetch real data, execute scripts, and modify external..."

- **WORD COUNT violation**: Brief is at 1,947 words, needs 2,500+. Expand the lead section with more mechanism/specificity, not more topics.

## Voice audit (Gemini)
- Option 1: 11/15 — REVISE (missing specific numbers, has fabrication issues with claim about Atlan agents)
- Option 2: 13/15 — ship with fix (minor rhythm issues)  
- Option 3: 12/15 — ship threshold (needs better hook specificity)

## Fabrication check
- Option 1: ⚠️ FABRICATION RISK: "At Atlan, when we build agents, we don't have them click buttons. They call APIs, read from databases, talk to other apps through MCPs" - needs verification against aayush-experiences.md
- Option 2: ✅ No fabricated claims detected
- Option 3: ✅ No fabricated claims detected

## Fact check (Gemini)
- ✅ ChatGPT Work/Chat mode split verified
- ✅ Simon Willison yt-dlp test verified
- ✅ Ethan Mollick Fable demonstration verified
- ✅ NotebookLM capabilities verified
- ❌ EM DASHES: 10 instances found in posts.md - all must be converted

## Adversarial (Grok)
- Brief: Angle is fresh - Work mode vs Chat mode distinction is a new framing
- Option 1: Saturated angle - many posts about task automation vs conversation already
- Option 2: Fresh angle - creative iteration compression is specific and new
- Option 3: Fresh angle - transparency in AI reasoning is underexplored

## Verdict: REVISE

Specific revision notes:
- Brief: Fix 2 "not X, it's Y" inversions
- Brief: Fix 2 guru voice violations ("Builders who...", "For builders,")  
- Brief: Convert all long sentences (>22 words) to shorter ones
- Brief: Expand to reach 2,500+ word minimum
- Posts: Convert all 10 em dashes to commas or periods
- Option 1: Remove/verify fabricated Atlan claims, add specific numbers
- All options: Address long sentence violations flagged by clean_text.py
