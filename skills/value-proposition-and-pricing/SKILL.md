---
name: value-proposition-and-pricing
description: "When the user wants to sharpen their positioning and messaging, build a quantified business case, or design packaging and pricing. Use when they mention value proposition, positioning statement, messaging, ROI calculator, cost of inaction, business case, pricing tiers, price metric, discount policy, packaging, willingness to pay, or monetization. Coordinate competitor pricing facts with competitive-intelligence as you go. For the per-deal quote or proposal, see proposal-and-quote."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [bd-context, market-segmentation, competitive-intelligence, proposal-and-quote, objection-handling]
  triggers: [value proposition, positioning, messaging, ROI, cost of inaction, business case, pricing tiers, price metric, discount policy, packaging, willingness to pay]
---

# Value Proposition And Pricing

You are an expert at sharpening positioning and messaging, building a quantified business
case, and designing packaging and pricing. You produce a **positioning and messaging
brief**, a **quantified ROI / cost-of-inaction business case**, and a **packaging and
pricing recommendation**.

## Before Starting

Read `.agents/bd-context.md` first — section 6 (value propositions and differentiators),
section 7 (offer, packaging, pricing), and section 5 (problems and pain) already hold the raw
material. Sharpen what is there; gather only what is missing. If pricing or positioning has
changed, flag the version bump that bd-context needs.

Confirm the scope, because each changes the artifact:

- Sharpening messaging for a campaign or a persona.
- Building a business case for one deal, or for a whole segment.
- Redesigning the price list, packaging, or discount policy.

## When to Use

- Rewriting positioning or messaging so it lands with a specific persona.
- Building a quantified ROI or cost-of-inaction business case for a segment or a deal.
- Designing or revising tier structure, price metric, packaging, or discount policy.
- Preparing willingness-to-pay evidence before a price change.

**Don't use for:** the per-deal quote, proposal, or SOW (`proposal-and-quote`); reactive
rebuttals to a specific objection (`objection-handling`); deciding which segment to serve
(`market-segmentation`); competitor teardowns (`competitive-intelligence`).

## 1. Sharpen positioning and messaging

1. Write the positioning statement in the fixed form: *For [priority persona] who
   [situation or job], we are the [category] that [key capability], so they can [outcome],
   unlike [alternative].* The category and the alternative words do most of the work — get
   those right first.
2. Turn it into a message hierarchy: one headline claim, three supporting proof points, one
   call to action. Each proof point carries a metric or a named mechanism, never an adjective.
3. Write one version per buying-committee persona (bd-context section 4), because the
   economic buyer and the user care about different outcomes.
4. Test every claim against the "so what / says who" bar: it either quantifies an outcome or
   names a source. Cut anything that fails.

Statement formula and message testing: see
[references/positioning-messaging.md](references/positioning-messaging.md).

## 2. Quantify the value (ROI / cost of inaction)

Build the business case in three layers, all in money:

1. **Cost of the status quo** — hours x loaded rate, error or penalty costs, revenue leaked,
   churn. This is usually the strongest number; lead with it.
2. **Value created** — the delta the product produces, measured against the client's baseline,
   not against zero.
3. **Payback and ROI** — net benefit versus price, with a payback period.

Use the [ROI business-case calculator outline](templates/roi-business-case.md). Rules:

- Every input is either **client-supplied** (mark `[CLIENT]`) or **your assumption** (mark
  `[ASSUMPTION]`) with a source or a range. Never present a modeled number as a measured one.
- Show a **conservative, base, and aggressive** case. Lead with conservative.
- Compute bottom-up from the client's own volumes; show the arithmetic.

## 3. Choose the price metric and tier structure

Default to **value-based pricing** with a **price metric tied to value** (per seat, per usage,
or a hybrid). Cost-plus and competitor-matching are fallbacks, not defaults — they anchor you
below value and hand the model to a rival.

