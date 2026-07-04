# LinkedIn posts, 2026-07-04

**Lead:** Fable's autonomous judgment beats rigid instructions for costs and creativity
**Briefing type:** pattern
**Best option:** 2 (pre-council self-score)

---

## OPTION 1, contrarian-philosopher (hook score: 8)

**Conviction:** L2: Most builders architect AI systems with human management instincts that bottleneck the very autonomy they're trying to unlock.

**Post:**

Most builders are micromanaging their AI agents into mediocrity.

They write elaborate rules. Specify which models to use. Define when to run tests. Control every decision.

Then wonder why their agents feel mechanical.

Every week I watch teams over-architect AI systems with human management instincts.

The pattern is always the same, detailed instructions that bottleneck the autonomous reasoning they paid for.

Simon Willison discovered something interesting this week. He told Fable "use your judgment to select appropriate lower-power models for subagents."

Token costs dropped. Output quality stayed the same. The system started making smarter compute decisions than his rules ever did.

When we build agents at Atlan, we don't have them click buttons. They call APIs, read databases, talk to other apps through MCPs. But we learned something harder.

The agent often knows better than we do when to run tests, which model fits the task, how deep to go on research.

Here's what I've noticed works better:

- "Use your judgment on model selection" beats rigid compute rules
- "Decide whether this needs testing" beats predetermined test triggers
- "Make this better" repeated beats specifying exactly how

Most builders think control equals quality.

But AI systems process context humans miss. They see task complexity, available information, and quality requirements simultaneously.

When you over-specify, you're optimizing for your comfort, not the system's capability.

IMO the best agent architects are learning to delegate decisions, not dictate them.

What decisions are you making for your AI that it could make better than you?

---

## OPTION 2, personal-I observer (hook score: 8)

**Conviction:** L1: I'm watching AI exercise genuine creative judgment that outperforms human specifications, but most people haven't noticed this shift happening yet.

**Post:**

I watched AI redesign a game 6 times in one conversation.

Ethan Mollick kept asking Claude Fable to make it "more AAA."

No specifications. No requirements. Just "make this better" repeated.

The system upgraded graphics autonomously. Added boss fights. Implemented custom soundtracks. Pushed to WebGL limits.

When Mollick clarified he meant "AAA" satirically, Fable pivoted completely. Added lootboxes, EULAs, useless settings, elaborate boot screens.

All its creative decisions. Zero human direction on the specifics.

I build AI agents at Atlan and this tracks perfectly with what I see.

The agents that produce the most surprising results get the least specific instructions.

My best automation pipeline? I told it "turn Demandbase exports into personalized emails" and let it figure out the 8-stage process.

- Parse CSV format interpretation
- Internal signal checking logic
- Research depth and sourcing
- Email tone and length decisions

Every decision I would have specified wrong.

Most teams I talk to are still writing detailed agent prompts like they're programming traditional software.

But AI systems don't execute instructions. They exercise judgment.

When you over-specify creative choices, you prevent the system from exploring solution space you didn't anticipate.

The pattern I keep seeing: the more ambitious the creative output, the vaguer the initial instruction.

"Make this captivating" beats "add transitions and improve pacing."

"Use your judgment" beats "follow these 12 rules."

What creative project are you micromanaging that you could delegate entirely?

---

## OPTION 3, absurdist-truth-teller (hook score: 8)

**Conviction:** L3: The market is punishing elaborate interfaces and rewarding direct utility, builders who prioritize functional depth over visual polish will dominate.

**Post:**

A decade of "tools for thought" demos got beaten by ugly command lines.

Swyx nailed it this week. Teams spent 10 years building beautiful canvas interfaces, elaborate visual workflows, and sophisticated interaction models.

Then Claude Code shipped. Cursor shipped. Low-contrast, poorly designed CLIs.

And they completely destroyed the pretty demos by doing commodity thinking for you.

Josh W. Comeau's latest course launch? One-third the sales of typical launches. His existing courses? Down significantly year-over-year.

The reason: AI handles developer learning directly now.

No elaborate learning interfaces. No visual progress tracking. No community features.

Just: describe what you want, AI builds it.

The pattern is everywhere once you see it.

- Complex project management tools losing to AI that just handles the project
- Elaborate design systems losing to AI that generates the interface
- Sophisticated workflow builders losing to AI that automates the entire workflow

Users don't want better tools to solve problems faster.

They want problems solved completely without tools at all.

At Atlan, we've learned this lesson building agent workflows. The humans never open the app when the agent is working.

The interface becomes: natural language input, autonomous execution, direct output delivery.

Everything in between is friction.

The successful pattern: functional depth over interface sophistication.

AI that understands intent and executes directly beats AI that helps humans execute through better interfaces.

Your beautiful UI is probably someone's unnecessary step.

What interface are you building that AI could just eliminate entirely?
