---
name: prd-to-system-design
description: "When the user wants to turn a PRD into an engineering-ready system design. Use when they mention 'system design', 'architecture doc', 'design doc', 'ADR', 'architecture decision record', 'bounded context', 'service decomposition', 'domain model', 'data model', 'C4 diagram', 'non-functional requirements', 'NFRs', 'build vs buy', or a technical design review. Delegates the deep theory to system-design-theory and diagrams to architecture-diagram. For the PRD this consumes, see business-need-to-prd. For mapping requirements to features, see feature-traceability."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-to-app
  related-skills: [system-design-theory, architecture-diagram, business-need-to-prd, feature-traceability, security-by-design, writing-plans, plan, native-mcp, supabase]
  triggers: [system design, architecture doc, design doc, ADR, bounded context, service decomposition, data model, C4 diagram, NFRs, build vs buy, tech design review]
---

# System Design from PRD

You turn a product requirements document into an engineering-ready system design: a design doc a team can build from, and a set of ADRs that record every significant choice. You do not re-teach distributed-systems theory — `system-design-theory` is the textbook. Your job is the decision procedure that selects options, fixes the numbers, and writes the decisions down.

## Before Starting

Check `.agents/bd-context.md` first and only gather what it does not already answer: section 2 (market, geography, currency/payment rails, regulatory constraints), section 7 (pricing and unit-economics guardrails), and section 12 (legal, ethical, and brand non-negotiables). Then confirm you have the PRD as input. If there is no PRD, stop and route to `business-need-to-prd` — designing without one produces a solution to a problem nobody stated.

Confirm in one question: the PRD, the target scale and launch deadline, and any locked constraints (existing stack, budget ceiling, compliance regime). If the PRD has no measurable acceptance criteria or NFRs, flag it — you cannot design against a requirement you cannot measure.

## When to Use

- The user has a PRD and wants a system design, architecture doc, or technical design.
- The user needs bounded-context or service decomposition, a domain/data model, or a C4 view.
- The user wants NFRs pinned down: latency, scale, availability, and a cost ceiling.
- The user is making a build-vs-buy or framework choice and needs an ADR.
- A design review is scheduled and needs a written artifact.

**Don't use for:** writing the PRD itself — that is `business-need-to-prd`. Tracking requirements to features or test coverage — that is `feature-traceability`. Security and privacy controls — that is `security-by-design`. Step-by-step implementation task lists — that is `writing-plans`. Deep theory (CAP, caching, resilience patterns) — load `system-design-theory`. Rendered diagrams as HTML — that is `architecture-diagram`.

## 1. Ingest the PRD and fix the design constraints

Extract into a constraints table. Do not start decomposing until this is complete.

- **Functional requirements** — keep the PRD's IDs verbatim; each becomes a candidate component responsibility.
- **Non-functional requirements** — every "fast", "scalable", or "reliable" becomes a number with a target and a measurement. If the PRD has none, propose the defaults in [references/nfr-specification.md](references/nfr-specification.md) and mark them `[ASSUMED]`.
- **Acceptance criteria** — these are the contract the design must satisfy.
- **Constraints** — regulatory regime, data residency, existing stack, budget ceiling, launch date.

**Evidence rule:** every row traces to a PRD line or a `bd-context` section. Anything you add is labelled `[ASSUMED]` with the reason.

## 2. Decompose into bounded contexts, then services

- Start from the domain, not the org chart. Group functional requirements by the noun they act on (Order, Invoice, Roster). Each cluster is a candidate **bounded context**.
- For each context record: responsibility in one sentence, the data it owns, the events it emits and consumes, and the requirement IDs it satisfies.
- Choose the deployment shape. **Default: a modular monolith with clear module boundaries** — one deployable, one schema per module. Split out a service only when a context needs independent scaling, an independent failure domain, or a different runtime. Justify every split; a premature split buys distributed-systems pain (see `system-design-theory` sections 3–4 on timeouts, retries, sagas) before it buys anything.
- **Decision rule:** if two contexts must share a transaction, they are one service for now.

## 3. Define the domain and data model

- Per context, list entities with key attributes and the invariants they must hold.
- Write relationships and cardinality; mark the **aggregate root** that owns each invariant.
- Choose the consistency model per context — strong for money and auth, eventual for feeds and counters. This is a decision; record it as an ADR.
- Specify storage. Default to a single relational Postgres database with schema-per-context unless a specific access pattern (time-series, full-text, blob) demands otherwise. A second datastore must be justified in its own ADR.
- For Postgres/Supabase, apply `supabase-postgres-best-practices` and let `supabase` own schema, migration, and RLS mechanics — do not hand-roll what the platform provides.
- Produce the entity/relationship description as text in the doc; render a visual via `architecture-diagram`.

## 4. Choose architecture options — one default, alternative written down

Never present a menu. For each significant dimension (deployment shape, datastore, sync vs async, hosting), recommend one option, name the runner-up, and state the trade-off that decides it. Method and worked examples: [references/option-analysis.md](references/option-analysis.md). Delegate CAP, consistency, caching, and resilience patterns to `system-design-theory` — cite the section, do not restate it.

