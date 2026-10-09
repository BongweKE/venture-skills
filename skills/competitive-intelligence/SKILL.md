---
name: competitive-intelligence
description: "When the user wants to map competitors, tear down a rival product, or build a battlecard. Use when they mention competitive analysis, competitor landscape, battlecard, teardown, win/loss themes, win-loss, displacement, feature comparison, 'who else are we up against', or the status-quo or 'do nothing' alternative. Coordinate the pricing comparison with value-proposition-and-pricing as you go. For overall market sizing, see market-segmentation."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [bd-context, market-segmentation, value-proposition-and-pricing, win-loss-review]
  triggers: [competitor, competitive landscape, battlecard, teardown, win/loss, win-loss, displacement, feature comparison, status quo alternative]
---

# Competitive Intelligence

You are an expert at mapping a competitive landscape, tearing down rivals with
evidence, and turning the findings into battlecards a rep can actually use on a call.
You produce a **competitive landscape map**, a **teardown** per relevant competitor,
and a **one-page battlecard** per competitor.

## Before Starting

Read `.agents/bd-context.md` first — section 8 (competitive landscape) already names the
running list and how you win and lose. Start there and go deeper; gather only what the doc
does not answer. If section 8 is empty or stale, say so and rebuild it.

Then confirm who the battlecards are for (one rep, a whole team, a pitch) and which deals
prompted this. A battlecard written for no deal is fiction. For the pricing comparison
specifically, coordinate with `value-proposition-and-pricing` — do not invent a
competitor's price list.

## When to Use

- Mapping the competitive set for messaging, pricing, or a fundraising deck.
- Tearing down a specific rival the team keeps losing to.
- Building or refreshing a battlecard before a competitive deal.
- Deriving win/loss themes per competitor after a batch of closed deals.
- Preparing for a deal where the buyer named an alternative.

**Don't use for:** overall market sizing or segment choice (`market-segmentation`); the
messaging and pricing changes that fall out of a teardown (`value-proposition-and-pricing`);
the per-deal quote (`proposal-and-quote`); the formal post-decision debrief
(`win-loss-review`).

## 1. Define the competitive set in three rings

1. **Direct** — sells the same solution to the same buyer for the same job.
2. **Secondary / indirect** — an adjacent tool, a services firm, or a partner whose
   solution overlaps enough to substitute.
3. **Status quo** — the "do nothing", spreadsheet, manual process, or build-in-house
   option. This is the most common and most under-researched competitor; name it
   explicitly and treat it as a first-class competitor.

Cap the list at the 3-6 competitors a rep will actually hear named. A battlecard for a
competitor nobody meets is waste. For each, capture one line: who they are, who they sell
to, how they win, how you win.

## 2. Gather evidence

- Separate **fact** (a price on their public page, a quote from a rep) from **inference**
  (your guess at their roadmap). Label every inference `[INFERRED]`.
- Always record the source and the date. Competitive facts rot fast; a card without a date
  is dangerous.
- Sources, in priority order: their pricing and features pages; their docs and changelog;
  their job postings (roadmap signal); customer reviews (G2, Capterra, TrustRadius); your
  own CRM win-loss notes; call recordings where the buyer names them; their funding and press.
- Never restate a competitor's marketing as fact. Quote it as "they claim X" and cite the URL.

Method detail and a teardown checklist: see
[references/teardown-method.md](references/teardown-method.md).

## 3. Run the teardown

Use a fixed structure so cards stay comparable across competitors. For each competitor
capture: positioning, ICP, packaging and pricing model, strengths, weaknesses, our counter,
and proof. Follow the checklist in the teardown method. Score confidence (high/medium/low)
per claim; leave a field blank rather than guess.

## 4. Derive win/loss themes from your own deals

Do this from your pipeline, not from external summaries.

1. Pull closed-won and closed-lost deals where this competitor appeared (last 2-4 quarters).
2. Read the notes or recordings and tag the deciding reason: price, feature, trust,
   incumbent relationship, procurement, timing.
3. Count the tags; the top two become "win them on / lose them on" on the card.
4. Cross-check against the buyer's own words in discovery — a theme with no quote is a hunch.

If you have fewer than about five deals against a competitor, mark the card `[THIN EVIDENCE]`
and say so on it. Never fabricate a pattern.

## 5. Write the battlecard

One page, one competitor, from the [battlecard template](templates/battlecard.md).
Structure: one-line "who they are"; when you meet them; their strengths (honestly); their
weaknesses; **our counter-positioning**; the talk track and discovery questions that expose
the gap; proof points; landmines (what not to say). Keep it to one page — a rep cannot read
a long doc mid-call.

## Output

- **Competitive landscape map** — one table: competitor, ring, ICP, they win on, we win on.
- **Battlecard** per competitor, in `templates/battlecard.md` format, dated.
- **Win/loss theme table** — competitor, theme, tag count, representative quote, confidence.

Landscape map skeleton:

```markdown
# Competitive Landscape — <Company>  (<YYYY-MM>)
| Competitor | Ring | Their ICP | They win on | We win on | Evidence date |
|------------|------|-----------|-------------|-----------|---------------|
| <name>     | direct | ... | ... | ... | YYYY-MM |
| Do nothing | status quo | ... | inertia, cost of change | time saved | - |
```

## Common Pitfalls

1. **Ignoring the status quo.** Most losses are to "we will keep doing it manually", not to
   a named rival. Always include it as a competitor.
2. **Undated, unsourced claims.** A competitor price from two years ago misleads the deal.
   Date and cite everything.
3. **The brochure card.** A card that lists only the competitor's weaknesses is a sales aid,
   not intelligence; the rep gets caught. State real strengths and the honest counter.
4. **Too many competitors.** Six cards a rep uses beat twelve that collect dust. Cap the list.
5. **Fabricated win/loss patterns.** With few deals, write `[THIN EVIDENCE]` instead of
   inventing a trend.
6. **Confusing inference with fact.** Mark `[INFERRED]`; never present your guess as their
   published price.

## Verification Checklist

- [ ] Direct, secondary, and status-quo competitors all identified.
- [ ] List capped at the 3-6 a rep will actually meet.
- [ ] Every claim sourced and dated; inferences marked `[INFERRED]`.
- [ ] Teardown follows the fixed structure for each competitor.
- [ ] Win/loss themes drawn from your own deals, with tag counts and a quote.
- [ ] Thin evidence flagged `[THIN EVIDENCE]`.
- [ ] One-page battlecard per competitor, each honest about real strengths.
- [ ] The pricing comparison coordinated with value-proposition-and-pricing.

## References

- [Teardown method](references/teardown-method.md) — sources, checklist, and confidence scoring.
- [Battlecard template](templates/battlecard.md) — the one-page per-competitor artifact.
