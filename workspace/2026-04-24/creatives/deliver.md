# LinkedIn creative — GPT-5.5 post

**Date:** 2026-04-24
**Supports post:** `gpt-55-my-feed-is-doing-the-thing.md` (Register B — observation-first, unresolved closer)
**Format:** 1080×1080, LinkedIn feed image

---

## 1. Core visual concept

A receipt-style price tag reading **"$180 / 1M tokens"** with one word stamped across it in red: **"PAID."** — the image signals the exact moment debate ends and payment starts, which is the whole argument of the post.

---

## 2. Three concept options

### Option A — The Receipt
**Hook:** A monospace receipt/invoice showing a single line item: `GPT-5.5 · 1,000,000 tokens · $180.00`, with a red "PAID" stamp angled across it and a tiny note at the bottom: *"no approval needed."*

**Why it pairs:** The post's spine is Lenny's quote — "Happy to pay $180 per million tokens." A receipt makes that line physical. It also matches Aayush's observation-first tone: the image is a document, not a statement. Reader has to look for a second to parse it.

**Risks:** Receipts are a slightly tired design trope on LinkedIn (lots of "founder receipts" memes in 2024). Has to be executed with restraint — no fake fonts, no coffee stains, no emojis on the receipt.

---

### Option B — The Two-Tier Budget Split
**Hook:** Two horizontal bars stacked. Top bar: a long line filled to ~90% labeled "teams with AI budget." Bottom bar: same width, filled to ~10%, labeled "teams without." A vertical dashed line at the $180 mark cuts both bars.

**Why it pairs:** Directly illustrates the pivot — "just unlocked a new capability / just got locked out of it." Makes the stratification argument legible in half a second. Works as a chart without needing a real dataset.

**Risks:** Reads as a real benchmark chart when it isn't — could feel like fake data. Also more "analyst deck" than builder's voice. Could drift into slop if the styling gets too polished.

---

### Option C — The Reversed Arrow
**Hook:** Pure typography. Big sentence broken across two lines:
> "AI democratized capability."
> "AI democratized capability." (struck through)
>
> Below, smaller: *"Capability ← Budget"* with the arrow pointing away from the reader.

**Why it pairs:** Leans hard on the "that story is reversing FAST" beat. All-typography matches Aayush's aesthetic — clean, minimal, no decoration, a built-not-branded look. The strike-through is the visual reversal.

**Risks:** Could feel too clever or too "designer-y." Text-heavy images underperform on LinkedIn unless the hierarchy is ruthless. Also — the quote isn't Aayush's, so there's a risk it reads like he's claiming the line.

---

## 3. Recommended concept — Option A (The Receipt)

The receipt wins because it carries Lenny's quote as the proof — which is the actual turn in the post — and because it's a document (an artifact), not a claim. Aayush can keep writing opinions in the body; the image just shows the receipt.

### Exact copy on the image

Only these strings appear:

- Top header (small, sans): `ORDER #0055 · 04.24.2026`
- Line item 1: `GPT-5.5` `1,000,000 tokens` `$180.00`
- Total line: `TOTAL` `$180.00`
- Angled stamp across middle: `PAID`
- Footer line (tiny, under the cut): `debate ended before checkout.`

Total words on image: **12.** Headline presence comes from `$180.00` and `PAID`, not a tagline.

### Layout / composition (1080×1080)

- Full-bleed off-white canvas (warm paper tone, not pure white)
- Centered receipt, ~520px wide, with subtle drop-shadow — sits like a photograph of paper, not a UI card
- Top of receipt aligned ~180px from top
- `$180.00` is the single largest element on the card (heavier weight, ~72px)
- `PAID` stamp: red, ~150px tall, rotated -12°, placed across the line item. Slightly misaligned so it reads hand-stamped, not generated
- Torn bottom edge on the receipt (jagged cut, not a clean line) — this is the detail that makes it feel real
- Footer line `debate ended before checkout.` sits *below* the torn edge, in the canvas, lowercase, small

### Color palette — "ledger paper"

- Canvas: warm off-white (think: old invoice paper, not Apple white)
- Receipt body: slightly whiter than canvas, ~2% contrast step
- Text: near-black, not true black
- Stamp: brick red (think: library date-stamp, not CTA button red)
- No gradients, no glow, no soft shadows beyond the paper shadow

### Typography

- **Receipt body:** monospaced (IBM Plex Mono, JetBrains Mono, or similar). Mono is load-bearing — it signals "machine-printed document"
- **Stamp "PAID":** condensed bold sans with slight letter-spacing. Rough/distressed edges if possible — a clean "PAID" looks fake
- **Footer line:** same mono, smaller, lowercase

No italics. No color variance except the stamp.

### Real asset vs. pure typography

**Pure typography / vector.** No screenshot needed. A real screenshot of an OpenAI bill would (a) be a privacy issue, (b) not exist yet because the post is about the moment of launch. A stylized receipt is honest about being a metaphor.

---

## 4. Text-only mockup

