---
name: proposal-and-quote
description: "When the user wants to turn discovery notes into a proposal, SOW, or quote. Use when they mention proposal, statement of work, SOW, quote, pricing table, executive summary, assumptions, exclusions, terms, validity, expiry, signature, or 'send the paperwork'. Covers section order, pricing presentation, discount guardrails, and the signature path. For designing the price itself, see value-proposition-and-pricing. For the negotiation around the document, see objection-handling."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [value-proposition-and-pricing, objection-handling, discovery-call]
  triggers: [proposal, statement of work, SOW, quote, pricing table, executive summary, assumptions, validity, signature]
---

# Proposal and Quote

You assemble a winning proposal, statement of work (SOW), or quote from discovery
notes and the user's context. The deliverable is one document a buyer can read
top-to-bottom and sign without a follow-up call to understand it.

## Before Starting

Check `.agents/bd-context.md` first. It holds the offer, tiers, price points,
discount policy, proof points, geography, and legal constraints, so you never
re-ask what is already written. Gather only what it does not answer.

Then collect the deal-specific inputs. If any are missing, ask before writing any
section:

- **Discovery notes / MEDDPICC** from `discovery-call` — the buyer's stated problem,
  success metric, decision criteria, buying process, and timeline.
- **Signatory and influencers** — economic buyer, champion, procurement, legal.
- **The offer chosen** — which tier, how many seats or units, what term.
- **Pricing and guardrails** — from `value-proposition-and-pricing`. Never invent a
  price, a discount, or a floor here.

Never proceed on a guess for price, term, or scope. Anything the buyer has not
confirmed becomes an explicit assumption (Step 6), not a silent default.

## When to Use

- The buyer asked for numbers, a proposal, or a contract after a discovery call.
- The user says "put together a proposal", "send a quote", "write the SOW",
  "they want a pricing sheet", or "formalise what we agreed".
- A deal needs a signable document to move out of verbal agreement.

**Don't use for:** deciding what the price should be or building the ROI case
(`value-proposition-and-pricing`); handling pushback during negotiation
(`objection-handling`); capturing the discovery notes in the first place
(`discovery-call`). This skill takes those inputs and renders them into a document.

## Step 1 — Choose the vehicle

Pick one; do not send a hybrid.

| Vehicle | Use when | Shape |
|---------|----------|-------|
| **Quote** | Buyer knows what they want and asked for numbers; standard offer | Priced 1-2 pages, signable |
| **Proposal** | New logo or multiple stakeholders; buyer needs the *why* | Narrative + pricing, 4-8 pages |
| **SOW** | You deliver services or implementation; effort and change control matter | Scope, milestones, acceptance, contract terms |

Decision rule: if you will do delivery work with milestones, use a **SOW**; else if
there is more than one stakeholder or the buyer has not yet agreed on the problem
framing, use a **Proposal**; else send a **Quote**. Default to Proposal for a new
relationship — it is the only vehicle that carries the executive summary.

## Step 2 — Write in this section order

Never re-order these. Buyers and procurement scan downward; a deviation reads as
disorganised and invites questions you already answered.

1. **Cover block** — buyer name, your company, date, deal reference, validity window.
2. **Executive summary**
3. **Understanding of the need**
4. **Proposed solution — scope and deliverables**
5. **Approach and timeline**
6. **Pricing**
7. **Assumptions and exclusions**
8. **Terms**
9. **Acceptance and signature**

### Executive summary

Write it last, place it first. Half a page, three short paragraphs:

1. The buyer's problem in their own words, plus the cost of inaction.
2. What you propose — one recommended tier — and the outcome it produces.
3. The investment, the term, and the single next step.

No product tour, no company history. If the buyer cannot repeat your proposition
after reading only this section, rewrite it.

### Understanding of the need

Mirror the discovery notes back in the buyer's language. Three to six bullets:
problem, quantified impact, success criteria, constraints, decision timeline. Cite
in the CRM where each came from; if you cannot, cut it. This section is how the
buyer confirms you listened — it is also where a mis-scoped deal gets caught early.

### Scope and deliverables

A two-column table: **Deliverable** | **Definition of done**. Every row must be
verifiable — "onboard 128 clinical seats with imported rosters" beats "improve HR".
If a deliverable is a service, state the input you require from the buyer to start
it. Do not list features; list what the buyer receives.

### Approach and timeline

Phases with durations or dates, the owner of each, and the buyer's responsibilities
(what you need from them to hit the dates). Name kickoff and go-live explicitly.
Where a statutory or contractual deadline exists, anchor the timeline to it.

## Step 3 — Present the price

Rules, not options:

- **Lead with ONE recommended tier.** Show alternatives as a short comparison table,
  never a menu of equals. A menu pushes the decision back to the buyer and stalls it.
- **Show a single number per line:** tier, seats/units, term, and total contract
  value (TCV) in the buyer's currency (`bd-context` §2).
