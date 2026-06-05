# Council — 2026-06-05 (iteration 1)

## Deterministic findings (pre-flight violations)

Based on clean_text.py output, the following violations were found:

### Em dashes: 7 violations in posts.md
These need immediate correction - em dashes are automatic failures.

### MBA vocabulary violations: 10 total flags
Brief violations:
- "matures" (2 instances)
- "vendor dependency" (2 instances)
- "ecosystem" 
- "compound monthly"

Posts violations:
- "matures" (2 instances)
- "infrastructure dependency"
- "vendor dependency" (2 instances)

### Not X, it's Y inversions: 7 violations total
Brief violations:
- "aren't funding innovation labs anymore. They're paying"
- "isn't a feature you add to existing workflows. It's becoming the"
- "aren't just experimenting with AI anymore. They're scaling"
- "aren't coming from traditional research labs anymore. They're coming"

Posts violations:
- "aren't funding innovation labs anymore. They're paying"
- "isn't about adding AI to existing workflows. It's about rebuilding"
- "aren't just experimenting with AI anymore. They're scaling"

### Neat bow violation: 1 in posts.md
- "The teams that figure this out early will have structural advantages. The ones still"

### Guru voice violations: 3 total
Brief violations:
- "companies view AI capabilities as competitive differentiators they need to own"
- "companies will need to wait"

Posts violations:
- "companies view AI capabilities as competitive differentiators they need to own"

### Long sentence violations: 24 total
Multiple sentences exceed the 22-word limit in both brief and posts.

## Aayush voice score (10-point, gate at 8)

- **Option 1**: 8/10 — PASS threshold but needs hedge marker fix
  - first_person_observer: 2 ("Every week I watch teams...")
  - hedge_markers: 0 (missing — needs IMO/tbh)
  - contrast_labels: 2 ("That's infrastructure thinking")
  - fragment_paragraphs: 2
  - specific_named_details: 2 (Anthropic $47B, Endava, 8-10 developers, etc.)
  - Fix: Add hedge marker like 'IMO' to transformation paragraph

- **Option 2**: 8/10 — PASS threshold but weak observer voice
  - first_person_observer: 1 (weak presence)
  - hedge_markers: 2 (has "IMO")
  - contrast_labels: 2 ("That's infrastructure thinking")
  - fragment_paragraphs: 1
  - specific_named_details: 2
  - Fix: Change "We're seeing" to "Every week I watch teams go through"

- **Option 3**: 6/10 — FAIL threshold, needs strengthening
  - first_person_observer: 2 ("Every team I talk to")
  - hedge_markers: 0 (missing)
  - contrast_labels: 1
  - fragment_paragraphs: 1
  - specific_named_details: 2
  - Fix: Insert 'IMO' before vertical integration wave prediction

**VERDICT: REVISE** - Multiple hard-rule violations plus Option 3 below voice threshold require correction before ship.
