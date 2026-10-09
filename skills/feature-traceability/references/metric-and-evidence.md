# Metric links and evidence — detail

Reference for `feature-traceability`. Load when defining a row's KPI link, deciding
what proves movement, or building the coverage report. The core workflow lives in
`SKILL.md`.

## 1. Anatomy of a metric link

Each KPI cell must be specific enough that two people reading it compute the same
number. Record four fields:

| Field | Meaning | Example form |
|-------|---------|--------------|
| Metric | The named measure | "payroll error rate" |
| Baseline | Value when the feature was proposed | "[X]% as of [date / source]" |
| Target | Expected value after the feature works | "[Y]% within one cycle" |
| Direction | Which way is good | lower / higher |

A link missing baseline or direction cannot be verified later. Treat it as incomplete
and send it back.

## 2. Source of truth

Every metric names exactly one source of truth — the query, dashboard, or report that
reports it. Two sources for one metric produce two arguments at review time. Write the
source next to the link, e.g. `query: analytics.kpi_payroll_error_rate`.

If no source exists yet, the feature's first deliverable is to instrument the metric. A
KPI you cannot read is a KPI you cannot report.

## 3. Choosing the right metric level

- **Outcome metric** — what the business cares about (revenue, retention, cost, risk,
  statutory accuracy). This is what a row traces to.
- **Output metric** — what the feature produces (adoption, usage, tasks completed). Use
  it as a leading indicator, never as the outcome.
- **Never trace to a vanity metric** the feature cannot plausibly move. If another team
  owns the driver, the link is false.

Aim to trace the feature to an outcome metric and record the output metric as the
short-term signal that predicts it.

## 4. Evidence discipline

- Never assert that a KPI moved without the source-of-truth number, with a date.
- Label anything inferred as an assumption: `[ASSUMPTION: ...]`.
- Distinguish correlation from cause. If a launch coincides with a season, a price
  change, or another release, name the confound.
- Preserve the raw read (baseline and current) so a later reviewer can re-check the math.
- A test result is evidence; a claim about a test result is not. Link the run.

## 5. Linking the acceptance test to the KPI

Two tests per feature, answering different questions:

- **Behavioral test** — does the feature do what it says? (unit, integration, e2e).
  Proves the build.
- **Measurement plan** — does the KPI move? (dashboard, cohort, holdout). Proves the
  outcome.

A feature with only a behavioral test has proved it shipped, not that it helped. The
acceptance-test column links the behavioral test; the KPI read is owned by Step 6 of
`launch-readiness`.

## 6. Coverage math

```
feature KPI coverage = features with a filled KPI link / active features
OKR coverage         = OKRs with >= 1 funded feature / OKRs this cycle
orphan rate          = open orphans / active rows
```

Report all three. Falling coverage with rising output means the team is shipping faster
than it is linking — a warning, not progress.

## 7. Worked example

A release proposes "automated statutory filing export".

- Outcome metric: statutory late-filing penalties per month; baseline 2; target 0;
  direction lower; source: finance report `penalties_monthly`.
- Output metric: share of payroll runs using the export; baseline 0%; target 90% within
  one cycle.
- Persona/pain: the payroll officer re-keying the statutory return manually (`bd-context` §4-5).
- SOP: the monthly filing runbook (`sop-to-automation`).
- Commercial goal: cost and risk — fewer penalties, lower support load.
- Control: data-export authorization and audit logging (`security-by-design`).
- Acceptance test: the export produces a schema-valid file for a fixture payroll
  (behavioral); `penalties_monthly` reads 0 for two cycles (measurement).

Every cell is filled and readable by a stranger. That is the standard.
