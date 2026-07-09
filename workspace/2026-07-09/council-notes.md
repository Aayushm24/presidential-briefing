# Council — 2026-07-09 (iteration 1)

## Deterministic findings (pre-flight)

**CONFIRMED hard-rule failures found. Verdict: REVISE**

### Brief.md violations (9 total):
- **Em dashes**: 9 occurrences found (zero tolerance - banned everywhere)
- **MBA vocabulary**: "commoditization" found (banned in briefs - use "everyone can buy it now" or "gets cheap")
- **Long sentences**: Multiple sentences over 22-word cap require splitting

### Posts.md violations (13 total):
- **Em dashes**: 13 occurrences found (zero tolerance - banned everywhere)
- **Not X, it's Y inversion**: "isn't the LLM anymore. It's context" found (AI-tell - rewrite as direct declarative)
- **Long sentences**: Multiple sentences over 22-word cap require splitting

**Total violations: 22 em dashes + 1 MBA vocab + 1 AI-tell inversion + multiple long sentences**

These are regex-hard rules that require fixing before any LLM passes can proceed. The council will still run voice audit, fact check, and adversarial review, but pre-flight findings take priority in revision.

## Fabrication check

Checking post claims against brief...
No fabrication risks detected. Post claims appear grounded in brief content.

## Voice audit (pending LLM pass)

## Fact check (pending LLM pass)

## Adversarial attack (pending LLM pass)

## Verdict: REVISE

**Critical revision priorities:**
1. **Em dashes**: Replace all 22 em dashes with commas, periods, or "..." 
2. **MBA vocabulary**: Replace "commoditization" in brief with plain English
3. **AI-tell inversion**: Rewrite "isn't the LLM anymore. It's context" as direct statement
4. **Long sentences**: Split all sentences over 22 words into shorter, clearer statements

LLM passes will follow after these deterministic fixes are applied.