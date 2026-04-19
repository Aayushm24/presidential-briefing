# Anti-AI-Slop Checklist

Adapted from Helix (`atlanhq/atlan-marketing-team/shared/anti-slop-checklist.md`). Run every draft through these before shipping. No exceptions.

Applies to briefs AND posts. Council `/attack` enforces via explicit LLM prompts + clean_text.py regex.

---

## The 5 Tests

### 1. Substitution Test
Replace the specific company/person in your lead with a generic one ("another AI company", "another tool"). Does the copy still work? **If yes → too generic. Rewrite until it can only be about THIS specific thing.**

Catches: *"the parallel to the early cloud era is almost exact"*, facile metaphors that apply to anything.

### 2. Specificity Count
At least **3 specific numbers, named companies, or concrete examples** per brief section (or per post). *"Cursor raised $2B at $50B"* beats *"valuations are soaring."* *"47% mobile app growth"* beats *"mobile apps are booming."*

### 3. Jargon Scan
Ctrl+F for these words and delete every instance:
- synergy
- leverage (unless financial context)
- seamlessly
- cutting-edge
- unlock
- empower
- harness
- robust
- scalable (unless with technical justification)

Also kill these phrases:
- "In today's landscape,"
- "It's important to note,"
- "At the end of the day,"
- "humbled and honored,"
- "proud to announce"

### 4. Stat-Stat-Reframe-Metaphor Check
**This is the #1 AI tell.** If a paragraph follows this pattern:

> "X% of companies... Y% fail... but here's the reframe... [clever metaphor]"

**Rewrite.** Humans don't write this way. Break the pattern: weave stats into the argument, don't bullet-stack them.

Catches: *"these two numbers landed in the same week and everyone treated them as separate stories"*, *"X% + Y% = reframe + metaphor"* scaffolding.

### 5. "So What?" Test
For every sentence, ask: **"So what does this mean for the reader?"** If you can't answer in one sentence → cut.

---

## Additional Patterns to Avoid

- **[Not X, it's Y] inversions:** *"These aren't unrelated stories. They're the same story."* / *"This isn't about compliance — it's about competitive advantage."* Real writers don't rhetorically signpost like this. Max 1 per document.

- **"Why now?" transitions:** *"What's happening is..."*, *"Here's why this matters..."*, *"Here's the thing..."* — real writers don't announce their rhetorical moves. Cut structural labels.

- **Em-dashes for drama:** Use periods, commas, or semicolons.

- **Passive voice:** *"The data is connected by the system"* → *"The system connects the data."*

- **Feature-first copy:** *"Claude provides..."* → Lead with the problem or outcome.

- **Hedging:** *"We believe,"* *"It seems like,"* *"I think perhaps"* — make the claim or don't. Replace with either a specific assertion or drop the sentence.

- **Neat bows at the end:** *"This is where the real race is."* *"The founders who see this will win. The ones who don't will retrofit."* End on an open question, honest uncertainty, or a grounded closer — never a drum-roll summary.

- **Fabricated authority:** *"here's what i've seen firsthand across a dozen teams"*, *"i've been tracking a rough metric"*, *"a 14-person team i advise"* — every first-person specific claim MUST trace to `config/aayush-experiences.md`. If no matching entry → rewrite as a take (not a story).

- **Forced LLM coinages:** *"tokenmaxxing"* and similar made-up terms signal AI trying to sound clever. Use established vocabulary.

---

## The Gold Standard

The best writing is **confident, specific, and direct**. It makes claims and backs them with receipts. It names things.

When in doubt, read Aayush's own shipped posts and reverse-engineer the rhythm. Voice matching from published work beats voice guide rules.

---

## Enforcement

- **`/attack` council** runs the 5 Tests as LLM questions + regex pre-flight
- **`scripts/clean_text.py`** auto-flags the specific phrases (stat-stat pattern, "Why now?" transitions, neat bows)
- **`/revise`** applies deterministic fixes first, then LLM polish
- **`/publish`** has hard gates — if any Test fails post-revise, pipeline exits 1, nothing ships
