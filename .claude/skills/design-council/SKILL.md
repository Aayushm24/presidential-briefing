# design-council — Conviction-first visual creative production

Manual skill. You paste a LinkedIn post (or point at a file). The skill runs a lite version of the Double Diamond (Define → Develop → Deliver), pausing for human review between phases, and produces 5 conceptually distinct creative options rendered to PNG.

This skill is adapted from Atlan's Marketing OS design-council (`atlanhq/atlan-marketing-team@staging:skills/design-council`). Core ideas ported:
- **Conviction Workshop before pixels.** Position + 3 bets + kill list + success criteria.
- **5 distinct options, not 1.** Named directions testing different mechanics.
- **7-dimension design review.** Hierarchy, Contrast, Flow, Layout, Clear Space, CTA, Scroll-Stop.
- **Human-paced pauses.** Never auto-advance. Human can kill, combine, redirect, restart.
- **Quality tests.** Logo-swap, 3-second, thumbnail.
- **Color theory.** Structured 5-color palettes (moods), 60-30-10 rule. See `references/color-theory.md`.
- **Plain-English copy.** Every word on the creative reads at 5th-grade level. No MBA vocabulary. See `.claude/skills/write-briefing/references/plain-english-rules.md`.

## Before writing ANY copy — mandatory reads

1. `config/post-blueprint.md` — **PRIMARY voice source.** If the creative is for a LinkedIn post, every chip, headline, body line, and footer follows this blueprint. Latest-of-latest voice direction lives here. Allowed vocabulary (moat, IMO, I doubt) and banned patterns (It's like X, [Not X it's Y]) are defined here.
2. `config/brief-blueprint.md` — if the creative accompanies a brief, use this instead.
3. `history/feedback-log.jsonl` — recent feedback entries.
4. `.claude/skills/design-council/references/color-theory.md` — pick mood based on post archetype.
5. `.claude/skills/write-briefing/references/plain-english-rules.md` — secondary (now subordinate to blueprints).

The copy on the creative is held to the SAME plain-English bar as the brief and the LinkedIn posts. A creative with "commoditization" on it is REVISE, no matter how pretty it looks.

