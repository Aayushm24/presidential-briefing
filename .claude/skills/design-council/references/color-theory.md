# Color theory — structured palettes for design-council

Replaces the old "pick one accent" rule. Now every creative picks a **mood** (a 5-color palette with roles) matched to the post archetype.

## Why palettes beat accents

A single accent on neutrals reads austere and corporate. A full palette with systematic roles reads designed and intentional. The Marketing OS reference you've anchored on uses 5 colors purposefully — primary hero, secondary surface, accent chips, surface canvas, ink. Not one accent plus emptiness.

## The 60-30-10 rule

Every creative allocates color by area:
- **60% surface** — the canvas, the bg, the breathing space
- **30% secondary** — cards, panels, secondary blocks, outlined shapes
- **10% hero + accent combined** — the hit color on the biggest text, plus pops on chips/underlines/punctuation

Break this ratio and the creative starts looking busy or flat.

## The 5 moods

Each mood has 5 role-mapped tokens. Pick the mood based on the post archetype (decision tree below). Never mix moods within one creative.

### Mood 1 — Violet thesis

Use for: philosophical / contrarian / thesis-driven posts. The post makes a claim that reframes the category ("AI is a commodity", "memory > models").

```css
--surface:   #fafaf9;  /* stone-50 — warmer than pure white, easier on feed */
--card:      #ffffff;
--hero:      #6d28d9;  /* violet-700 — deep, confident */
--hero-soft: #e9d5ff;  /* violet-200 — background for chips on hero color */
--accent:    #f472b6;  /* pink-400 — small pops, underlines, chip bg */
--ink:       #0a0a0a;
--ink-dim:   #52525b;  /* zinc-600 */
--border:    #e4e4e7;
```

Signals: premium, creator, takes a stand.

### Mood 2 — Indigo system

Use for: architecture / dot-connecting / system explainer posts. The post is showing how parts fit together.

```css
--surface:   #f8fafc;  /* slate-50 */
--card:      #ffffff;
--hero:      #4338ca;  /* indigo-700 */
--hero-soft: #c7d2fe;  /* indigo-200 */
--accent:    #06b6d4;  /* cyan-500 — tech/AI accent */
--ink:       #0f172a;
--ink-dim:   #475569;
--border:    #e2e8f0;
```

Signals: technical, trustworthy, enterprise-adjacent without being corporate.

### Mood 3 — Emerald growth

Use for: stat-driven / number-heavy / "growth" posts. The post leads with a metric.

```css
--surface:   #fafaf9;  /* stone-50 */
--card:      #ffffff;
--hero:      #059669;  /* emerald-600 */
--hero-soft: #a7f3d0;  /* emerald-200 */
--accent:    #f59e0b;  /* amber-500 */
--ink:       #0a0a0a;
--ink-dim:   #52525b;
--border:    #e4e4e7;
```

Signals: numbers-up, optimistic without being naive, proof-backed.

### Mood 4 — Coral urgency

Use for: contrarian-alarm / "wake up" / "this is broken" posts. The post is calling out something wrong.

```css
--surface:   #fafaf9;
--card:      #ffffff;
--hero:      #dc2626;  /* red-600 */
--hero-soft: #fecaca;  /* red-200 */
--accent:    #f59e0b;  /* amber-500 */
--ink:       #0a0a0a;
--ink-dim:   #52525b;
--border:    #e4e4e7;
```

Use sparingly. Coral is a loud voice — it should be for posts where the loudness is earned.

### Mood 5 — Ink thesis

Use for: story / confession / vulnerable / "I quit my job" posts. The post is personal, reflective, hard-won.

```css
--surface:   #fafaf9;
--card:      #ffffff;
--hero:      #18181b;  /* zinc-900 — deep black, not pure */
--hero-soft: #d4d4d8;  /* zinc-300 */
--accent:    #facc15;  /* yellow-400 — optimism peeking through */
--ink:       #18181b;
--ink-dim:   #52525b;
--border:    #e4e4e7;
```

Signals: earned, honest, no performance. The yellow accent is the one point of brightness — use it once (a chip, a single highlight).

## Decision tree

Map post → mood:

```
Is the post a thesis/contrarian reframe?          → Violet thesis
Is it architecture or system explanation?         → Indigo system
Is the hook a specific stat/number?               → Emerald growth
Is it a "this is broken / wake up" alarm?         → Coral urgency
Is it story / confession / vulnerable?            → Ink thesis
Not sure?                                         → Default to Violet thesis (safest for the Aayush feed)
```

## How to use within a creative

1. **Surface (60%):** canvas background + any negative-space zones.
2. **Card (30%):** cards, panels, secondary blocks get `--card` bg. Optional: swap to `--hero-soft` for 1-2 accent panels that should stand apart.
3. **Hero (≤10%):** the single biggest text — the word, the number, the claim — uses `--hero`. One hero element per image. Not two.
4. **Accent (≤5%):** chips, underlines, quote marks, punctuation pops. Use `--accent`. Max 1-2 accent elements per image.
5. **Ink:** body copy, subheads, footer text.
6. **Ink-dim:** secondary text (captions, metadata, dates).
7. **Border:** card borders, dividers, subtle outlines.

Rule: never more than 5 distinct colors in one creative. The 5 mood tokens are all you get.

## Ban list (still applies)

- 🚫 Gradients on backgrounds (reads as 2015 startup)
- 🚫 Multiple hero colors in one creative
- 🚫 Accents at 50%+ saturation when placed on white (blows out)
- 🚫 Ink on hero-soft (too low contrast — use ink on surface/card instead)

## Contrast rules

- Hero text on surface: contrast ≥ 8:1 (no exception)
- Body text on surface: contrast ≥ 4.5:1
- Accent on surface: contrast ≥ 3:1 for decorative, ≥ 4.5:1 for text
- White text on hero block: only if hero ≥ violet-700 / indigo-700 / emerald-600 / red-600 / zinc-900 equivalent darkness

Test: open in grayscale. If the hierarchy still reads (hero dominates), contrast is right.

## Footer standard (applies to every creative)

Replace the old `@aayush-maheshwari · presidential briefing` footer with:

```
[LinkedIn SVG icon, 20×20, in LinkedIn blue #0a66c2] aayush-maheshwari    2026-MM-DD
```

The LinkedIn icon is the official rounded-square glyph. Inline SVG — no external asset:

```html
<svg class="li-icon" width="20" height="20" viewBox="0 0 24 24" fill="#0a66c2" xmlns="http://www.w3.org/2000/svg">
  <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.063 2.063 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
</svg>
<span>aayush-maheshwari</span>
```

CSS:
```css
.footer-handle { display: inline-flex; align-items: center; gap: 8px; font-size: 15px; font-weight: 500; color: var(--ink); }
.li-icon { display: inline-block; vertical-align: middle; }
```

No "presidential briefing" text anywhere.
