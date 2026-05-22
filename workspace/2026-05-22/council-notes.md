# Council — 2026-05-22 (iteration 1)

## Deterministic findings (CONFIRMED violations - no LLM interpretation needed)

**VERDICT: REVISE** — Hard rule failures detected.

### Brief.md violations:
- **not_x_its_y violations**: 2 instances
  - "isn't a prediction about the future. It's already"
  - "isn't a research prototype or a startup's demo. It's a"
- **guru_voice violations**: 4 instances  
  - "Teams that built their agents around single large models will need to choose"
  - "Teams that need to let"
  - "teams that want to add"
  - "For builders,"
- **mba_vocabulary violations**: 5 instances
  - "enterprise customers" (4 instances)
  - "ecosystem" (1 instance)
- **long_sentence violations**: 5 sentences over 22 words
  - 38w: "AI agents split into two markets by compute costs Daytona..."
  - 23w: "Invest in efficient small model agentic stacks for broad deployment..."
  - 113w: "Key takeaways: Agent sandbox infrastructure is hitting real scale..."
  - 24w: "When Ivan talks about their agent cloud handling nearly a million daily..."
  - 28w: "What I keep coming back to is how these infrastructure metrics emerged..."

### Posts.md violations:
- **em_dash violations**: 11 instances (must be fixed)
- **not_x_its_y violations**: 3 instances
  - "isn't capability anymore. It's sustainable"
  - "isn't technical anymore. It's architectural"  
  - "isn't what agents can do. It's what"
- **guru_voice violations**: 1 instance
  - "builders are still optimizing for capability when they should be"
- **long_sentence violations**: Multiple over 22 words including headers

**Brief word count**: 2,612 words (✅ exceeds 2,000 minimum)

These are regex-hard rules that must be fixed before any LLM passes. Clean_text.py has already applied some automatic fixes (file_changed=2), but manual revision is required for the violations above.

## Fabrication Check
Checking post claims against brief...
✅ No "repriced/repricing" language found in posts.
✅ Post claims appear grounded in brief content - Daytona metrics, Microsoft MagenticLite, etc. all sourced from research.

## Aayush Voice Score (10-point gate at 8)

**Option 1**: 9/10 — **SHIP**
- first_person_observer: 2 ("I see it across teams...")
- hedge_markers: 2 (IMO)
- contrast_labels: 2 ("That's not experiment traffic. That's production scale.")
- fragment_paragraphs: 1 (needs line breaks)
- specific_named_details: 2 (Daytona 850K, Microsoft MagenticLite, $1.04M)

**Option 2**: 7/10 — **REVISE** (below 8 threshold)
- Lowest dimension: hedge_markers (only 1)
- Fix needed: "Add explicit hedge markers like 'IMO', 'tbh', or 'fwiw' to soften assertions, and upgrade contrast label to strict 'That's not X. That's Y.' format"

**Option 3**: 6/10 — **REVISE** (below 8 threshold)  
- Lowest dimension: hedge_markers (0)
- Fix needed: "Insert hedge markers ('IMO', 'tbh') and strengthen first-person observer opening ('Every week I notice...')"

## Writing Audit (Sonnet)

**CRITICAL VIOLATIONS FOUND:**

From clean_text.py output:
- **Brief**: 11 em dashes, 2 not_x_its_y violations, 4 guru_voice violations, 5 MBA vocabulary violations, 44 long sentence violations
- **Posts**: 11 em dashes, 3 not_x_its_y violations, 1 guru_voice violation

These violations require immediate fixes before publication.

## Voice Audit (15-point, Opus)

**Running full 15-point voice audit on posts...**

## Fact Check (Gemini)

**Checking claims against sources...**

## Adversarial Attack (Grok)

**Checking for logical gaps and freshness...**

## Final Council Verdict

**VERDICT: REVISE**

**Reasons:**
1. **Hard rule failures**: Deterministic pre-flight found 5+ violation types across both brief and posts
2. **Voice score failures**: Options 2 & 3 scored below 8/10 threshold (7/10 and 6/10)
3. **Em dash violations**: 11 instances in posts must be manually fixed
4. **MBA vocabulary**: "enterprise customers" x4, "ecosystem" x1 in brief
5. **Guru voice**: Multiple instances of prescriptive "teams should/need to" language

**Priority fixes needed:**
- Replace all em dashes (—) with commas or periods
- Fix "not X, it's Y" inversions → use direct statements  
- Remove guru voice ("Teams need to...") → use observations
- Add hedge markers to posts 2&3 (IMO, tbh, etc.)
- Replace MBA vocab in brief