Skipped (relative to Atlan's): full Discover phase, state management JSON, Figma handoff, Imagen production generation. The personal LinkedIn use case is one-shot, fast, doesn't need designer handoff.

---

## Invocation

```
/design-council <post-text-or-file-path>
```

If arg is a path (ends in `.md` / `.json` / `.txt`), read it. Otherwise treat as the post text. If it's `posts.json`, ask which option.

---

## Phase 1: Define (Conviction Workshop) — REQUIRED, NON-SKIPPABLE

**Why this exists:** most creative processes skip straight to "make something pretty" and produce generic output. Locking the conviction first is the difference between "another LinkedIn graphic" and a scroll-stopper. If the human rejects the conviction, we've saved the cost of building 5 wrong options.

### What to produce

Write to `creatives/YYYY-MM-DD/define-<slug>.md`:

```markdown
# Define — <slug>

## Source post
<the full post text verbatim>

## Position statement
One sentence. What should this creative make the viewer **feel** and **do**?
NOT "show the message." Accomplish something specific.

Example: "Make a founder feel that their AI infrastructure bet is risky, and
want to forward this post to their CTO."

## 3 conviction bets (specific, falsifiable)

Each bet is a testable belief. If it's generic ("clean and modern"), it's nothing.
Write bets you could be proved wrong about.

1. **<Named bet>** — <specific claim about what will/won't work visually and why>
2. **<Named bet>** — <specific claim>
3. **<Named bet>** — <specific claim>

Examples of good bets:
- "A 240px hero number will create more scroll-stop than any headline treatment
  because stats are the highest-trust visual element on LinkedIn"
- "The indigo-accent-only rule will outperform multi-color because single-accent
  reads as confident; multi-color reads as template-made"
- "Leaving 60% negative space below the hero will beat filling with supporting
  text because it forces the eye to the one thing that matters"

## Kill list (at least 5 explicit "will NOT do" items)

Each item prevents a specific failure mode. Be concrete.

1. Will NOT use gradients on backgrounds (reads as 2015 startup)
2. Will NOT use emoji as design elements (decoration, not meaning)
3. Will NOT center-align the hero (F-pattern scan requires top-left anchor)
4. Will NOT use stock illustrations (immediately marks content as AI-generic)
5. Will NOT include Aayush's photo (the claim should stand without the person)

## Success criteria (how we know if it works)

Three tests. Every option must pass all three in Deliver phase.

- **3-second test:** <what the viewer must get in 3 seconds — name the 2-3 facts>
- **Thumbnail test:** <what must still be readable when the image is 400px wide>
- **Logo-swap test:** if you replaced "@aayush-maheshwari" with a random handle,
  <what specifically would feel wrong — the voice, the conviction, the angle>

## Design constraints

- **Color palette:** ONE accent from {indigo / violet / emerald / coral / slate}. State your pick and why.
- **Typography:** Inter only. Hero weight 800-900, body 400-500.
- **Mandatory elements:** <list — e.g., "the $10B number", "Aayush handle", nothing else>
- **Forbidden elements:** <list — anything from kill list plus post-specific no-gos>
- **Dimensions:** 1200×1200 default. 1200×1500 for story/confession posts. Justify if different.
```

### Phase 1 pause

After writing `define-<slug>.md`, **STOP**. Show the file to the user. Say:

> "Define phase done. Here's the conviction brief. Review the position statement, bets, and kill list. Reply 'approved' to continue to Develop, or point at what to change."

Do not proceed until the human approves. If they push back, iterate on define.md only. The 5 options haven't been built yet — no wasted work.

---

## Phase 2: Develop (5 distinct options)

**Why 5:** one option is fragile. Three is what most people do. Five forces real exploration across different visual mechanics.

### Rules

1. Each option must be **conceptually distinct**, not a variation. Different:
   - Visual mechanic (stat-focus vs quote-focus vs contrast)
   - Hierarchy strategy (where the eye lands first)
   - Entry point (top-left vs center vs bottom-up)
2. Each option gets a **2-word name** that captures its mechanic: "Quiet Tension", "The Split", "Card Stack", "Bold Claim", "Single Number".
3. Each option must satisfy the position statement, respect the kill list, and test ≥ 1 conviction bet explicitly.
4. Use one of the 5 archetypes below OR invent one, as long as it follows the design system.

### Archetype menu (pick 5, can include variations)

| Archetype | Mechanic | Best for |
|---|---|---|
| **Big-Number Card** | Massive stat + short claim | Posts with $X or Y% |
| **Pull-Quote Card** | The sharpest line typeset huge | Contrarian one-liners |
| **Two-Panel Contrast** | Split: what-everyone-thinks / what-actually | Not-X-it's-Y posts |
| **Architecture Diagram** | Nested panels, chip-labeled components | System/process posts |
| **Story Card** | Portrait 1200×1500, bold hook, vulnerable tone | "I quit my job" stories |
| **Tweet-Style Card** | Long-form body, monospace accents | Dev/engineering posts |
| **List Card** | 3-5 items stacked with accent numbers | Rule-of-three posts |
| **Negative-Space Card** | One word/number on mostly empty canvas | Maximum confidence plays |

### What to produce per option

For each of the 5 options, write a complete HTML file to `creatives/YYYY-MM-DD/option-<N>-<name-slug>.html` and render to `option-<N>-<name-slug>.png`.

Document each option in a single `creatives/YYYY-MM-DD/develop-<slug>.md`:

```markdown
## Option 1: Quiet Tension
- Archetype: Big-Number Card
- Conviction bet tested: #1 (the 240px hero)
- Kill list compliance: no gradients, single accent (indigo), top-left anchor ✓
- Mechanic: all weight on the stat, no competing elements
- Files: option-1-quiet-tension.html, option-1-quiet-tension.png

## Option 2: <name>
...
```

### Render loop

```bash
python3 scripts/render_creative.py \
  creatives/YYYY-MM-DD/option-<N>-<slug>.html \
  creatives/YYYY-MM-DD/option-<N>-<slug>.png \
  --width 1200 --height 1200
```

Or 1200×1500 for Story archetype.

### Phase 2 pause

Read all 5 rendered PNGs yourself via Read tool. Show them to the user by listing paths + the develop.md. Say:

> "Develop phase done. 5 options in `creatives/YYYY-MM-DD/`. Open them to review. Reply with what to ship, what to kill, what to combine, or what new direction to try."

Do not proceed until user selects ≥ 1 survivor.

---

## Phase 3: Deliver (7-dimension critique + verdict)

For each surviving option (1-3 typically), apply the 7-dimension design review:

### The 7 dimensions

| # | Dimension | What to check |
|---|---|---|
| 1 | **Visual Hierarchy** | Does the eye land on the most important thing first? Is the hero 2-3x larger than everything else? |
| 2 | **Contrast** | Enough contrast between accent and ink? Accessible on small screens? |
| 3 | **Flow** | Does the eye move through the composition in the intended order (usually F-pattern or Z-pattern)? |
| 4 | **Layout + Golden Ratio** | Are divisions roughly 1:1.618 or 1:1 or 1:2? Not awkward mid-ratios. |
| 5 | **Clear Space** | ≥ 80px breathing room on the outer canvas? No elements fighting for the same pixel? |
| 6 | **CTA Placement** | If there's a CTA, is it in the bottom-third or right-third (where eyes rest)? |
| 7 | **Engagement / Scroll-Stop** | Would this stop a thumb in 400ms? Blur test: if you blurred all text except the biggest, does that alone make someone pause? |

### Conviction audit

Per option:
- Does it satisfy the position statement? (yes/no + why)
- Does it pass all 3 success criteria (3-second, thumbnail, logo-swap)? (yes/no per test)
- Does it respect the full kill list? (any leaks?)
- Which conviction bet does it validate? Which does it contradict?

### Verdict

Per option: **Ship** / **Revise** / **Kill**, with specific action points.

Write to `creatives/YYYY-MM-DD/deliver-<slug>.md`. Show user. Offer the winner(s) as final.

---

## Design system (unchanged from v1)

### Colors

```css
/* Canvas */
--bg-canvas:     #f8f9fb;
--bg-card:       #ffffff;
--ink-primary:   #0a0b0c;
--ink-secondary: #52525b;
--border-subtle: #e4e4e7;

/* Accents — pick ONE per image */
--accent-indigo: #4338ca;   /* trustworthy, enterprise */
--accent-violet: #7c3aed;   /* premium, creator */
--accent-emerald:#059669;   /* growth, numbers-up */
--accent-coral:  #dc2626;   /* urgency, contrarian */
--accent-slate:  #0f172a;   /* understated, philosophical */
--accent-soft:   #eef2ff;   /* pale accent bg — indigo variant */
```

### Typography

Inter via Google Fonts. Weights: 400/500/600/700/800/900. Use them aggressively.

| Element | Size | Weight | Tracking |
|---|---|---|---|
| Hero number | 140-240px | 800-900 | -0.03 to -0.05em |
| Headline | 48-72px | 700-800 | -0.02em |
| Subhead | 24-32px | 600 | -0.01em |
| Body | 18-22px | 400-500 | 0 |
| Chip/label | 12-14px | 600 | +0.05em, UPPERCASE |

### Grid

8-point system. All margins, gaps, radii as multiples of 8.
Canvas padding: 80-96px minimum on 1200px canvas.
Card radii: 16-24px (never > 32px, looks toy-like).
Chip radii: 9999px (full pill).

### Anti-patterns (hard rejects)

- 🚫 Gradients on backgrounds
- 🚫 Stock illustrations or generic iconography
- 🚫 Emojis as design elements (max 1 in a label)
- 🚫 Drop shadows (exception: 1 hero card, max `0 1px 2px rgb(0 0 0 / 0.05)`)
- 🚫 Multiple accent colors
- 🚫 Rounded corners > 32px
- 🚫 Text < 14px
- 🚫 Centered everything (use left-align + grid)
- 🚫 AI-stylized decoration (neural swooshes, "AI" badges)

---

## LLM model routing (simple version)

Aayush's use case is manual single-shot, so all 3 phases run in the main Claude Code context (Opus). No external model calls needed for v1.

Upgrade path (future):
| Phase | Model | Source |
|---|---|---|
| Define | Claude Opus | main context |
| Develop SVG | Claude Opus | main context |
| Deliver critique | Claude Opus | main context |
| Competitive visual scan (optional) | Gemini 3.1 Pro + Google grounding | llmproxy.atlan.dev |
| Image gen (optional photographic) | Imagen 4 Ultra | llmproxy.atlan.dev |

If ever added, keep the routing in a separate `council.json` alongside this SKILL.md, same pattern as `config/council.json` at the project root.

---

## Reference examples

Two reference HTML files in `examples/`:
- `stat-card.example.html` — Big-Number Card (Cerebras $10B)
- `architecture.example.html` — Architecture Diagram (system map)

These were hand-built to match the Marketing OS aesthetic. Match this quality bar — don't copy content.

---

## Summary of process

1. **Define** (Conviction Workshop) → pause for human approval
2. **Develop** (5 distinct options, rendered PNGs) → pause for human selection
3. **Deliver** (7-dim critique + verdict on survivors) → ship winner(s)

Three pauses. No phase skips itself. Define is where quality is won or lost — if convictions are wrong, 5 options will all be wrong.
