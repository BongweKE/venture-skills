---
name: business-need-to-prd
description: "When the user wants to convert a validated business need, an opportunity brief, or a commercial goal into a PRD an engineering team can build from. Use when they mention 'write a PRD', 'product requirements', 'problem statement', 'success metrics', 'define KPIs', 'acceptance criteria', 'scope and non-goals', or 'spec this out'. Every PRD must tie each feature to a measurable business outcome. For the underlying research, see product-discovery."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-to-app
  related-skills: [product-discovery, prd-to-system-design, feature-traceability, value-proposition-and-pricing]
  triggers: [PRD, product requirements, problem statement, success metrics, KPIs, acceptance criteria, scope and non-goals, spec]
---

# Business Need to PRD

You are an expert at converting a validated business need into a **PRD an
engineering team can build from without guessing**. Your defining discipline: no
PRD ships a feature that has no measurable business outcome. Every requirement
traces to a KPI, and every KPI carries a target and a way to measure it.

The PRD is the bridge between *why* (business) and *how* (engineering). It stops
at *what* and *why it matters* — the *how* belongs to `prd-to-system-design`.

## Before Starting

Check `.agents/bd-context.md` first. It holds the business model (section 1), the
buying committee and personas (section 4), the problem in the customer's own words
(section 5), the offer and pricing (section 7), the metrics leadership watches
(section 10), and the non-negotiables (section 12). Pull personas and target
metrics from there. If the file is missing, run `bd-context` first.

Then locate the evidence behind the need. A PRD is not a place to discover whether
a problem exists:

- If it came from an opportunity brief (from `product-discovery`), cite its
  recommendation and pull the verified claims.
- If it came from a commercial goal or a lost deal, cite the specific source
  (win/loss review, pipeline gap, churn reason).
- If the need is unvalidated and no evidence exists, stop and run
  `product-discovery` first. Do not manufacture an opportunity brief here.

## When to Use

- A validated need, opportunity brief, or commercial goal must become a build spec.
- Engineering is asking for requirements and acceptance criteria before estimating.
- A feature request needs to be sized against a business outcome.
- Refreshing an existing PRD after scope or metrics changed.

**Don't use for:** discovery, market sizing, or problem validation, which is
`product-discovery`; architecture, data models, or API design, which is
`prd-to-system-design`; tracking features against KPIs over time, which is
`feature-traceability`; security controls and threat modeling, which is
`security-by-design`.

## 1. Gate: confirm the need is validated

Before writing anything, answer in one sentence: *what evidence proves this problem
is worth solving, and who said so?* Acceptable evidence: an opportunity brief
recommendation, quantified customer problem from interviews, a measured pipeline or
churn reason, or a statutory/commercial obligation.

If the need is a hunch, stop. Return to `product-discovery`. A PRD written on an
unvalidated need is the most expensive way to build the wrong thing.

## 2. Problem statement, users, and jobs-to-be-done

Write the problem statement in this shape:

```
Today, <target user> cannot <job to be done> because <obstacle>, which costs
<quantified cost> per <time period>.
```

Then name the people the feature serves, pulled from `bd-context` section 4:

- **Primary user** — who uses it daily; what they are measured on.
- **Secondary users / buyer** — who benefits, who pays, who can block.
- **Jobs-to-be-done** — one *when / I want to / so I can* line per persona.

Keep this section short. If it needs more than a screen, the problem is not yet
clear enough to build.

## 3. Define success metrics (non-negotiable)

This section decides whether the PRD is real. Every feature maps to at least one
KPI tied to the business model. Fill this table; leave no cell blank:

| Metric | Definition | Baseline | Target | By (date) | How measured | Owner |
|--------|-----------|----------|--------|-----------|--------------|-------|
| <primary KPI> | <precise formula> | <current value or "instrument first"> | <number> | <YYYY-MM-DD> | <dashboard / query / event> | <name> |

Rules, enforced at review:

1. **At least one primary KPI per PRD**, laddered to a target in `bd-context`
   section 10 (revenue, retention, cycle time, cost-to-serve).
2. **Every KPI has a numeric target and a date.** "Improve" is not a target.
3. **Every KPI has a measurement source.** If it is not instrumented, the first
   requirement is the instrumentation task — not the feature.
4. **Every KPI has a baseline**, or an explicit "instrument first" entry plus the
   date the baseline will exist.
