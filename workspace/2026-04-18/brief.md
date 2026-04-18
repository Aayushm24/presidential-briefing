# AI is spawning new platform layers, and the smart money is building infrastructure, not apps

The App Store just had its best quarter for new AI-native apps since the iPhone launch era. Meanwhile, Sam Altman's World is selling human verification to Tinder.

These two stories look unrelated. They're not. As AI floods every surface with generated content, generated identities, and generated interactions, the businesses that win won't be the ones generating. They'll be the ones providing the trust and distribution layers that sit underneath. We're watching two new platform categories form in real time: proof-of-humanity infrastructure and AI-native mobile distribution. Builders who recognize these as platform opportunities, not features, have a narrow window to build on top of them.

**Key takeaways:**
- App Store downloads of AI-native apps surged in Q1 2026, driven by a new wave of mobile-first AI products, not just ChatGPT wrappers
- World (formerly Worldcoin) signed Tinder as its first major B2B customer for iris-based human verification, signaling a real product category around identity
- Both stories point to the same root cause: AI-generated content and identities are creating demand for new infrastructure that didn't need to exist two years ago
- The winners in this cycle won't be model companies. They'll be the trust layers and distribution rails that other products build on
- Small teams can build on these emerging platforms right now, before incumbents lock them down

### The App Store is having a second boom

Apple's App Store saw a significant spike in new AI-native app submissions and downloads in Q1 2026, according to TechCrunch's reporting. This isn't the 2023 wave of thin ChatGPT wrappers. These are mobile-first products that use on-device models, multimodal input, and agent-style workflows designed specifically for phones.

The pattern matters more than any single app. **Mobile AI is becoming its own distribution channel**, not a desktop experience crammed into a smaller screen. Apps that use the camera, microphone, location, and notification stack as native inputs for AI are finding product-market fit in ways that browser-based tools can't replicate.

Think about what this means for builders. The App Store's 30% cut has always been painful, but it comes with something browser apps don't have: a built-in trust and payment layer that 1.5 billion people already use. When your product is an AI agent that acts on behalf of the user, that trust layer matters enormously. People will let an app access their camera. They won't give that same permission to a random website.

This is a distribution opportunity that favors small teams. A three-person team with Claude Code and a good product instinct can ship a polished AI-native iOS app in weeks. The coordination cost of building mobile used to require dedicated iOS engineers, backend teams, QA cycles. That's collapsing. The YC W26 batch is full of two and three person teams shipping mobile AI products that would have required 15 people in 2023.

### World's pivot from crypto curiosity to B2B identity platform

World, the Sam Altman-backed project formerly known as Worldcoin, just signed Tinder as its first major B2B integration partner. The deal lets Tinder users verify they're human through World's iris-scanning Orb hardware, with the verification credential living on World's network.

> World is positioning its iris-based identity verification as infrastructure that any app can plug into, starting with the platforms most damaged by AI-generated fake profiles.

This is a sharp strategic move. **Tinder is the perfect first customer** because dating apps have the most acute fake-profile problem and the highest user motivation to verify. If you're swiping on someone, you want to know they're real. That willingness to verify creates pull that World couldn't generate by just asking people to scan their eyeballs for crypto tokens.

The bigger signal is that human verification is becoming a standalone product category. Two years ago, "prove you're human" meant CAPTCHAs. Now it means biometric identity infrastructure sold as a B2B API. World is betting that as AI-generated text, images, voice, and video become indistinguishable from human-created content, every platform will need a verification layer. Dating apps are first. Social networks, marketplaces, and financial services are next.

The skeptics have fair points. Iris scanning raises real privacy concerns. World's crypto token economics remain confusing. The Orb hardware is expensive to deploy. But strip away the crypto wrapper and what you see is a company building the identity layer for an AI-saturated internet. That's a real business regardless of what happens to the token.

### The pattern underneath both stories

Here's what connects a booming App Store and an eyeball-scanning identity company: **AI is creating demand for infrastructure that didn't need to exist before**.

When AI can generate a convincing dating profile, you need a verification layer. When AI can build a functional app in an afternoon, you need a distribution and trust layer that helps users find the good ones. Both are platform-level problems, not feature-level problems.

> The businesses that win in AI won't be the ones generating content. They'll be the ones providing the trust and distribution layers underneath.

This is the classic platform playbook. In the early internet, the winners weren't the websites. They were the search engines, payment processors, and hosting providers. In mobile, the winners weren't the apps. They were the app stores, push notification networks, and analytics platforms. We're watching the same dynamic play out with AI, and the platform layer is still wide open.

