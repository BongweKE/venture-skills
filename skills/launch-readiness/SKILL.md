---
name: launch-readiness
description: "When the user wants to decide whether a built feature is ready to ship. Use when they mention launch checklist, go-live, release gate, ship, canary, staged rollout, rollback plan, go/no-go, or post-launch metrics. Covers a seven-domain readiness checklist (product, security, privacy, operations, support, data migration, go-to-market), a staged rollout with numeric rollback triggers, and a post-launch plan that checks whether the KPI the feature was built for moved. For designing the security controls, see security-by-design. For the renewal conversation, see qbr-and-renewal. For the opportunity hypothesis, see product-discovery."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-to-app
  related-skills: [security-by-design, feature-traceability, product-discovery, qbr-and-renewal, deployed-change-verification, dogfood]
  triggers: [launch checklist, go-live, release gate, canary, staged rollout, rollback plan, go/no-go, post-launch metrics]
---

# Launch Readiness

You run the go/no-go gate that decides whether a built feature ships. The deliverable
is a completed readiness checklist across seven domains, a staged rollout plan with
explicit rollback triggers, and a post-launch measurement plan that confirms the KPI
the feature was built for actually moved.

## Before Starting

Check `.agents/bd-context.md` first. The pricing and packaging (§7), the ICP and
personas (§3-4), the sales motion (§9), the metrics leadership watches (§10), and the
constraints and non-negotiables (§12) all feed the go-to-market and measurement
sections. Gather only what the context does not answer: the release/change ticket, the
feature's traceability row, the monitoring and alerting stack, the support channel, the
rollback mechanism, and the data-migration plan.

If the feature has no KPI and no acceptance test, run `feature-traceability` first —
you cannot certify readiness for a feature whose success is undefined.

## When to Use

- A feature, service, or change is built and someone must decide go / no-go.
- The user mentions launch checklist, go-live, ship, release gate, canary, staged
  rollout, rollback plan, or post-launch metrics.
- Preparing a release that touches money, personal data, statutory deadlines, or safety.
- Re-reviewing a launch after a rollback or a failed rollout.

**Don't use for:** choosing or designing the security controls (`security-by-design`);
the renewal or expansion conversation once the feature is live (`qbr-and-renewal`);
deciding whether the opportunity is worth building at all (`product-discovery`);
confirming a deploy actually landed in production (`deployed-change-verification` — this
skill gates the *decision to launch*, that skill verifies the *deployed change*). This
skill is the last gate before general availability, not the build, the sell, or the
post-mortem.

## The seven readiness domains

Every release is assessed across these. Each has a question, required evidence, and an
owner.

| Domain | Question it answers | Evidence required | Owner |
|--------|---------------------|-------------------|-------|
| Product | Do all acceptance criteria pass? | Test report, criteria checklist | Product |
| Security | Are the required controls verified? | Control test results, scan output | Security |
| Privacy/compliance | Is data handling lawful and documented? | Data map, retention note | Compliance |
| Operations | Can we run, monitor, alert, and roll back? | Dashboards, alerts, runbook, rollback drill | Ops |
| Support | Can support help the user and recover the issue? | Docs, escalation path, known issues | Support |
| Data | Is migration and backfill correct and reversible? | Migration dry-run, row counts, undo | Data |
| Go-to-market | Is pricing, enablement, and comms ready? | Price config, sales note, comms plan | GTM |

A domain is not "ready" because nobody objects; it is ready when its evidence exists
and has been read.

## Step 1 — Assemble the readiness checklist

Open `templates/readiness-checklist.md` and fill it top to bottom. For each line record
the item, the evidence (a link, a query result, a test run — not a verbal assurance),
the verifier, and a status of pass, fail, or waived-with-reason.

Rules:

- **No empty evidence cells.** "It works on my machine" is not evidence. Link the CI
  run, the dashboard, or the test output.
- **Waivers are explicit and owned.** A waived item names who accepted the risk and why.
  Silent waivers are how incidents start.
- **A failed item blocks the gate.** Any fail in Product, Security, Privacy, or Data is
  a hard stop until fixed or formally waived by the accountable owner.

## Step 2 — Verify, do not trust

The gate is only as strong as its verification. For each domain:

- **Product** — run the acceptance suite on the release candidate, not a stale build.
  Confirm each acceptance criterion maps to a passing test.
- **Security** — confirm the controls named in `security-by-design` are deployed and
  tested; attach the scan or audit output. A "planned" control is not verified.
- **Privacy/compliance** — confirm the data map covers the feature, retention is
  defined, and any statutory deadline (filing, notification) is respected. Cross-check
  `bd-context` §12.
- **Operations** — confirm the dashboard shows the new path, the alert fires on failure,
  the runbook exists, and a rollback was run once.
- **Support** — confirm user documentation exists, the escalation path reaches an
  on-call owner, and known issues are listed.
- **Data** — run the migration against a copy, compare row counts, and prove the
  backfill and its undo.
- **Go-to-market** — pricing is configured in the product and the billing system, sales
  has the enablement note, and comms (internal and customer) are scheduled.

Where the release is deployed infrastructure, hand final confirmation to
`deployed-change-verification`; do not accept a green pipeline as proof the change is
live.

## Step 3 — Stage the rollout

Ship in stages, never all at once. Default three:

