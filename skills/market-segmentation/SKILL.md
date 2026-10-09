---
name: market-segmentation
description: "When the user wants to define or refine their market segments, size the opportunity, or decide which segment to prioritize. Use when they mention ICP, ideal customer profile, total addressable market, TAM SAM SOM, market sizing, segment scorecard, beachhead, SWOT, Porter's Five Forces, PESTEL, BCG matrix, Ansoff, or 'who should we target first'. Coordinate messaging and pricing with value-proposition-and-pricing as you go. For competitor teardowns, see competitive-intelligence."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [bd-context, competitive-intelligence, value-proposition-and-pricing]
  triggers: [ICP, market segmentation, TAM SAM SOM, market sizing, segment scorecard, beachhead, SWOT, Porter's Five Forces, PESTEL, BCG matrix, Ansoff]
---

# Market Segmentation

You are an expert at cutting a market into segments, sizing each one honestly, and
deciding which segment earns the next dollar of go-to-market spend. You produce two
artifacts: a **segmentation memo** (the narrative and the decision) and a **segment
scorecard** (the ranked, scored evidence behind it).

## Before Starting

Read `.agents/bd-context.md` first. It already holds the lightweight ICP (section 3),
market and geography (section 2), and the core problem in the customer's own words
(section 5). Build on those; gather only what the doc does not answer. If the file is
missing, run `bd-context` first — this skill goes deep where bd-context stays
deliberately light.

Then pin down the decision this work feeds, because it changes how you size and score:

- **Entry** — should we enter segment X at all? Weight market attractiveness heavily.
- **Prioritization** — we serve several segments; which one gets the next hire or dollar?
  Weight right-to-win and access heavily.
- **Fundraising or board** — a credible TAM/SAM/SOM number. Weight defensibility of the
  sizing method.

Do not accept "size the market" as a goal. Ask what decision the number changes; if
nothing changes, you are producing a brochure, not analysis.

## When to Use

- Refining the ICP beyond the lightweight version captured in bd-context.
- Sizing an opportunity: TAM/SAM/SOM for planning, hiring, or a board/investor conversation.
- Choosing a beachhead, or deciding which segment to de-prioritize this year.
- Running a structured framework analysis: SWOT, Porter's Five Forces, PESTEL, BCG, Ansoff.
- Re-segmenting after a positioning, pricing, or product change.

**Don't use for:** a single competitor teardown, battlecard, or win/loss themes
(`competitive-intelligence`); writing the segment's messaging or setting its prices
(`value-proposition-and-pricing`); a named-account target list (`prospect-research`);
capturing the company's baseline facts (`bd-context`).

## 1. Choose one segmentation basis

Pick ONE primary axis and slice on it. Do not stack axes until you have a reason to.

- **Needs-based (recommended default).** Segment by the job the buyer is trying to do,
  the trigger that starts the search, and how they buy. This axis predicts behaviour;
  firmographics only predict where to find them.
- **Firmographic.** Industry, size, geography, business model. Use as the top-level cut
  only when the buying motion genuinely differs by industry (for example, regulated
  versus unregulated).

Combine them as descriptor + behaviour: "mid-size clinics that must file statutory
payroll every month" — not "healthcare", and not "companies that value efficiency".

Validate every candidate against the **five tests**; drop any that fails one.

| Test | Question |
|------|----------|
| Measurable | Can you count the buyers and estimate their size? |
| Substantial | Is it big enough to matter (revenue or strategic value)? |
| Accessible | Can you reach them at acceptable cost? |
| Differentiable | Do they respond to a distinct message or offer? |
| Actionable | Can you serve them with a distinct play? |

## 2. Size the market honestly

Produce TAM, SAM, and SOM. **Bottom-up is the default** — it survives scrutiny and
exposes bad assumptions. Use top-down only to sanity-check, never as the headline.

1. **TAM** — everyone who could conceivably buy this category: count of buyers x annual
   contract value.
2. **SAM** — the slice you can serve with today's product, geography, and compliance
   posture.
3. **SOM** — the realistic share you can win in 24-36 months. Tie it to a capacity model
   (reps x quota x cycle), not a percent of TAM.

Full method, worked structure, and inflation traps: see
[references/market-sizing.md](references/market-sizing.md).

State each number with its basis inline:
`SAM = 1,200 clinics x KES 840k/yr = KES 1.0B [source: KNBS registry count, client price sheet]`.
An unsourced number is a liability in a board deck.

## 3. Run the framework analysis the decision needs

Match the framework to the question; do not run all five.

| Framework | Use it when | Default? |
|-----------|-------------|----------|
| Porter's Five Forces | judging structural attractiveness of a segment | yes, for entry |
| PESTEL | macro or regulatory risk shapes entry (licensing, data law) | yes, if regulated |
| SWOT | synthesizing findings you already have | only as a summary |
| BCG matrix | allocating across an existing product or segment portfolio | no, for new segments |
| Ansoff | enumerating growth options (new vs existing product/market) | yes, for growth planning |

Full how-to, inputs, output, and the trap for each: see
[references/frameworks.md](references/frameworks.md).

## 4. Score and prioritize segments

Fill the [segment scorecard](templates/segment-scorecard.md). Score each segment 1-5 on
seven criteria, apply the weights, and rank. The defaults below suit a **prioritization**
decision; adjust for entry or fundraising per section 1 and say so in the memo.

| Criterion | Weight | What a 5 looks like |
|-----------|--------|---------------------|
| Segment size (SAM) | 20% | Clears your revenue bar on its own |
| Growth rate | 15% | Growing faster than the category |
| Right-to-win | 20% | Existing proof, references, or product fit |
| Access | 15% | Reachable via a channel you already run |
| Willingness to pay | 15% | Will pay list price; pain is quantified |
| Competitive intensity | 10% | Few credible alternatives; low switching cost |
| Cost to serve | 5% | Onboarding and support fit your model |

Decision rules:

- **Beachhead** = highest weighted score with right-to-win at least 4. A large segment you
  cannot win is not a beachhead.
- **Invest** = top two scores; fund both.
- **Watch** = mid-field; revisit next planning cycle.
- **Deprioritize** = bottom of the ranking; write down why so the decision is not relitigated.

Always name the segment you are saying no to and why. A ranking with no explicit reject is
a wish list.

## Output

Deliver the **segmentation memo** (in chat or a file under `.agents/`) plus the filled
scorecard. Memo skeleton:

```markdown
# Segmentation Memo — <Company>  (<YYYY-MM>)
Decision: <entry | prioritization | fundraising>

## Recommendation
<One paragraph: the beachhead segment, the runner-up, and the number that justifies it.>

## Segments considered
| Segment | SAM | Weighted score | Rank | Verdict |

## Sizing
TAM / SAM / SOM, each with basis and source. Assumptions marked [ASSUMPTION].

## Framework findings
<Only the frameworks run, one short block each.>

## Risks and disconfirming evidence
<What would change this decision; what evidence is missing.>

## Next steps
<Owner + date for the 2-3 actions this unlocks.>
```

The scorecard lives in `templates/segment-scorecard.md`; copy it, fill it, and link it
from the memo.

## Common Pitfalls

1. **Sizing before deciding.** A TAM is not an output; it is an input to a decision. Ask
   what the number changes before you compute it.
2. **Top-down TAM as the headline.** "1% of a $50B market" is a pitch, not analysis. Build
   bottom-up; use top-down only to check the bottom-up figure.
3. **Selling to the biggest segment instead of the winnable one.** Size and right-to-win
   are different axes. The beachhead rule exists because the largest segment is often
   where you have no proof.
4. **Firmographics dressed up as a strategy.** "Healthcare" is a list, not a segment. Add
   the trigger, the job, and the buying behaviour.
5. **Unsourced numbers.** Every market figure needs a basis and a source. Mark inferences
   `[ASSUMPTION]`.
6. **No explicit reject.** If nothing was cut, nothing was decided.
7. **Running every framework.** Frameworks cost pages and tokens. Run only the ones the
   decision needs; a framework that changes nothing should not be in the memo.

## Verification Checklist

- [ ] One primary segmentation basis chosen and defensible.
- [ ] Every candidate segment passes all five tests (or is documented as failing one).
- [ ] TAM/SAM/SOM built bottom-up, each with a stated basis and source.
- [ ] Only decision-relevant frameworks run; each feeds a finding in the memo.
- [ ] Scorecard filled with 1-5 scores, weights applied, ranked.
- [ ] Beachhead named, runner-up named, and at least one segment explicitly rejected with a reason.
- [ ] Assumptions and missing evidence marked.
- [ ] Next steps carry an owner and a date.

## References

- [Market sizing method](references/market-sizing.md) — the bottom-up TAM/SAM/SOM build and its traps.
- [Framework how-tos](references/frameworks.md) — Porter, PESTEL, SWOT, BCG, Ansoff.
- [Segment scorecard](templates/segment-scorecard.md) — the scored ranking artifact to fill in.
