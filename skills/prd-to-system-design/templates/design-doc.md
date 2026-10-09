# System Design Doc — <Feature / Product>

**Version:** 0.1.0 · **Date:** <YYYY-MM-DD> · **Owner:** <name> · **Status:** draft | reviewed | approved
**Source PRD:** <link or path> · **Related ADRs:** <links>

Fill every section. Write "n/a — <reason>" rather than leaving a heading empty.

## 1. Constraints

| Constraint | Value | Source (PRD line / bd-context §) | Notes |
|------------|-------|----------------------------------|-------|
| Regulatory / data residency | | | |
| Existing stack | | | |
| Budget ceiling | | | |
| Launch date | | | |
| Scale assumption | | | |

Non-functional requirements are in section 6. Everything inferred rather than given is marked `[ASSUMED]`.

## 2. Bounded contexts

| Context | Responsibility (one sentence) | Data owned | Events out / in | Requirement IDs |
|---------|-------------------------------|------------|-----------------|-----------------|
| | | | | |

**Deployment shape:** modular monolith / service split — chosen because <reason>. Any service split is justified per context below.

## 3. Domain & data model

Per context:

- **Entities:** name, key attributes.
- **Invariants:** what must always hold.
- **Aggregate root:** which entity owns each invariant.
- **Consistency model:** strong / eventual — and why.
- **Store:** relational / other — and why.

Relationships and cardinality:

```text
<Entity A> 1—* <Entity B> ; <Entity B> *—1 <Entity C>
```

## 4. Architecture

For each dimension: chosen option, runner-up, deciding trade-off.

| Dimension | Chosen | Runner-up | Deciding trade-off | ADR |
|-----------|--------|-----------|--------------------|-----|
| Deployment shape | | | | |
| Datastore | | | | |
| Sync vs async | | | | |
| Hosting | | | | |

Theory references: `system-design-theory` §<n>. Do not restate it here.

## 5. C4 views

**System Context (C1):**

```text
<Actor> -> <System> : <goal>
<System> -> <External system> : <protocol / purpose>
```

**Container (C2):**

```text
<Client> -> <API container> : HTTPS
<API container> -> <Datastore> : SQL
<API container> -> <Message bus> : publish <event>
<Worker> -> <Message bus> : subscribe <event>
```

Rendered diagram: `<file>.html` (produced via `architecture-diagram`).

## 6. NFR table

| NFR | Target | Measurement | Consequence if missed |
|-----|--------|-------------|-----------------------|
| p95 latency | | | |
| Peak RPS | | | |
| Data volume / year | | | |
| Availability | | | |
| Monthly cost ceiling | | | |
| Unit cost | | | |

Security and privacy NFRs are owned by `security-by-design`.

## 7. Build vs buy

| Capability | Decision | Score / criteria | Why | ADR |
|------------|----------|------------------|-----|-----|
| Auth | buy | | | |
| Payments | | | | |
| Search | | | | |

## 8. Open questions

| Question | Owner | Needed by |
|----------|-------|-----------|
| | | |

## 9. ADR index

- `adr/0001-<slug>.md` — <title>
- `adr/0002-<slug>.md` — <title>
