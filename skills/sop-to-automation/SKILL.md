---
name: sop-to-automation
description: "When the user wants to turn a documented standard operating procedure or a manual business process into software requirements. Use when they mention 'automate this SOP', 'standard operating procedure', 'process map', 'RACI to permissions', 'turn SLA into alerts', 'validation rules', 'escalation workflow', or 'turn a manual process into software'. Produces a process-to-requirements spec that feeds the PRD. For the build spec itself, see business-need-to-prd."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-to-app
  related-skills: [business-need-to-prd, feature-traceability, security-by-design]
  triggers: [SOP, standard operating procedure, process automation, process map, RACI, SLA, escalation, validation rules, workflow requirements]
---

# SOP to Automation

You are an expert at reading a documented standard operating procedure (or a
manual business process) and converting it into **software requirements an
engineering team can build from** — without automating the procedure's mistakes.

You produce a **process-to-requirements spec**: every step mapped, every decision
and exception made explicit, every role turned into a permission, every SLA into a
monitored service level, every checklist into a validation rule, and every
escalation into a state transition. You finish by deciding, step by step, what a
machine should do and what a human must still own.

## Before Starting

Check `.agents/bd-context.md` first. It holds the personas and buying committee
(section 4), how the company operates and what it promises (sections 5 and 12), and
the non-negotiables that bound any automation (section 12). Pull role names and
constraints from there so your permissions match reality. If the file is missing,
run `bd-context` first.

Then get the SOP in front of you. Acceptable inputs: a written SOP document, a
process recorded in a workflow tool, or a structured interview with the person who
runs it. If only an interview is available, capture it as an as-is process map and
mark every step you could not verify `[UNVERIFIED]`. If a written SOP already
exists, treat it as a draft to correct — SOPs routinely encode workarounds, not the
ideal process.

## When to Use

- A documented SOP must become software requirements.
- A manual process (billing run, onboarding, compliance filing, support triage)
  needs to be partially or fully automated.
- Turning roles and approvals into a permission model.
- Converting service-level promises into alerts and escalation workflows.
- Ranking which steps to automate first versus keep human.

**Don't use for:** the build spec or acceptance criteria themselves, which is
`business-need-to-prd` (this skill feeds it); tracking features against KPIs over
time, which is `feature-traceability`; security controls, threat modeling, and
access-review policy, which is `security-by-design`.

## 1. Read the SOP into a process map

Map the process as **trigger -> ordered steps -> outcome**. For every step, capture:

| # | Step | Actor | System / tool | Input | Output | Decision? | Time / SLA | Exception |
|---|------|-------|---------------|-------|--------|-----------|------------|-----------|

Rules: one action per row; name the actor, not a department; and log the **actual**
system used, not the one the SOP claims. Where steps loop or branch, note the branch
in the Decision column and handle it in section 2. Notation, event-log analysis, and
how to map an untold process: see [references/process-mining.md](references/process-mining.md).

## 2. Extract decision points and exception paths

Every "if X, then Y" is a decision point. Make each one explicit, with **all**
outcomes enumerated — including the unhappy path. Classify every exception the
process can hit:

- data missing or malformed, validation failure, timeout, external system down,
  human unavailable, approval denied, duplicate/retry.

Rule: every exception path gets an owner and a fallback action. An exception with no
handling is an outage waiting for a busy day. If the SOP does not say what happens,
ask, then record the answer — do not invent one.

## 3. Convert the RACI into roles and permissions

Take the RACI on the SOP and turn it into a role/permission model. Read it as:

- **Responsible** -> executes the step -> the owning role gets **write/execute**.
- **Accountable** -> owns the outcome -> exactly **one** role, the step owner.
- **Consulted** -> must review before completion -> **review/comment**.
- **Informed** -> notified after -> **read + notify**.

| Step | R | A | C | I | System role(s) | Permissions |
|------|---|---|---|---|----------------|-------------|

Rules: enforce **least privilege**; a role that only needs to read must not get
write. Exactly one Accountable per step, or the process has no owner. For the actual
access-control design and review cadence, hand off to `security-by-design`.

## 4. Turn SLAs into service levels and alerts

Every SLA in the SOP ("respond within 1 hour") becomes a measurable service level
with a monitoring signal and alert thresholds.

| SLA (SOP wording) | Service level | Measure | Warn at | Breach at | Alert target | Escalation |
|-------------------|---------------|---------|---------|-----------|--------------|------------|

Rules: an SLA with no measurement is a wish, not a requirement; define the clock
(when it starts, when it pauses) explicitly. Warn fires before breach so a human can
act. Every alert names a recipient and the escalation it triggers (section 6).

## 5. Turn checklists into validation rules

Each checklist item becomes either a **validation rule** (enforced by the system) or
a **task confirmation** (a human judgement the system cannot make).

