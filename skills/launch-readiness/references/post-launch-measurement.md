# Post-launch measurement — detail

Reference for `launch-readiness`. Load when writing the measurement plan or reading the
result after the launch window. The core workflow lives in `SKILL.md`.

## 1. Measure the outcome, not the deploy

A deploy log proves code is live. It does not prove the feature helped. The measurement
plan answers one question: did the KPI the feature was built for move? If that KPI is
undefined, stop and run `feature-traceability` — a launch with no metric is a hope with a
deploy log.

## 2. The plan, written before launch

Record these five fields before shipping, not after:

| Field | Meaning |
|-------|---------|
| KPI | The named outcome metric (from the traceability row) |
| Baseline | Value at the proposal, with date and source |
| Target | Expected value after the feature works |
| Source of truth | The one query/dashboard/report that reads it |
| Window | How long until the read (default: one full business cycle) |

If no source of truth exists, instrumenting the KPI is part of the launch, not an
afterthought.

## 3. Reading the result honestly

- **Pull the number, do not eyeball a trend.** Compare baseline to current over the window.
- **Name the confounds.** Seasonality, a price change, a concurrent release, or a market
  shift can produce movement the feature did not cause. Say so.
- **Small numbers move noisily.** On a low-volume KPI, require a longer window or a cohort
  comparison before claiming an effect.
- **Report three states:** moved (with magnitude), did not move, or too early. "Too early"
  is a valid, honest read.

## 4. Attribution: baseline vs holdout

- **Baseline (before/after)** is the fast default. Accept it when no other change landed
  in the window.
- **Holdout (A/B or cohort)** is stronger: hold the change back from a comparable group
  and compare. Use it when the KPI is noisy, the stakes are high, or a confound is likely.
- Never claim causation from a single before/after read when a confound is present;
  downgrade to correlation and label it.

## 5. Feeding the result back

- Write the result onto the traceability row, closing the loop this suite exists to close.
- **KPI moved:** the hypothesis held; consider the follow-on in `product-discovery` or
  expansion in `qbr-and-renewal`.
- **KPI did not move:** a finding, not a failure. Return to `product-discovery` for the
  next hypothesis; do not silently keep the feature.
- **KPI too early:** set a date to read again; do not leave the loop open.

## 6. Worked example

Feature: automated statutory filing export. KPI: statutory penalties per month. Baseline:
2. Target: 0. Source: finance report `penalties_monthly`. Window: two filing cycles.

- After cycle 1, `penalties_monthly` = 0. Confound: a filing-extension notice that month.
  Read: promising, not yet conclusive.
- After cycle 2, `penalties_monthly` = 0 with no extension. Read: KPI moved; record it on
  the traceability row.
- Had it stayed at 2, the read would be "did not move" and the finding would go back to
  `product-discovery`.

The discipline is the same in every case: name the number, name the window, name the
confound, and write the outcome down.
