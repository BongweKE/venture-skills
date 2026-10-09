---
name: qbr-and-renewal
description: "When the user wants to prepare a quarterly business review or drive a renewal, expansion, or save. Use when they mention \"QBR\", \"quarterly business review\", \"business review\", \"renewal\", \"renewal plan\", \"churn risk\", \"health score\", \"save play\", \"upsell timing\", \"expansion conversation\", or \"net revenue retention\". For account strategy, see account-planning. For the papering of a renewal deal, see proposal-and-quote. For pipeline mechanics, see pipeline-forecast."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [account-planning, proposal-and-quote, pipeline-forecast]
  triggers: [QBR, quarterly business review, business review, renewal, churn risk, health score, save play, upsell timing, net revenue retention]
---

# QBR and Renewal

You are an expert at running a quarterly business review that proves value, then converting that proof into a renewal and expansion plan. The output is a QBR deck built from a fixed outline and `<account>-renewal-plan.md` covering health, churn risk, save plays, expansion timing, and the pricing conversation.

## Before Starting

Read `.agents/bd-context.md` first (value props, pricing and discount policy, personas, sales stages, constraints). Only gather what it does not answer.

Then pull, and source, the evidence the QBR needs:

1. Adoption and usage since the last review (active seats, feature depth, usage trend).
2. Outcome metrics the customer cares about (hours saved, error rate, cycle time, cost, risk avoided).
3. Support ticket and escalation history, with its trend.
4. Invoice and payment history (on-time, disputes).
5. The contract: term, renewal date, notice period, price, any uplift or indexation clause.
6. The last QBR's commitments from both sides.

Rule: never show a metric you cannot trace to an export. A wrong number in a QBR costs more trust than an omitted one. Label projections `[ASSUMPTION]`.

## When to Use

- Preparing a quarterly business review for an existing customer.
- Health-scoring an account and deciding renew, expand, or save.
- A renewal is inside its notice window and needs a plan.
- Building a save play for an at-risk account.

**Don't use for:** the account's overall strategy — that is `account-planning`. Papering the renewal deal itself (quote, SOW, order form) — that is `proposal-and-quote`. Pipeline mechanics and forecast — that is `pipeline-forecast`.

## Step 1 — Decide the cadence and format

Match effort to tier: strategic accounts get a formally presented QBR each quarter with the executive sponsor present; growth accounts get a written review each half-year plus a call; watch accounts get a check-in only when a risk signal fires. If there is nothing new to say, send a written update instead of holding a meeting — a hollow QBR signals you have nothing and invites churn.

## Step 2 — Score account health

Score five inputs 0-2 and sum to a 0-10 health score:

| Input | 0 | 1 | 2 |
|---|---|---|---|
| Adoption (active/licensed seats) | < 50% | 50-80% | > 80% |
| Executive engagement (sponsor contact in 90 days) | none | indirect | direct |
| Support (escalations and trend) | open P1s or rising | stable | resolved and falling |
| Commercial (payment, renewal clarity) | late or disputed | on time | on time, multi-year |
| Value proof (outcomes documented) | none | partial | quantified |

Decision rule: 8-10 = expand; 5-7 = defend and fix the weakest input; 0-4 = save play and escalate to `account-planning`. The score sets the purpose of the QBR before you build the deck. Always compare to the prior period — the trend matters more than the point.

## Step 3 — Build the value-realized story

Lead with the customer's outcomes, not your features. For each value prop from context, show a before and after with a sourced number and the customer's own words:

| Outcome | Baseline | Now | Source | Customer quote |
|---|---|---|---|---|
| | | | | |

If a metric has no baseline, establish one now so next quarter has a comparison. If the customer disputes a number, drop it — a contested metric loses the room.

## Step 4 — Build the agenda and talk track

Use [templates/qbr-deck-outline.md](templates/qbr-deck-outline.md). Sections in order: (1) purpose and agenda, (2) value realized since last QBR, (3) their goals and what changed, (4) roadmap and the commitments we owe, (5) the ask — renewal, expansion, or referral, (6) next steps and owners. Default split: the customer talks for at least half the time. End every section with an agreed next step.

## Step 5 — Read churn-risk signals

Score the signals in [references/churn-signals.md](references/churn-signals.md) and classify the account green / amber / red. A red signal overrides a healthy score — a champion leaving or a usage collapse matters more than a good metric. Record every signal with its date and source.

## Step 6 — Choose the save play

For amber and red accounts, pick one primary save play before the QBR and one fallback:

- **Executive reset** — sponsor changed or went quiet: rebuild the sponsor relationship.
- **Adoption rescue** — low usage: ship training plus one workflow win within 30 days.
- **Value gap** — outcomes not landing: re-baseline and re-scope what success means.
- **Commercial relief** — budget or price pressure: restructure term or packaging, never cut price without reducing scope.

Each play names the owner, the 30-day action, and the success signal that says it worked.

## Step 7 — Time the expansion and price the renewal

Expansion timing rule: pitch expansion in the QBR *after* a documented win, and only when health is 8 or above. Pitching expansion on a low-adoption account reads as upselling and accelerates churn.

Renewal pricing, in order:

1. Anchor on realized value and the agreed success metrics.
2. Apply the context's standard renewal uplift or indexation clause if one exists.
3. If the customer pushes on price, trade rather than discount: add term, add seats, or change packaging. Get the discount policy and approval threshold from context before the call.
4. Prefer a multi-year commitment in exchange for a locked rate.

If the renewal needs a formal quote or order form, stop and route to `proposal-and-quote`.

## Output

Two artifacts:

1. A QBR deck built from [templates/qbr-deck-outline.md](templates/qbr-deck-outline.md).
2. `<account>-renewal-plan.md` from [templates/renewal-plan.md](templates/renewal-plan.md): health score, churn signals, chosen save play, expansion timing, renewal terms, and the pricing position with a walk-away.

## Common Pitfalls

1. **A features deck instead of a value deck.** Buyers renew outcomes, not capabilities. Lead with their numbers.
2. **Unsourced or invented metrics.** One wrong figure costs the meeting. Source every number or omit it.
3. **A health score with no trend.** A single point-in-time score hides a falling account; always compare to the prior period.
4. **Upselling a sick account.** Pitching expansion at healthy adoption but low usage accelerates churn. Fix adoption first.
5. **Discounting on the first push.** Trade terms before price; a reflex discount trains the buyer to push every cycle.
6. **Letting the renewal window close.** Start the renewal plan at least one notice period plus 30 days before term end.
7. **No joint next steps.** A QBR that ends without owners and dates has no follow-through. Close every section with them.

## Verification Checklist

- [ ] Cadence matched to tier; a hollow meeting replaced with a written update.
- [ ] Health score computed from the five inputs with a prior-period comparison.
- [ ] Every value-realized metric is sourced or labelled `[ASSUMPTION]`; the customer's words are quoted.
- [ ] Deck follows the six sections and ends each with an owner and date.
- [ ] Churn signals scored from the reference; account classified green/amber/red.
- [ ] One primary save play chosen for amber/red accounts, with owner and 30-day action.
- [ ] Expansion pitched only after a documented win at healthy adoption.
- [ ] Renewal pricing has a value anchor, a trade-first policy, and a walk-away; formal quoting routed to `proposal-and-quote`.

## References

- [Churn-risk signals](references/churn-signals.md)
- [QBR deck outline](templates/qbr-deck-outline.md)
- [Renewal plan template](templates/renewal-plan.md)
