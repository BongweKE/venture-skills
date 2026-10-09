---
name: pipeline-forecast
description: "When the user wants to define sales stages or build a forecast. Use when they mention pipeline, forecast, commit, best case, weighted pipeline, stage gates, exit criteria, CRM hygiene, funnel conversion, win rate, coverage ratio, or a weekly deal review. Covers stage-gate definitions, a commit/best-case/weighted forecast model, and funnel analytics. For inspecting an individual deal, see discovery-call. For the account growth path, see account-planning. For post-decision learning, see win-loss-review."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [discovery-call, win-loss-review, account-planning]
  triggers: [pipeline, forecast, commit, best case, weighted pipeline, stage gates, exit criteria, CRM hygiene, funnel conversion, win rate, deal review]
---

# Pipeline Forecast

You define the stage gates, CRM rules, and forecast model that make a pipeline
trustworthy. The deliverable is a stage-gate definition, a forecast the user can
defend to leadership, and a weekly inspection agenda that keeps deals honest.

## Before Starting

Check `.agents/bd-context.md` first. It holds the sales motion and stage list
(§9) and the current metrics — pipeline value, win rate, cycle length, ACV (§10).
Build the model on those numbers. Gather only what the context does not answer:
the CRM in use, the fiscal periods, and who reviews the forecast.

If the context has no stage list or metrics yet, run `bd-context` first — a forecast
without a stage definition is a guess with a percentage attached.

## When to Use

- The user wants to define or fix sales stages and their exit criteria.
- The user wants to build a forecast: commit, best case, weighted pipeline, coverage.
- Pipeline hygiene is degrading — deals stuck, stages meaningless, forecasts miss.
- The user wants a weekly deal-inspection agenda or funnel conversion numbers.

**Don't use for:** advancing or inspecting one specific deal (`discovery-call`); the
expansion path for an existing account (`account-planning`); root-cause learning
after wins and losses (`win-loss-review`). This skill owns the *system* the deals
flow through, not the deals themselves.

## Step 1 — Define stage gates with exit criteria

A stage is not a feeling; it is a gate with an objective exit criterion. A deal sits
in a stage until it *provably* meets the criterion. Use this default eight-stage
model and adapt the labels to the context:

| # | Stage | Exit criterion (provable) | Evidence required |
|---|-------|---------------------------|-------------------|
| 1 | Prospect | Problem and ICP fit confirmed | Named contact, qualifying note |
| 2 | Discovery | Needs, impact, and timeline captured | Discovery notes / MEDDPICC fields |
| 3 | Solution fit | Buyer's success criteria documented | Written criteria or agreed scope |
| 4 | Validation | Buyer confirms the solution meets criteria | Technical/pilot outcome |
| 5 | Proposal | Priced proposal delivered | Proposal ref + amount + validity |
| 6 | Negotiation | Terms under active discussion | Named blocker or open terms |
| 7 | Commit | Buyer confirms intent, date and path agreed | Mutual action plan |
| 8 | Closed | Contract signed | Signature date |

Rules:
- **No stage skipping.** A deal cannot enter Proposal without Validation evidence.
  If the buyer already knows the product, compress Discovery, do not delete it.
- **One exit criterion per stage.** If a stage needs two criteria, split the stage.
- **The gate is objective.** "Champion likes it" is not a criterion; "champion
  confirmed success criteria in writing" is.

## Step 2 — Enforce CRM hygiene rules

A forecast is only as good as the data underneath it. Non-negotiable rules:

- **Every stage move logged with a date.** Stale stages are invisible without one.
- **Amount and close date always set.** No blank amounts; a blank deal corrupts the
  weighted forecast.
- **A next step with a date on every open deal.** No next step = at risk by default.
- **No "pushed" close dates.** If a close date slips, note why; repeated pushing is a
  disqualification signal, not a forecast input.
- **One owner per deal.** Shared ownership hides no-progress deals.
- **Flag stalled deals.** Define "stalled" as no stage change and no logged activity
  for `N` days (default 21 for early stages, 10 for Commit); surface them weekly.

## Step 3 — Build the forecast

Forecast in three categories, then weight the whole pipeline for reference:

| Category | Definition | Confidence |
|----------|-----------|------------|
| **Commit** | Buyer-confirmed, dated path agreed; you would stake your number on it | ~90% |
| **Best case** | Real, winnable, but not yet buyer-confirmed (typically Negotiation) | ~50% |
| **Pipeline** | Qualified beyond Discovery but uncommitted | stage weight |

