# Process Mining and SOP Conversion

Depth behind the SKILL.md workflow: process-map notation, the exception taxonomy,
RACI-to-RBAC mapping, SLA-to-service-level conversion, checklist-to-validation,
escalation-to-state-machine, and the automation-classification rubric.

## 1. Process-map notation

Model the process as **trigger -> ordered steps -> outcome**. For each step capture:
actor, system/tool, input, output, whether it is a decision, its time or SLA, and
its exceptions. Keep one action per row.

```
Trigger: <event that starts the process>
  [1] <actor> does <action> in <system>  (input -> output)
  [2] <decision>?  yes -> [3] ;  no -> [5]
  [3] ...
  Outcome: <terminal success state>
```

Two ways to recover an as-is process:

- **Document review** — read the SOP, but treat every step as a claim to verify.
  SOPs often describe the intended path, not the real one.
- **Event-log analysis** — if a system already records events (ticket states, order
  timestamps, approval logs), mine the log for the actual path, the real durations,
  and the exception frequency. This is the only objective source; prefer it when
  available.

If neither exists, run a structured interview and mark every unverified step
`[UNVERIFIED]`.

## 2. Decision points and the exception taxonomy

Every "if X, then Y" becomes an explicit branch with **all** outcomes listed,
including the unhappy path. Classify every exception it can hit:

| Exception | Typical handling |
|-----------|------------------|
| Data missing / malformed | Validate at entry; route to a fix task |
| Validation failure | Block, notify the actor, allow resubmission |
| Timeout | Timer-based escalation (section 6) |
| External system down | Retry with backoff; dead-letter after N attempts |
| Human unavailable | Reassign to a backup role after a timer |
| Approval denied | Route back to the requester with a reason |
| Duplicate / retry | Idempotency key so it is not processed twice |

Rule: every exception gets an owner and a fallback. An unhandled exception is an
outage waiting for a busy day. If the SOP is silent, ask the process owner and
record the answer — do not invent it.

## 3. RACI to roles and permissions

Read the RACI as a permission model, then enforce least privilege:

| RACI letter | Meaning | System permission |
|-------------|---------|-------------------|
| R — Responsible | executes the step | write / execute on the object |
| A — Accountable | owns the outcome | one role only; owns the state transition |
| C — Consulted | must review before done | review / comment (no write) |
| I — Informed | notified after | read + notification only |

Rules: exactly one Accountable per step (else the process has no owner); a role that
only needs to read must not get write; test the model against real roles from
`bd-context` section 4. For access-control design, review cadence, and segregation
of duties, hand off to `security-by-design`.

## 4. SLA to service level and alerts

Convert every SOP SLA into a measurable service level:

1. Define the clock: when does it start, when does it pause (waiting on the
   customer?), when does it stop.
2. Pick a measure and a window (e.g. "90% of P1 tickets first-responded within 1h,
   measured monthly").
3. Set a **warn** threshold (act before breach) and a **breach** threshold.
4. Name the recipient and the escalation on breach.

An SLA with no measurement is a wish. "Respond quickly" is unenforceable.

## 5. Checklist to validation rule

Each checklist item becomes one of:

- **Blocking validation** — required field, format, range, or cross-field
  consistency the system can evaluate. Stops the step until satisfied.
- **Advisory validation** — a soft warning the actor may override with a reason.
- **Human sign-off** — a judgement call ("looks correct") the system cannot
  evaluate; require an explicit confirmation with the signer's identity.

Rule: do not turn a judgement call into a hard block; the system will either block
valid work or be bypassed. Match the enforcement to what the machine can actually
evaluate.

## 6. Escalation to state machine

Model the workflow as states; escalations are transitions. Define:

- **States** with an entry condition and an owner.
- **Timers** for time-based escalation (not polling loops).
- **Transitions** on event, on timer expiry, and on failure.
- **Terminal states** — done, cancelled, rejected — so the workflow always ends.
- **Notifications** that are idempotent: fire once per state entry, deduplicate,
  and name the recipient. Alert spam trains people to ignore alerts.

Add **retry with backoff** for external calls and a **dead-letter** state when
retries exhaust, so failures surface instead of vanishing.

## 7. Automation classification rubric

Apply to every step; record the verdict and the reason.

| Classification | Criteria | Example |
|----------------|----------|---------|
| Automate | Rule-based, deterministic, high-volume, machine-verifiable, low judgement | Recompute a total, send a templated reminder |
| Assist | Judgement needed, but data can be pre-assembled | Draft a decision packet for a manager |
| Keep human | Money, legal, safety, or relationship; accountable to a named person | Approve a payment, sign a statutory filing |

Hard rules:

- Never fully automate a decision a **named human is accountable for** by regulation
  or contract (money movement, statutory filing, clinical or safety calls). Automate
  the preparation; the human approves and the approval is logged.
- Never automate a step with unstructured inputs and costly errors — assist it until
  the inputs are structured.
- Every automated step needs a human fallback for when it fails.

## 8. Pitfalls specific to SOP conversion

1. **Automating the workaround.** The manual step exists because of a system gap.
   Fix the gap, then automate — or you scale the workaround.
2. **Happy-path-only modeling.** Enumerate exceptions per step.
3. **Invented permissions.** Derive roles from RACI; least privilege; one owner.
4. **Unmeasured SLAs.** Define clock, measure, warn, breach.
5. **Judgement calls as hard blocks.** Make them advisory or human sign-off.
6. **Notification storms.** Idempotent notifications, timers not loops.
7. **Automating the accountable decision.** Keep the human approval, log it.
8. **No fallback.** Every automation gets a human path on failure.

## 9. Output contract

Produce the process-to-requirements spec from the template: process map, decisions
and exceptions, roles and permissions, service levels and alerts, validation rules,
state machine, and the automation classification. This spec is the evidence-and-
requirements source handed to `business-need-to-prd`.
