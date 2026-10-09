---
name: feature-traceability
description: "When the user wants to keep every feature, epic, and user story traceable back to the business it serves. Use when they mention traceability matrix, requirements traceability, RTM, orphan feature, orphan KPI, coverage report, feature-to-KPI mapping, feature-to-SOP mapping, or 'why are we building this'. Maintains the living matrix linking each story to the KPI it moves, the persona it serves, the SOP it automates, the commercial goal it supports, the control it must satisfy, and the acceptance test that proves it. For defining the KPI, see business-need-to-prd. For the SOP being automated, see sop-to-automation. For the control being satisfied, see security-by-design."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-to-app
  related-skills: [business-need-to-prd, sop-to-automation, security-by-design, pipeline-forecast, launch-readiness, product-discovery]
  triggers: [traceability matrix, requirements traceability, RTM, orphan feature, orphan KPI, coverage report, feature-to-KPI, why are we building this]
---

# Feature Traceability

You maintain the living traceability matrix that ties every epic, feature, and user
story back to the business outcome it exists to move. The deliverable is a matrix
with no orphan features and no orphan KPIs, kept current each cycle, plus a coverage
report leadership can act on.

## Before Starting

Check `.agents/bd-context.md` first. It holds the company goal (§1), personas and
their pain (§4-5), value props (§6), the offer and pricing (§7), and the metrics
leadership watches (§10) — the anchors every row must trace to. Do not invent a KPI
the context does not support.

Then gather only what the context does not answer:

- Where the backlog lives (GitHub Issues, Linear, Jira, a spreadsheet).
- Where the PRD / requirement set lives (the `business-need-to-prd` output).
- The SOP register and the control register.
- Who the business owners are — named people, not teams.

If no KPI/OKR set exists yet, run `business-need-to-prd` first. A matrix that traces
to undefined KPIs traces to nothing.

## When to Use

- The user wants to create or update a requirements traceability matrix (RTM) for a
  product, release, or epic.
- A feature is proposed and you must confirm which KPI, persona, SOP, and control it
  serves before it enters the backlog.
- The user asks whether the team is building features that move no metric (orphan
  features) or holds KPIs with no work behind them (orphan KPIs).
- A cycle review or a coverage report for leadership is due.
- An audit or compliance review asks for evidence that every requirement traces to a test.

**Don't use for:** defining the KPI or its target (`business-need-to-prd`); documenting
the SOP being automated (`sop-to-automation`); choosing the security or privacy control
(`security-by-design`); pipeline or funnel metrics (`pipeline-forecast`). This skill
owns the *links between* those artifacts, not the artifacts themselves.

## The matrix — one row per story

Every row is one epic, feature, or user story. Every row fills seven business-facing
columns. An empty cell is a defect, not a gap to fill later.

| Column | What it records | Source of truth |
|--------|-----------------|-----------------|
| ID | Stable reference (e.g. FT-001) | this skill |
| Feature / story | What is built, one line | backlog / PRD |
| Business owner | Named person accountable for the outcome | named at entry |
| KPI / OKR moved | The metric, direction, baseline, target | `business-need-to-prd` |
| Persona and pain | Whose problem this solves | `bd-context` §4-5 |
| SOP automated or replaced | The process it retires | `sop-to-automation` |
| Commercial goal | Revenue, retention, cost, or risk | `bd-context` §7, §10 |
| Control satisfied | Security/privacy control it must meet | `security-by-design` |
| Acceptance test | The test that proves it works | test suite / PRD |

Keep the matrix as one versioned file (default: `docs/traceability.md`), one row per
story, updated in the same pull request that changes the feature.

## Step 1 — Build the matrix top-down

Do not start from the backlog. Start from the business and work down, so every row
has a home before it is written.

1. List the KPIs/OKRs from `business-need-to-prd` and `bd-context` §10.
2. List the personas and their pains from `bd-context` §4-5.
3. List the SOPs from the SOP register.
4. List the controls from the control register.
5. For each existing backlog item, fill the seven columns. Mark unknown cells
   `[UNKNOWN]` — an honest gap beats a plausible fiction, which gets quoted in an audit.
6. Reconcile with `business-need-to-prd`: every requirement should already name its
   KPI; if it does not, send it back.

## Step 2 — Enforce the entry rule

No feature enters the backlog without all three:

- A **named business owner** — a person, not a team or "the product".
- A **measurable outcome** — the KPI it moves, with direction, baseline, and target.
- An **acceptance test** that proves the movement — behavioral for the feature, plus a
  measurement plan for the KPI.