- **Commit must be evidence-based** — a mutual action plan with dates. If you cannot
  name the path and the date, it is best case, not commit.
- **Weighted pipeline** = sum of (deal amount x stage probability). Set probabilities
  from the user's *own* historical conversion, not textbook defaults; pull round
  numbers from `bd-context` §10. See `references/funnel-analytics.md` for the method.
- **Coverage ratio** = open pipeline / target. Healthy default is **3x**; below 3x,
  pipeline generation is the problem, and discounting will not fix a coverage gap.
- Report all three categories every period. A single blended number hides the risk
  that lives in the gap between commit and best case.

## Step 4 — Read the funnel

Conversion analytics tell you *where* the forecast leaks. Compute stage-to-stage
conversion from closed deals, not from opinion:

- **Stage conversion rate** — of deals that entered stage N, what share reached N+1.
  The lowest rate is the bottleneck; put coaching there.
- **Cycle time by stage and total** — compare against `bd-context` §9.
- **Win rate** — wins / (wins + losses), split by segment and by source.
- **Velocity** — qualified pipeline x win rate x average deal size / cycle length.
  This is the retrodicted revenue rate; compare it to the target.
- **Source quality** — which channels produce the highest win rate and shortest cycle.

Formulas and a worked example: `references/funnel-analytics.md`. Feed the patterns to
`win-loss-review` for root-cause; do not re-litigate individual losses here.

## Step 5 — Run the weekly deal inspection

One agenda, same order every week. The point is to inspect the *deals*, not to read
the CRM aloud. Use the agenda in `templates/forecast-and-review.md`.

Default flow:
1. **Numbers first (5 min)** — commit, best case, pipeline, coverage; delta vs last week.
2. **Commit deals (one line each)** — evidence of the dated path; anything thin drops
   to best case on the spot.
3. **At-risk and stalled** — deals with no recent stage change or a slipped date.
4. **Best-case promotions** — which deals earned Commit this week, and why.
5. **Bottleneck stage** — one coaching theme from the funnel data.
6. **Actions** — a dated next step and owner for every deal touched.

Rule: no deal leaves the review without either an advanced stage, a required next
step, or a drop in category.

## Output

- **Stage-gate definition** — the stage table (Step 1), stored in `bd-context` §9 or
  the CRM stage config.
- **Weekly forecast + review pack** — built from `templates/forecast-and-review.md`:
  commit / best-case / pipeline totals, coverage, the weighted number, the funnel
  snapshot, and the dated inspection agenda.

## Common Pitfalls

1. **Stages defined by feeling.** "They're close" is not a stage. Fix by enforcing a
   single provable exit criterion per stage.
2. **Commit inflation.** Optimistic commit destroys forecast credibility faster than a
   miss. Commit needs a dated path; everything else is best case.
3. **Textbook stage probabilities.** Default weights that ignore the user's own
   conversion produce a weighted number nobody trusts. Derive weights from history.
4. **Reading the CRM instead of inspecting deals.** The review is for hard questions,
   not status recital.
5. **Ignoring coverage.** A forecast miss at 1.5x coverage is a pipeline-generation
   problem, not a closing problem.
6. **Blending the three categories.** A single number hides the risk between commit
   and best case; always report all three.
7. **Blank amounts or missing next steps.** Silent data gaps corrupt every downstream
   calculation; treat them as at-risk by default.
8. **Forecast theatre.** If the same deals sit in Negotiation for a quarter, the stage
   definition is wrong or the deals are dead. Enforce the stall flag.

## Verification Checklist

- [ ] `.agents/bd-context.md` read; stages and metrics reused, not invented.
- [ ] Every stage has exactly one provable exit criterion and required evidence.
- [ ] CRM hygiene rules documented (dated moves, no blanks, next step, stall flag).
- [ ] Commit deals each have a dated, buyer-confirmed path.
- [ ] Weighted probabilities derive from the user's own historical conversion.
- [ ] Coverage ratio computed and compared to the 3x default.
- [ ] Funnel conversion, cycle time, win rate, and velocity computed from closed deals.
- [ ] Weekly agenda follows the fixed order; every deal leaves with an action + owner.
- [ ] Patterns handed to `win-loss-review`; individual deals to `discovery-call`.

## References

- `references/funnel-analytics.md` — conversion formulas, weighted-forecast method,
  velocity, cohort reads, and a worked example.
- `templates/forecast-and-review.md` — the weekly forecast model and inspection agenda.
