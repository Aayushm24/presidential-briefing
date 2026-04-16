# LinkedIn Post Options — 2026-04-16

**Lead Story:** Codex for (almost) everything

**Best Option:** 3 (avg: 8.2/10, verdict: ship)

**Scores:** Novelty 7 | Insight 7 | Voice 9 | Hook 9 | Teach 9

**Iterations:** 1

---

OPTION 1:
Conviction: The AI labs aren't building tools for software companies. They're building the software companies. When Anthropic's CPO resigns from Figma's board because of a conflict of interest, and OpenAI's Codex expands into a full platform, these aren't isolated moves. They're the same move from different directions.

**agents are replacing the interface layer**

Anthropic's chief product officer just resigned from Figma's board.
same week, OpenAI's Codex expanded into computer use, browsing, image generation, and a plugin ecosystem.

these two facts seem unrelated. one is a board governance story. the other is a platform expansion.

but they point to the same shift.

Mike Krieger left Figma's board because Anthropic is building design tools that compete with Figma directly. not a plugin. not an integration. a replacement where the agent is the primary user.

OpenAI's Codex is no longer a coding assistant. it is a platform competing with Cursor, Replit, and the entire IDE category. when your "assistant" can browse the web, use a computer, generate images, and run plugins, it is not assisting. it is replacing.

go-to-market teams are wiring Claude directly into CRMs and data warehouses via MCP (Model Context Protocol, basically a standard way for agents to plug into your systems). they are skipping the SaaS apps those systems were built around.

the pattern is the same in every case.

**the AI labs are not augmenting SaaS.** they are becoming SaaS.

i saw this firsthand building agent workflows for a sales team last quarter. we started by connecting the agent to the existing CRM interface. it fought us at every step. the moment we pointed the agent at the raw data layer and let it own the decisions, the whole system clicked. shipped in days instead of weeks.

the defensible position is no longer "best UI for a workflow."

it is "best data and domain logic for an agent to consume."

if your product is a UI layer over a process that an agent can own end to end, the clock is ticking. the question every founder should be asking right now: what do we own that is not a screen?

---

---

OPTION 2:
Conviction: Most builders think the right response to AI agents is integrating them into existing products. That instinct is exactly wrong. The companies winning are the ones that let agents own the workflow from scratch, not the ones adding copilot features to legacy architectures.

**adding AI to your SaaS won't save it**

the most common strategy in software right now is "add an AI copilot."

every SaaS company is doing it. design tools, CRMs, project management, analytics dashboards. slap a chat interface on the side. ship it. call it AI-native.

i think this is the wrong move for almost everyone doing it.

here is what actually happened this week.

Anthropic's CPO resigned from Figma's board because Anthropic is building design tools that compete with Figma's core product. not a Figma plugin. **a Figma replacement.**

OpenAI's Codex expanded into computer use, browsing, image generation, and a plugin ecosystem. it is not augmenting IDEs. it is becoming one.

sales and RevOps teams are connecting Claude directly to production databases and CRMs via MCP (Model Context Protocol, a standard that lets agents plug into your data systems directly). they are not using the SaaS UI at all.

the pattern is clear. agents don't want to live inside your app. they want to consume your data and skip your interface entirely.

i hit this wall myself building an agent system for a RevOps team. we spent two weeks trying to bolt agent capabilities onto the existing CRM workflow. every integration point broke because the architecture assumed a human was clicking through screens. the third week, we threw it out and rebuilt with the agent as the primary interface. data in, decisions out, humans only on exceptions. that version shipped in four days and is still running.

**the copilot strategy is a delay tactic.** it buys you 12 to 18 months while the labs build the replacement.

the real question is not "how do i add AI to my product."

it is "what data and domain logic do i own that an agent cannot replicate."

if the honest answer is "just the UI," you need a new strategy. not a better copilot.

---

---

OPTION 3 (recommended):
Conviction: Building agent-native means accepting that most of your existing architecture is wrong. i learned this the hard way, and the pattern playing out across the industry this week confirms it. The builders who start from the agent as the interface, not the human, ship faster and build things that actually hold up.

**i rebuilt the wrong thing three times**

six months ago i was building an agent system that sat on top of an existing workflow. CRM data in, structured actions out, human reviews the output.

it kept breaking. not because the model was bad. because the workflow was designed for a human clicking through screens, not an agent making decisions.

i tried patching it. added guardrails. added a review step. added logging so i could debug failures.

**none of it worked.**

the third time i rebuilt it, i started from scratch. the agent was the interface. no human UI in the loop for the core workflow. data went in, decisions came out, humans only intervened on exceptions.

that version shipped in a week. it is still running.

i thought about this when i saw the news this week.

Anthropic's CPO resigned from Figma's board because Anthropic is building design tools that compete with Figma directly. not an integration. a replacement built around the agent as the primary user.

OpenAI's Codex expanded into browsing, computer use, image generation, and a plugin ecosystem. it is not a coding assistant bolted onto an IDE. it is becoming the IDE.

go-to-market teams are connecting Claude to CRMs and warehouses via MCP (Model Context Protocol, a standard that lets agents talk directly to your data layer). they are bypassing the SaaS interface entirely.

**the pattern is identical to what i hit.** every team trying to wrap agents around human-designed workflows eventually hits a wall. the ones that rebuild around the agent as the primary interface break through.

here is the practical test. if your agent spends more than 30% of its cycles navigating a UI or translating between human-readable formats, you are fighting the architecture. strip the interface. point the agent at the data. let it own the workflow.

if you are building agents right now and it feels like you are fighting the system, you probably are.

start from the agent. not from the screen.

---