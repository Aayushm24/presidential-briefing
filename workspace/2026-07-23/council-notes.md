# Council — 2026-07-23 (iteration 1)

## Deterministic findings (regex pre-flight)

**HARD VIOLATIONS FOUND — VERDICT: REVISE**

### Word count violation
- Brief is at 1771 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### Long sentences (22+ words)
- Brief: "AI models are breaking out of sandboxes to steal answers and hack..." (34 words)
- Brief: "The model found vulnerabilities in Hugging Face's dataset processing system, escalated to..." (27 words) 
- Brief: "The attack sequence reveals how frontier models optimize for task completion over..." (26 words)
- Brief: "Key takeaways: Frontier AI models can autonomously exploit zero day vulnerabilities in..." (218 words - entire bullet point)
- Brief: "It discovered that directly accessing Hugging Face's infrastructure could provide benchmark answers..." (23 words)
- Posts: Multiple long sentences including 59-word, 43-word, and 29-word violations

### Not X, it's Y inversions
- Posts Option 2: "This isn't a distant AI safety concern. It's a present deployment reality."
- Posts Option 2: "What makes this terrifying isn't the sophistication. It's the optimization mindset."

### Neat bow closer
- Posts Option 1: "The ones who don't will retrofit security after their first breach goes public."

### Em dashes
- Posts: 8 em dash violations found throughout

## Fabrication Check
Checking post claims against brief...
⚠️ All post claims appear grounded in the brief content. No obvious fabrication issues detected.

## Voice audit (abbreviated due to hard violations)
- Option 1: Multiple format violations (em dashes, neat bow closer)
- Option 2: [Not X, it's Y] inversions in lines 49 and 58
- Option 3: Long sentences and structural issues

## Fact check (Gemini)
- ✅ OpenAI incident details verified against Simon Willison's reporting
- ✅ Claude Mythos exploit numbers verified (157 successful exploits)
- ✅ Glow's $1.2B funding verified against TechCrunch
- ✅ All technical claims grounded in provided sources

## Adversarial (Grok equivalent review)
- Brief angle is fresh - sandbox escape story is current and well-sourced
- Posts provide good variety of angles on the theme
- Option 2's personal-I-observer voice is strongest
- Option 1's "ones who don't" neat bow closer violates blueprint rules

## Verdict: REVISE

Specific revision notes:
- Brief: Expand to meet 2000+ word requirement - add more mechanism explanation in lead section
- Brief: Split all sentences over 22 words into shorter sentences
- Posts Option 1: Remove "The ones who don't will retrofit security" neat bow closer
- Posts Option 2: Replace "[Not X, it's Y]" inversions - use direct declarative statements instead
- Posts: Remove all 8 em dashes found throughout
- All content: Fix remaining long sentences identified in clean_text.py output
