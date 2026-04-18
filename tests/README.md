# Tests

Regex + structural tests that run on every PR via `.github/workflows/tests.yml`.

These are cheap, fast checks — they catch format regressions and voice drift without requiring LLM calls. The expensive adversarial review (`/attack` council) runs inside the daily-brief pipeline, not in CI.

## Tests

### `golden-format.sh`

Validates every `workspace/*/brief.md` structurally:
- Exactly 1 H1
- 3–8 H3 headers
- `**Key takeaways:**` present
- `### What to do this week` present
- `## Sources` footer with ≥3 numbered sources
- No em dashes (U+2014)
- No H2 outside Sources
- Word count 600–3,000

Also takes an explicit file argument for single-file checks.

### `kill-list-regex.sh`

Scans `workspace/*/posts.md` + `workspace/*/brief.md` for banned words/patterns from `.claude/skills/write-posts/references/kill-list.md`. Catches regressions when the voice profile or kill list gets weakened.

Categories checked: 1A buzzwords, 1B fluff, 1C AI tells, 1D emotion, 1E transitions, 1F openers, 1G em-dash + bullets, 1H "It's like X" analogies, 1K corporate announce, 1L audience direct-address.

Also: bullets (`•`), em dashes (`U+2014`).

### Voice regression fixtures

Directory: `tests/fixtures/voice/`. Should contain 20 approved historical posts. Each PR that modifies `voice.md` or `kill-list.md` runs `kill-list-regex.sh` against every fixture — if any historical post now FAILS, it means the rule change is too aggressive.

**To seed:** copy 20 posts from shipped `workspace/*/posts.md` that Aayush personally approved. Name them `tests/fixtures/voice/YYYY-MM-DD-option-N.md`.

---

## Running locally

```bash
# All tests
./tests/golden-format.sh
./tests/kill-list-regex.sh

# Single file
./tests/golden-format.sh workspace/2026-04-19/brief.md
./tests/kill-list-regex.sh workspace/2026-04-19/posts.md
```

Exit code 0 = pass, 1 = failure. `chmod +x` if shell says "permission denied."

## What these tests do NOT check

- Voice nuance (requires LLM — handled by `/attack` council)
- Fact accuracy (requires live web — handled by Gemini pass in `/attack`)
- Freshness (requires X search — handled by Grok pass in `/attack`)
- Tone or rhythm

Those are agent-loop checks. These tests are regex guardrails for the stuff that has crisp rules.