If any is missing, the item is not ready. Return it to `business-need-to-prd` rather
than accepting a promise to fill it in later. The entry rule is the point: retrofitting
traceability onto shipped code is archaeology, not management.

## Step 3 — Detect orphans

Run this pass every cycle. Four orphan types, each ending in a decision:

| Orphan | Test | Decision |
|--------|------|----------|
| Orphan feature | No KPI, or KPI links to no OKR | Attach a real KPI, or cut / defer |
| Orphan KPI | An OKR/KPI with zero features linked | Fund a feature, or record as not pursued |
| Orphan test | Test with no feature, or feature with no test | Delete the dead test or write the missing one |
| Orphan control | A required control no feature satisfies | Raise a compliance-gap item with an owner |

An orphan feature is the most common and most expensive: it consumes build capacity
while moving nothing leadership measures. Surface every one by name.

## Step 4 — Review the matrix each cycle

Run a fixed-agenda review every sprint or release, 30 minutes, before planning locks:

1. **Orphans first** — every orphan feature, KPI, test, and control, with a decision.
2. **New rows** — items proposed since the last review; confirm each met the entry rule.
3. **Moved outcomes** — features now live: did their KPI move? Pull the number, do not assume it.
4. **Drift check** — rows whose KPI or owner changed because the business changed; re-link.
5. **Actions** — a dated next step and an owner for every row touched.

Rule: no row leaves the review without either a valid seven-column fill, a cut, or a
dated action. Agenda and report blocks: `templates/traceability-matrix.md`.

## Step 5 — Report coverage to leadership

Report the same shape every period so trends are visible:

- **Feature KPI coverage** — share of active features with a filled KPI link (target: 100%).
- **OKR coverage** — share of this cycle's OKRs with at least one funded feature (target: 100%).
- **Orphan count** — open orphans by type, and the trend versus last period.
- **Commercial mix** — features split by goal: revenue, retention, cost, risk.
- **Outcome movement** — for features launched last cycle, KPI baseline vs current.

Never report a feature as "done" on shipped code alone; report it done when its KPI
link is filled and its acceptance test passes. Detail and worked example:
`references/metric-and-evidence.md`.

## Output

Produce two artifacts:

- **`docs/traceability.md`** — the living matrix, one row per story, seven columns
  filled. Built from `templates/traceability-matrix.md`.
- **A cycle coverage report** — the leadership summary from Step 5, using the report
  block in the same template.

## Common Pitfalls

1. **Building the matrix bottom-up.** Starting from the backlog produces rows that
   trace to nothing. Start from the KPIs and personas and work down.
2. **The orphan feature nobody names.** A feature with no KPI stays invisible until
   someone reads the matrix. Run Step 3 every cycle or the orphans compound.
3. **Team as business owner.** "The platform team" owns nothing. Require a named
   person; accountability without a name is accountability without an owner.
4. **Vanity KPIs.** A metric no feature can plausibly move is noise. Trace to outcome
   metrics the feature can actually shift.
5. **Retro-tracing shipped code.** Filling cells after shipping is archaeology. Enforce
   the entry rule at the backlog gate.
6. **Filling cells with guesses.** A guessed KPI gets quoted in an audit. Mark unknowns
   `[UNKNOWN]` and resolve them.
7. **Set-and-forget.** A matrix reviewed once is a snapshot. Review each cycle and log
   drift when the business changes.
8. **Redefining KPIs here.** This skill links to KPIs; it does not define them. If the
   KPI is wrong, fix it in `business-need-to-prd` and re-link.

## Verification Checklist

- [ ] `.agents/bd-context.md` read; every row traces to a context anchor.
- [ ] Matrix lives in one versioned file, one row per story, seven columns present.
- [ ] Every active feature has a named business owner and a measurable outcome.
- [ ] Every feature has an acceptance test; no test is orphaned from a feature.
- [ ] Orphan features, KPIs, tests, and controls all detected and decided this cycle.
- [ ] Cycle review run against the fixed agenda; every row leaves with an action.
- [ ] Coverage report produced: KPI coverage, OKR coverage, orphan count, mix, movement.
- [ ] Unknowns marked `[UNKNOWN]`, not guessed.
- [ ] KPI definitions owned by `business-need-to-prd`; SOP links by `sop-to-automation`;
      controls by `security-by-design`.

## References

- `references/metric-and-evidence.md` — how to define a metric link (baseline, target,
  direction, source of truth), evidence discipline, coverage math, and a worked example.
- `templates/traceability-matrix.md` — the living matrix and the cycle coverage report.
