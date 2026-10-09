# Option Analysis — Choosing Architecture Without a Menu

This reference supports steps 4, 5, and 7 of the skill: picking one option per dimension, recording the runner-up, and scoring build-vs-buy. The theory behind these choices (CAP/PACELC, replication, caching, resilience patterns, queue semantics) lives in `system-design-theory` — load it, cite the section, do not copy it here.

## The selection procedure

For every significant dimension, run these five steps and write the output into the design doc and an ADR:

1. **State the driver.** Which requirement or constraint forces a choice here? If nothing forces it, take the simplest option and move on.
2. **List two or three candidates.** More than three means you have not framed the decision.
3. **Fill the trade-off matrix** (below) with real numbers where possible.
4. **Recommend one.** Name the winner and the runner-up, and the single trade-off that decides it.
5. **Write the ADR** with a revisit trigger.

## Trade-off matrix

Score each candidate 1–5 (5 = best) against the drivers that matter for this system. Weight only the rows that are actual drivers.

| Criterion | Question |
|-----------|----------|
| Fit to requirement | Does it meet the functional and NFR targets without heroics? |
| Time to first value | How long until it works in production? |
| Operational burden | Who runs it at 03:00, and what toil does it add? |
| Cost at target scale | Monthly cost and unit cost at the assumed peak, not today. |
| Reversibility | How expensive is it to change our mind in 12 months? |
| Team familiarity | Can the current team build and debug it? |

Sum the weighted scores. When two options tie, prefer the **more reversible** one — the cost of a wrong bet is the cost of reversing it.

## Common dimensions and the default recommendation

- **Deployment shape.** Default: modular monolith. Choose services only for independent scaling, an independent failure domain, or a different runtime. (Distributed-systems tax is real: see `system-design-theory` §3.)
- **Datastore.** Default: one relational Postgres database, schema-per-context. Choose a second store only for a demonstrated access pattern (time-series, full-text, blob, graph) and record why.
- **Sync vs async.** Default: synchronous request/response for user-facing reads and writes. Go async (queue/event) only when a step is slow, unreliable, or must be retried — and then design idempotency first (`system-design-theory` §4).
- **Hosting.** Default: a managed platform that provides the database, auth, and object storage together, unless a compliance or cost constraint forbids it.
- **Consistency.** Default: strong for money/auth, eventual for feeds/counters. State it per context; it is a decision, not a side effect.

## C4 view conventions

Keep both views as text in the doc (source of truth); render with `architecture-diagram`.

- **C1 System Context:** the system as one box; the humans and external systems that interact with it; each relationship labelled with the goal or protocol. No internal detail.
- **C2 Container:** each deployable unit (web app, mobile, API, worker, scheduled job), each datastore, each message bus; relationships labelled with protocol and purpose. This is the view most reviewers actually need.

Rules: every box in a container view maps to something you could deploy or a store you could back up. If a box has no clear owner or interface, it is a module, not a container — keep it inside its parent.

## Build-vs-buy scoring

Default to **buy/adopt** for non-differentiating capabilities. Score each candidate against:

| Criterion | Weight guide |
|-----------|--------------|
| Time to first value | High when the capability is not your moat |
| Total cost at target scale | High — include the hidden sync/integration cost |
| Lock-in / exit cost | High when data residency or contracts bind you |
| Operational burden | Medium–high for a small team |
| Compliance fit | Hard gate: fails the regime, it is out |

Recommend one. If the answer is buy, record the vendor, the data it receives, and the exit path (this feeds `security-by-design` §7).
