---
name: account-planning
description: "When the user wants to build or refresh a strategic account plan for a key or high-value customer. Use when they mention \"account plan\", \"key account plan\", \"strategic account\", \"whitespace analysis\", \"stakeholder map\", \"org map\", \"expansion path\", \"mutual action plan\", \"land and expand\", or \"account risk\". For the whole-pipeline view, see pipeline-forecast. For the quarterly customer-facing meeting, see qbr-and-renewal."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [pipeline-forecast, qbr-and-renewal, competitive-intelligence]
  triggers: [account plan, key account, strategic account, whitespace, stakeholder map, expansion path, mutual action plan, account risk]
---

# Account Planning

You are an expert at turning one high-value account into a written, owned plan. The output is `<account>-account-plan.md`: background and financials, an org and stakeholder map, a whitespace analysis, an expansion path, a mutual action plan, and an account risk register. Every fact is sourced or labelled `[ASSUMPTION]`; nothing about the account is invented.

## Before Starting

Read `.agents/bd-context.md` first — ICP, personas, product tiers and pricing, sales stages, competitive landscape, proof points, and constraints. Only gather what it does not answer.

Then pull account-specific inputs in this order:

1. CRM account record plus every open and closed opportunity.
2. The signed contract or order form: term, renewal date, tiers, seat counts, price.
3. Product usage or adoption data (active vs licensed seats, feature depth).
4. Support and escalation history.
5. Only public or authorised financial material (filings, annual reports, press). Never scrape a private profile or a platform that forbids it.

Evidence rule: every factual line carries its source (CRM field, contract clause, usage export, URL). Anything inferred is written as `[ASSUMPTION]`. If a contact or number cannot be sourced, leave it out rather than guessing — a guessed fact gets quoted back in a real meeting.

## When to Use

- The user is building or refreshing a plan for a named, high-value account.
- Preparing a land-and-expand, whitespace, or executive stakeholder map.
- A renewal or QBR exposed a gap that needs an account-level strategy reset.
- Onboarding a new strategic account owner who needs a written handover.

**Don't use for:** the whole-pipeline coverage or forecast view — that is `pipeline-forecast`. The quarterly customer-facing meeting and renewal mechanics — that is `qbr-and-renewal`. Researching a brand-new cold prospect — that is `prospect-research`. A competitor teardown — that is `competitive-intelligence`.

## Step 1 — Decide whether the account earns a plan

Not every account gets a full plan; a plan nobody maintains is worse than none. Tier every account first:

| Tier | Definition | Plan depth | Review cadence |
|---|---|---|---|
| Strategic | Top ~10 by value or strategic weight | Full plan | Quarterly |
| Growth | Named expansion potential, mid value | Full plan | Semi-annual |
| Watch | Small or at-risk | One page | Annual or on trigger |

If the account is below Growth, do not write a full plan — note it in the pipeline and stop. Spend the effort where the plan changes a decision.

## Step 2 — Account background and financials

Capture one snapshot table so every later section reasons from the same numbers: legal name; industry; HQ and operating geographies; headcount; estimated revenue; parent or ownership; fiscal-year end; first contract date; renewal or term end; current ARR/ACV; tiers in use; seats licensed vs active; primary payment rail.

Then write two lines: what changed since the last review, and the single biggest financial exposure (renewal size, revenue concentration, or price risk).

## Step 3 — Org and stakeholder map

Follow [references/stakeholder-and-whitespace-method.md](references/stakeholder-and-whitespace-method.md). Map the whole buying committee, not just your contact:

| Name | Title | Role | Sentiment | Influence | Measured on | Last contact |
|---|---|---|---|---|---|---|
| … | … | Economic buyer / Champion / User / Tech / Procurement / Blocker | Advocate / Neutral / Skeptic | H / M / L | … | YYYY-MM-DD |

Decision rule: if the economic buyer is unnamed, or the champion has left, or every relationship runs through one person (single-thread), that is the account's top risk — carry it into Step 7 immediately.

