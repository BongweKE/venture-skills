# Rollout and rollback plan — template

**Release:** [name / ticket]  **Owner:** [name]  **Date:** [YYYY-MM-DD]
**Flag / kill switch:** [name]  **Rollback path:** [how]

## 1. Stages

| Stage | Audience | Hold window | Advance gate | Owner |
|-------|----------|-------------|--------------|-------|
| Canary / internal | [team + 1-2 friendly users] | [24 h] | no new error/latency signal | [name] |
| Limited | [segment or 5-10%] | [72 h] | metrics stable, no support spike | [name] |
| General | all users | - | limited hold passed clean | [name] |

## 2. Rollback triggers (numeric)

| Signal | Threshold | Action | Watcher |
|--------|-----------|--------|---------|
| Error rate | > [X]% over [window] | roll back | [name] |
| Latency p95 | > [X] ms over [window] | roll back | [name] |
| Target KPI | wrong direction past [floor] | roll back | [name] |
| Safety / statutory / data-integrity | any occurrence | roll back now | [name] |
| Support volume | > [X] tickets / [window] | pause + decide | [name] |

## 3. Rollback drill (complete before canary opens)

- Drill run on: [date]  **Time to recover:** [minutes]
- Previous state fully restored (data / schema / flags / caches): [yes/no]
- Manual steps required: [list or "none"]

## 4. Per-stage decision log

| Stage | Started | Hold passed? | Decision (advance / hold / roll back) | By | Time |
|-------|---------|--------------|---------------------------------------|----|------|
| Canary | [time] | [y/n] | [decision] | [name] | [time] |
| Limited | [time] | [y/n] | [decision] | [name] | [time] |
| General | [time] | - | [decision] | [name] | [time] |

## 5. Post-launch measurement plan

- KPI: [metric]  **Baseline:** [value, date, source]
- Target: [value]  **Source of truth:** [query / dashboard]
- Window: [one full business cycle]  **Read date:** [YYYY-MM-DD]

## 6. Rollback note (if used)

- Trigger: [signal]  **Detected:** [time]  **Rolled back:** [time]  **Time-to-recover:** [min]
- Suspected cause: [one line]
- Re-ship requires: readiness gate re-run + fix verified

## Handoffs

- Deploy landed in production -> `deployed-change-verification`.
- Exploratory QA of the live change -> `dogfood`.
- KPI moved -> consider `qbr-and-renewal`; KPI did not -> `product-discovery`.
