# Council — 2026-07-05 (iteration 1)

## Deterministic findings (CONFIRMED violations)

**Verdict: REVISE** — Hard rule violations found in pre-flight checks:

### Em dash violations (19 total)
- 14 instances in brief.md  
- 5 instances in posts.md
- Zero tolerance rule - all em dashes (—) must be removed

### MBA vocabulary violations (6 instances)
- "maturation" (appears twice in brief)
- "commoditization" (brief)
- "table stakes" (brief)  
- "enterprise customers" (brief)

### Long sentence violations (2 confirmed violations)
Multiple sentences exceed 22-word limit - must be shortened to improve readability

### Not X, it's Y inversions (2 instances)
- "isn't about general capability. It's about reliability" (brief)
- "isn't AI capability anymore. It's human" (posts)
- Rewrite to say what it IS, not what it ISN'T

### Neat bow violations (1 confirmed)
- "The founders who build these capabilities early win deals. The ones who..." closer pattern needs replacement

### Guru voice violations (3 instances)  
- "founders selling AI dev tools to large organizations must build" (brief)
- "Founders targeting enterprise markets should study" (brief)
- "team shipping to customers should be" (posts)
- Must rewrite as first-person observations, not third-person prescriptions

### Word count violation
Brief is at 1814 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

## Aayush Voice Score (10-point audit)
- **Option 1**: 6/10 — REVISE (missing hedge markers, weak first-person)
- **Option 2**: 9/10 — SHIP (strong across all dimensions except contrast labels)  
- **Option 3**: 6/10 — REVISE (no first-person observer, no hedge markers)

**Gate failures:** Options 1 and 3 both score below 8/10 threshold

## Fact Check (Critical Issues)
⚠️ **MAJOR CONCERN**: "Claude Fable" is not a confirmed Anthropic model name
- Anthropic uses Claude 3 Haiku/Sonnet/Opus and Claude 3.5 naming conventions
- "Fable" does not appear in any verified Anthropic release
- All content depends on this potentially false model name

**Other findings:**
- $149.25 cost figure, 5 release blockers, technical details all UNVERIFIABLE without confirmed source tweet
- Simon Willison quote about Opus vs Fable trust UNVERIFIABLE
- 37 prompts, 34 commits figures UNVERIFIABLE

## Adversarial Attack (Grok findings)

### Brief issues:
- **Logical gaps**: Leaps from one developer's workflow to "universal new development pattern" without evidence
- **Unsupported claims**: "Multiple credible practitioners report" when only Simon cited
- **Guru voice violations**: "Teams that recognize this shift early gain competitive advantage", "What to do this week", "Teams need regression test suites"
- **Neat bow patterns**: "The winners build for the conservative segment from the start"
- **Verdict**: REJECT

### Posts analysis:
- **Option 1**: Relatable Human style, but has guru voice ("Use both", "Your human reviewers are...") — REVISE
- **Option 2**: Vulnerable Victor style, fresh angle, but contains fabricated claim ("I've been running AI code review wrong for months") not in aayush-experiences.md — REVISE  
- **Option 3**: Contrarian Philosopher style, but reads as Corporate Analyst with third-person generalizations — REJECT

## FINAL VERDICT: REVISE

**Priority fixes:**
1. **CRITICAL**: Verify "Claude Fable" model name or replace with confirmed model
2. Remove all em dashes (19 instances)
3. Replace MBA vocabulary (6 instances)
4. Fix guru voice violations in brief and posts
5. Remove fabricated personal claims in Option 2
6. Expand brief to 2000+ words
7. Add first-person observations and hedge markers to posts

**Post recommendation**: Option 2 has best bones but needs fabrication fix and guru voice removal.
