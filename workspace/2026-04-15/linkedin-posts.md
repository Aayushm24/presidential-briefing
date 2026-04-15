# LinkedIn Post Options — 2026-04-15

**Lead Story:** The next evolution of the Agents SDK

**Best Option:** 3 (avg: 8.4/10, verdict: ship)

**Scores:** Novelty 8 | Insight 8 | Voice 9 | Hook 9 | Teach 8

**Iterations:** 1

---

OPTION 1:
Conviction: The agent infrastructure stack is hardening across every layer simultaneously, from runtime primitives to security tooling, and the builders who wire these layers together now will compound their advantage as each layer stabilizes.

a startup called Gitar just raised $9M to secure AI-generated code

OpenAI just shipped sandboxed execution and long-running agent support in their Agents SDK

these two facts seem unrelated. they are not.

the first tells you the output volume from agents is now large enough to create its own security market. Gitar exists because agents are writing real code that ships to production. enough of it that someone raised $9M just to audit what comes out the other side.

the second tells you the runtime primitives builders have been hacking around for months are finally becoming first-class infrastructure. container management, state persistence, isolated code execution. all of that just became platform-level features.

now layer in what we are seeing from major software companies. creative tools, productivity suites, dev platforms. they are all moving from single-app AI features to multi-step agent workflows that coordinate across products.

this is multiple layers of the agent stack hardening at once. runtime, orchestration, and security.

Notion's cofounder recently shared they rebuilt their agent system five times before it worked. used 100+ tools. wrestled with tradeoffs between different integration approaches that had no clear answers. that is the honest cost of production agents today.

but that cost drops dramatically when the underlying primitives stabilize. native sandboxed execution means you stop building container infrastructure. long-running support means you stop managing state yourself. security tooling means you stop manually auditing agent output.

i think builders who wire these layers together now, even imperfectly, will have a structural edge. not because the tools are perfect. because the muscle memory of building multi-step, multi-tool agent systems compounds in ways that reading changelogs does not.

waiting for v2 of everything sounds rational. but the teams shipping today are the ones defining what v2 looks like.

---

OPTION 2:
Conviction: The conventional wisdom that agent tooling is "too early" has quietly become wrong. The real risk is no longer building too soon. It is building too late and having to unlearn prototype patterns that do not survive production constraints.

most people think agent infra is too early to bet on

i think that window already closed

the common take goes like this. the SDKs are immature, the patterns are not settled, wait for things to stabilize before investing serious engineering time.

sounds reasonable. it is also wrong.

OpenAI just shipped sandboxed execution and long-running agent support in their Agents SDK. these are not experimental features. these are the exact primitives builders have been duct-taping together with custom orchestration for months. container management, state persistence, isolated code execution. all just became first-class infrastructure.

major software companies are shipping agents that coordinate across entire product suites. not a chatbot in one app. multi-app agent orchestration where one workflow touches five or six different tools.

Notion's cofounder shared they rebuilt their agent system five times. used over 100 tools. fought through integration decisions that had no clear answers at the time.

that last detail is the one people miss. Notion did not wait for stable tooling. they built through the instability and now they have a working agent product while others are still planning.

i have seen this pattern before in infrastructure cycles. the teams that build during the messy phase develop intuitions you cannot get from documentation. they learn which abstractions leak. which tool combinations break under load. where the real bottlenecks hide.

Gitar just raised $9M to secure AI-generated code. that market only exists because enough agents are shipping real output to create security debt worth solving. the ecosystem is not waiting.

the risk is not that you build on primitives that change. the risk is that you spend six months prototyping while competitors spend six months in production learning things prototypes never teach you.

agent infra is not too early. it is early enough that showing up still matters.

---

OPTION 3 (recommended):
Conviction: Building agent systems before the tooling is ready is painful and expensive, but the architectural intuitions you develop through that pain become your biggest advantage once the platforms catch up.

i rebuilt an agent pipeline three times last month

not because i made mistakes. because the right architecture kept changing underneath me.

first version used a simple loop. model calls tool, gets result, calls next tool. worked fine until the workflow needed to run for more than a few minutes. state management became a nightmare.

second version added persistent state and container isolation. i was essentially building my own sandbox runtime. it worked but i spent more time on infrastructure than on the actual agent logic.

third version stripped it back down after i realized half my custom code was solving problems that should be platform-level primitives.

then OpenAI shipped their updated Agents SDK with native sandboxed execution and long-running agent support.

i almost laughed. two of the three rebuilds were solving exactly what they just made first-class features.

but here is what i did not expect. having built those layers myself, i understood the new SDK at a level i would not have reached by just reading the docs. i knew which tradeoffs they made. i knew where the abstractions would leak. i knew what to test first.

Notion's cofounder recently shared they rebuilt their agent system five times and used 100+ tools. that number did not surprise me at all. that is what production agents actually cost right now.

the stack is maturing fast. Gitar raised $9M just to handle the security debt from all the code agents are producing. the primitives are stabilizing. the security layer is forming. the orchestration patterns are emerging.

i think the builders who will benefit most from this wave are not the ones who waited for stable tooling. they are the ones who built through the instability and developed intuitions about multi-step execution, tool orchestration, and failure modes that no SDK tutorial can teach.

the concrete is setting. better to have your hands in it than to show up after it dries.