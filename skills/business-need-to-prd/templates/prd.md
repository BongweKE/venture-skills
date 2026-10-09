# PRD — <feature>

Copy to `.agents/prd-<slug>.md` (or the repo's PRD location) and fill every section.
No section may be left blank; write "N/A — <reason>" if genuinely inapplicable. Do
not add solution design; the *how* belongs to `prd-to-system-design`.

**Status:** <draft / in review / approved>   **Owner:** <name>   **Date:** <YYYY-MM>

## Summary

<One paragraph: the validated need, the primary KPI, and the value delivered.>

## Evidence

<Link to the source that validates the need (opportunity brief, win/loss review,
churn reason, statutory obligation), with its key verified claims.>

## Problem statement

```
Today, <target user> cannot <job to be done> because <obstacle>, which costs
<quantified cost> per <time period>.
```

## Users and jobs-to-be-done

- Primary user: <role> — measured on <what>; JTBD: *when <situation>, I want to
  <motivation>, so I can <outcome>*.
- Secondary users / buyer: <role> — <why they care>.
- Blockers / approvers: <role> — <what they need>.

## Success metrics

| Metric | Definition (formula) | Baseline | Target | By (date) | How measured | Owner |
|--------|----------------------|----------|--------|-----------|--------------|-------|
| <primary KPI> | | <value or "instrument first"> | | | | |
| <counter-metric> | | | | | | |

Laddered to `bd-context` section 10: <which business target, and how>.

## Scope

1. <capability>
2. <capability>

## Non-goals

- <deferred capability> — <reason>. (At least three.)

## Requirements and acceptance criteria

```
R1. <capability>  [Must | Should | Could]
  As a <persona>, I want <capability> so that <outcome>.
  - Given <state>, when <action>, then <observable result>.
  - Given <state>, when <action>, then <observable result>.

R2. ...
```

Non-functional constraints (not designs): performance budget <...>; data privacy
<...>; accessibility <...>; security review flagged for `security-by-design`.

## Dependencies and risks

| Dependency | Type (internal / external / data / vendor) | Owner | Needed by |
|------------|--------------------------------------------|-------|-----------|
| | | | |

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|------------|-------|
| | | | | |

## Open questions

| Question | Owner | By (date) |
|----------|-------|-----------|
| | | |
