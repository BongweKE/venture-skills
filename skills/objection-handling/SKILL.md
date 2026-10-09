---
name: objection-handling
description: "When the user wants to answer a sales objection or plan a negotiation. Use when they mention objection, pushback, 'too expensive', 'not now', 'we're happy with what we have', 'talk to my boss', competitor, discount, BATNA, ZOPA, concession, closing, or 'they went quiet'. Builds a reusable objection library and a negotiation plan with concession guardrails. For controlled rebuttals rooted in positioning, see value-proposition-and-pricing. For the document that formalises agreed terms, see proposal-and-quote."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [value-proposition-and-pricing, proposal-and-quote, discovery-call]
  triggers: [objection, pushback, too expensive, not now, BATNA, ZOPA, concession, discount, negotiation, closing]
---

# Objection Handling

You turn objections into a reusable library and turn a deal into a negotiated
agreement. The deliverable is an objection library the team can rehearse and a
negotiation plan that names the walk-away, the trade space, and the close.

## Before Starting

Check `.agents/bd-context.md` first. It holds the value propositions, proof points,
personas and their likely objections, tiers, discount policy, and the floor price —
so you build responses from the user's real positioning, not generic scripts. Gather
only what it does not answer, then confirm the objection actually heard from the
buyer, in their words, from `discovery-call` or the call notes.

If the same objection recurs across deals, it is a positioning problem, not a
tactics problem — route the underlying message to `value-proposition-and-pricing`.

## When to Use

- A buyer raised pushback — price, timing, status quo, authority, trust, or a
  competitor — and the user needs a response.
- The user is preparing to negotiate and wants a plan: walk-away, trade space,
  concessions, close.
- The team wants a library of reusable objections and responses.

**Don't use for:** designing or repositioning the offer's messaging
(`value-proposition-and-pricing`); writing the document that captures the final
terms (`proposal-and-quote`); capturing objections during discovery
(`discovery-call`). This skill handles the moment of resistance and the negotiation
around it.

## Step 1 — Classify the objection

Every objection belongs to one of six families. Classify first; the family determines
the response strategy. Misclassifying is the most common failure — a "price"
objection is often really "value" or "authority".

| Family | Sounds like | What it usually means | Default move |
|--------|-------------|-----------------------|--------------|
| **Price** | "Too expensive", "over budget" | Value not yet believed, or no budget authority | Re-anchor on cost of the problem; reframe to cost per outcome |
| **Timing** | "Not now", "next quarter" | No compelling event, or a competing priority | Quantify the cost of waiting; tie to their deadline |
| **Status quo** | "We're fine as we are" | Switching cost appears higher than the pain | Make the cost of the current state concrete and visible |
| **Authority** | "I need to check with X", "not my call" | Not talking to the economic buyer, or a stall | Ask who decides and how; request a joint call |
| **Trust** | "How do we know this works?" | No proof, no reference, no risk transfer | Offer proof, a pilot, a guarantee, or a reference |
| **Competition** | "We're also looking at [X]" | A comparison is being run; you are not the default | Reframe the evaluation criteria, not the competitor |

Rule: **never answer a price objection with a discount.** Diagnose first (Steps 2-3);
the discount is Step 6, and only against a trade.

## Step 2 — Build the library entry

Each objection becomes one entry with a fixed shape. Consistency is what makes the
library rehearseable. Use `templates/objection-library.md`.

For every entry capture:

1. **Objection (verbatim)** — the buyer's own words.
2. **True meaning** — the family and the underlying concern from Step 1.
3. **Acknowledge** — one sentence that shows you heard it; do not argue yet.
4. **Reframe** — shift from your cost to their outcome or the cost of inaction.
5. **Proof** — the specific evidence: metric, reference, guarantee, or pilot. Cite
   the source; never invent a reference (`bd-context` §11).
6. **Question close** — end with a question that advances, not a defensive statement.
7. **Source** — where the objection was heard (deal, call, date).

Acknowledge then reframe then prove then ask is the default order. It de-escalates
before it persuades, and it ends by returning control of the next step to the buyer.

## Step 3 — Diagnose before responding

Ask the one clarifying question that reveals the real objection:

- Price: "Is it the total, or how you would fund it?" (budget vs value vs authority)
- Timing: "What changes next quarter that makes it easier to decide?"
- Status quo: "What is the current process costing you per month?"
- Authority: "Who else needs to be comfortable, and what will convince them?"
- Trust: "What proof would make this an easy yes?"
- Competition: "What two or three things are you comparing on?"