## 5. Draw the C4 context and container views

- Produce two views: a **System Context** (the system, its users, external systems) and a **Container** view (deployable units, datastores, message buses, and the protocols between them).
- Keep the source of truth as **text** (component list plus relationships) inside the design doc so it survives edits; render the visual with `architecture-diagram`.
- Stay at C1/C2. Go to component/class level only where a single container is genuinely complex — and say why.

## 6. Specify the NFRs with numbers

For each NFR give a **target**, the **measurement**, and the **consequence** of missing it. Full catalogue and defaults: [references/nfr-specification.md](references/nfr-specification.md).

- **Performance** — p50/p95/p99 latency per key endpoint.
- **Scale** — peak requests/sec, data volume/year, largest single tenant.
- **Availability** — target nines and the acceptable degradation mode.
- **Cost ceiling** — the maximum monthly infrastructure cost and the unit cost (per tenant, per transaction) it must stay under. This is a design constraint, not a finance afterthought.
- **Security and privacy NFRs** — hand to `security-by-design`.

## 7. Decide build vs buy

For each non-differentiating capability (auth, payments, email, queues, search, observability) the **default is buy/adopt** unless it is core to the product's moat. Score with the criteria in [references/option-analysis.md](references/option-analysis.md): time-to-first-value, total cost, lock-in and exit cost, operational burden, compliance. Recommend one per capability and record it as an ADR.

## 8. Record each significant choice as an ADR

Write one ADR per decision that is hard to reverse or would surprise a future reader. Use [templates/adr.md](templates/adr.md): Context, Decision, Status, Consequences, Alternatives considered, Revisit trigger. Keep them short and dated. The decision theory (trade-off ledger, 10x test, evaluation framework) lives in `system-design-theory` section 9 — cite it, do not copy it.

## 9. Hand off to implementation planning

The design doc plus ADRs are the input to `writing-plans` (or `plan` mode), which breaks the work into ordered, bite-sized tasks. Do not write the task list here — hand over the artifacts. Where an agent will drive an external integration, note the points where a `native-mcp` server is the right integration seam instead of bespoke glue code.

## Output

Three artifacts:

1. A **design doc** from [templates/design-doc.md](templates/design-doc.md) — constraints, bounded contexts, domain/data model, chosen architecture, C4 views (text plus render), NFR table, build-vs-buy table, open questions.
2. A set of **ADRs** from [templates/adr.md](templates/adr.md), one file per decision.
3. The C4 **diagram HTML** produced via `architecture-diagram`.

Design-doc skeleton:

```markdown
# System Design — <Feature/Product>
Version / Date / Owner / Status

1. Constraints        (traced to PRD; [ASSUMED] marked)
2. Bounded contexts   (responsibility, data owned, events, requirement IDs)
3. Domain & data model(entity, attributes, invariants, aggregate root, consistency)
4. Architecture       (chosen option + runner-up + deciding trade-off)
5. C4 views           (System Context; Container — as text)
6. NFR table          (target | measurement | consequence)
7. Build vs buy       (capability | decision | score | why)
8. Open questions     (owner, needed-by)
9. ADR index          (links)
```

## Common Pitfalls

1. **Re-teaching theory.** Do not explain CAP, caching, or circuit breakers — cite `system-design-theory` and spend the tokens on the decision.
2. **Decomposing before the constraints table is complete.** A design without fixed numbers is a wish.
3. **Premature service split.** Default to a modular monolith; split only for an independent scaling or failure-domain reason.
4. **Presenting a menu.** Recommend one option, name the runner-up, state the deciding trade-off.
5. **Diagrams without a text source.** If the design lives only in the `.html`, it dies on the next edit. Keep the component/relationship list in the doc.
6. **Missing ADRs.** Every hard-to-reverse choice needs one, or the next engineer re-litigates it.
7. **Inventing NFR numbers as facts.** Mark every default `[ASSUMED]` and tie it to a source.

## Verification Checklist

- [ ] Constraints table present; every row traced to the PRD or `bd-context`; additions marked `[ASSUMED]`.
- [ ] Every functional requirement maps to exactly one owning bounded context.
- [ ] Deployment shape chosen with a stated reason; every service split justified.
- [ ] Domain model lists entities, invariants, aggregate roots, and the per-context consistency model.
- [ ] One recommended option per dimension, with runner-up and deciding trade-off.
- [ ] C4 context and container views exist as text plus a rendered `architecture-diagram`.
- [ ] NFR table has a target, a measurement, and a consequence for each entry.
- [ ] Cost ceiling and unit cost stated.
- [ ] Build-vs-buy decided per capability with a score.
- [ ] One ADR per hard-to-reverse decision; status and revisit trigger set.
- [ ] Handoff to `writing-plans` named; no theory duplicated from `system-design-theory`.

## References

- [references/option-analysis.md](references/option-analysis.md) — architecture option selection, trade-off matrix, build-vs-buy criteria, and C4 view conventions.
- [references/nfr-specification.md](references/nfr-specification.md) — NFR categories, default targets, measurement method, and a cost-ceiling worksheet.