- **Separate one-off from recurring** — onboarding/setup fee is its own line, never
  buried in the monthly figure.
- **Recommend the annual-prepaid option** where the context offers a discount; it is
  the default recommendation when the buyer's cash position allows.
- **Discount guardrails.** Never go below the floor or exceed the approval threshold
  in `bd-context` §7 without written approval. Never discount without a trade — term,
  seats, prepayment, a reference, or a faster signature. Every discount row shows the
  list price, the discount, and the value returned. An unearned discount is a price
  cut that signals your number was never real.

Worked pricing table and discount-trade examples: `references/proposal-structure.md`.

## Step 4 — Assumptions and exclusions

Two numbered lists — this section is your protection against scope creep. A proposal
without it is a blank cheque.

- **Assumptions** — things you believe true that, if false, change price or scope
  (data quality, seat count, integration availability, buyer resourcing).
- **Exclusions** — what is explicitly NOT included (out-of-scope modules, travel,
  custom development, taxes, third-party licences).

Every assumption names the consequence: "Assumes clean historical payroll data;
remediation is quoted separately." That sentence is what makes the assumption useful.

## Step 5 — Validity, expiry, and terms

- **State a validity window** (default 30 days) with the exact expiry date —
  "valid until 15 November 2026", not "valid for a month". State what expiry means:
  prices subject to re-quote, seats not held. If the buyer asks to extend, re-check
  pricing against current tier rules before agreeing.
- **Terms** — keep commercial terms to one page; link the master agreement (MSA) for
  the rest. Cover: term and renewal (auto vs fixed), payment schedule (in advance?),
  late-payment/dunning path, price review at renewal, termination and notice, SLAs
  where the offer carries one, data-protection roles (controller vs processor), and
  any liability cap your standard terms set.
- **Never draft legal terms from scratch.** Pull regulated text — data-protection,
  statutory obligations, non-negotiables — from `bd-context` §2 and §12. If legal
  review is required, say so and attach the MSA rather than paraphrasing it.

Full terms checklist and sample clause language: `references/proposal-structure.md`.

## Step 6 — Build the signature path

Make acceptance frictionless and unambiguous:

- One signature block per signatory: name, title, company, date, and signature method
  (wet or e-sign).
- A single call to action: "Sign and return to proceed" plus the exact next step.
- Name the counterparty contact and expected turnaround to pre-empt procurement.
- Default to **e-signature** for speed; use wet signature only when the buyer's
  procurement requires it.
- On send, log the proposal in the CRM with stage, amount, close date, and the
  validity window so `pipeline-forecast` can count it.

## Output

One document built on `templates/proposal.md`. Fill every bracketed field; delete
any section the vehicle does not need (a Quote drops the narrative sections, a SOW
expands scope and acceptance). The output must contain, in order: cover block,
executive summary (Proposal/SOW), need, scope, timeline, pricing table, assumptions,
exclusions, terms, validity, signature block.

## Common Pitfalls

1. **Pricing before the price is designed.** Do not improvise a tier or a discount;
   pull tiers and the floor from `bd-context` §7 or run `value-proposition-and-pricing`.
2. **Executive summary written first.** It summarises the deal, so it needs the rest
   of the document drafted. Written first, it becomes a feature list.
3. **A menu of pricing tiers.** Present one recommendation; alternatives are context,
   not choices of equal weight.
4. **Discount with no trade.** Every concession buys term, seats, prepayment, proof,
   or speed — or it does not happen.
5. **No assumptions or exclusions.** The fastest route to an unprofitable delivery.
6. **Burying the price.** Buyers distrust a proposal where the number is hard to
   find; put TCV and the recommended tier where they are seen, not in an appendix.
7. **"Valid for 30 days."** Give the exact expiry date and what expiry means.
8. **Legal text invented.** Copy regulated terms from `bd-context` or attach the MSA;
   do not paraphrase law.

## Verification Checklist

- [ ] Surface check: `.agents/bd-context.md` read; only un-answered facts were asked.
- [ ] Vehicle chosen deliberately (Quote / Proposal / SOW) with the decision rule.
- [ ] Sections appear in the fixed order (Step 2).
- [ ] Executive summary can stand alone and names the cost of inaction.
- [ ] Every deliverable has a verifiable definition of done.
- [ ] One recommended tier; TCV, term, and one-off fees shown separately.
- [ ] Every discount has a trade and stays inside the guardrail in the context.
- [ ] Assumptions and exclusions are numbered and each names its consequence.
- [ ] Validity has an exact expiry date and states the effect of expiry.
- [ ] Terms reference the MSA; regulated text sourced from `bd-context`, not invented.
- [ ] Signature block names each signatory and one clear next step.
- [ ] Proposal logged in the CRM with stage, amount, close date, validity window.

## References

- `references/proposal-structure.md` — section-by-section writing detail, pricing
  table and discount-trade examples, full terms checklist and sample clauses.
- `templates/proposal.md` — the proposal/SOW/quote template to fill in.
