# Plain English Rules — shared by /write-briefing + /write-posts

Both writing skills MUST read this before composing. These are hard rules, not guidelines.

The goal: a smart high-schooler with no AI background should parse any sentence in one read. Reference: Brendan J Short's The Signal (thesignal.club) — short declaratives, named things, specific numbers, active verbs, no MBA vocabulary.

---

## Rule 1: No abstract-noun stacks

**Limit: max 2 abstract nouns per sentence.** If a sentence has 3+, rewrite.

An abstract noun names a concept you can't point at: *maturation, commoditization, dependency, differentiation, adoption, transformation, deployment, scalability, optimization, integration*.

```
❌ "The AI infrastructure layer is maturing from private bets into public
    markets and commercial deployment at scale."
    (5 abstract nouns: layer, maturing, bets, markets, deployment-at-scale)

✅ "AI companies used to be risky bets. Now they're going public. Real
    businesses are paying for them."
    (2 abstract nouns across 3 sentences: bets, public-markets)
```

Rewrite test: replace abstract nouns with concrete verbs + named things.
- *"infrastructure commoditization"* → *"everyone can buy the same chips"*
- *"market maturation"* → *"real customers pay real money"*
- *"competitive advantage moves up the stack"* → *"the fight shifts to apps"*

---

## Rule 2: Sentence length cap — 22 words

Count words. Anything over 22 gets split into two sentences.

```
❌ "When specialized AI hardware companies can justify public valuations,
    the underlying market has moved beyond experimental deployments into
    production workloads at scale."  (29 words)

✅ "Wall Street will now pay for AI chip companies. That means real
    businesses buy this stuff daily. It's past the experiment phase."
    (23 + 8 + 8 = three sentences, avg 13)
```

The Signal newsletter averages 12-14 words per sentence. Aim for that.

---

## Rule 3: Banned vocabulary (kill-list)

Reject these words. Their presence = auto-revise.

| Banned | Replace with |
|---|---|
| maturation / matures / maturity (of markets) | "real companies pay real money for X" |
| commoditization / commoditize(s) | "everyone can buy X now" / "X is cheap now" |
| table stakes | "everyone has it" / "it's not special anymore" |
| moat (metaphorical) | "the thing competitors can't copy" / name it concretely |
| differentiation | "what makes you different" / "what your competitor can't do" |
| the stack / up the stack / move up the stack | "apps" / "the product layer" / "the part customers touch" |
| underlying market | "the market" / "customers" |
| dependency (on a vendor) | "needing [vendor]" / "being stuck with [vendor]" |
| signals maturity / signals market maturation | "proves real money is moving" |
| generating real revenue / generating scale revenue | "charging customers" / "making $X" |
| production workloads at scale | "actual live systems" / "real daily use" |
| enterprise customers (when stating obvious) | "big companies" (or just skip) |
| ecosystem | name the specific thing (tools, people, products) |
| paradigm shift / disruption | "this changes" + the specific change |
| leverage (verb) | "use" |
| utilize | "use" |
| seamless / seamlessly | just delete |
| revolutionary / game-changing / cutting-edge | delete. If it really is, show, don't tell |

This list is enforced by regex in `scripts/clean_text.py`. Hits trigger REVISE from council.

---

## Rule 4: The 5th-grade test

For every sentence, ask: **could a smart 16-year-old with no AI background parse this in one read?** If no, rewrite.

Quick signals it fails:
- The reader has to re-read the sentence to figure out what modifies what
- You used a word they'd have to look up (maturation, proliferate, leverage)
- The main verb is hidden 15 words into the sentence
- There's a metaphor that assumes industry knowledge (moat, stack, flywheel)

Quick signals it passes:
- You could read the sentence to a friend at dinner and they'd nod
- Every noun is either concrete (a thing you can point at) or already explained
- The verb comes early and does real work (not "is", "has", "becomes")

---

## Rule 5: Concrete-first, abstract-earned

Abstract claims must immediately follow a concrete example. Never float.

```
❌ "Infrastructure is becoming table stakes rather than competitive
    advantage." (pure abstraction, no anchor)

✅ "Cerebras just sold chips to OpenAI for $10 billion. AWS put them in
    its data centers. When everyone can buy the same chips, having them
    stops being special."
    (concrete fact → concrete fact → earned abstraction)
```

Pattern: **Fact · Fact · Claim** or **Number · Name · Rule**. The abstraction earns its place by sitting right after the proof.

If you want to open with an abstraction, fine — but the very next sentence must cash it out with a specific named thing.

---

## Rule 6: Active voice, concrete verbs

Active voice. Concrete verbs. Ban "is/are/was/were" as main verbs where possible — they're weakest-link verbs.

```
❌ "The AWS partnership is the key detail."
✅ "The AWS deal matters most."  (or: "Watch the AWS deal.")

❌ "Differentiation is moving up the stack."
✅ "Apps win now. Chips don't."

❌ "Cerebras is making the jump from private capital to public markets."
✅ "Cerebras is going public."  (or even: "Cerebras went public.")
```

---

## Rule 7: Name things

Instead of categories, name the specific company / tool / person / number. Specificity = credibility + clarity.

```
❌ "Cloud providers don't integrate new chip architectures for experimental
    workloads."

✅ "AWS doesn't plug in a new chip unless customers will pay for it."
```

The first version could be anyone. The second version tells you who, what, and why in plain words.

---

## How the skills enforce this

1. **Read this file at the start of /write-briefing and /write-posts** (both skills reference it explicitly).
2. **clean_text.py** has regex checks for the Rule 3 kill-list — hits get flagged.
3. **council/attack** runs a "plain English pass" that quotes any sentence violating Rules 1, 2, 5, 6.
4. **revise** step must fix every flagged sentence before shipping.

---

## Reference voice (match this)

From The Signal newsletter (thesignal.club):

> "Most founders think AI will write their cold emails. It won't. Not yet.
> The tech still misses context. It gets names wrong. It writes like a bot.
>
> Here's what actually works. You use AI for research. It pulls 10-K
> filings, recent press, LinkedIn activity. You use AI for outlines. It
> gives you 3 angles. Then you write the email yourself in 4 minutes.
>
> That's it. That's the playbook."

Notice: short sentences. Named things (10-K, LinkedIn). Concrete verbs (pulls, gives, write). Zero MBA vocabulary. Every claim backed by a next-sentence example.

**That's the target voice.**
