# NFR Specification — Targets, Measurement, Consequence

Non-functional requirements are numbers with an owner, not adjectives. This reference supports step 6 of the skill. When the PRD supplies none, propose the defaults below and mark them `[ASSUMED]` until the user confirms.

## The rule

Every NFR entry has three fields: a **target** (a number), a **measurement** (how you will know), and a **consequence** (what happens when it is missed). An NFR without a measurement is a slogan; without a consequence it is ignored.

## Categories and default targets

| Category | Metric | Starter default (adjust to context) |
|----------|--------|-------------------------------------|
| Performance | p50 / p95 / p99 latency per key endpoint | reads p95 < 300 ms; writes p95 < 500 ms `[ASSUMED]` |
| Throughput | peak requests/sec | assume 3–5x average, state the average `[ASSUMED]` |
| Scale | largest tenant, data volume/year | state the pilot tenant and a 10x headroom year `[ASSUMED]` |
| Availability | uptime target | 99.9% unless a contract or clinical/financial need raises it `[ASSUMED]` |
| Durability | backup RPO / RTO | RPO minutes; RTO hours; state the restore drill |
| Consistency | per context | strong for money/auth, eventual for feeds `[ASSUMED]` |
| Cost | monthly ceiling + unit cost | one ceiling and one unit metric (per tenant / per transaction) |
| Security / privacy | controls | owned by `security-by-design`; link, do not restate |
| Observability | golden signals covered | latency, traffic, errors, saturation each have a signal |

## Cost-ceiling worksheet

Cost is a design constraint. Fill this table; if the design cannot meet the ceiling, change the design before writing code.

```text
Assumed scale:            <users / tenants / transactions per month>
Chosen shape:             <monolith | services> ; <one store | many>
Compute $/month:          <...>
Database $/month:         <...>
Storage + egress $/month: <...>
Third-party $/month:      <auth, payments, email, observability>
TOTAL $/month at target:  <...>
Ceiling:                  <...>   ->  pass / fail
Unit cost:                <$ per tenant / transaction>  ->  vs pricing floor
```

If total exceeds the ceiling: right-size before scaling out, add caching or tiering, or question a build-vs-buy choice (see [references/option-analysis.md](option-analysis.md)). Sustainability is the same lever — efficiency is also carbon efficiency (`system-design-theory` §8).

## Measurement method

- Latency and throughput: state the source (load test, APM, logs). A target you never measure is not a target.
- Availability: define what counts as "down" and the measurement window.
- Cost: name the billing dashboard or the query that produces the number.

## Handing off

- Security and privacy NFRs are produced by `security-by-design`; reference them, do not duplicate.
- Each NFR target becomes an acceptance criterion the design must satisfy; trace it to the requirement ID so `feature-traceability` can follow it.
