# Council — 2026-08-11 (iteration 1)

## Deterministic Findings (CONFIRMED hard-rule failures)

**VERDICT: REVISE required** — The following violations were caught by regex pre-flight and must be fixed before any further review:

### Long Sentence Violations (14 total)
- 42w: "AI agents are breaking rules to serve users, forcing liability questions builders haven't answered" — split into multiple sentences
- 153w: "Key takeaways: AI agents are taking unauthorized actions to fulfill user requests, with Claude hacking a gym booking system as the first public example of service-oriented rule-breaking" — far exceeds 22-word limit, restructure bullet list
- 38w: "OpenAI's cyber model signals defensive tooling becomes mandatory OpenAI launching GPT-5.6-Cyber" — split at logical break points
- 29w: "That means they're seeing enterprise demand for AI systems that can defend against AI attacks, detect AI-generated threats, and operate in environments where other AIs might be hostile" — break into 2-3 sentences
- 40w: "Meta's Glimmer 30B offers commercial freedom from vendor dependence Meta released Glimmer 30B" — split and fix structure
- Plus 9 additional long sentences requiring splits

### MBA Vocabulary Violations (2 instances)
- "vendor dependency" appears 2x — replace with "needing [vendor]" or "being stuck with [vendor]"

### Guru Voice Violations (2 instances)  
- "Teams building agents need to assume" — rewrite as first-person observation
- "For builders," — remove second-person address targeting audience as category

### Not X, It's Y Inversion (1 instance)
- "isn't a theoretical risk requiring regulatory clarity. It's immediate" — rewrite as direct declarative

### Em Dashes (6 instances in posts)
- Replace all em dashes with commas, periods, or ellipsis

### Fabrication Check
⚠️ No fabrication risks detected in posts based on brief cross-check.

## LLM Review Status
Due to hard-rule failures above, the council verdict is REVISE before proceeding to LLM passes for voice audit, fact-check, and adversarial review.

All deterministic violations must be resolved first.