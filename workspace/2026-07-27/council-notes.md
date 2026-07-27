# Council — 2026-07-27 (iteration 1)

## Deterministic Findings (CRITICAL - Must Fix)

### Pre-flight violations (23 total)
- **Em dashes**: 23 hits across both files (14 brief, 9 posts) — ZERO tolerance rule violated
- **Brief word count**: 1493 words (requires 2000+) — expand lead section with more mechanism/specificity
- **MBA vocabulary**: 3 hits in brief ("differentiation", "ecosystem", "utilization") — banned vocabulary violations
- **Guru voice**: 3 hits in brief ("Teams building AI products should", "For builders,", "for builders,") — advice voice violations
- **"Not X, it's Y" inversions**: 2 hits in posts ("isn't cost. It's control", "isn't betting on which model wins. It's betting") — AI-tell pattern

### Long sentence violations (13 total)
Brief.md violations (word counts):
- 105w: "Key takeaways: Model releases accelerated to weekly drops..."
- 37w: "Open weight models crossed the enterprise threshold Six new open weight models..."
- 24w: "The coincidence suggests builders face a choice..."
- 41w: "Hugging Face CEO called for 'radical transparency'..."
- 24w: "Token relay markets in China resell API access..."

Posts.md violations:
- 79w: "LinkedIn posts, 2026 07 27 Lead: The frontier model..."
- 51w: "The technical debt accumulates fast: Prompt engineering..."
- 46w: "OPTION 2, data point hook score: 8 Conviction..."
- 24w: "The coincidence suggests builders face a choice..."
- 41w: "OPTION 3, dot connecting hook score: 8 Conviction..."

## Verdict: REVISE

**Reason**: Deterministic violations trigger automatic REVISE. Pre-flight found 23 em dashes (zero-tolerance), brief under word count floor, MBA vocabulary violations, guru voice violations, AI-tell inversions, and 13 over-length sentences.

## Specific Revision Notes:
1. **Remove ALL 23 em dashes** — replace with commas, periods, or delete entirely
2. **Brief expansion**: Add 500+ words to reach 2000+ minimum — expand the lead section mechanism explanations
3. **MBA vocabulary fixes**:
   - "differentiation" → "what makes them different" or name the specific advantage
   - "ecosystem" → name the specific thing (tools, companies, products)  
   - "utilization" → "use"
4. **Guru voice fixes**:
   - "Teams building AI products should evaluate" → first-person observation + personal reaction
   - "For builders," → remove advice framing, make observational
5. **Fix "Not X, it's Y" inversions**:
   - "isn't cost. It's control" → rewrite as parallel structure with different subjects
   - "isn't betting on which model wins. It's betting" → rewrite as direct declarative
6. **Break all sentences over 22 words** — split into shorter, clearer sentences

**Priority order**: Em dashes first (hard gate), then word count expansion, then sentence breaking, then vocabulary substitutions.