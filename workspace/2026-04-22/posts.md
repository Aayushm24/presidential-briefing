# LinkedIn posts - 2026-04-22

**Lead:** AI coding tools are entering a volatile pricing and consolidation phase that will force every dev team to re-evaluate their tooling stack
**Best option:** 2

---

## OPTION 1 - contrarian (1306c)

**Conviction:** The $60B Cursor valuation and 'nobody uses it' are both true, they're measuring different things.

SpaceX priced Cursor at $60B this week.

George Hotz wrote "nobody I know uses Cursor anymore" the same week.

I've been staring at these two sentences for three days.

They're both probably right. SpaceX engineers ship millions of lines of code for rockets, satellites, Starlink. If xAI gives Cursor a 40% velocity edge, that's $60B of strategic infrastructure, not a subscription tool.

Hotz is watching developer behavior. SpaceX is buying developer distribution. Different markets, same week.

What worries me is the gap between those two things.

Every AI coding tool is currently valued by its distribution potential, not its actual usage. That means the pricing reflects what someone hopes to control, not what developers actually choose.

I keep asking dev teams: if your primary coding tool got acquired tomorrow, what's your migration plan?

Most don't have one.

The teams I see being thoughtful about this treat AI tooling like cloud infrastructure, assume repricing, keep the core workflows portable, don't build a dependency you can't port in a week.

The ones who aren't doing this are one acquisition announcement from a painful quarter.

What's your exit plan?

P.s. "Nobody I know uses Cursor" and "$60B for Cursor" being true at the same time is the whole story of 2026 AI valuations. 👇🏻

---

## OPTION 2 - personal-discovery (1426c)

**Conviction:** AI coding tool volatility is the market's way of telling you to keep workflows portable.

I ran an internal audit of our AI coding tools at Atlan this week.

Three hours. Every tool we use, what it's actually doing, which workflows depend on it, how long migration would take.

Turned out we had way more lock-in than I thought.

The audit was triggered by three things that happened the same week.

GitHub paused new Copilot signups and cut premium model access to the top tier. Anthropic accidentally leaked a $100/month Claude Code tier through a broken A/B test and walked it back. SpaceX locked in a $60B option on Cursor.

None of it was planned. All of it landed in the same 5 days.

What I realized from the audit: the switching cost is invisible until it's not. Custom agent rules, specific prompt formats, API response assumptions, review pipeline integrations, none of these show up on a budget sheet. But they represent real weeks of engineering if you need to migrate.

The tools that embed deepest don't necessarily win on features. They win on how thoroughly they can make themselves load-bearing before you notice.

IMO the switching cost is the product now. That's what SpaceX is buying for $60B. That's what GitHub is protecting. That's what Anthropic is actually pricing.

I've started treating AI coding tools the way I treat cloud infrastructure: assume repricing, keep workflows portable, never build a dependency you can't port in a week.

Could you swap your primary AI coding tool in 5 days?

---

## OPTION 3 - pattern-observation (1464c)

**Conviction:** Meta's employee keystroke harvesting is a data play, not just a privacy story.

Meta started recording employee keystrokes for AI training.

I've been watching AI companies fight for proprietary data for two years. Everyone scrapes the web, buys datasets, tries to get user opt-ins.

Nobody cracked actual workplace behavior until now.

The bottleneck was never compute or model architecture. It was always the data of what knowledge work actually looks like. How fast engineers type when they're debugging vs. writing docs. When people copy-paste vs. retype. How many times something gets rewritten before it goes out.

Meta just solved that. Their employee base is now a proprietary training dataset no competitor can access without hiring the same people.

This is the data that makes an AI assistant feel like it understands your work. The model is the same. The training distribution finally includes what work actually looks like.

At Atlan, half my work is building AI agents. The agents that work are the ones trained on actual workflow patterns, not generic examples. Meta is doing at scale what we do manually on every agent we build.

The companies with access to proprietary behavioral data are going to build products that feel qualitatively different, a different category, not just an increment.

What unique behavioral data does your product see that nobody else can replicate?

P.s. This is also why SpaceX's $60B Cursor bet makes more sense than it looks. They want the engineering behavior data, not the code completions. 👇🏻

---
