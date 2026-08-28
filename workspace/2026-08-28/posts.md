# LinkedIn posts, 2026-08-28

**Lead:** Claude Code's auto mode blocks its own cleanup commands after prompt injection attacks
**Briefing type:** pattern
**Best option:** 1 (pre-council self-score)

---

## OPTION 1, contrarian-philosopher (hook score: 8)

**Conviction:** L2 - The security community has the infrastructure answer, but AI companies keep looking for prompt fixes

**Post:**
Johann Rehberger achieved an 80% success rate breaking Claude Code's auto mode.

The safety mechanism designed to protect coding agents actually prevented Claude from cleaning up its own compromise.

Every team I talk to is asking the same question: how do we secure agents in production?

The answer isn't better classifiers. It's containers.

At Atlan, when we build agents for GTM workflows, they run isolated from our main systems. Network restrictions. Credential isolation. Container boundaries.

The infrastructure approach that's worked in security for decades.

But AI companies keep trying to solve this with smarter prompts and better command analysis.

Here's what's actually happening:

Auto mode analyzes each command in isolation. It approved "create file from base64" then blocked "kill process" without understanding these were attack and response.

Command-level classification can't see sequences. A zip file extraction followed by Python imports that resolve unexpectedly. Legitimate operations that become malicious through timing and context.

The gap between what agents observe and what runtimes actually execute.

Simon Willison reached the same conclusion: containers remain mandatory infrastructure, not optional safety.

Teams treating Claude Code like an IDE plugin instead of autonomous code execution are missing the threat model entirely.

The convenience of unrestricted access isn't worth the blast radius when the attack succeeds.

IMO, the founders who figure out secure agent deployment early get access to capabilities that unprotected teams can't risk using.

What's the ugliest security workaround in your current agent setup?

---

## OPTION 2, personal-I-observer (hook score: 7)

**Conviction:** L1 - Most founders missed the unit economics shift that makes AI agents economically viable now

**Post:**
AI companies bled money for two years running agents at scale.

That just changed.

I've been tracking AI unit economics across dozens of startups since 2024. Most founders still think agents are too expensive to deploy continuously.

They're optimizing for the wrong cost structure.

Tomasz Tunguz quantified what I've been seeing: AI went from -94% gross margins to revenue-per-megawatt positive in 2026.

The shift happened through inference cost collapse, not training efficiency.

Teams that couldn't afford to run agents at startup-scale usage can now deploy them profitably.

When we build agents at Atlan, the cost conversation moved from "can we afford to run this?" to "does this generate enough value per compute hour?"

The economic constraint shifted from operational costs to opportunity costs.

Revenue-per-megawatt becomes the new unit economic foundation for AI-first companies. Like revenue-per-employee was for software companies.

Teams that master this calculation early get access to AI capabilities that were financially impossible six months ago.

The infrastructure requirements make sense when agents pay for themselves through revenue generation rather than bleeding compute costs.

I think this economic foundation is why we're seeing realtime video generation and reasoning models become practical simultaneously.

The compound effect of multiple AI capabilities reaching economic viability at once creates new product possibilities that neither enabled alone.

What AI capability would your team deploy if the economics suddenly made sense?

---

## OPTION 3, absurdist-truth-teller (hook score: 8)

**Conviction:** L3 - Teams building video features need to know realtime generation crossed the speed barrier this week

**Post:**
H3 Max creates high-quality video faster than it takes to watch it.

Meanwhile, most teams still think video AI means submitting jobs and waiting for results.

Ethan Mollick documented the speed breakthrough that changes everything: realtime generation through a web interface, including prompt enhancement processing.

The feedback loop compression that makes video creation feel like collaborative document editing.

I build AI agents that generate marketing assets for Atlan's GTM workflows. Until this week, video meant batch processing. Request, wait, review, iterate tomorrow.

Now it means: create, iterate, ship.

The technical achievement centers on inference optimization, not model architecture improvements. H3 Max reaches realtime speeds through specialized hardware acceleration and pipeline improvements.

Similar speed gains are possible across other video systems with similar infrastructure investments.

For product teams, this enables video features that require immediate user feedback:

- Prototyping workflows become interactive
- Educational content creation happens in real-time
- Marketing asset generation supports synchronous collaboration

The infrastructure requirements align perfectly with the container-based security model teams need for coding agents anyway.

Teams investing in proper AI infrastructure get access to both secure agent deployment and realtime media generation simultaneously.

The economic model mirrors the broader unit economics shift. Realtime generation makes video AI practical for applications with immediate feedback requirements.

Teams can now justify video AI investments based on user engagement metrics rather than just production efficiency gains.

What video workflow would you automate if generation happened at conversation speed?