## Step 4 — Whitespace analysis

Follow the method reference. Build a matrix with products or tiers as rows and the customer's business units, sites, or departments as columns. Each cell is one of: **Adopted**, **Partial**, **White space** (could buy), **No-fit** (should not). Separate white space from no-fit — chasing a no-fit cell burns the relationship.

Quantify each white-space cell in seats or modules, then convert to potential value using the pricing in `.agents/bd-context.md`. Rank the cells by value x winnability and keep the top three as expansion vectors. Never present the whole matrix as "the opportunity" — a shortlist is what actually gets worked.

## Step 5 — Expansion path

Turn the top three vectors into dated waves:

| Wave | Window | Target white space | Entry trigger | Owner | Value | Evidence needed |
|---|---|---|---|---|---|---|
| Now | 0-90 days | … | … | … | … | … |
| Next | 90-270 days | … | … | … | … | … |
| Later | 270+ days | … | … | … | … | … |

Default motion is land-and-expand: prove value inside the current footprint before pitching a new one. If adoption in the current footprint is below the context's healthy threshold, the first wave is fixing adoption, not selling more.

## Step 6 — Mutual action plan

A MAP is a joint, dated, owned list of steps to the next commitment (expansion, renewal, or exec review):

| Milestone | Date | Owner | Dependency | Status |
|---|---|---|---|---|
| … | YYYY-MM-DD | us / them | … | open / done / blocked |

Rules: every row has a named owner on the customer side as well as yours. A MAP where every action is yours is a wish list — if the customer will not co-own it, the deal is stalling; say so plainly.

## Step 7 — Account risk register

| Risk | Category | Likelihood | Impact | Mitigation | Owner | Review by |
|---|---|---|---|---|---|---|
| … | Relationship / Commercial / Product / Compliance / Competitive | H/M/L | H/M/L | … | … | YYYY-MM-DD |

Always check these categories: single-thread relationship, champion departure, low adoption, rising support escalations, active competitor evaluation, regulatory or compliance change, procurement or security block, pricing pressure. Every high x high risk needs a mitigation with a date, not a noun.

## Output

Write `<account>-account-plan.md` using [templates/account-plan.md](templates/account-plan.md). Lead the file with a five-line executive summary: current value, the single expansion bet, the single biggest risk, the next mutual milestone, and the review date. Hand the file to the account owner and record the review date in the CRM.

## Common Pitfalls

1. **Inventing facts about the account.** A fabricated contact or number gets quoted in a real meeting and destroys trust. Source it or label it `[ASSUMPTION]`.
2. **A menu instead of a shortlist.** Dumping the entire whitespace matrix on the reader guarantees nothing gets worked. Rank and cut to three.
3. **Mapping only your contact.** A plan with a single relationship is a plan to lose the account when that person moves. Name the economic buyer.
4. **A one-sided MAP.** If all rows are your actions there is no mutual commitment — treat it as a stall signal, not a plan.
5. **Confusing the account plan with the QBR.** The plan is your internal strategy; the QBR is a customer-facing meeting. Keep them separate.
6. **Writing the plan once.** A plan with no review date is already stale. Set the next review before you close the file.

## Verification Checklist

- [ ] Every fact is sourced or marked `[ASSUMPTION]`; no invented contacts or numbers.
- [ ] Account tiered in Step 1; below-threshold accounts were not given a full plan.
- [ ] Stakeholder map names the economic buyer and champion and flags single-thread risk.
- [ ] Whitespace matrix uses Adopted/Partial/White space/No-fit and ranks the top three vectors.
- [ ] Expansion waves each have a window, trigger, owner, and value.
- [ ] MAP has mutual owners and dates; a one-sided MAP was called out.
- [ ] Risk register gives every high x high risk a mitigation and a review date.
- [ ] File written to `<account>-account-plan.md` with a five-line executive summary.

## References

- [Stakeholder mapping and whitespace method](references/stakeholder-and-whitespace-method.md)
- [Account plan template](templates/account-plan.md)
