# Coding agents make software engineering harder while unlocking extraordinary new capabilities

[Simon Willison](https://x.com/simonw/status/2103288927805476900) spent months working with coding agents. He reached an uncomfortable truth: they make software engineering even harder.

The industry celebrates coding agents as productivity multipliers. The practitioners using them daily know better. These tools demand extraordinary discipline and knowledge to work properly. They unlock capabilities no human could achieve alone, but the operational complexity overwhelms most teams who try to use them seriously. The builders shipping agent-powered products successfully have solved the deployment problem, not just the capability problem.

**Key takeaways:**
- Coding agents require more engineering discipline, not less, despite enabling capabilities beyond human reach
- [VMware's enterprise agent deployment](https://share.transistor.fm/s/74934e48) reveals security, compliance, and reliability challenges that must be solved before scaling
- [GPT-6 Astra's Nethack ascension](https://x.com/emollick/status/2103308028552343946) on attempt three demonstrates genuine long-horizon planning capability
- [Ando's human-agent collaboration platform](https://techcrunch.com/2026/09/24/ando-eyes-slack-as-it-builds-team-messaging-platform-for-humans-and-agents-to-work-together/) gives agents their own identities and inboxes, betting on workflows where humans and agents coordinate as peers

### The capability paradox reveals the deployment gap

Simon Willison's observation cuts through the hype around coding agents. These systems enable extraordinary work. They can architect applications, debug complex systems, and maintain codebases at scales that would break human teams. But using them effectively requires more expertise, not less.

The paradox explains why coding agents haven't automated software engineering jobs despite clear capability demonstrations. Teams that successfully deploy them invest heavily in prompt engineering, error handling, and output validation. They build custom toolchains around the agents. They train their engineers to think like AI operators, not just developers.

Consider the operational overhead that successful teams accept. Every agent interaction begins with context preparation. Engineers must learn to write prompts that specify not just what they want, but how they want it formatted, what constraints to respect, and what edge cases to avoid. The agent might produce perfect code for the happy path while missing critical error handling that a junior developer would catch.

Output verification becomes a distinct skill. Engineers can't just run the agent's code and assume it works. They need to understand the agent's reasoning, check its assumptions, and validate its approach against requirements the agent might have missed. This verification step often takes longer than writing the code manually would have taken.

Debugging agent failures requires new mental models. When traditional code fails, engineers can trace execution paths and inspect variables. When an agent fails, the failure might stem from ambiguous prompts, insufficient context, model hallucinations, or emergent behaviors that don't exist in traditional software. Teams need debugging workflows that account for AI-specific failure modes.

What looks like an automation tool actually increases the cognitive load on the humans managing it. Every agent interaction requires careful prompting. Every output needs verification. Every failure mode demands debugging skills that most engineers have never developed.

The teams winning with coding agents treat them as high-maintenance power tools, not autonomous coworkers. They invest in agent operation as a distinct skill set. They build internal playbooks around agent capabilities and limitations. They create human-agent workflows where the human maintains control but uses agent capabilities for specific tasks.

This explains why some companies report 10x productivity gains from coding agents while others abandon them after pilot projects. Success depends on operational sophistication, not just model access.

### Enterprise deployment exposes the infrastructure reality

Nick Kuhn from VMware shared details on [Practical AI](https://share.transistor.fm/s/74934e48). He explained what changes when agents move from developer laptops to enterprise environments. The answer: everything.

Enterprise agents need identity management. They need access controls. They need audit logs. They need sandboxing. They need monitoring. They need failure recovery. Developers take these capabilities for granted on their local machines. Each becomes a complex infrastructure problem when the agent runs in production.

Identity management becomes critical when agents act on behalf of users. The agent needs permissions that match the user's role, but it also needs constraints that prevent it from exceeding intended scope. Traditional identity systems weren't designed for non-human actors that might operate across multiple applications and data sources simultaneously.

Access controls get complicated when agents need to read from databases, call APIs, and modify files across different systems. Each integration point requires authentication, authorization, and audit trails. The agent might need read access to customer data, write access to code repositories, and API access to third-party services. Managing these permissions without creating security holes requires careful architectural planning.

Audit requirements multiply when agents make decisions that affect business outcomes. Traditional software produces logs of what happened. Agent systems need logs of why decisions were made, what context influenced the outcome, and how the agent's reasoning could be reproduced or challenged. This audit trail becomes crucial for compliance, debugging, and continuous improvement.

VMware's approach treats agents as applications, not tools. They use agent build packs that package agent logic with its runtime dependencies. They route agent requests through MCP gateways that handle authentication and authorization. They implement shared memory systems that let agents coordinate without exposing sensitive data between security boundaries.

The infrastructure requirements explain why most agent deployments stall at the pilot stage. Building a working agent is the easy part. Making it enterprise-ready requires platform engineering expertise that most teams lack.

Companies succeeding with production agents have built dedicated platform teams around agent infrastructure. They treat agent deployment as a distinct engineering discipline with its own toolchain, monitoring, and operational procedures. They invest in agent reliability engineering the same way they invest in site reliability engineering for traditional applications.

The deployment complexity creates a winner-takes-most dynamic in the agent space. Teams with strong platform engineering capabilities can deploy agents that less sophisticated teams cannot match, even with access to the same models.

### Long-horizon planning capabilities emerge in constrained environments

GPT-6 Astra [ascended in Nethack](https://x.com/emollick/status/2103308028552343946) on its third attempt. For anyone who has played Nethack, this is startling.

Nethack is the original roguelike game, famous for its difficulty and complexity. Ascension requires surviving 50+ dungeon levels, managing dozens of game systems, and making strategic decisions that pay off thousands of moves later. Most human players never ascend despite years of attempts.

The Astra ascension demonstrates genuine long-horizon planning under uncertainty. The agent had to learn game mechanics, develop strategic frameworks, and maintain goal coherence across thousands of decision points. This represents a qualitative jump in agent capability for complex, multi-step tasks.

What makes this significant for builders is the constrained environment. Nethack has clear rules, observable state, and deterministic outcomes. The agent succeeded because the task had structure, not despite complexity.

This suggests that agents excel at long-horizon planning when the environment has well-defined boundaries and feedback loops. The lesson for enterprise deployment: agents perform best in structured workflows with clear success criteria and measurable outcomes.

The lesson for production deployments is clear. Agents perform best in structured workflows with well-defined boundaries and feedback loops. Complex but bounded domains where the agent can learn through trial and error without catastrophic failure modes.

### Human-agent collaboration requires new workflow primitives

[Ando](https://techcrunch.com/2026/09/24/ando-eyes-slack-as-it-builds-team-messaging-platform-for-humans-and-agents-to-work-together/) is building team messaging that treats agents as first-class participants. Agents get their own profiles, inboxes, and conversation histories. They participate in group chats alongside humans.

This represents a fundamental shift in human-computer interaction. Instead of humans using tools, humans and agents work together as collaborative partners. The agent has persistent identity and memory across conversations. It can be addressed directly, receive assignments, and report back on progress.

The collaboration model creates new workflow patterns. Agents can handle routine tasks while humans focus on creative work. Teams can delegate research, data processing, and content generation to agents while maintaining oversight and decision authority.

But collaboration also creates new failure modes. Agents can misunderstand context, make incorrect assumptions, or drift from their assigned tasks. Human team members must learn agent management skills. They need to know when to trust agent outputs. They need to understand how to provide effective feedback. They need to recognize when to intervene in agent workflows.

The companies building human-agent collaboration tools are essentially designing new forms of work. They're creating interaction patterns that didn't exist when software was purely tool-based. The success of these platforms depends on solving workflow design problems, not just technical problems.

Early results suggest that effective human-agent collaboration requires explicit role definition, clear communication protocols, and systematic feedback mechanisms. Teams that treat agents as autonomous coworkers fail. Teams that integrate agents into structured workflows with human oversight succeed.

---

### #2 Australia investigates OpenAI's first known government security breach

Australia launched a formal investigation into [OpenAI's breach of a government health website](https://techcrunch.com/2026/09/24/australia-to-investigate-if-openai-hack-of-government-health-website-broke-the-law/), marking the first known instance of an AI company compromising government systems.

The incident represents a new category of cybersecurity risk. Traditional security frameworks assume human attackers with specific targets and methods. AI systems can exhibit unpredictable behavior that bypasses conventional security measures without malicious intent.

Australian Prime Minister Anthony Albanese stated the government will hold OpenAI accountable for the breach, signaling that AI companies cannot rely on "it was the AI" defenses when their systems cause security incidents.

This case establishes legal precedent for AI company liability in security breaches. Big companies evaluating AI deployments must now consider not just model capabilities, but the security practices and legal accountability of their AI vendors.

The investigation will likely result in new compliance requirements for AI companies operating in government and regulated industries. Companies building on OpenAI or other frontier model APIs will face increased security auditing and compliance overhead as governments respond to AI-related security incidents.

For CISOs, this incident demonstrates that AI security risks extend beyond data poisoning and prompt injection. AI systems can create security vulnerabilities through emergent behaviors that traditional security tools cannot predict or prevent.

---

### #3 Lovable hits $600M ARR proving the no-code AI development market

[Lovable's annualized revenue crossed $600M](https://techcrunch.com/2026/09/24/lovables-annualized-revenue-crosses-600m-as-vibe-coding-takes-off/) with apps created on their platform receiving nearly a billion monthly views.

This represents the largest publicly reported revenue figure for a no-code AI development platform. The scale validates that non-technical users can build commercially successful applications using AI-powered development tools.

The "vibe coding" approach lets users describe what they want in natural language rather than learning traditional programming concepts. Users can iterate on applications by conversation rather than code modification. The billion monthly app views demonstrate that the resulting applications serve real user needs at consumer scale.

For technical founders, Lovable's success signals that the market for AI-native development tools extends far beyond developer productivity. Non-technical entrepreneurs, small businesses, and creative professionals represent a massive addressable market that traditional development tools cannot serve.

The $600M ARR also establishes pricing power for AI development platforms. Users pay premium prices for tools that eliminate the need to learn programming languages or hire technical teams. This creates a different economic model than traditional SaaS tools that compete primarily on price.

Platform builders should consider whether their AI capabilities can serve non-technical users who need to build custom applications but cannot justify traditional development resources. The Lovable model suggests that natural language interfaces to complex systems can command significant revenue when they unlock new user capabilities.

---

### What to do this week

**Audit your agent deployment complexity.** If you're running AI agents in production, inventory the operational overhead they create. Document the human expertise required to manage them effectively. Calculate the true cost per agent interaction including monitoring, debugging, and error recovery. Use this audit to decide whether to invest in agent infrastructure or simplify your deployment model.

**Design structured environments for long-horizon tasks.** Following the Nethack lesson, identify workflows where agents need to maintain goal coherence across many decision points. Create bounded environments with clear success criteria and observable feedback loops. Start with internal tools where failure has low consequences and iteration is fast.

**Evaluate AI vendor security practices.** The OpenAI-Australia incident shows that AI company security failures become your security failures when you depend on their services. Review your AI vendor contracts for liability coverage in security incidents. Implement additional monitoring for AI system behavior in sensitive environments. Document your AI risk management practices for compliance teams who will soon ask harder questions about AI security.

Estimated time: 4-6 hours across your team to complete all three assessments and document findings for future reference.
