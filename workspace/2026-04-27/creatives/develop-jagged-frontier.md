# Develop — jagged-frontier

5 conceptually distinct options. Each tests a different visual mechanic against the post.

| # | Name | Concept (one line) | Why it pairs with the post | Risk to flag |
|---|---|---|---|---|
| 1 | **Capability Chart** | Hand-drawn jagged line chart with two specific tasks labeled — "complex algorithms" sitting on a peak, "counting characters" sitting in a valley, single brick-red dot on the valley. | The post NAMES these two exact tasks. The chart shows them. Artifact-as-argument: the chart IS the proof. | If the line is too clean it reads as McKinsey infographic. Imperfection has to land. |
| 2 | **The Gap** | Typography-only contrast. Top half: "PEAKS" in huge ink. Bottom half: "VALLEYS" in brick-red, kerned wider. A hairline rule between them is itself jagged (zigzag). | Strips the metaphor to its core: one word per zone, one ragged seam. Maximum negative space, maximum confidence. | Risks reading as "motivational poster" if the zigzag isn't sharp. Type weight has to do all the work. |
| 3 | **Automation Invoice** | Direct callback to the GPT-5.5 receipt. A line-itemized "Automation Estimate" receipt. "AUTOMATION 80%" with a strikethrough, "HANDOFF 20%" stamped in brick-red. | Already a proven aesthetic for Aayush; the post is literally about an "80% pitch" being wrong. Receipt format mocks the founder's pitch deck. | Risks looking too similar to the 04-24 receipt and feeling like a re-run. Different content, same vessel. |
| 4 | **Topographic Map** | Contour lines forming peaks and valleys. One peak labeled "code" in tiny mono caps, one valley labeled "count chars". Brick-red elevation marker on the valley. | Topography literalizes "frontier" — a terrain you map, not conquer. Adds depth without illustration. | Contour lines can read as decorative noise if not tight enough. Risks crossing into "infographic" territory. |
| 5 | **Stack Diff** | Two narrow column blocks side by side. Left: "WHAT THEY SOLD: 80% AI". Right: "WHAT SHIPPED: handoff at 20%". The 80% is grayed out and struck through; the handoff line is brick-red. | Mirrors the post's "naive pitch vs reality" structure with a builder's diff aesthetic. | Heavy on text, harder to keep under 12 words. Risks getting talky. |

## Selection for render

Picking **#1 Capability Chart**, **#2 The Gap**, and **#3 Automation Invoice** for HTML + PNG render.

Reasoning:
- #1 directly executes the strongest conviction bet (the chart IS the post).
- #2 is the most distinct register from #1 (zero illustration, pure type).
- #3 is the proven receipt callback and gives Aayush a known-working option as a safety net.

#4 (topo) and #5 (stack diff) documented but not rendered — they share too much DNA with #1 and #2 respectively, and the spec asks for 3 strongest options.
