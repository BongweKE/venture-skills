# Rollout mechanics and rollback — detail

Reference for `launch-readiness`. Load when staging a rollout, setting hold windows,
choosing a flag strategy, or defining rollback triggers. The core workflow lives in
`SKILL.md`.

## 1. Why stage, not big-bang

Blast radius is the number of users a defect can reach at once. Big-bang launches set it
to everyone, so any defect is a full outage. Staging trades a little coordination for the
ability to catch a defect while it affects almost no one. The canary is not a formality;
it is the incident you did not have.

## 2. The three stages

| Stage | Audience | Hold default | Advance gate |
|-------|----------|--------------|--------------|
| Canary / internal | team, then 1-2 friendly users | 24 h | no new error/latency signal; smoke path green |
| Limited | one segment or 5-10% of users | 72 h | metrics stable; no support spike; KPI trend not negative |
| General | all users | - | limited-stage hold passed clean |

Adjust the defaults upward for changes touching money, personal data, statutory
deadlines, or safety — a week is reasonable for a payroll or filing change. Adjust the
audience, not the discipline.

## 3. Feature-flag strategy

- Put the change behind a flag so the audience can be widened or narrowed without a
  redeploy.
- Flags have an owner and an expiry. A flag nobody removes becomes permanent complexity
  and a hidden risk.
- The flag's "off" path is the rollback path — test it before the canary, not during the
  incident.

## 4. Hold-window discipline

During each hold, watch a fixed short list: error rate, latency, the target KPI signal,
and support volume on the new path. Two outcomes only:

- **Advance** — the hold passed; widen the audience.
- **Roll back** — any trigger fired; revert, then re-run the readiness gate.

Sitting in a stage past its hold window without deciding is its own failure: the defect
keeps reaching the limited cohort while nobody acts.

## 5. Rollback triggers (write these as numbers)

| Signal | Example threshold | Action |
|--------|-------------------|--------|
| Error rate | > [X]% over [window] | roll back |
| Latency p95 | > [X] ms over [window] | roll back |
| Target KPI | wrong direction past [floor] | roll back |
| Safety / statutory / data-integrity | any occurrence | roll back immediately |
| Support volume | > [X] tickets per [window] on new path | pause, then decide |

Notes:

- **Roll back, then diagnose.** Rolling forward under pressure often turns a small
  incident into a large one.
- **One decision owner** for the rollback so there is no cluster of "maybe we should".
- **Time-to-recover is a metric.** Record trigger -> detected -> rolled back, and improve
  it next release.

## 6. The rollback drill

Before the canary opens, run the rollback once on the same path production will use:

1. Deploy the release candidate to the canary.
2. Invoke the rollback.
3. Confirm the previous state is fully restored (data, schema, flags, caches).
4. Record the time it took and any manual steps.

An untested rollback is a hope. The drill converts it into a procedure someone can
follow at 2 a.m.

## 7. Data safety during rollout

- Migrations run forward-compatible: the previous app version must still work against
  the migrated schema during the hold.
- A backfill is separate from the deploy and reversible; verify row counts before and
  after (use `deployed-change-verification` for the production read-back).
- Never couple a destructive migration to a general-stage rollout; stage the schema and
  the feature independently.

## 8. After a rollback

Produce a short note — trigger, action, time-to-recover, and the suspected cause — and
attach it to the release ticket. Feed it to the cycle review so the same defect is not
re-shipped. Retrying requires the readiness gate to pass again; a rollback is not a pause
button.