```
┌──────────────────────────────────────────────────┐
│                                                  │
│                                                  │
│         ┌─────────────────────────────┐          │
│         │  ORDER #0055 · 04.24.2026   │          │
│         │  ─────────────────────────  │          │
│         │                             │          │
│         │  GPT-5.5                    │          │
│         │  1,000,000 tokens   180.00  │          │
│         │     ╔════════════╗          │          │
│         │     ║   P A I D  ║          │          │
│         │     ╚════════════╝          │          │
│         │  ─────────────────────────  │          │
│         │  TOTAL              $180.00 │          │
│         │                             │          │
│         └───⌐ ⌐ ⌐ ⌐ ⌐ ⌐ ⌐ ⌐ ⌐ ⌐ ⌐───┘          │
│                (torn edge)                       │
│                                                  │
│       debate ended before checkout.              │
│                                                  │
└──────────────────────────────────────────────────┘
```

The `PAID` stamp sits angled across the 1M-tokens line. The torn bottom edge is the visual flourish that separates the metaphor from a generated card.

---

## 5. HTML/SVG mockup

```html
<!doctype html>
<html>
<head>
<style>
  :root {
    --paper: #f4efe6;
    --receipt: #fbf8f1;
    --ink: #141414;
    --stamp: #a8301f;
  }
  body { margin: 0; background: var(--paper); font-family: 'IBM Plex Mono', ui-monospace, monospace; }
  .canvas {
    width: 1080px; height: 1080px;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    gap: 48px;
    position: relative;
  }
  .receipt {
    width: 540px;
    background: var(--receipt);
    padding: 44px 44px 0 44px;
    color: var(--ink);
    box-shadow: 0 6px 24px rgba(20,20,20,0.08), 0 1px 2px rgba(20,20,20,0.06);
    position: relative;
  }
  .receipt::after {
    /* torn edge */
    content: "";
    position: absolute;
    left: 0; right: 0; bottom: -22px;
    height: 24px;
    background: var(--receipt);
    clip-path: polygon(
      0 0, 5% 90%, 10% 30%, 15% 100%, 20% 40%, 25% 95%,
      30% 25%, 35% 90%, 40% 40%, 45% 100%, 50% 20%, 55% 90%,
      60% 40%, 65% 100%, 70% 30%, 75% 95%, 80% 25%, 85% 90%,
      90% 35%, 95% 100%, 100% 40%, 100% 0
    );
  }
  .head { font-size: 14px; letter-spacing: 0.08em; opacity: 0.7; }
  .rule { border: none; border-top: 1px dashed rgba(0,0,0,0.3); margin: 18px 0; }
  .line { display: flex; justify-content: space-between; font-size: 20px; margin: 10px 0; }
  .hero { font-size: 28px; font-weight: 600; margin-top: 10px; }
  .total { display: flex; justify-content: space-between; font-size: 22px; font-weight: 600; margin-top: 6px; }
  .stamp-wrap { position: relative; height: 120px; }
  .stamp {
    position: absolute; left: 60px; top: 10px;
    transform: rotate(-11deg);
    border: 4px solid var(--stamp);
    color: var(--stamp);
    padding: 10px 28px;
    font-family: 'Bebas Neue', 'Arial Narrow', sans-serif;
    font-size: 64px; letter-spacing: 0.2em;
    opacity: 0.9;
    box-shadow: inset 0 0 0 1px rgba(168,48,31,0.2);
  }
  .footer {
    font-size: 18px;
    color: rgba(20,20,20,0.62);
    letter-spacing: 0.01em;
  }
</style>
</head>
<body>
  <div class="canvas">
    <div class="receipt">
      <div class="head">ORDER #0055 &middot; 04.24.2026</div>
      <hr class="rule" />
      <div class="hero">GPT-5.5</div>
      <div class="line"><span>1,000,000 tokens</span><span>$180.00</span></div>
      <div class="stamp-wrap">
        <div class="stamp">PAID</div>
      </div>
      <hr class="rule" />
      <div class="total"><span>TOTAL</span><span>$180.00</span></div>
      <div style="height: 24px"></div>
    </div>
    <div class="footer">debate ended before checkout.</div>
  </div>
</body>
</html>
```

Drop this into any browser at 1080×1080 viewport, screenshot → ship. For production, swap in IBM Plex Mono (Google Fonts) and a distressed stamp SVG for the "PAID" text to kill the last bit of CSS-cleanness.

---

## Notes for Aayush

- The footer line `debate ended before checkout.` is the only editorial beat on the image. It mirrors the post's argument without repeating its words. Cut it if you want the image to be pure artifact.
- If the stamp feels too on-the-nose, swap `PAID` for `APPROVED` (same visual weight, slightly cooler tone). `PAID` is the right call because it matches Lenny's quote exactly.
- Do not add Atlan branding. This is Register B — no company hook.
- Do not add an OpenAI logo. Trademark risk, plus it drags the image toward "corporate announcement" energy.
