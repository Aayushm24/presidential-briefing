# Example: Agent Stack Hardening (12 engagement)

## Post

Someone raised $9M just to babysit AI-generated code.

Not to write it. Not to improve it. To audit what agents spit out.

The startup Gitar secured funding on this exact thesis. Agents are now writing enough production code that securing it is a venture-scale problem.

Same week, OpenAI shipped sandboxed execution and long-running agent support. The container management and state persistence builders have been duct-taping for months? Platform-level now.

These two things look unrelated. They're not.

This is multiple layers of the agent stack hardening at once:
- runtime primitives becoming first-class
- orchestration getting native support
- security tools catching up to output volume

And the big software companies? Creative tools, productivity suites, dev platforms. All moving from single-app AI features to multi-step agent workflows.

Notion's cofounder shared they rebuilt their agent system five times before it worked. 100+ tools. Tradeoffs with no clear answers.

At Atlan, we've been building agents for months and this tracks.

The results can be magical. But "magical" still costs you hours of fighting context management, output quality, hallucinations, edge cases, and latency.

Here's why IMO that cost should drop now:
- native sandboxed execution = stop building infra
- long-running support = stop managing state yourself
- security tooling = stop manually auditing agent output

Each primitive that stabilizes removes a full layer of pain from your stack.
Waiting for v2 of everything sounds rational. But the teams shipping today are the ones defining what v2 looks like.

Muscle memory of building multi-step, multi-tool agent systems compounds in ways that reading changelogs never will.

What's the ugliest workaround in your current agent setup? 👀

## What makes this work

- Absurdist opener: '$9M just to babysit AI-generated code' — unexpected specific
- At Atlan anchor: 'At Atlan, we've been building agents for months and this tracks'
- IMO as genuine hedge: 'Here's why IMO that cost should drop now:'
- Closing is an invitation: 'What's the ugliest workaround in your current agent setup?'
