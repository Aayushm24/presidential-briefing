# Hook Patterns (scored)

The hook is everything. Under 70 characters. One line on mobile. Creates immediate tension or curiosity. No throat-clearing.

Each pattern has a score (1–10) reflecting 4-week LinkedIn engagement. The `/weekly-feedback` skill updates these numbers every Sunday based on shipped posts' actual performance (saves > comments > likes > impressions).

When writing 3 post options, default weighting: score 8+ gets one option guaranteed. Score 6- gets rejected. Rewrite if top hook scores below 7.

---

## Pattern A: Contrarian Truth — score 8
Challenge what everyone believes. High save rate.

Examples:
- "think step by step" is making your AI worse.
- AI isn't your competitive advantage. It's a commodity.
- RAG is dead.
- coding is not the bottleneck. thinking is.

**When to use:** brain finds a CONTRADICTS connection, or the lead story challenges consensus.

### Pattern A.b: Two-line binary hook — score 8 (corpus-confirmed 3/6 as of 2026-04-28)
Variant of A. Pair a universal claim with an immediate inversion on the next line. The contrast IS the hook.

Examples:
- *"Everyone has Claude Code. / Almost no one is using it right."* (Post 4)
- *"Everybody these days is an AI automation expert. / It's a great service to sell to founders."* (jagged-frontier 2026-04-26)
- *"That second question used to have one answer per cloud. / Now it has one answer, period."* (openai-50b-anywhere 2026-04-28 — used as closer, not opener)

**When to use:** the gap between line 1 and line 2 IS the whole point. Works as opener AND closer. No observer framing required. See `config/post-blueprint.md` §"Pattern A.b".

### Pattern A.c: Numeric-anchor lede — score 8 (corpus-confirmed 2/6 as of 2026-04-28)
Variant of A. Open with a specific dollar figure tied to a paradoxical purpose. The number is the hook, the paradox is the tension.

Examples:
- *"Someone raised $9M just to babysit AI-generated code."* (agent-stack-hardening, Post 1)
- *"OpenAI just paid $50 billion to give up their biggest moat."* (openai-50b-anywhere 2026-04-28)

Pattern: `[Subject] [verb-paid/raised/spent] [$ figure] [paradoxical purpose].` Distinct from Pattern E (Specific Number + Surprise) — A.c requires the dollar figure AND a paradox; Pattern E accepts any data point. Distinct from A.b — the punch is in line 1 alone, no inversion needed.

**When to use:** lead story has a specific dollar figure where the spend itself is the paradox. See `config/post-blueprint.md` §"Pattern A.c".

## Pattern B: Identity / Confession — score 9
Open with vulnerability. Audience relates before they learn. Aayush's top-performing pattern.

Examples:
- i've been sabotaging my own AI pipelines for months.
- i don't celebrate my success. haven't for a while.
- i'm the most average bloke ever.
- i was wrong about RAG for 6 months.

**When to use:** Aayush has direct experience. Default format when nothing else fits.

## Pattern C: Absurd Comparison — score 7
Humor disarms defenses. Hidden truth in comedy.

Examples:
- a cat with Instagram makes more than your MBA.
- the term ARR is getting redefined.
- i met an AI copywriter who said "regenerate response" in real life.

**When to use:** topic has an absurd angle that reveals truth. Use sparingly — too many absurd hooks feel forced.

## Pattern D: Time Bomb — score 7
Stakes clear. Something is about to happen or already did.

Examples:
- i posted my first LinkedIn post 3 years ago. it changed my life.
- the exit interview wasn't the surprise.
- in 90 days, this agent pattern breaks.

**When to use:** lead story extends a past thread, or the news has a deadline/window quality.

### Pattern D-ellipsis: Time Bomb with trailing ellipsis — score 8
Variant of D. End the hook with `…` (or `...`) instead of a period. The trail
creates suspense — the reader has to keep scrolling to resolve the stake.

Examples:
- *"AI startups have 12 months before they die…"* (Aayush 2026-04-20)
- *"the next OpenAI release breaks half your product…"*
- *"six months until every agent team faces this choice…"*

**When to use:** hook names a countdown, threshold, or looming shift. The
ellipsis must be at the END of the hook line only, never mid-sentence. Do
not stack ellipsis with a question mark or exclamation — one mark only.

**Do NOT use** for factual claims ("Notion shipped X…") — the ellipsis only
works when the tension is about what happens NEXT, not what already did.

## Pattern E: Specific Number + Surprise — score 8
Data creates authority. Surprise creates clicks.

Examples:
- 97% of LinkedIn creators are men. I'm in the 3%.
- 15 minutes × 5 days × 5 devs = 6+ hours a week.
- new research tested CoT across 15 models. all of them got worse.
- Notion rebuilt their agent system 5 times.

**When to use:** lead story has a specific number worth surfacing. Always combine number + surprise, not number alone.

## Pattern F: Direct Challenge — score 6
No setup. Just the claim. Punchy but saturated on LinkedIn.

Examples:
- Cancel your daily standup.
- stop hiring engineers.
- your AI stack has a dependency problem.

**When to use:** only with strong, specific proof backing the claim. Score drops if overused.

## Pattern G: Dot-Connecting — score 8 (new, added 2026-04)
Two facts that seem unrelated. Connect them.

Examples:
- Cursor raised $900M. Copilot loses money on every user.
- OpenAI shipped voice mode. ElevenLabs raised at $3B.
- Notion added agents. Linear added agents. Zapier added agents.

**When to use:** brain finds BRIDGE connection between two past themes, or today's stories independently point to the same shift.

## Pattern H: Pattern Reveal — score 7 (new)
"Across N founder conversations, I noticed..." — builds authority.

Examples:
- across 10 founder conversations this month, one pattern keeps showing up.
- i've reviewed 50 agent stacks. 40 have the same bug.
- every failing AI team i've seen makes the same first mistake.

**When to use:** conviction is a pattern Aayush has observed repeatedly. Never fabricate the count.

## Pattern I: News Take — score 6
"They shipped X. Here's what's actually interesting."

Examples:
- Anthropic shipped Claude 4.7. the headline isn't the context window.
- OpenAI dropped a new model. here's what nobody is talking about.

**When to use:** Significance score 9–10 on lead story + Aayush has an original angle. Score drops if the angle is predictable.

## Pattern J: Evolution — score 6
"I used to believe X. Now I believe Y."

Examples:
- i used to think RAG was the future. 6 months of production changed that.
- 6 months ago I hired a second engineer. i wouldn't today.

**When to use:** Aayush's thinking has genuinely shifted. Don't force.

---

## Rules for all hooks

- Under 70 characters. One line on mobile.
- No questions as hooks (engagement bait — algorithm penalized).
- No "I" as first word (use lowercase "i" in confessional style, or start with the topic).
- No colons (they look like templates).
- No "Here's what" or "Let me share" or "Great question!"
- No explaining why you're qualified before the hook.
- The hook creates a gap — the reader MUST know what comes next.
- The best hooks feel inevitable, not engineered.

## Hook scoring rubric (for /attack)

For each hook, score 1–10:
1. **Scroll-stop** (1–10): would a tired founder scrolling LinkedIn pause for this?
2. **Specificity** (1–10): does it name something concrete or stay abstract?
3. **Tension** (1–10): does it create curiosity, or is it self-contained?
4. **Voice-match** (1–10): does it sound like Aayush, or like any "AI thought leader"?

Target combined: 32+ (out of 40). Below 28 → rewrite.
