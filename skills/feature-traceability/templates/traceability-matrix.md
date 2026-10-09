# Traceability matrix — template

Two artifacts: the living matrix, and the cycle coverage report leadership reads. Copy
the matrix table into `docs/traceability.md`, one row per story.

---

# Part A — The matrix

**Owner:** [name]  **Updated:** [YYYY-MM-DD]  **Cycle:** [sprint / release / month]

| ID | Feature / story | Business owner | KPI / OKR moved | Persona and pain | SOP automated | Commercial goal | Control satisfied | Acceptance test | Status |
|----|-----------------|----------------|-----------------|------------------|---------------|-----------------|-------------------|-----------------|--------|
| FT-001 | [one line] | [person] | [metric, dir, baseline -> target] | [persona / pain] | [SOP id] | revenue / retention / cost / risk | [control] | [test link] | planned / build / live / done |

Column rules:

- **Business owner** is a named person, never a team.
- **KPI / OKR moved** carries direction and baseline -> target; `[UNKNOWN]` if unresolved.
- **Acceptance test** links the behavioral test; the KPI read is posted at launch.
- **Status** is `done` only when the KPI link is filled and the acceptance test passes.

## Orphan register (run every cycle)

| Type | Item | Why orphaned | Decision | Owner | Date |
|------|------|--------------|----------|-------|------|
| feature | FT-004 | no KPI linked | cut / attach KPI | [person] | [date] |
| KPI | [okr] | zero features | fund / not pursued | [person] | [date] |
| test | [test] | no feature | delete / add feature | [person] | [date] |
| control | [control] | unsatisfied | raise gap item | [person] | [date] |

---

# Part B — Cycle coverage report

**Period:** [cycle]  **Prepared:** [YYYY-MM-DD]

- **Feature KPI coverage:** [x%] (target 100%)  **vs last cycle:** [+/-]
- **OKR coverage:** [x%] (target 100%)  **vs last cycle:** [+/-]
- **Open orphans:** [n] ([features] / [KPIs] / [tests] / [controls])
- **Commercial mix:** revenue [n] | retention [n] | cost [n] | risk [n]

## Outcome movement (features launched last cycle)

| ID | Feature | KPI | Baseline | Current | Moved? | Notes / confounds |
|----|---------|-----|----------|---------|--------|-------------------|
| FT-001 | [feature] | [metric] | [value] | [value] | yes / no / too early | [confound] |

## Review agenda (30 min, fixed order)

1. Orphans — every item, with a decision recorded.
2. New rows — confirm each met the entry rule (owner + outcome + test).
3. Moved outcomes — pull the number, do not assume.
4. Drift — rows whose KPI or owner changed with the business.
5. Actions — dated next step and owner for every row touched.

**Closing rule:** no row leaves the review without a valid seven-column fill, a cut, or
a dated action.

## Handoffs

- KPI wrong or missing -> `business-need-to-prd`.
- SOP link missing -> `sop-to-automation`.
- Control gap -> `security-by-design`.
- Pipeline or funnel metric -> `pipeline-forecast`.
- Feature ready to ship -> `launch-readiness`.
