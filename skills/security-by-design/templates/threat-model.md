# Threat Model — <System / Feature>

**Version:** 0.1.0 · **Date:** <YYYY-MM-DD> · **Owner:** <name>
**Inputs:** design doc / PRD link · **Regime:** <named data-protection law from bd-context §2>

Re-run this model whenever a new external interface, tenant boundary, or data class appears. A filed-and-forgotten threat model is a liability.

## 1. Data classification

| Data element | Classification | Lawful basis / purpose | Retention | Where stored |
|--------------|----------------|------------------------|-----------|--------------|
| | Public / Internal / Confidential / Regulated-personal / Regulated-sensitive | | | |

Health, financial, and biometric elements default to Regulated-sensitive. If unsure, classify up.

## 2. Data flow and trust boundaries

```text
<Actor> --boundary A--> <System entrypoint> --boundary B--> <Service>
       --boundary C--> <Datastore>        --boundary D--> <Third party>
```

| Boundary | From -> To | Data crossing | Controls at the boundary |
|----------|-----------|---------------|--------------------------|
| A | | | |
| B | | | |

Every boundary is a place a control must sit. A boundary with no control is a finding.

## 3. STRIDE threats

| # | Boundary | STRIDE | Threat | Likelihood x Impact | Control | Residual risk | Owner |
|---|----------|--------|--------|---------------------|---------|---------------|-------|
| 1 | | | | | | | |

Cover all six STRIDE letters at each boundary that carries sensitive data. A threat you cannot mitigate becomes an accepted risk with a named owner — never a silent omission.

## 4. Abuse cases

| Story / requirement | Abuse case (who, to what end) | System must refuse | Test owner |
|---------------------|-------------------------------|--------------------|------------|
| | | | |

Minimum coverage: cross-tenant privilege escalation, IDOR / object-reference tampering, mass assignment, payment or credit manipulation, enumeration and rate abuse.

## 5. Authentication and authorization

- **Authentication:** <provider/model>, MFA <required/available>, session lifetime <...>, token type <...>, revocation <...>.
- **Authorization model:** RBAC + per-tenant attribute scope (default). <Policy layer if any.>
- **Data-scoping:** every tenant-owned table enforces "principal scope only" at the data layer. Implementation path: `supabase` row-level security.

### Permission matrix

| Role | Resource | Action | Scope (tenant_id / owner_id) | Enforced where |
|------|----------|--------|------------------------------|----------------|
| | | | | app / RLS / both |

## 6. Secrets, keys, and encryption

| Secret / key | Class | Held by | Rotation | Storage |
|--------------|-------|---------|----------|---------|
| | signing / encryption / API | | | managed store / env |

Encryption in transit: <TLS everywhere>. At rest: <platform-managed / customer-managed>.

## 7. Supply chain

| Dependency / service | Data it receives | Agreement / DPA | Exit path |
|----------------------|------------------|-----------------|-----------|
| | | | |

## 8. Privacy obligations

| Obligation | Requirement | Mechanism | Source (statute / link) |
|------------|-------------|-----------|-------------------------|
| Retention | | | |
| Access / portability | | | |
| Rectification | | | |
| Erasure | | | |
| Breach notification | | | |

## 9. Accepted risks

| Risk | Reason accepted | Owner | Review date |
|------|-----------------|-------|-------------|
| | | | |
