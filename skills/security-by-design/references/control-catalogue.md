# Control Catalogue — Control by Boundary

The reference behind steps 2, 4, 5, 6, and 7 of the skill. For each control: what it is, why it matters, how to verify it, and the STRIDE letter it addresses. Pick the controls that fit the system's boundaries — do not bolt on the whole table. Implementation of row-level security belongs to `supabase`; exploitation testing belongs to `web-pentest`; static review belongs to `requesting-code-review`.

## Identity and access

| Control | What / why | Verify by | STRIDE |
|---------|------------|-----------|--------|
| Managed identity + MFA | Never store passwords yourself; MFA blunts credential theft | Config inspection; MFA enrolment test | Spoofing |
| Short-lived, revocable sessions/tokens | Limits the blast radius of a stolen token | Token lifetime and revocation test | Spoofing, Elevation |
| Least privilege on service accounts | A compromised service cannot exceed its role | Review IAM policy vs actual calls | Elevation |
| Authorization at the data layer (RLS / row scoping) | App-layer-only checks leak when one query forgets a filter | Cross-tenant probe must return empty/404 | Information disclosure, Elevation |
| Separation of duties on admin paths | Prevents one compromised admin from total control | Test admin flows; require two-party for destructive ops | Elevation |

## Data protection

| Control | What / why | Verify by | STRIDE |
|---------|------------|-----------|--------|
| TLS everywhere (internal too) | Blocks in-flight interception | Certificate/mTLS check on internal calls | Information disclosure, Tampering |
| Encryption at rest | Protects data if storage is exposed | Storage config; key management review | Information disclosure |
| Data minimization | Less data stored is less data to lose | Map each field to a stated purpose | Information disclosure |
| Tokenization / field encryption for sensitive fields | Keeps raw secrets out of general queries | Inspect schema for protected columns | Information disclosure |
| Verified backups with tested restore | Ransomware/corruption recovery | Run a restore drill; record RTO/RPO | Tampering |

## Input and output

| Control | What / why | Verify by | STRIDE |
|---------|------------|-----------|--------|
| Allow-list input validation at each boundary | Rejects malformed/malicious input early | Boundary input fuzzing (via web-pentest) | Tampering, Elevation |
| Context-aware output encoding | Stops injection (HTML, SQL, shell, URL) | Static scan + crafted payloads | Tampering |
| Parameterized queries / ORM | Removes SQL injection by construction | Code review for string-built SQL | Tampering |
| Safe deserialization and upload handling | Blocks RCE and stored-XSS vectors | Upload test with disallowed types | Elevation |
| CSRF protection and SameSite cookies | Blocks cross-site state changes | Forged-request test | Tampering |

## Availability

| Control | What / why | Verify by | STRIDE |
|---------|------------|-----------|--------|
| Rate limits and quotas | Protects auth, enumeration, and payment paths | Load/probe test to trigger limits | Denial of service |
| Timeouts and circuit breakers | One dead dependency must not cascade | Fault injection (`system-design-theory` §3) | Denial of service |
| Bounded queues and backpressure | Prevents OOM from a slow consumer | Load test past capacity | Denial of service |
| Idempotency keys on mutations | Makes retries and replays safe | Duplicate-request test | Tampering |

## Audit and accountability

| Control | What / why | Verify by | STRIDE |
|---------|------------|-----------|--------|
| Tamper-evident audit log | Enables non-repudiation and forensics | Attempt to alter/delete a log entry | Repudiation |
| Structured logs without personal payloads | Trace without leaking | Inspect sample logs for PII | Information disclosure |
| Alerts on auth/authorization anomalies | Detects attacks in progress | Fire a synthetic failure; confirm alert | Repudiation, Elevation |

## Privacy controls

| Control | What / why | Verify by |
|---------|------------|-----------|
| Purpose-bound collection | Only lawful, necessary data | Field-to-purpose map |
| Retention + automated deletion | Bounds exposure and meets law | Deletion job test on aged records |
| Subject-rights paths (access, portability, rectification, erasure) | A right you cannot exercise is a violation | End-to-end DSAR exercise |
| Breach detection and notification | Statutory duty | Tabletop drill; confirm owner and deadline |

## Supply chain

| Control | What / why | Verify by |
|---------|------------|-----------|
| Pinned, locked dependencies | Reproducible, auditable builds | Lockfile present; diff on update |
| Dependency review before adoption | Fewer maintainers, fewer risks | Review transitive tree and maintainer activity |
| Third-party data-flow register | Know who sees what, and the exit path | Per-vendor entry with agreement reference |

## Choosing controls

Map each control to a boundary and a threat from the threat model. A control with no mapped threat is scope creep; a threat with no control is a finding. Record the residual risk for anything left uncontrolled and give it an owner.
