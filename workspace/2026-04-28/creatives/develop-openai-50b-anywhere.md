# Develop — openai-50b-anywhere

5 conceptually distinct options. Each tests a different visual mechanic against the post.

| # | Name | Concept (one line) | Why it pairs with the post | Risk to flag |
|---|---|---|---|---|
| 1 | **Wall Breach** | Hand-drawn brick wall in ink. One section is knocked out. The breach-shaped opening is brick-red. A small annotation reads "azure" on the bricks; a label on the gap reads "anywhere". | The post's central image is "this week that wall came down." This option literally shows it. Artifact = argument. | If the bricks read as decorative or cute, the conviction collapses. The torn edge has to feel violent, not playful. |
| 2 | **Price Tag** | A single oversized price tag dangling on a string. Front of the tag: "$50B". Underneath in small caps: "to not be exclusive." A brick-red TORN diagonal across one corner. | Pure negative-space play. The tag is the receipt's cousin — physical artifact metaphor. The number does the scroll-stop work. | Risks looking like a Black Friday graphic if the tag is too clean. Hand-drawn imperfection has to dominate. |
| 3 | **Procurement Contract** | A redacted procurement document. Body lines mostly faded ink. The line "Cloud provider: ___ EXCLUSIVELY" is struck through in brick-red and replaced with "anywhere" in the margin. A faint "INITIALED" stamp at the bottom corner. | Mirrors the receipt aesthetic that Aayush already validated (GPT-5.5, Automation Invoice). The doc IS the procurement conversation the post is about. | Risks looking too similar to the receipts. Mitigation: legal-document layout, not retail receipt — denser text body, redaction style. |
| 4 | **One Answer** | Pure typography. Top: "ONE ANSWER PER CLOUD" struck through in ink. Below: "ONE ANSWER" in 200px brick-red. Below that, tiny: "period." | The post's most quotable line ("Now it has one answer, period.") rendered as a single composition. Strips the metaphor to its quotable spine. | Risks feeling like a motivational poster if the strike-through isn't sharp. Type weight does all the work. |
| 5 | **Cloud Diff** | Two stacked stack-diagram blocks — like a git diff. Top block: `- exclusive: azure` (struck, faded). Bottom block: `+ anywhere: aws · gcp · azure` (brick-red plus sign and accent line). A `// $10B/year to flip this line` comment in monospace at the right margin. | The diff format is native to the builder audience the post is written for. The minus-to-plus encoding mirrors the post's "lock-in unlocked" beat. | Heavier text load — has to stay under 14 words while still reading as a real diff. The comment has to feel like code, not copy. |

## Selection for render

All five rendered to HTML + PNG per skill spec (5 distinct mechanics, not 3).

- **#1 Wall Breach** — the post's literal central metaphor as artifact
- **#2 Price Tag** — physical-object metaphor + the $50B number doing the heavy lifting
- **#3 Procurement Contract** — receipt-aesthetic callback, denser document register
- **#4 One Answer** — pure typography, maximum negative space, post's quotable line
- **#5 Cloud Diff** — git-diff format native to the builder audience

Mechanics covered: artifact-illustration (#1), price-tag stat-focus (#2), document/receipt (#3), pure typography (#4), code-diff comparison (#5). No two share a mechanic.
