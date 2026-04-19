# Grok Adversarial Prompt

Used by `/attack` council to critique briefs AND posts. Ported verbatim from Helix (`atlanhq/atlan-marketing-team/skills/helix-write/SKILL.md` Step 2).

Grok is picked specifically for this pass because of its low hallucination rate (4.22%) — it won't flag fake problems. Its large context window reads the full draft + research in one pass.

---

## The Prompt

Send this verbatim to `grok-4` via `https://llmproxy.atlan.dev/responses` (no `x_search` tool needed — this is a pure reasoning pass):

```
Review this draft critically. Find:

(1) Logical gaps between sections
(2) Claims not supported by the research brief
(3) Straw-man arguments or unfair framing
(4) Sections where the argument breaks down

Be specific — cite the exact sentences that have problems.

Additional anti-slop checks:
(5) Any paragraph matching the Stat-Stat-Reframe-Metaphor pattern ("X% / Y% / reframe / metaphor")
(6) Any "[Not X, it's Y]" rhetorical inversions
(7) Any "Why now?" / "What's happening is" / "Here's why" structural-label transitions
(8) Any "neat bow" closing (drum-roll summary instead of open question)
(9) Any fabricated first-person specific claims (numbers, teams, code lines) that can't be verified

For each finding, return:
- Exact quoted sentence(s)
- Which rule violated (1-9)
- Specific fix suggestion

Return JSON:
{
  "logical_gaps": [...],
  "unsupported_claims": [...],
  "straw_men": [...],
  "argument_breakdowns": [...],
  "stat_stat_reframe": [...],
  "not_x_its_y": [...],
  "structural_labels": [...],
  "neat_bows": [...],
  "fabricated_claims": [...],
  "overall_verdict": "ship" | "revise" | "reject"
}

DRAFT:
<draft>
{draft_contents}
</draft>

RESEARCH BRIEF:
<research>
{research_contents}
</research>
```

---

## Integration

The `council/attack` skill calls this prompt against `brief.md` and `posts.md` each iteration. Findings feed into `council-notes.md`. `/revise` addresses each finding — if 5/6/7/8 flagged, `scripts/clean_text.py` handles automatically; if 1/2/3/4/9, LLM revise handles with Opus.

If `overall_verdict` is `"reject"`, the orchestrator forces a full rewrite of the affected options (not just patching).
