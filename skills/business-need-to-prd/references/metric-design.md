# Metric Design for PRDs

How to choose, target, and instrument the KPIs that make a PRD real. The SKILL.md
section 3 is the workflow; this file is the depth. Rule zero: a PRD with no
measurable business outcome does not ship.

## 1. KPI vs metric vs vanity number

- **Metric** — any measurement (page views, ticket count). Descriptive.
- **KPI** — a metric tied to a business outcome the company is trying to move
  (revenue, retention, cost-to-serve, cycle time). Decision-driving.
- **Vanity number** — a metric that only ever goes up and changes no decision
  (cumulative signups). Refuse these as the primary.

A PRD names KPIs, not metrics. Every KPI in the table must be something a leader
would act on if it moved.

## 2. Ladder the KPI to the business model

Pull the target from `.agents/bd-context.md` section 10 and connect the feature to
an existing business number. Do not invent an orphan metric.

| Business goal (bd-context §10) | Candidate feature KPI |
|--------------------------------|-----------------------|
| Revenue growth | Activation rate, expansion revenue, win rate |
| Retention / NRR | Weekly active usage, renewal rate, support-ticket drop |
| Cost-to-serve | Manual hours per run, error rate, tickets per account |
| Cycle time | Time-to-first-value, time-to-resolution |

If a feature cannot be laddered to any of these, it is either a pure enabler (name
the feature whose KPI it serves) or it should be cut.

## 3. Leading vs lagging

- **Lagging** — the outcome (churn, revenue). Real, but slow and hard to attribute.
- **Leading** — the behaviour that drives it (weekly active admins, rota published
  before deadline). Fast, attributable, actionable in the sprint.

Default: pick one **leading** KPI you can move this quarter, and at least one
**lagging** KPI it is expected to influence. State the causal link and how you will
check it.

## 4. Baseline

Every KPI needs a starting point, or the win is unprovable.

- If the metric is instrumented: record the current value and the measurement window.
- If it is not: the **first requirement** is the instrumentation task, with a date
  the baseline will exist. Do not ship the feature before you can measure it.
- Never estimate a baseline and present it as measured — mark it `[ASSUMPTION]`.

## 5. Setting a target

Use the strongest method available, in this order:

1. **Benchmark** — a comparable internal process or an external figure with a source.
2. **Capacity / model** — derive from unit economics: `target = volume x conversion x
   value`. Show the arithmetic.
3. **Negotiated commitment** — the business owner commits to a number; record who.

Rules: targets are numeric and dated. "Increase" is not a target. A target with no
method is a guess — label it `[ASSUMPTION]`.

## 6. The measurement plan

For each KPI, specify exactly how it will be read so two people get the same number:

| Metric | Formula | Data source | Window | Segment | Dashboard / query |
|--------|---------|-------------|--------|---------|-------------------|

Rules: define the formula, not the concept ("statutory filing accuracy = 1 -
(rejected filings / total filings)"). Name the event or table it reads from. Name
the window (daily, monthly). Name who owns the dashboard.

## 7. Counter-metrics (guardrails)

Every KPI can be gamed. Pair each primary KPI with at least one counter-metric that
must not degrade:

| Primary KPI | Counter-metric (guardrail) |
|-------------|----------------------------|
| Throughput (shifts filled) | Rest-rule violations do not rise |
| Support time-to-close | Reopen rate does not rise |
| Onboarding speed | Data-migration error rate does not rise |

A win that damages the guardrail is not a win. State the guardrail threshold.

## 8. SMART check

Run every KPI through: Specific, Measurable, Achievable, Relevant, Time-bound. If it
fails any, fix it before the PRD moves to `prd-to-system-design`.

## 9. False precision and measurement debt

- **False precision** — "increase retention to 91.4%" with no model. Round to the
  precision you can defend.
- **Measurement debt** — shipping features faster than you instrument them. It is
  debt: it makes every later "is it working?" answer a guess. Pay it in the PRD by
  making instrumentation a first-class requirement.
- **Attribution** — a KPI can move for reasons unrelated to the feature. Note the
  confounders and, where cheap, plan a holdout.

## 10. Output contract

Return the KPI table (Metric / Definition / Baseline / Target / By / How measured /
Owner) plus the counter-metric row. Every primary KPI ladders to a `bd-context`
section-10 target. This table is the contract the feature is judged against after
launch, and the input to `feature-traceability`.
