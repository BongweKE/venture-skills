# Proposal structure, pricing, and terms — detail

Reference for `proposal-and-quote`. Load when writing the document; the table of
contents and quick rules live in `SKILL.md`.

## 1. Section-by-section writing guide

### Cover block
Include: buyer company, the recipient's name and title, your company and contact,
date issued, a deal reference (so procurement can file it), and the validity window
with the exact expiry date. One block, no logo wall.

### Executive summary (Proposal and SOW; optional for Quote)
- 150-250 words. Three paragraphs: problem, proposal, investment + next step.
- Quantify the cost of inaction using the buyer's own numbers from discovery.
- Name the outcome, not the product. "Payroll filed correctly by the 9th" beats
  "automated statutory engine".
- The test: read only this section; the buyer should be able to forward it to their
  boss and have it make sense.

### Understanding of the need
Pros of mirroring the discovery language verbatim: it proves you listened and it
makes the buyer correct you early if you misheard. Structure as five labelled lines:
- **Problem** — one sentence.
- **Impact** — quantified, with the source (a number the buyer gave or a metric).
- **Success criteria** — how the buyer will judge this worked.
- **Constraints** — compliance, budget, timeline, integrations.
- **Timeline** — the buyer's decision and go-live dates.

### Scope and deliverables
Two columns: Deliverable | Definition of done. Rules:
- One outcome per row; group rows by phase if there are more than eight.
- "Definition of done" must be observable by a third party.
- State buyer dependencies inline ("requires roster export by week 1").
- Put anything ambiguous in Exclusions, not here.

### Approach and timeline
- Phase | Duration/Date | Owner | Buyer responsibility.
- Call out kickoff and go-live.
- Anchor to a real deadline when one exists (statutory filing date, contract renewal,
  funding milestone).

## 2. Pricing table and discount trades

### Worked recommended-tier table

```markdown
## Investment

| Item | Detail | Amount |
|------|--------|--------|
| Roster tier | 128 active seats x KES 700/month | KES 89,600 / month |
| Onboarding | One-off, data migration | KES 25,000 (waived on annual prepay) |
| **Total contract value** | 12 months, annual prepaid | **KES 1,100,200** |

Recommended: annual prepay waives the onboarding fee and applies the 10% annual
discount. Month-to-month is available at list price with the onboarding fee payable.
```

Rules that make a pricing table credible:
1. One number per row; no merged cells hiding arithmetic.
2. Show list price and any discount as separate rows so the value is visible.
3. State the currency and whether tax is included.
4. No more than three tiers in a comparison — beyond that the buyer defers.

### Discount trade examples

| Buyer asks for | Grant only if they return |
|----------------|---------------------------|
| Lower per-seat price | Longer term (annual prepay) or more seats |
| Waived onboarding | Faster signature or a named reference |
| Multi-year price lock | 2-3 year commitment signed now |
| Budget-cap accommodation | Scope reduction, not price reduction |

Never: a discount with nothing returned, a price below the `bd-context` §7 floor, or
a verbal discount the document does not reflect.

## 3. Terms checklist

Cover each of these or state explicitly that it is in the linked MSA:

- **Term and renewal** — fixed term vs auto-renew; notice period.
- **Payment** — schedule (in advance / on signature / milestone), method, currency.
- **Late payment** — interest or dunning steps and the escalation path.
- **Price review** — when and how prices may change at renewal.
- **Termination** — for cause vs convenience; notice; what is owed on exit.
- **SLA** — response/resolution targets, credits, if the offer carries a service level.
- **Data protection** — which party is controller vs processor; where data lives;
  export/portability and deletion obligations at exit.
- **Confidentiality** — or reference the MSA clause.
- **Liability** — cap and exclusions, copied from standard terms; do not invent.
- **Governing law and jurisdiction.**

Sample framing sentence for validity:

> This proposal is valid until <date>. Prices and seat availability are not held
> after that date; a re-quote may differ. Onboarding is scheduled once the signed
> copy is received.

Sample assumption language:

> 3. Assumes the buyer supplies clean historical payroll and roster data by
>    <date>. Data remediation, if required, is quoted separately.

## 4. Pre-send quality gate

Run this before the document leaves the building:

- [ ] One recommended tier; price is easy to find on first scan.
- [ ] Every number traces to `bd-context` §7 or a signed-off input.
- [ ] Assumptions and exclusions numbered; each assumption names its consequence.
- [ ] Validity has an exact date; terms reference the MSA.
- [ ] One clear next step and a signature block per signatory.
- [ ] No legal text paraphrased; regulated text comes from `bd-context`.
- [ ] Logged in the CRM with stage, amount, and close date.
