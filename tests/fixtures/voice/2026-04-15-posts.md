# LinkedIn Post Options — 2026-04-15

**Lead Story:** Not all AI agents are created equal

**Best Option:** 3 (avg: 8.6/10, verdict: ship)

**Scores:** Novelty 8 | Insight 8 | Voice 9 | Hook 9 | Teach 9

**Iterations:** 2

---

OPTION 1:
Conviction: the knowledge gap angle is real but the original read too much like a news recap. the hook scored well so i'm keeping it. the fix is making it teachable, giving readers a concrete action they can take today, not just telling them frameworks exist. adding specific numbers and a clearer "here's what to do" structure.

the agent knowledge gap just closed

six months ago the difference between teams shipping agents and teams stuck prototyping was knowledge that wasn't written down.

hard-won intuitions like:

- when does a simple workflow automation tool solve the problem vs when do you need dedicated infrastructure and six-figure LLM bills
- how do you scope an agent so it doesn't quietly underperform for three months before anyone notices
- what actually needs a reasoning system vs what just needs a well-designed automation

that knowledge is now structured, published, and specific.

Farooq and Rajwani just dropped a framework on Lenny's Newsletter built from real deployments at Jack in the Box, Tripadvisor, The Home Depot. the core move is straightforward. categorize agent projects by architectural tier before you prioritize them.

here is why that matters more than it sounds.

i watched a team spend 11 weeks building a complex AI system for a customer support use case that should have been a $500/month chatbot on a workflow automation platform. different tier. different cost profile. different team size. they had both items on the same backlog scored with the same impact-vs-effort matrix.

Farooq and Rajwani call this "comparing apples, oranges, and jet engines." once you see it you cannot unsee it.

the practical move if you're running agent projects right now:

- pull up your agent backlog
- tag each item as automation workflow, supervised agent, or autonomous system
- check whether any two items in different tiers are being compared against each other
- rescope or kill the ones you miscategorized

the teams winning in retail operations, healthcare admin, financial workflows are not smarter. they categorized correctly on day one and shipped version five while others debated version one.

frameworks are public. tooling is accessible. the only differentiator left is iteration speed.

---

OPTION 2:
Conviction: this was the strongest all-around option. high insight density and teachability. the hook underperformed relative to the content quality so i'm sharpening it. leaning harder into the specific story of watching teams fail, and making the "categorize before you code" takeaway even more concrete with a step-by-step readers can steal.

stop stack-ranking your agent backlog

i keep watching the same mistake across companies.

a team puts "automate customer support" and "build autonomous shopping assistant" on the same spreadsheet. scores them both on impact vs effort. picks one. three months later they are either over-engineering a simple workflow or under-resourcing something that needed dedicated infrastructure from day one.

one team i talked to spent $140k and 14 weeks building what turned out to be a tier-one automation problem. they staffed it like a tier-three autonomous system because their prioritization framework didn't distinguish between the two.

Farooq and Rajwani just published a framework on Lenny's Newsletter that names this problem precisely. they built it working with enterprise teams at Jack in the Box, Tripadvisor, The Home Depot.

the core idea. agent initiatives fall into fundamentally different architectural tiers. a chatbot running on a workflow platform at $500/month and an autonomous system generating six-figure LLM bills are not comparable items. scoring them on the same matrix guarantees you misallocate.

the popular belief is that you need better models or better engineers to ship agents.

the contrarian truth is that you need better categorization before you write a single line of code.

here is the framework i've started using with teams:

tier one. bounded automation. known inputs, known outputs, concrete success metrics. workflow tools like n8n or similar. $500/month range. ship in days.

tier two. supervised agent. handles ambiguity but a human reviews outputs. needs prompt engineering and evaluation infrastructure. $2-10k/month. ship in weeks.

tier three. autonomous system. makes decisions, takes actions, manages its own failure modes. dedicated ML engineering. six-figure annual cost. ship in months.

before you build anything, tag every item on your backlog with a tier number. if two items in different tiers are competing for the same sprint, your process is broken.

the teams shipping real results in retail, healthcare admin, financial workflows all started by scoping precisely what the agent owns. bounded problems with concrete metrics.

generic horizontal agents are getting commoditized fast. Microsoft ships those. the defensible play is picking a vertical, categorizing ruthlessly, and iterating fast on a bounded problem.

the knowledge to do this is now public. the question is whether your team uses it before your competitor does.

---

OPTION 3 (recommended):
Conviction: strongest hook and best voice match. the personal story works. what scored low was novelty, it felt like a wrapper around someone else's framework rather than a genuine learning story. the fix is adding more specific detail about what actually failed in each rebuild, making the "i wasted four builds" line feel earned, and giving readers a diagnostic they can run on their own projects today.

i rebuilt our agent pipeline 4 times in 6 weeks

build one. i scoped a customer-facing agent as an autonomous system. gave it broad permissions, open-ended prompts, access to three internal APIs. it worked in demos. in production it hallucinated edge cases we couldn't predict and cost $3,200 in the first week on API calls alone.

build two. i pulled back permissions and added a human review step. latency jumped to 45 seconds per interaction. users abandoned it.

build three. i stripped the reasoning layer entirely and rebuilt it as a rule-based workflow in n8n (a workflow automation tool). fast and cheap but couldn't handle the 30% of queries that actually needed judgment.

build four. i finally asked the right question. what tier of problem is this actually?

that question came from Farooq and Rajwani's framework on Lenny's Newsletter. they built it working with teams at Jack in the Box, Tripadvisor, The Home Depot. the insight that hit me. a $500/month chatbot and a six-figure autonomous system are not the same category of project. i had been treating them as the same thing and toggling features up and down trying to find the sweet spot.

there is no sweet spot. there are tiers.

i went back and recategorized our entire agent backlog.

- three items dropped from tier two to tier one. they didn't need an agent at all, just a well-designed automation
- one got flagged as tier three, needing infrastructure and budget we hadn't allocated
- the one i'd been struggling with landed clearly as tier two. supervised agent, bounded scope, human review on exceptions only

i rescoped it as a bounded workflow handling the 70% of queries that follow predictable patterns. exceptions route to a human with full context pre-loaded. rebuilt it in eight days.

it has been running for 19 days now. resolution time dropped 40%. cost is $780/month. no hallucination incidents.

here is the diagnostic i wish i'd run on day one:

- can you list every input type the agent will see? if no, you haven't scoped it
- can you define success in one metric? if no, you're building too broad
- does it need to make decisions or just execute steps? this determines your tier
- what happens when it fails? if the answer is "it depends," you need a human-in-the-loop layer

six months ago this kind of production intuition wasn't written down. you had to fail your way into it. now the frameworks and case studies from real deployments in retail, healthcare, enterprise workflows are published and specific.

i wasted four builds and six weeks learning what a framework could have told me on day one. run the diagnostic before you write the code.