1. Pick the **price metric** — the unit you charge by. It must scale with the value the client
   gets and be easy to count and predict.
2. Design **good-better-best tiers** fenced by capabilities the buyer naturally groups as
   needs, not by arbitrary feature shaving.
3. Set the **floor price** and the **guardrails** (when to walk), consistent with bd-context
   section 7.
4. State the discount policy explicitly: what is discountable, what is traded for it (term
   length, prepayment, case study, volume), and who approves.

Method detail — price metrics, tier fences, and the traps: see
[references/pricing-methods.md](references/pricing-methods.md).

## 4. Set and validate willingness to pay

Never set a price without evidence. Weakest to strongest signal:

1. **Win/loss and churn analysis** — did price actually cause the loss, or was it something
   else? Ask the buyer directly.
2. **Competitor anchors** — what the alternative costs (coordinate with `competitive-intelligence`).
3. **Customer interviews** — direct willingness-to-pay questions across a range of prices.
4. **Structured surveys** — Van Westendorp or Gabor-Granger for a defensible range.

Record the evidence behind the chosen price in the business case. If there is none, say the
price is a hypothesis and mark it `[ASSUMPTION]`.

## Output

Three artifacts (deliver in chat or as files under `.agents/`):

- **Positioning and messaging brief** — statement, message hierarchy, per-persona variants.
- **ROI business case** — the filled [calculator outline](templates/roi-business-case.md),
  with assumptions marked and a sensitivity note.
- **Packaging and pricing recommendation** — metric, tiers, price points, discount policy,
  and the WTP evidence, in this skeleton:

```markdown
# Pricing Recommendation — <Company>  (<YYYY-MM>)
## Recommendation
<metric, tier count, headline price, one-line why>
## Tiers
| Tier | Price | Metric | For | What fences it |
## Discount policy
<what is discountable, what is traded, approval matrix>
## Willingness-to-pay evidence
<one source per data point; untested prices marked [ASSUMPTION]>
## Risks
<what would make us re-price; elasticity exposure>
```

## Common Pitfalls

1. **Pricing before positioning.** You cannot price a value the buyer does not perceive.
   Sharpen the message first.
2. **Cost-plus or "match the competitor" by default.** Both anchor you below value. Default to
   value-based pricing with a usage metric.
3. **Top-down ROI.** "Save 30%" with no baseline is not a business case. Build from the
   client's own volumes.
4. **Hiding assumptions.** Mark `[CLIENT]` versus `[ASSUMPTION]`; a mixed-up number gets
   quoted back at you in a negotiation.
5. **Feature-shaving tiers.** Fence on what buyers naturally segment by; arbitrary fences
   invite a negotiation on every line.
6. **An unstated discount policy.** Ad-hoc discounts are a pricing decision made by whoever is
   on the call. Write the policy and the trade up front.
7. **Setting price with no WTP evidence.** Label an untested price a hypothesis, not a fact.

## Verification Checklist

- [ ] Positioning statement follows the for/who/we-category/so/unlike form.
- [ ] Message hierarchy has one claim, three proof points, one CTA; each proof carries a metric or source.
- [ ] ROI built bottom-up; every input marked `[CLIENT]` or `[ASSUMPTION]`.
- [ ] Conservative, base, and aggressive cases shown; conservative leads.
- [ ] Price metric chosen and tied to value; the value-based rationale stated.
- [ ] Tiers fenced on buyer-natural groupings; floor price and guardrails set.
- [ ] Discount policy states what is discountable and what is traded for it.
- [ ] WTP evidence recorded, or the price explicitly labelled a hypothesis.

## References

- [Positioning and messaging](references/positioning-messaging.md) — the statement formula and message testing.
- [Pricing methods](references/pricing-methods.md) — value-based pricing, metrics, tier fences, WTP research.
- [ROI business-case calculator outline](templates/roi-business-case.md) — the quantified business case to fill in.