| Stage | Audience | Purpose | Advance when |
|-------|----------|---------|--------------|
| Canary / internal | team, then 1-2 friendly users | catch breakage at near-zero blast radius | no new error or latency signal for the hold window |
| Limited | one segment or 5-10% of users | confirm behavior and KPI trend on real data | metrics stable, no support spike |
| General | all users | full availability | limited-stage hold passed clean |

Rules:

- **Hold each stage for a defined window** (default canary 24h, limited 72h; longer for
  money, data, or safety changes). Advance on the hold passing, not on a feeling.
- **Advance or roll back — never sit.** Every stage ends in a decision.
- **The kill switch is tested before the canary opens.** A rollback nobody has run is
  not a rollback plan.
- For high-blast-radius changes, use a feature flag so the audience narrows without a
  redeploy.

Mechanics, hold windows, and flag strategy: `references/rollout-and-rollback.md`.

## Step 4 — Define rollback triggers

Write the triggers before launch, quantitatively. A good trigger is a number someone
can watch:

- Error rate above `[X]%` over `[window]`.
- p95 latency above `[X] ms` over `[window]`.
- The target KPI moving the *wrong* direction past a floor.
- A safety, statutory, or data-integrity breach (any amount).
- A support ticket spike above `[X]` per `[window]` on the new path.

On trigger: roll back to the last known-good state, then re-run the readiness gate
before retrying. Rolling forward under pressure trades a small incident for a large one.
Every rollback produces a short note — trigger, action, time-to-recover — fed to the
cycle review.

## Step 5 — Run the go/no-go

A single 30-minute meeting with a named decision owner and three possible outcomes:

1. **Go** — every domain passes or has an owned waiver; rollout and rollback plans attached.
2. **Conditional go** — go at canary/limited only, with named conditions to clear before
   the next stage.
3. **No-go** — one or more blockers; list them with owners and dates.

Record the decision in the release ticket: who decided, when, the evidence reviewed, and
the conditions. This is the audit trail that a launch passed a gate.

## Step 6 — Measure post-launch

A launch is not done when it ships; it is done when you know whether the KPI moved.
Before launch, write the measurement plan:

- **The KPI** the feature was built to move (from `feature-traceability`), with baseline
  and target.
- **The source of truth** — the exact query, dashboard, or report that reports it.
- **The window** — long enough for the effect to show (default: one full business cycle).
- **The read** — compare baseline to post-launch; state the movement plainly and label
  confounds.

At the end of the window, record the result on the traceability row. If the KPI did not
move, that is a finding, not a failure to hide — feed it to `product-discovery` or the
next traceability review. Method and worked example: `references/post-launch-measurement.md`.

## Output

Produce three artifacts per release:

- **Readiness checklist** — `templates/readiness-checklist.md`, filled with evidence and
  a status per line across the seven domains.
- **Rollout and rollback plan** — `templates/rollout-plan.md`, with stages, hold windows,
  and numeric rollback triggers.
- **Post-launch measurement plan** — the KPI, baseline, target, source of truth, and
  window, attached to the release ticket.

## Common Pitfalls

1. **Checklist theatre.** Filling boxes without evidence is worse than no checklist — it
   manufactures false confidence. Require a link per item.
2. **Verbal readiness.** "Ops says it is fine" is not evidence. The dashboard, the alert,
   and the rollback drill are.
3. **Big-bang launch.** Shipping to everyone at once maximizes blast radius. Stage it;
   the canary exists to be boring.
4. **Rollback plan never tested.** An untested rollback fails under pressure. Run it once
   before the canary.
5. **No numeric triggers.** "Roll back if it looks bad" is not a trigger. Set the error,
   latency, and KPI thresholds in advance.
6. **Rolling forward mid-incident.** Retrying instead of reverting extends outages. Roll
   back first, diagnose after.
7. **Stopping at "shipped".** The gate includes the KPI read. A launch with no
   measurement is a hope with a deploy log.
8. **Resurrecting pre-build security.** Re-designing controls at the gate means the gate
   fails. Controls come from `security-by-design`; the gate verifies, it does not design.
9. **Confusing deploy success with launch.** A green pipeline is not production. Use
   `deployed-change-verification` for that read-back.

## Verification Checklist

- [ ] `.agents/bd-context.md` read; pricing, personas, constraints reused, not invented.
- [ ] Feature has a KPI and an acceptance test (`feature-traceability` row exists).
- [ ] All seven domains have evidence links and a status; no empty cells.
- [ ] Waivers are explicit, owned, and reasoned; hard-stop domains never silently waived.
- [ ] Security and privacy evidence attached; controls verified, not planned.
- [ ] Rollback tested before the canary; numeric triggers defined.
- [ ] Rollout staged canary -> limited -> general with hold windows and a decision per stage.
- [ ] Go/no-go recorded in the release ticket with owner, date, evidence, and conditions.
- [ ] Post-launch measurement plan written: KPI, baseline, target, source, window.
- [ ] Deploy confirmation handed to `deployed-change-verification`; exploratory QA to
      `dogfood` where used.

## References

- `references/rollout-and-rollback.md` — staged-rollout mechanics, hold windows, flag
  strategy, rollback triggers, the rollback drill, and data safety.
- `references/post-launch-measurement.md` — measurement design, baseline vs holdout,
  reading the result honestly, and a worked example.
- `templates/readiness-checklist.md` — the seven-domain go/no-go checklist.
- `templates/rollout-plan.md` — the staged rollout and rollback plan.
