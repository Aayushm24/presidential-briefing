# Section Order (mandatory)

Every briefing follows this structure. The `/attack` skill enforces presence of each section.

---

## 1. Title

```
# [title in sentence case — one sharp claim, not a description]
```

**Good:** `# The agent knowledge moat is evaporating`
**Bad:** `# Today's AI news — Notion, OpenAI, Anthropic updates`

Title is a claim. Descriptions are boring.

---

## 2. Hook (1 line)

One sentence. One specific, surprising detail. No setup.

**Good:** "Notion rebuilt their agent system five times."
**Bad:** "Today there's a lot happening in AI agents."

---

## 3. Bottom line (2–3 sentences)

The thesis. Say it ONCE, say it well, right here. **Do NOT repeat this at the end.**

**Good:** "The knowledge required to build production AI agents went from locked inside a few teams' heads to publicly accessible in the last 24 hours. Frameworks, case studies, post-training courses. The remaining differentiator isn't knowledge. It's how fast you iterate."

**Bad:** "This is a big day for AI agents because there are many things happening that could be important for businesses."

---

## 4. Key takeaways (4–5 bullets)

```
**Key takeaways:**
- [scannable bullet 1 — specific]
- [scannable bullet 2 — specific]
- [scannable bullet 3 — specific]
- [scannable bullet 4 — specific]
- [scannable bullet 5 — specific, optional]
```

A reader who stops here got 80% of the value. Every bullet must be usable standalone — no references to "see below."

---

## 5. Lead section (main piece)

```
### [descriptive section header — sentence case]

[content — short paragraphs, bold key phrases, block quotes, NO dividers]

### [next section header]

[content]

### [last section of main piece]

[content — weave the connection between stories naturally in the final paragraphs. DO NOT create a "how these connect" header. Flow into it. End with a punchline that sticks, not a summary.]
```

Rules:
- H3 headers only (no H2)
- Sentence case
- 2–4 sections total in the lead piece
- No `---` dividers between sections
- Every section opens with the point
- At least one block quote in the lead piece
- Named companies, specific numbers, linked tools

---

## 6. Divider + secondary posts

```
---

### #2 [secondary post title in sentence case]

[content — shorter, 200-400 words. Same rules as lead but compressed.]

---

### #3 [secondary post title in sentence case]

[content]
```

Secondary posts are for:
- Standalone stories that didn't fit the main theme
- Connected-but-not-primary evidence
- Minor news worth knowing but not worth the lead slot

Each gets `---` divider above, `### #N` header, 200–400 words.

Max 3 secondary posts (#2, #3, #4). If the day has more, cut to the strongest three.

---

## 7. Closing: What to do this week

```
---

### What to do this week

[1-3 specific, concrete actions based on today's briefing. Not vague advice.
Specific: "Pick one agent initiative from your backlog. Run it through Farooq's framework.
If it lands in the bottom tier, ask yourself: will a platform ship this in 12 months?"
Name the tools. Link the resources. Tell them exactly what to do and how long it takes.]
```

Rules:
- Max 3 actions
- Every action names a tool, a link, or a specific technique
- Include time estimates ("30 minutes")
- Never "reflect on", "consider", "think about" — always a concrete verb

---

## 8. Sources (auto-generated footer)

```
---

## Sources

1. [Article title] — [author, publication, date]. URL.
2. [Article title] — [author, publication, date]. URL.
...
```

Every cited claim maps to a numbered source. If a claim doesn't have a source, it gets tagged `[UNGROUNDED]` in the draft (gets resolved or killed during `/attack`).

---

## What NOT to include

- ❌ "Wrapping up" or "In conclusion" or "To summarize"
- ❌ Re-stating the bottom line at the end
- ❌ "How these connect" header (flow into connections naturally)
- ❌ TLDR at both top and bottom (bottom line + key takeaways at top = TLDR)
- ❌ H2 headers (they create ugly dividers)
- ❌ Title Case headers
- ❌ Horizontal dividers within the lead piece

---

## Validation (used by `/attack` council)

Pipeline enforces structure via `tests/golden-format.sh`:
- H1 count: exactly 1 (the title)
- H3 count: 3–8 (sections + secondary posts + closing)
- "Key takeaways:" bold present
- "### What to do this week" present (or `### [Week-specific title]` ending in `this week`)
- "## Sources" footer present with ≥3 numbered sources
- No em dashes (regex)
- No H2 headers outside Sources
- Word count: 800–2,500