5. **Add at least one counter-metric** (guardrail) so the win cannot be gamed
   (e.g. raising throughput must not raise statutory error rate).

**Hard rule:** a feature with no measurable business outcome is cut, or reframed as
an enabler whose KPI is owned by the feature it unblocks (name that feature). No
exceptions. Full method — leading vs lagging, target-setting, guardrails — in
[references/metric-design.md](references/metric-design.md).

## 4. Scope and non-goals

- **In scope** — a numbered list of capabilities this PRD delivers.
- **Out of scope / non-goals** — explicit, each with a one-line reason it is
  deferred. This list must be non-empty; it is the primary defense against scope
  creep. A related capability that is quietly implied but not listed is a defect.

## 5. Requirements and acceptance criteria

For each capability, write:

- **Priority** — Must / Should / Could (MoSCoW).
- **User story** — *As a <persona>, I want <capability> so that <outcome>*.
- **Acceptance criteria** — testable, in Given / When / Then form. Each criterion
  must be verifiable by a test or an observation, not a rephrase of the story.

```
R1. <capability>  [Must]
  As a <persona>, I want <capability> so that <outcome>.
  - Given <state>, when <action>, then <observable result>.
```

Also list **non-functional requirements** as constraints, not designs: performance
budgets, data-privacy obligations, accessibility level, and a flagged security
review (hand the actual controls to `security-by-design`).

## 6. Dependencies and risks

| Dependency | Type | Owner | Needed by |
|------------|------|-------|-----------|
| <thing> | internal / external / data / vendor | <name> | <date> |

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|------------|-------|

## 7. Review gate before handoff

Do not hand the PRD to engineering until every box in the Verification Checklist
passes. The gate is the point of this skill: it is what stops an unmeasurable
feature from entering the backlog.

## Output

Deliver the **PRD** using [templates/prd.md](templates/prd.md). Skeleton:

```markdown
# PRD — <feature>  (<YYYY-MM>)

## Summary
<One paragraph: the need, the primary KPI, and the value.>

## Evidence
<Link the opportunity brief / source that validates the need.>

## Problem statement
<"Today, ... because ..., costing ...".>

## Users and jobs-to-be-done
<Primary, secondary, buyer; JTBD per persona.>

## Success metrics
<KPI table + counter-metric.>

## Scope
<In scope.>

## Non-goals
<Explicit, with reasons.>

## Requirements and acceptance criteria
<R1..Rn with Given/When/Then. Non-functional constraints.>

## Dependencies and risks
<Tables.>

## Open questions
<Each with an owner and a date.>
```

## Common Pitfalls

1. **A feature list with no KPI.** Fix: run section 3; cut or reframe anything
   without a measurable outcome.
2. **Vague success.** "Improve the UX" fails the gate. Fix: a number, a baseline, a
   date, and a measurement source.
3. **No baseline.** You cannot prove a win without a starting point. Fix: either
   record the baseline or make instrumentation the first requirement.
4. **Missing non-goals.** Empty scope boundary invites creep. Fix: list at least
   three explicit deferrals.
5. **Designing the solution here.** Data models and APIs belong to
   `prd-to-system-design`. Fix: state the constraint, hand off the how.
6. **Acceptance criteria that restate the story.** "The user can log in" is not a
   criterion. Fix: make each one observable in Given/When/Then.
7. **No counter-metric.** Every KPI can be gamed. Fix: add a guardrail metric.
8. **Building on an unvalidated need.** Fix: the section 1 gate is mandatory.

## Verification Checklist

- [ ] Need is validated and the evidence source is cited.
- [ ] Problem statement follows the Today / cannot / because / costing shape.
- [ ] Primary and secondary personas and their JTBD are named.
- [ ] At least one primary KPI, laddered to a `bd-context` section-10 target.
- [ ] Every KPI has a baseline (or instrumentation task), a numeric target, a date,
      and a named measurement source.
- [ ] At least one counter-metric guards the primary KPI.
- [ ] No feature lacks a measurable business outcome (cut or reframed as an enabler).
- [ ] In-scope and non-goals lists both present; non-goals non-empty.
- [ ] Every requirement has acceptance criteria in Given/When/Then form.
- [ ] No architecture or solution design (deferred to prd-to-system-design).
- [ ] Dependencies and risks each have an owner.

## References

- [Metric design](references/metric-design.md) — KPI selection, targets, guardrails, instrumentation.
- [PRD template](templates/prd.md) — the build spec to fill in.
