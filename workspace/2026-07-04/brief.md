# Fable's autonomous judgment beats rigid instructions for costs and creativity

[Simon Willison](https://x.com/simonw/status/2073117641020215566) discovered that letting Claude Fable select lower-powered models for coding subagents saves significant tokens compared to rigid compute rules.

The pattern emerging across multiple builders is clear. AI systems perform better when given autonomy over their own execution decisions. This beats strict constraints every time. This extends from compute selection to testing strategies to creative choices, and the productivity gains compound across entire workflows.

**Key takeaways:**

- Delegating model selection to Fable itself cuts token costs meaningfully while maintaining output quality
- [Ethan Mollick's](https://x.com/emollick/status/2073165421268594871) iterative "make this more AAA" prompts pushed Fable to WebGL performance limits autonomously
- The Claude Code team recommends judgment-based instructions over rule-based constraints for agentic workflows
- Most users underuse frontier models by sticking to basic tasks instead of ambitious, long-horizon projects
- Simple CLI tools outperform elaborate "tools for thought" interfaces by handling commodity thinking directly

### The token economics of model autonomy

[Simon Willison's](https://x.com/simonw/status/2073117641020215566) discovery reveals something fundamental about agentic architecture. When he told Fable "use your judgment to decide an appropriate lower power model and run that in a subagent" for coding tasks, the system began self-selecting compute levels that maintained quality while cutting costs.

This matters because most builders approach AI systems with human management instincts. They specify which model to use, when to run tests, how to structure outputs. But Fable processes context that humans miss. It knows when a task requires Opus-level reasoning versus when Claude 3 Haiku handles the job. It recognizes when a code change needs full test coverage versus when it's safe to skip automated testing.

The [Claude Code team](https://simonwillison.net/2026/Jul/3/judgement/#atom-everything) confirmed this pattern during their AIE presentation. Rather than rigid rules like "only use automated testing for larger features, don't update and run tests for small copy or design changes," they recommend telling Fable to use its own judgment about testing strategy. The model makes better context-aware decisions than predetermined rules.

What I keep coming back to is the economic implication. Token costs scale with both model selection and context length. When Fable autonomously routes simple tasks to cheaper models, it's performing real-time cost optimization that human-written rules can't match. The system sees task complexity, available context, and quality requirements simultaneously, then selects the minimum viable compute path.

This autonomous compute selection becomes more valuable as model prices remain high and usage scales. A workflow that makes hundreds of model calls daily benefits dramatically from intelligent routing. The savings compound: cheaper models for routine tasks free budget for expensive models on genuinely complex problems.

The mechanism behind this autonomy reveals why it outperforms human-designed rules. When Fable evaluates a coding task, it processes multiple context layers simultaneously: the complexity of the required logic, the existing codebase architecture, the error tolerance for the specific function, and the downstream dependencies that might be affected. Human-written routing rules typically optimize for one or two of these factors, missing the multidimensional optimization that the model performs naturally.

Consider a concrete example from Willison's experiments. When Fable encounters a request to "add error handling to this API endpoint," it analyzes the endpoint's role in the application architecture, the types of errors that could occur, the existing error handling patterns in the codebase, and the criticality of the service. Based on this analysis, it might route simple validation errors to Claude 3 Haiku while escalating complex distributed system failure scenarios to Opus. A human-written rule might categorize this as "error handling = medium complexity = Claude 3.5 Sonnet," missing the nuanced requirements analysis that drives optimal model selection.

This context-aware routing creates a feedback loop that improves over time. Each successful task completion provides data about which complexity indicators correlate with model requirements. The system learns to recognize subtle patterns in task descriptions, code context, and user intent that predict optimal compute allocation. This learning happens across all user interactions, creating a constantly improving routing intelligence that static rules cannot match.

### Creative judgment exceeds human specification

[Ethan Mollick](https://x.com/emollick/status/2073165421268594871) ran a live experiment that demonstrates AI creative autonomy. He repeatedly asked Claude Fable to make a game "more AAA" without specifying what that meant. The system autonomously upgraded graphics, added boss fights, implemented custom sounds and soundtracks, and pushed the project to WebGL performance limits.

When Mollick clarified he wanted ["AAA" in the satirical sense](https://x.com/emollick/status/2073226212462215300) that online gamers recognize, Fable autonomously added lootboxes, EULAs, achievements, useless graphical settings, and elaborate boot screens. The model understood both the technical specification and the cultural context without explicit instruction.

This demonstrates genuine creative judgment, not pattern matching. Fable made architectural decisions about code structure, user experience design, and feature prioritization. It exercised taste about what "AAA" means in different contexts. Most importantly, it sustained creative momentum across multiple iterations without losing coherence.

The [video production example](https://x.com/emollick/status/2072875319615213878) extends this pattern. Mollick never touched any tools or made design choices. The AI selected all visual elements, wrote all prompts, and made all production decisions. When Mollick pushed back asking for "captivating to watch, not just a pretty slide show," the system revised its entire approach autonomously.

This creative autonomy outperforms specification-heavy approaches because human instructions bottleneck creative exploration. When builders over-specify desired outcomes, they prevent AI systems from discovering better solutions. Autonomous creative judgment lets the model explore possibility space that humans don't anticipate.

The technical implementation of this creative autonomy involves what AI researchers call "multi-objective optimization without explicit objectives." When Mollick asked for "more AAA," Fable didn't execute a predefined checklist of AAA game features. Instead, it performed real-time evaluation of multiple creative dimensions: visual fidelity, gameplay complexity, user experience sophistication, and industry-standard feature sets. The model balanced these objectives dynamically, making trade-offs between performance requirements and creative ambition that no static specification could capture.

What makes this particularly powerful is the model's ability to maintain creative coherence across iterations. Each "make this more AAA" request built upon previous decisions, creating a creative trajectory rather than random feature additions. The system tracked the evolving creative vision, ensuring that new features enhanced rather than conflicted with existing design choices. This sustained creative reasoning across multiple iterations demonstrates genuine design thinking, not just feature generation.

### Most builders underuse frontier model capability

[Ethan Mollick's](https://x.com/emollick/status/2073112767515492741) observation cuts through current AI deployment patterns: "Many models are excellent as a Google replacement, for homework help, etc. It is someone's agentic use of frontier AI on long-horizon real problems that is impactful."

The pattern is visible across thousands of AI deployments. Teams use GPT-4 for text summarization, Claude for code review, frontier models for search queries. These are commodity applications that underutilize model reasoning capability. The teams shipping meaningful AI value deploy frontier models on ambitious, complex, long-horizon projects where the full reasoning capacity matters.

This connects to Simon Willison's token optimization insight. If you're using frontier models for basic tasks, you're paying premium prices for commodity capability. The economic and capability sweet spot is: frontier models for genuinely complex reasoning, cheaper models for routine execution, and autonomous routing between the two.

The gap between basic usage and ambitious deployment represents most of the unrealized AI value in 2026. Every AI company I watch targets users who attempt long-horizon projects, not users who want better search. The long-horizon users pay more, use more, and create stronger product attachment.

This usage pattern creates a significant compounding advantage for teams that embrace ambitious AI deployment. As they tackle more complex projects, they develop better prompting techniques, learn to structure multi-step workflows, and build institutional knowledge about AI capability boundaries. These teams become increasingly effective at extracting real value from frontier models, while teams stuck in basic usage patterns miss the capability development that drives real productivity gains.

What separates impactful AI usage from commodity usage is sustained project ambition combined with iterative refinement. Mollick didn't ask Fable to "create a game" once. He asked it to "make this more AAA" repeatedly, pushing the system through multiple creative iterations. The compound effect of autonomous judgment across multiple iterative rounds produces results no single prompt achieves.

---

### #2 Altman's DC engagement signals regulatory acceleration

[Sam Altman](https://www.therundown.ai/p/altman-invites-washington-inside-the-ai-industry) is increasing Washington engagement as AI regulation moves from theoretical to practical implementation phases.

The timing matters for builders and CTOs building AI systems. Regulatory frameworks emerging in 2026 will define compliance requirements and market structure through 2030. Teams that track regulatory development early can architect systems that align with likely requirements rather than retrofitting later.

Altman's DC focus represents OpenAI positioning for regulatory capture scenarios where established players influence rule-making that affects competitive dynamics. For smaller AI companies, this means monitoring regulatory developments that could create compliance barriers favoring established players or, conversely, requirements that level competitive playing fields.

The specific regulatory areas gaining momentum include model evaluation frameworks, deployment safety standards, and liability allocation for AI system outputs. Each creates different competitive implications depending on implementation details. Founders should track these developments as business planning inputs, not just compliance obligations.

The broader pattern shows AI regulation transitioning from academic discussion to operational implementation. DC engagement increases when regulatory outcomes become predictable enough to warrant lobbying investment. What I see across AI companies is that 2026-2027 will define the regulatory environment they'll operate within for years.

---

### #3 Interface sophistication loses to functional utility

[Swyx observes](https://x.com/swyx/status/2073220591684096087) that "tools for thought" projects with elaborate visual interfaces got "completely mogged by low contrast poorly designed CLIs just winning because they do commodity thinking for you."

The market evidence supports this. [Josh W. Comeau](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) reports his latest course sales at one-third of typical launch performance, with existing course sales down significantly year-over-year. He attributes the decline primarily to AI tools handling developer learning and skill development directly rather than through educational content.

This represents a fundamental shift in how people interact with complex software capabilities. Rather than learning elaborate interfaces to access functionality, users prefer tools that understand intent and execute directly. The interface becomes conversational rather than navigational.

The economic implications extend beyond individual tool selection. Developer education markets shrink when AI handles skill transfer directly. Visual design markets compress when AI generates interfaces from natural language descriptions. Complex workflow tools lose users to AI systems that automate the entire workflow rather than facilitating human execution.

for builders building AI products, this suggests prioritizing functional depth over interface sophistication. Users want AI that solves their problems completely, not AI that helps them solve problems faster through better interfaces. The successful pattern is: natural language input, autonomous execution, direct output delivery.

The CLI advantage over visual interfaces reflects this preference for directness over discoverability. Command-line interactions optimize for power users who know what they want to accomplish. Visual interfaces optimize for exploration and learning. When AI handles the cognitive load of figuring out what to accomplish, directness wins over exploration.

---

### What to do this week

**Test autonomous model selection in your AI workflows** (30 minutes): If you're using Claude Code, Cursor, or similar agentic tools, try Simon Willison's approach. Instead of specifying compute levels, tell your AI system to use its judgment for model selection on different task types. Monitor token costs and output quality over a week of usage. Document which tasks benefit from autonomous routing versus fixed model selection.

**Experiment with iterative creative refinement** (1 hour): Pick a creative or technical project where you'd normally specify detailed requirements. Instead, give the AI a basic goal and repeatedly ask it to "make this better" or "make this more [quality]" without specifying how. Track how the system's autonomous creative decisions compare to your initial specifications. This works for code refactoring, content creation, or UI design.

**Audit your AI usage patterns for complexity gaps** (45 minutes): Review your last month of AI tool usage. Categorize interactions as basic (search replacement, simple Q&A) versus ambitious (multi-step reasoning, creative projects, complex problem-solving). If more than 70% falls into the basic category, identify one complex project you could tackle using iterative AI collaboration rather than traditional manual approaches.
