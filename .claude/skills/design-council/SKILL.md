# design-council — generate a scroll-stopping visual for a LinkedIn post

Manual invocation. User pastes a LinkedIn post text (or points you at a `.md` / `posts.json` file). You pick the best visual archetype, write custom HTML using the design system below, render it to PNG via Playwright, and show the result.

Target: a visual that matches the Marketing OS aesthetic — precise typography, clean spacing, purposeful color, zero AI-image-model chartjunk. This is HTML+CSS, not a diffusion model.

## Invocation

```
/design-council <post-text-or-file-path>
```

If the arg looks like a path, read it. Otherwise treat the entire arg as the post text. If ambiguous, show the user the first 200 chars and ask to confirm.

## Process (5 steps)

### Step 1: Extract
From the post, identify:
- **Hook** (first 1-2 lines — the scroll-stopper)
- **Key number/stat** (if any — "$10 billion", "400% better", "3x faster")
- **Structure** (is this: stat-driven / contrarian claim / story / absurd comparison / architecture-explainer?)
- **Named entities** (Cerebras, Claude, OpenAI — anything concrete)
- **Core claim** (one sentence summary of the post's argument)

### Step 2: Pick archetype
Match structure → archetype:

| Post structure | Archetype | Dimensions | When |
|---|---|---|---|
| Single big stat | **Big-Number Card** | 1200×1200 | "$10B deal", "392 engagement", "500% increase" |
| Contrarian one-liner | **Pull-Quote Card** | 1200×1200 | "AI chips are not a winner-take-all game" |
| Before/after or "not X, it's Y" | **Two-Panel Contrast** | 1200×1200 | "everyone thinks X / actually Y" |
| System with 3+ components | **Architecture Diagram** | 1200×1200 or 1200×1500 | Marketing OS, Helix, context layers |
| Story / confession / vulnerable | **Story Card** | 1200×1500 | "I quit my job", "last week was a huge win" |

If multiple fit, pick the one that makes the HOOK land hardest. When in doubt → Big-Number or Pull-Quote (simplest, highest thumb-stop rate).

### Step 3: Write HTML
Write complete standalone HTML using the design system (below). Save to `creatives/YYYY-MM-DD/draft-<slug>.html`. Use the 2 reference files in `.claude/skills/design-council/examples/` as structural anchors — don't copy them, but match the aesthetic.

### Step 4: Render
```
python3 scripts/render_creative.py creatives/YYYY-MM-DD/draft-<slug>.html creatives/YYYY-MM-DD/<slug>.png --width 1200 --height 1200
```

If Playwright isn't installed, the script will print install instructions. Pass those to the user.

### Step 5: Show + iterate
- Read the PNG back (you can view images via Read tool) and critique it yourself before showing user
- Self-critique: Does the hook fit in 400ms glance? Text readable at 300×300 thumbnail? First 5 words in top-left quadrant?
- If it fails any check, regenerate HTML with the fix
- Show final PNG to user, offer: "ship this, tweak the X, or try a different archetype?"

## Design system

### Color palette (tech-forward, restrained)

```css
/* Primary */
--bg-canvas:     #f8f9fb;   /* off-white page bg */
--bg-card:       #ffffff;   /* card / panel bg */
--ink-primary:   #0a0b0c;   /* headlines + body */
--ink-secondary: #52525b;   /* labels + captions */

/* Accent (pick ONE per image — don't mix) */
--accent-indigo: #4338ca;    /* trustworthy, enterprise-feel */
--accent-violet: #7c3aed;    /* premium, creator-feel */
--accent-emerald:#059669;    /* growth, numbers-up */
--accent-coral:  #dc2626;    /* urgency, contrarian */
--accent-slate:  #0f172a;    /* understated, philosophical */

/* Support */
--border-subtle: #e4e4e7;    /* dividers, card edges */
--bg-accent-soft:#eef2ff;    /* pale accent bg (matches indigo) */
```

### Typography

Load Inter (variable) via Google Fonts. Use its weights aggressively.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
```

| Element | Size (px) | Weight | Tracking |
|---|---|---|---|
| Hero number / headline | 96-140 | 800-900 | -0.03em |
| Section H1 | 48-64 | 700-800 | -0.02em |
| Subhead | 24-32 | 600 | -0.01em |
| Body | 18-22 | 400-500 | 0 |
| Label / chip | 12-14 | 600 | +0.05em, uppercase |

### Layout

- **Canvas:** always start with `padding: 80px` on the outer container. Breathing room is free quality.
- **Grid:** 8-point system. Margins, gaps, radii all multiples of 8 (8, 16, 24, 40, 64, 80).
- **Cards:** `border-radius: 24px`, `background: var(--bg-card)`, subtle border `1px solid var(--border-subtle)`, avoid shadows (too decorative).
- **Chips/pills:** `border-radius: 9999px`, padding `6px 14px`, font-size 12-14, uppercase, weight 600.
- **Accent usage:** accent color on ONE element only — the number, the headline, or a single chip. Never multiple accents.

### Anti-patterns (reject)

- 🚫 Gradients on backgrounds (reads as 2015 startup)
- 🚫 Stock illustrations or generic iconography (Heroicons ok if one, single-color, 32px max)
- 🚫 Emojis as design elements (one in a label is fine; don't decorate with them)
- 🚫 Drop shadows (except 1 on hero card if needed, max `0 1px 2px rgb(0 0 0 / 0.05)`)
- 🚫 Rainbow text or multiple accent colors
- 🚫 Rounded corners bigger than 32px (looks toy-like)
- 🚫 Any text smaller than 14px (unreadable on mobile)
- 🚫 Centered layouts for architecture diagrams (use left-align + grid)
- 🚫 AI-stylized elements ("AI-powered" badges, neural net swooshes)

### Archetype templates

**Big-Number Card** — one massive number, accent color, supporting label + caption:
```
[small uppercase label chip in accent-soft bg]
[massive hero number — 140px, accent color]
[one-line claim — 32px bold, ink-primary]
[caption — 18px, ink-secondary, max 2 lines]
[tiny footer: source / @aayush-maheshwari]
```

**Pull-Quote Card** — the post's sharpest line, typeset huge:
```
[decorative quote mark or thin accent bar at top-left]
[the quote — 56-72px bold, ink-primary, max 3 lines]
[attribution — 18px ink-secondary: "— Aayush" or context]
[tiny footer]
```

**Two-Panel Contrast** — split vertically or horizontally:
```
LEFT panel: light bg,  ink-primary text, label "WHAT EVERYONE THINKS"
RIGHT panel: accent bg, white text,      label "WHAT ACTUALLY HAPPENS"
Each with a 1-line claim + optional supporting detail
```

**Architecture Diagram** — nested rectangles, Marketing-OS-style:
```
Outer container: bg-canvas, 80px padding
Section headers: 14px uppercase labels above each block
Big blocks (Context Layer, Agents, etc.): bg-card, 24px radius, 32-40px inner padding
Sub-items inside blocks: small chips/pills, 6-8 per row, flex-wrap
Arrows: thin accent lines with arrowheads (use SVG inline, not text symbols)
Keep everything left-aligned and grid-snapped.
```

**Story Card** — vertical 1200×1500, portrait:
```
Top: tiny chip with the theme ("I QUIT MY JOB")
Middle: big bold headline (the hook) — 64-80px
Below: 1-2 supporting sentences — 24px, generous line-height 1.4
Bottom: Aayush's handle + a small date chip
```

### Quality checklist (run before shipping)

1. Does the hook hit in < 400ms? (Ask: if you blurred everything except the biggest text, does that text alone make someone stop?)
2. Does it read at 300×300 thumbnail (LinkedIn feed preview size)? Open the PNG, resize mentally, confirm readability.
3. Top-left quadrant carries the point? (Readers scan F-pattern.)
4. Max 7 words in the hero text. If more, it's a quote card not a big-number card.
5. ONE accent color used, nothing else competing.
6. All text ≥ 14px.
7. Generous margins (80px+ around content on 1200px canvas).
8. No gradients on main surfaces. Flat or near-flat only.

## Output

After the render step:
1. File paths to the draft HTML and final PNG
2. Brief explanation: "I picked [archetype] because [reason]. Accent: [color]."
3. Offer next steps: "Ship this as-is, tweak the [element], or try a different archetype?"

## Reference examples

Two complete HTML files live in `.claude/skills/design-council/examples/`:
- `stat-card.example.html` — Big-Number Card for a funding stat
- `architecture.example.html` — Architecture Diagram in Marketing-OS style

Read those first when invoked to calibrate your aesthetic. Match the quality bar, don't copy the content.
