# Council — 2026-06-27 (iteration 1)

## Deterministic findings (CONFIRMED violations)

Based on clean_text.py analysis, found multiple hard-rule failures requiring REVISE:

**Em dashes (posts):** 6 instances found. ZERO tolerance policy.

**Not X, it's Y inversions:** 7 total instances across both files:
Brief (3 instances):
- "isn't speculative policy discussion. It's operational"
- "isn't abstract policy commentary. It's based"
- "isn't another demo or benchmark with carefully curated examples. It's a"

Posts (4 instances):
- "aren't about safety. They're about picking"
- "aren't the ones with the best use cases. They're the"
- "isn't temporary. It's the"
- "isn't just a technical and commercial resource anymore. It's a"

**MBA vocabulary violations:**
Brief: "enterprise customers" (2x), "ecosystem" (2x)
Posts: "table stakes"

**Guru voice violations (brief):** 5 instances of third-person prescriptions:
- "startup building on frontier APIs must treat"
- "startups now need to assess"
- "Founders selling AI products to large companies now need to factor"
- "Founders will need to navigate"
- "For builders, [advice clause]"

**Neat bow violation (posts):** "The ones who adapt early get structural advantages over teams that assume access will remain unrestricted."

**Long sentence violations:** 30+ instances across both files, including sentences of 65w, 113w, 41w.

**Word count:** Brief is adequate at sufficient length.

**Verdict:** REVISE (due to deterministic violations above)

These violations must be fixed before any LLM passes can recommend SHIP.

## Voice audit (pending)
[Will run after deterministic fixes]

## Fact check (pending)
[Will run after deterministic fixes]

## Adversarial (pending)
[Will run after deterministic fixes]

## Specific revision notes:
Priority 1 (deterministic fixes required):
1. Remove all 6 em dashes from posts
2. Rewrite all 7 "Not X, it's Y" inversions to direct declarative statements
3. Replace MBA vocabulary: "enterprise customers" → "big companies", "ecosystem" → specific entities, "table stakes" → "everyone has it"
4. Rewrite 5 guru voice instances to first-person observations
5. Remove neat bow closer in posts
6. Break all long sentences (>22 words) into shorter ones