| Checklist item | Type | Field / entity | Rule | Blocking or advisory |
|----------------|------|----------------|------|----------------------|

Rules: required fields, formats, ranges, and cross-field consistency become blocking
validation. Judgement calls ("looks correct") become advisory or a required human
sign-off — never a hard block the system cannot actually evaluate.

## 6. Turn escalation paths into notification and state-machine rules

Model the workflow as a **state machine**; escalations are transitions.

| State | Entry condition | Owner | Timer / trigger | On-expiry transition | Notify whom | Terminal? |
|-------|-----------------|-------|-----------------|----------------------|-------------|-----------|

Rules: define every terminal state (done, cancelled, rejected); use timers for
time-based escalations, not polling loops; make notifications **idempotent** (fire
once per state entry) to avoid alert spam; add retry with backoff for external calls
and a dead-letter state when retries exhaust. If two states can both be true, the
model is wrong — resolve it.

## 7. Classify each step: automate, assist, or keep human

Apply this default rubric to every step and record the verdict with a reason:

| Classification | When |
|----------------|------|
| **Automate** | Rule-based, deterministic, high-volume, machine-verifiable, low judgement. |
| **Assist** | Judgement needed, but the system can pre-assemble the data and hand it to a human. |
| **Keep human** | Touches money, legal, safety, or a customer relationship; or is accountable to a named person. |

Hard rules:

- Never fully automate a decision that a **named human is accountable for** by
  regulation or contract (money movement, statutory filing, clinical or safety
  calls). Automate the preparation; the human approves.
- Never automate a step whose inputs are unstructured and whose errors are costly.
  Assist it instead until the inputs are structured.
- Every automated step needs a human fallback path when it fails.

## 8. Emit the process-to-requirements spec

Fill [templates/process-to-requirements.md](templates/process-to-requirements.md).
This spec is the evidence-and-requirements source that `business-need-to-prd`
converts into a PRD — hand it over rather than writing acceptance criteria here.

## Output

The **process-to-requirements spec**. Skeleton:

```markdown
# Process-to-Requirements — <process name>  (<YYYY-MM>)
Source SOP: <link or reference>   Owner: <name>

## Process map
<Trigger -> steps -> outcome table from section 1.>

## Decisions and exceptions
<Decision points and the exception taxonomy, each with an owner and fallback.>

## Roles and permissions
<RACI -> role/permission table.>

## Service levels and alerts
<SLA -> service level -> alert table.>

## Validation rules
<Checklist -> validation rule table.>

## State machine and escalations
<State / transition / notify table.>

## Automation classification
<Step -> automate / assist / keep human, with reason and approval point.>

## Open questions and gaps
<Each with an owner and a date. Files marked [UNVERIFIED].>
```

## Common Pitfalls

1. **Automating the SOP verbatim.** The SOP often encodes workarounds. Fix: map the
   as-is process, then question every manual step before automating it.
2. **Missing exception paths.** Only the happy path is modeled. Fix: enumerate the
   exception taxonomy in section 2 for every step.
3. **Ignoring the RACI.** Permissions get invented arbitrarily. Fix: derive roles
   from RACI and enforce least privilege.
4. **SLAs with no measurement.** "Respond quickly" is unenforceable. Fix: define the
   service level, the clock, and the alert thresholds.
5. **Checklist items as hard blocks.** Judgement calls cannot be validated by a
   machine. Fix: make them advisory or a human sign-off.
6. **Notification spam.** Every state change fires an alert. Fix: idempotent
   notifications plus timers.
7. **Automating accountable human decisions.** Money, legal, and safety calls need a
   named human. Fix: automate the prep; keep the approval human.
8. **No fallback when automation fails.** Fix: give every automated step a human
   path.

## Verification Checklist

- [ ] Process map covers trigger, ordered steps, outcome; actual systems recorded.
- [ ] Every decision point enumerates all outcomes, including the unhappy path.
- [ ] Every exception has an owner and a fallback action.
- [ ] RACI mapped to roles and permissions; exactly one Accountable per step.
- [ ] Least privilege applied; security design deferred to security-by-design.
- [ ] Every SOP SLA has a service level, a measure, and warn/breach thresholds.
- [ ] Every checklist item is a validation rule or a human sign-off, not both.
- [ ] State machine has terminal states; notifications idempotent; retries bounded.
- [ ] Every step classified automate / assist / keep human with a stated reason.
- [ ] No accountable human decision fully automated; automation has a fallback.
- [ ] Unverified steps marked `[UNVERIFIED]`; handoff to business-need-to-prd stated.

## References

- [Process mining](references/process-mining.md) — process-map notation, exception taxonomy, RACI-to-RBAC, state machines, classification rubric.
- [Process-to-requirements template](templates/process-to-requirements.md) — the artifact to fill in.