Record the answer in the library entry. An objection you cannot diagnose is an
objection you cannot answer.

## Step 4 — Plan the negotiation: BATNA and ZOPA

Do this before the negotiation call, not during it.

- **Your BATNA** — your best alternative if this deal fails. Name it concretely
  (another deal, a smaller scope, walking). A weak BATNA is why teams over-discount;
  knowing the walk-away protects the floor.
- **Their likely BATNA** — what they do if you hold firm (competitor, do nothing,
  build in-house). Their BATNA sets the ceiling on what they will pay.
- **Walk-away** — the minimum acceptable terms (price floor, term, scope). Pull the
  floor from `bd-context` §7; never negotiate below it without written approval.
- **ZOPA** — the zone of possible agreement: the overlap between your walk-away and
  their maximum. If there is no overlap, the deal is not ready — change scope, term,
  or timing rather than price.

Record BATNA, walk-away, and the estimated ZOPA in the negotiation plan.

## Step 5 — Build the concession ladder

Plan concessions as a ladder, not as reactions. Each rung gives something and asks
for something of equal or greater value in return.

| Rung | You give (least costly first) | You ask for |
|------|-------------------------------|-------------|
| 1 | Faster timeline, dedicated onboarding slot | Signature within a set date |
| 2 | Extended validity, added seats at list price | Named reference or case-study permission |
| 3 | Waived onboarding / setup fee | Annual prepayment |
| 4 | Multi-year price lock | Multi-year commitment |
| 5 | Per-seat discount (within guardrails) | More seats, longer term, or both |
| 6 | Below-floor price | Escalation to leadership and a major trade |

Rules: concede in decreasing increments (a big first move then small moves signals
your floor); never concede twice without a counter-ask; never open with your best
offer. Detail and worked examples: `references/negotiation-playbook.md`.

## Step 6 — Close

Match the close to the deal's readiness:

- **Value accepted, price resists** — trade, do not cut (Step 5).
- **Silent after a proposal ("went quiet")** — send a dated nudge tied to the
  validity window, with one easy yes/no question.
- **Authority missing** — ask for the joint call with the economic buyer; do not let
  the champion relay your case second-hand.
- **Timing** — agree a mutual action plan with dated steps and a booked next meeting;
  a "next quarter" with no date is a no.

Always exit a negotiation with the next step and its owner written down.

## Output

Two artifacts:

- **Objection library** — one file per recurring objection or a single grouped file,
  built on `templates/objection-library.md`, using the seven-field entry shape above.
- **Negotiation plan** — BATNA (yours and theirs), walk-away terms, estimated ZOPA,
  the concession ladder, the intended close, and the discount guardrail in force.

## Common Pitfalls

1. **Answering price with a discount.** The fastest way to teach a buyer that your
   first number was fiction. Diagnose, then trade.
2. **Reframing before acknowledging.** Leading with the rebuttal reads as defensive
   and hardens the buyer.
3. **Inventing a proof point.** A fabricated reference or metric destroys trust the
   moment it is checked. Use `bd-context` §11 or state plainly that none exists.
4. **No BATNA.** Without a walk-away you cannot hold the floor, and every concession
   feels necessary.
5. **Conceding without a counter-ask.** A free concession trains the buyer to ask for
   more; every rung buys something.
6. **Mistaking the family.** Treating an authority objection as a price objection
   leads to a discount that never closes the deal.
7. **"Next quarter" with no date.** An undated deferral is a polite no; agree a dated
   mutual action plan or qualify it out.
8. **A one-off library.** Capture each objection as it is heard, with its source, so
   the library compounds instead of being rebuilt per deal.

## Verification Checklist

- [ ] Objection classified into one of the six families, with the diagnosis recorded.
- [ ] Every entry has all seven fields; proof points sourced, none invented.
- [ ] Responses use acknowledge, reframe, prove, ask — not a rebuttal first.
- [ ] BATNA (yours and theirs), walk-away, and ZOPA documented before the call.
- [ ] Concession ladder ordered; each rung trades; increments decrease.
- [ ] Discount floor from `bd-context` §7 respected; below-floor needs approval.
- [ ] Close matched to deal readiness; a dated next step with an owner.
- [ ] Recurring objections offered to `value-proposition-and-pricing` as a message fix.

## References

- `references/negotiation-playbook.md` — BATNA/ZOPA theory, concession strategy,
  a worked negotiation example, and closing tactics.
- `templates/objection-library.md` — the seven-field objection library template.
