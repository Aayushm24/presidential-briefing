# LinkedIn posts, 2026-05-03

**Lead:** AI agents are forcing teams to rebuild trust systems from scratch
**Briefing type:** pattern
**Best option:** 1 (pre-council self-score)

---

## OPTION 1, contrarian (hook score: 8)

**Conviction:** L2: Most builders treat agent permission creep as a bug when it's actually a feature that needs explicit design

**Post:**
Every AI agent starts with file access.

And ends up managing your entire life.

Swyx's personal agent began reading documents. A few months later, it was running backups at 2 AM, monitoring system health, and drafting his business emails.

No single permission felt dangerous. The end state was an AI system with deeper access than he'd ever explicitly authorized.

This is happening to every team shipping agents right now.

The permission model breaks because it's binary, "file access: yes/no", instead of contextual. Users want the agent to get more capable. They don't want to wake up discovering their AI is managing business communications without explicit authorization.

At Atlan, when we build agents, we design expansion triggers that require user confirmation. Instead of gradual scope creep, you get explicit checkpoints: "Agent can read files, will ask permission before modifying, reports every action taken."

The UI becomes less about features and more about governance.

Most teams I talk to are building permission systems like it's still 2022. Trust boundaries need to be designed from day one, not bolted on after users complain about scope creep.

The teams that get this early will ship agents users actually trust. The ones that don't will face adoption collapse or reputational damage later.

What permission boundaries are you designing into your agent stack?

---

## OPTION 2, personal-I observer (hook score: 7)

**Conviction:** L3: Software engineering is restructuring around plan-review loops where engineers design AI tasks and evaluate outputs

**Post:**
Every week I watch engineering teams restructure around AI.

The pattern is always the same.

Teams that adapt fast nail the plan-review loop. Engineers spend time designing AI tasks and evaluating outputs, not writing code line by line. They ship features in days that used to take weeks.

Teams that don't adapt find themselves slower than pure human development.

The middle ground doesn't exist.

Swyx's retrospective on 2021-2025 frames the mental model CTOs are using now. AI ate the middle of software development. Engineers still plan the work and review the output. The AI generates the code.

The skills that matter flip completely:
- Code review becomes the core competency
- Architecture design becomes more valuable
- Junior engineers who prompt well beat senior engineers who can't evaluate AI output

At Atlan, we're seeing this firsthand. Teams report spending 40% of their time on prompt engineering and 60% on output validation. The coordination effects compound when everyone operates this way.

The actual job becomes unrecognizable. Not "people who write code" but "people who design systems and verify AI execution."

Agile sprints designed for human velocity don't fit AI-native development cycles. Scrum ceremonies built around individual productivity miss the new coordination points.

What does your team's plan-review cycle look like right now?

---

## OPTION 3, data-point (hook score: 8)

**Conviction:** L1: Executive AI perception gets shaped by social media narratives, not technical ground truth

**Post:**
Ethan Mollick gets asked about AI labs by executives weekly.

The questions come from X discussions filtered through LinkedIn. Not from technical benchmarks, API reliability, or cost analysis.

This creates a two-track reality every AI founder faces. Engineers evaluate models based on performance. Executives evaluate AI partnerships based on brand perception and peer network signals.

The same technology gets different strategic treatment based on narrative, not capability.

I see this gap in every AI pitch meeting. Technical documentation for the builders. Executive briefings that meet C-suite audiences where they actually form opinions, which is social media momentum, not ground truth.

The Oscar Academy's decision to exclude AI-generated content from award eligibility shows how institutional gatekeepers operate on reputational risk. The rule protects organizational prestige, not artistic quality.

For AI media startups, this means regulatory environments get shaped by institutional self-preservation. Building the best AI video generation doesn't matter if major distribution channels ban AI content for brand safety.

Every industry has equivalent gatekeepers making similar calculations. Product-market fit includes navigating gatekeeper perception, not just user adoption.

AI companies need institutional relationship development as much as technical development. The best model loses if it can't get past the perception layer.

How are you communicating AI strategy to decision-makers who form opinions on LinkedIn?
