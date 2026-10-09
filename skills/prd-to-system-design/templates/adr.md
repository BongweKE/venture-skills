# ADR <NNNN> — <Short decision title>

**Status:** proposed | accepted | superseded by ADR-<NNNN> | deprecated
**Date:** <YYYY-MM-DD> · **Deciders:** <names> · **Supersedes:** ADR-<NNNN> (if any)

One ADR per decision that is hard to reverse or would surprise a future reader. Use the `adr/NNNN-slug.md` naming convention. Keep it under one page.

## Context

The forces at play: the requirement, the constraint, the scale, the deadline. State the trade-off space in two or three sentences. Link the relevant PRD requirement IDs and design-doc section.

## Decision

The choice, in the active voice: "We will <do X>." One paragraph. If it is a build-vs-buy call, name the vendor or the standard we adopt.

## Alternatives considered

| Option | Why not chosen |
|--------|----------------|
| | |

At least two real alternatives. "Do nothing" is a valid one when it is.

## Consequences

- **Positive:** what this buys us.
- **Negative:** what it costs — the debt, the lock-in, the operational burden we accept.
- **Neutral:** what changes for other teams or contexts.

## Revisit trigger

The specific event or threshold that reopens this decision (e.g. "peak load exceeds 5x the assumed RPS" or "tenant count passes 500"). Without a trigger, a decision is permanent by accident.

---

Theory for weighing trade-offs (10x test, trade-off ledger, evaluation framework) is in `system-design-theory` §9.
