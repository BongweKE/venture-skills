# Process-to-Requirements — <process name>

Copy to `.agents/process-to-req-<slug>.md` (or the working dir) and fill every
section. This spec is the evidence-and-requirements source that
`business-need-to-prd` converts into a PRD. Mark unverified steps `[UNVERIFIED]`.

**Source SOP:** <link or reference>   **Process owner:** <name>
**Date:** <YYYY-MM>   **Prepared by:** <name>

## Process map

Trigger: <event that starts the process>   Outcome: <terminal success state>

| # | Step | Actor | System / tool | Input | Output | Decision? | Time / SLA | Exception |
|---|------|-------|---------------|-------|--------|-----------|------------|-----------|
| 1 | | | | | | | | |

## Decisions and exceptions

| Step | Decision point | Outcomes | Exception class | Owner | Fallback action |
|------|----------------|----------|-----------------|-------|-----------------|
| | | | | | |

## Roles and permissions

| Step | R | A | C | I | System role(s) | Permissions |
|------|---|---|---|---|----------------|-------------|
| | | | | | | |

Exactly one Accountable per step. Least privilege enforced. Access-control design
handed to `security-by-design`.

## Service levels and alerts

| SLA (SOP wording) | Service level | Measure | Warn at | Breach at | Alert target | Escalation |
|-------------------|---------------|---------|---------|-----------|--------------|------------|
| | | | | | | |

## Validation rules

| Checklist item | Type (blocking / advisory / sign-off) | Field / entity | Rule | Notes |
|----------------|---------------------------------------|----------------|------|-------|
| | | | | |

## State machine and escalations

| State | Entry condition | Owner | Timer / trigger | On-expiry transition | Notify whom | Terminal? |
|-------|-----------------|-------|-----------------|----------------------|-------------|-----------|
| | | | | | | |

Terminal states: <done / cancelled / rejected>. Notifications idempotent; external
calls retried with backoff; dead-letter state on exhaustion.

## Automation classification

| Step | Automate / Assist / Keep human | Reason | Human approval point? |
|------|-------------------------------|--------|-----------------------|
| | | | |

## Open questions and gaps

| Question / gap | Owner | By (date) |
|----------------|-------|-----------|
| | | |

## Handoff

- Feeds: `business-need-to-prd` (converts this into a PRD with KPIs).
- KPI mapping over time: `feature-traceability`.
- Security controls: `security-by-design`.
