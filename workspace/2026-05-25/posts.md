# LinkedIn posts, 2026-05-25 (iteration 1)

**Lead:** AI augmentation requires more human judgment and craft, not less, the 'more automation, more humans' paradox is becoming a product design principle
**Briefing type:** pattern
**Revision trigger:** council REVISE verdict at iter 0
**Best option:** 2 (revised score: 8.4/10 average)

---

## OPTION 1, commentary-take (hook score: 8)

**Conviction:** L2: The AI automation paradox reveals that successful products amplify human judgment rather than replace it. The interface layer becomes the competitive moat.

**Post:**
I've been thinking about why founders automate the wrong things.

They build agents that handle complex decisions. They skip the boring stuff that actually compounds.

Dan Shipper spent a year watching 30 employees use AI daily at Every. The more automation they added, the more human decisions they had to make.

Every automated workflow spawned new judgment calls. When to intervene, how to interpret outputs, which tools to chain together.

The employees who got the most value from AI spent more time on meta-work. Deciding what to automate, evaluating results, switching context between systems.

I build AI agents for GTM workflows at Atlan and this tracks perfectly. The magic happens in the spaces between automated tasks.

- Prompt crafting for specific contexts
- Output evaluation against business goals
- Context switching between different systems
- Exception handling when automation breaks

When we build agents at Atlan, we don't have them click buttons. They call APIs, read from Snowflake and Postgres, talk to Slack and Salesforce through MCPs, and post results where we want them.

But the humans never open the app when the agent is working. They're busy making judgment calls about what the automation should do next.

IMO, the builders who design AI products assuming users will delegate entirely will lose to those who design for active human participation.

The interface layer, how humans and AI negotiate who does what and when, becomes the competitive moat.

What does your team spend more time on, configuring AI or using it?

---

## OPTION 2, data-point (hook score: 9)

**Conviction:** L3: The 30-employee experiment at Every proves that AI augmentation creates more human touchpoints. Successful teams need workflow scaffolding designed for active participation.

**Post:**
30 employees used AI daily for a year.

The result was more human decisions, with new categories of judgment work showing up everywhere.

Dan Shipper runs Every, a media company that became an accidental laboratory for AI-assisted work. Every person from editors to operations used AI for their daily tasks.

What he discovered breaks the standard automation narrative. The more AI his team used, the more judgment calls they had to make.

Every automated workflow created new categories of human work:

- When to intervene in AI outputs
- How to interpret results for stakeholders
- Which tools to chain for specific contexts
- How to handle edge cases automation missed

The employees who got the most value didn't delegate tasks to AI. They developed personal systems for human-AI handoff.

Writers started drafts themselves, fed specific sections to Claude for expansion, evaluated tone against their intended message, then wove AI content back into their voice.

Operations people automated data pulls but spent significantly more time on interpretation and exception handling. Editors automated research but invested much more effort in source verification and angle development.

Every week i watch this play out in my own work at Atlan. I've been shipping GTM agents for months and the results can be magical. Magical still costs hours of fighting context management, output quality, hallucinations, edge cases, and latency.

Tbh, the most valuable human work happens in the spaces between automated tasks. I think the teams that nail this human-AI collaboration pattern create products their users can't live without.

What percentage of your AI workflow time goes to configuring vs using the output?

---

## OPTION 3, pattern-observation (hook score: 7)

**Conviction:** L1: Most agent frameworks optimize for complex reasoning while missing the reflex tasks that actually compound into productivity gains. Boring automation beats brilliant reasoning.

**Post:**
Everyone building AI agents focuses on the prefrontal cortex.

Planning. Reasoning. Multi-step chains.

Meanwhile, your mortgage gets paid by standing order, running quietly in the background while you sleep.

Garry Tan nailed it. Most agent frameworks treat all cognition as high cognition. The winners nail boring stuff first.

Dan Shipper's year-long experiment with 30 employees at Every confirms this split. The highest-impact AI implementations automated reflex tasks. Pulling data, formatting documents, scheduling posts.

This freed cognitive capacity for editorial decisions, strategy calls, creative problem-solving.

The teams at Every that tried to automate creative or strategic work found AI helpful for generating options. Human judgment remained essential for selecting and executing the best ones.

I've been thinking about why so many builders optimize for the wrong cognitive layer. They chase sophisticated reasoning systems when simple automations that eliminate decision fatigue create more value.

A workflow that automatically sorts incoming emails by urgency beats a sophisticated agent that drafts responses. Sorting happens reflexively. Response crafting requires active human judgment about tone, strategy, relationship context.

At Atlan, we've learned this the hard way building GTM agents across Slack, Salesforce, and Snowflake. The magic happens when you automate the routine tasks so humans can focus on the judgment calls that compound.

Human brains handle roughly seven pieces of information simultaneously. Every routine task that requires active attention consumes one slot.

Automate the routine tasks and you liberate cognitive capacity for higher-value decisions. IMO, the race is to identify which tasks should become reflexive and which require active human participation.

What boring task takes you 15 minutes weekly that you haven't automated yet?
