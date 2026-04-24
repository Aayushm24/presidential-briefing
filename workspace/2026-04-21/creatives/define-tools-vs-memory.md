# Define — tools-vs-memory

## Source post

Everyone has Claude Code. Almost no one is using it right.

I see it across my network, teams shipping with identical tools, but getting wildly different outcomes.

The difference lies in what happens when your Claude conversation ends.

Intercom's Brian Scanlan did something very interesting.

He built telemetry that logs every Claude Code interaction.

Patterns analyzed. Skills saved to a shared repository. Engineers, designers, and PMs in the same system.

9 months later: 2x velocity. Zero regression.

The tools were identical (using claude code is not a moat 🤷🏻‍♂️). The infrastructure was completely different.

There are only two AI engineering orgs now:
- Teams with tools
- Teams with tools + institutional memory

Teams with tools start fresh every sprint.
Teams with memory compound every sprint.

That's the gap.

OpenAI acquired Skybysoftware this week for state persistence: agents that remember your environment, preferences, and deployment history across sessions.

Same bet. Same week. Different companies.

The real food for thought is whether anything your team learns from survives their current session.

I doubt most teams have asked that question yet.

The ones who have are already 9 months ahead.

What does your team remember from last sprint's Claude Code usage?

p.s. the detail that hit this home — at Intercom, designers and PMs now merge PRs through Claude Code. The telemetry changed who could ship.

p.p.s. at Atlan we've been building this layer for a while. happy to compare notes with anyone doing the same. 👇🏻

---

## Position statement

Make a founder feel the quiet dread of a compounding gap — their team resets every sprint while a competitor quietly builds 9 months of advantage — and want to screenshot this and put it in their team Slack.

## 3 conviction bets (specific, falsifiable)

1. **The binary split beats the stat** — "Teams with tools / Teams with tools + memory" rendered as a literal two-column contrast will create more scroll-stop than leading with the "2x velocity" number, because the binary forces the viewer to self-identify (which side am I on?) before they even read a word. A stat is information. A mirror is a verdict.

2. **"9 months ahead" is the right hero text, not "2x velocity"** — "2x velocity" is a metric any startup claims. "9 months ahead" is a time gap with a named source (Intercom / Brian Scanlan) attached to it. Time gaps feel real and personal in a way percentages don't. The hero number should be the gap, not the outcome.

3. **The visual split must feel unequal, not symmetric** — if both columns look the same size and weight, the creative implies the two states are equal choices. The "memory" side should visually dominate (heavier ink, accent treatment) to communicate that this isn't a preference — it's an asymmetric advantage. A 50/50 split would lie about the stakes.

## Kill list (at least 5 explicit "will NOT do" items)

1. Will NOT use "2x velocity" as the hero — it reads like a vendor claim; the 9-month time gap is the emotional hit
2. Will NOT use neural-net swoosh decorations or "AI" circuit-board motifs as background texture
3. Will NOT place both sides of the contrast in identical typography weight — the memory side must visually outweigh tools-only
4. Will NOT write "institutional memory" anywhere on the creative — that's MBA vocabulary; write "what your team remembers"
5. Will NOT use a gradient background — reads as 2015 SaaS startup
6. Will NOT include Aayush's headshot or photo — the claim stands alone
7. Will NOT put a checklist or bullet icons as decorative elements — this is not a "top 5 tips" post
8. Will NOT show any logo or icon for Claude Code, OpenAI, or Intercom — the copy is doing that work; icons become noise at 400px thumbnail
9. Will NOT center-align the hero — F-pattern scan requires top-left anchor to read as editorial, not decorative

## Success criteria

- **3-second test:** Viewer gets two things without reading body copy: (1) there are two kinds of teams, (2) one is 9 months ahead. Those two facts must be visible at the hero level within 3 seconds.
- **Thumbnail test:** At 400px width, the binary split labels ("tools only" vs "tools + memory") and the "9 months ahead" element must still be readable. The hierarchy cannot collapse to unreadable chips at small size.
- **Logo-swap test:** If you replaced "aayush-maheshwari" with a random handle, what would feel wrong is the specificity — "Brian Scanlan", "Intercom", "9 months", "Skybysoftware" — and the hedge voice ("I doubt most teams have asked"). Generic thought leadership posts don't name the person, the company, the quarter, and the acquisition in the same frame. The conviction in the specifics is what marks this as Aayush's.

## Design constraints

- **Color palette:** Violet thesis (`--hero: #6d28d9`, `--accent: #f472b6`, `--surface: #fafaf9`, `--card: #ffffff`, `--ink: #0a0a0a`). Rationale: this post is a philosophical reframe — "the difference lies in what happens when your Claude conversation ends" is a thesis, not a metric or an alarm. Violet signals a stand being taken. The post also ends with a question, not a verdict, which matches the violet mood's "takes a stand, premium, creator" register. Emerald (growth) would imply the answer is obvious and positive. Coral (urgency) would imply panic. Violet holds the right tension.
- **Typography:** Inter only. Hero text at 140-180px, weight 800-900. Binary labels at 48-56px, weight 700. Body quote or attribution at 20-22px, weight 400-500.
- **Mandatory elements:** The binary pair ("tools only" / "tools + memory"), the "9 months ahead" as hero text or near-hero callout, Aayush handle in footer (LinkedIn icon + aayush-maheshwari + 2026-04-21).
- **Forbidden elements:** Gradients, neural/circuit decorations, emoji as design elements, stock illustrations, Aayush's photo, logos of any named company, drop shadows (except 1 hero card, ultra-subtle), centered layout, text below 14px.
- **Dimensions:** 1200×1200. This is a thesis/contrast post — not a confession story that earns the 1200×1500 portrait. Square keeps the two-column contrast readable and symmetric on desktop feed.