What makes this moment unusual is how accessible these opportunities are. You don't need a 50-person team to build an AI-native mobile app that leverages the App Store's distribution. You don't need to build your own identity system when World is opening up B2B APIs. The infrastructure is forming right now, and the teams that build on it first, while it's still early and the APIs are still flexible, will have the same structural advantage that early Stripe or early Shopify developers had. Small teams that move fast on new platforms beat large teams that deliberate. That's not a platitude. It's the math of 2026.

---

### #2 Anthropic warms up to the Trump administration

Anthropic's relationship with the current White House appears to be thawing, per TechCrunch reporting. After months of tension rooted in Anthropic's vocal support for AI safety regulation, the company has been making quieter, more pragmatic moves to align with the administration's deregulatory stance.

This matters for one reason: **enterprise procurement**. Government contracts and government-adjacent enterprise deals increasingly flow through political channels. Companies that are perceived as adversarial to the administration face real friction in federal sales cycles, defense partnerships, and regulated industry deployments.

Anthropic's shift isn't ideological. It's commercial. Claude is competing with GPT and Gemini for the same enterprise budgets, and being locked out of government-adjacent deals is a competitive disadvantage they can't afford. Dario Amodei has been meeting with administration officials and reportedly softening Anthropic's public messaging around mandatory regulation.

For builders, the practical implication is simple. If you're building on Claude for enterprise customers in regulated industries, Anthropic's political positioning reduces one source of procurement risk. If you're choosing between model providers for a government-adjacent product, this is a factor worth tracking. The model quality differences between Claude, GPT, and Gemini are narrowing. The business and compliance differences are widening.

---

### #3 OpenClaw and the messy reality of open-source AI agents

Latent Space covered the emerging debate around OpenClaw, the open-source agent framework that's been gaining traction among developers building autonomous coding agents. The discussion highlights a genuine tension: OpenClaw makes it trivially easy to spin up agents that write and execute code, but the guardrails are minimal and the failure modes are poorly understood.

This is the "two sides" problem with every open-source AI tool. The same low barrier that lets a solo founder build a powerful coding agent also lets someone deploy an agent that runs arbitrary code with no sandboxing, no audit trail, and no kill switch.

The practical takeaway for builders: if you're using OpenClaw or similar open-source agent frameworks, **invest in your own guardrails before you invest in capabilities**. The framework gives you the execution layer for free. The memory architecture, the permission system, the state management across sessions, that's still your problem to solve. And it's the part that determines whether your agent is a product or a liability.

---

### What to do this week

**1. Audit your product for AI-native mobile potential (2 hours).** If you have a web-based AI product, spend two hours sketching what it would look like as a mobile-first experience that uses camera, mic, or location as primary inputs. The App Store boom is rewarding products designed for phones, not ports. Use Claude Code to prototype a basic SwiftUI interface if you want to test the idea fast.

**2. Check World's developer docs for B2B verification APIs.** If you're building any product where user identity matters, such as marketplaces, social platforms, fintech, or hiring tools, look at [World's developer documentation](https://world.org) to understand what verification credentials you could integrate. The API is early, which means early integrators get the most support and flexibility.

**3. If you're using open-source agent frameworks, add a session memory layer this week.** Pick one agent workflow you run regularly. Add persistent memory using something as simple as a local JSON store or a lightweight vector DB like ChromaDB. Track what the agent did, what worked, what failed, across sessions. This is the difference between a demo and a product, and it takes an afternoon to set up with Claude Code.

---

## Sources

1. The App Store is booming again, and AI may be why, TechCrunch/Latent Space, 2026-04-18. https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/
2. Sam Altman's project World looks to scale its human verification empire. First stop: Tinder., TechCrunch/Latent Space, 2026-04-18. https://techcrunch.com/2026/04/17/sam-altmans-project-world-looks-to-scale-its-human-verification-empire-first-stop-tinder/
3. Anthropic's relationship with the Trump administration seems to be thawing, TechCrunch/Latent Space, 2026-04-18. https://techcrunch.com/2026/04/18/anthropics-relationship-with-the-trump-administration-seems-to-be-thawing/
4. [AINews] The Two Sides of OpenClaw, TechCrunch/Latent Space, 2026-04-18. https://www.latent.space/p/ainews-the-two-sides-of-openclaw
5. Adding a new content type to my blog-to-newsletter tool, TechCrunch/Latent Space, 2026-04-18. https://simonwillison.net/guides/agentic-engineering-patterns/adding-a-new-content-type/#atom-everything
6. My Workflow for Understanding LLM Architectures, TechCrunch/Latent Space, 2026-04-18. https://magazine.sebastianraschka.com/p/workflow-for-understanding-llms
7. Join us at PyCon US 2026 in Long Beach - we have new AI and security tracks this year, TechCrunch/Latent Space, 2026-04-18. https://simonwillison.net/2026/Apr/17/pycon-us-2026/#atom-everything
