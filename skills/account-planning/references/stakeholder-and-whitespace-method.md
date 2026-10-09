# Stakeholder Mapping and Whitespace Method

Detail for Steps 3 and 4 of `account-planning`. Load this when the stakeholder map or the whitespace matrix needs to be built properly.

## Stakeholder mapping

### The buying committee, by role

A B2B decision is made by a committee, not a person. Identify each role; one person may hold two.

| Role | What they do | What you need from them |
|---|---|---|
| Economic buyer | Approves budget and signs | Value in their financial language; a reason to act now |
| Champion | Advocates internally, sells when you are absent | Proof, ammunition, and your candour about the gap |
| Users | Live with the product daily | Adoption, workflow fit, the pain in their words |
| Technical / security | Vets integration, security, compliance | Evidence: docs, certifications, references, an architecture answer |
| Procurement | Owns terms, price, process | Predictable terms, a defensible price, no surprises |
| Blocker | Opposes or stalls the deal | To be named, heard, and neutralised with facts, not ignored |

### Influence vs sentiment

Plot each stakeholder on two axes:

- **Influence** — can they stop the deal on their own? High / Medium / Low.
- **Sentiment** — Advocate / Neutral / Skeptic.

High-influence skeptics are the biggest single threat and are usually unnamed. High-influence advocates are your champions. Low-influence skeptics can be managed; low-influence advocates are allies, not decision-makers.

### Rules

1. Never leave the economic buyer unnamed. If you do not know who signs, you do not have a plan — make identifying them the first action.
2. Count how many independent relationships you hold. One is single-thread risk; two is thin; three or more is a position.
3. Record the last-contact date for every high-influence person. No contact in 90 days is a cooling signal.
4. Write down what each person is measured on. You sell to their metric, not your feature.
5. On any champion change, re-run the map. A departed champion invalidates the plan above it.

### Sourcing contacts

Use CRM fields, the customer's public leadership page, an email signature, or an authorised introduction. Do not scrape restricted profiles or infer private data. If a name cannot be sourced, leave the row as a role (for example "Economic buyer: unknown") rather than filling a guess.

## Whitespace method

### Definition

Whitespace is the subset of a customer's remaining need you could credibly serve — not everything they do not yet buy. Two neighbours are excluded:

- **No-fit** — products or use cases outside your ICP. Selling these hurts margin and support.
- **Locked** — needs served by a contract or platform the customer will not move this cycle.

### Build the matrix

Rows = your products, tiers, or modules. Columns = the customer's business units, sites, or departments. One cell each, one of:

- **Adopted** — in use, healthy.
- **Partial** — some seats or some sites only.
- **White space** — a fit, not yet bought.
- **No-fit** — a fit you should not pursue.
- **Locked** — served elsewhere; re-check next cycle.

### Quantify and rank

1. Size each white-space and partial cell in units the customer counts: seats, sites, transactions, or modules.
2. Convert to potential value using the pricing in `.agents/bd-context.md`. State the assumption behind the conversion.
3. Rank cells by **value x winnability**. Winnability reflects: an existing advocate in that unit, a fit with what they already buy, and a trigger to act.
4. Keep the top three. The rest stay in the matrix as a watchlist.

A matrix with every cell marked "white space" is not an analysis; it is a wish list. If that happens, the customer's real boundary has not been found — go back and mark the no-fit and locked cells honestly.

### Common white-space vectors

- Extra seats in a department already using the product.
- A second site or subsidiary not yet provisioned.
- A higher tier or module the adopted tier sits beneath.
- A workflow they run manually next to the product.
- A geography or entity added since the last contract.

Each vector must name the trigger that makes the customer act now. No trigger, no wave — it stays on the watchlist.
