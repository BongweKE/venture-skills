# Pre-Launch Security Control Checklist — <Release>

**Version:** 0.1.0 · **Date:** <YYYY-MM-DD> · **Release:** <name/tag>
**Threat model:** <link> · **Signed off by:** <name>

Every row needs an owner and a piece of **verification evidence** (a test, a screenshot, a log line, a config path) — not an assertion. Do not ship with an unticked row unless it is an accepted risk recorded in the threat model.

## Gate A — Pre-build (before implementation starts)

- [ ] Data classification complete; every element assigned a tier.
- [ ] Trust boundaries identified and mapped.
- [ ] STRIDE run at every boundary; each threat has a control and owner.
- [ ] Authn/authz model chosen; permission matrix agreed.
- [ ] Data-scoping rules specified per sensitive table.
- [ ] Privacy obligations mapped to the named regime with a source.

Sign-off needed before code: ______ (name, date).

## Gate B — Pre-launch (before release)

### Access control

- [ ] Every sensitive table has data-scoping / RLS enabled and tested with a cross-tenant probe.
- [ ] No endpoint relies on client-side authorization.
- [ ] Least privilege applied to service accounts and roles.
- [ ] MFA available; admin paths protected and audited.

### Secrets and data

- [ ] No secret, key, or token in source, config, or logs (verified by scan).
- [ ] Secrets in a managed store; rotation schedule set; keys separated from the data they protect.
- [ ] TLS enforced in transit (external and internal); encryption at rest in place.
- [ ] Personal payloads excluded from logs; audit events recorded instead.

### Input / output / abuse

- [ ] Input validated at every trust boundary; output encoded per context.
- [ ] Every abuse case from the threat model has a passing negative test.
- [ ] Rate limits and quotas on authentication, enumeration-prone, and payment endpoints.
- [ ] Safe defaults for uploads, redirects, and deserialization.

### Supply chain

- [ ] Dependencies pinned; lockfiles committed.
- [ ] Third-party data flows and exit paths recorded.
- [ ] No unexplained install-time scripts or typosquat-risk packages.

### Privacy and operations

- [ ] Retention enforced by an automated mechanism per data class.
- [ ] Export (access/portability) and erasure paths exercised end to end.
- [ ] Breach detection and notification path defined and owned.
- [ ] Logging and alerting live for authentication, authorization failures, and privilege changes.

### Independent verification

- [ ] `requesting-code-review` pre-commit security scan run, findings resolved.
- [ ] `web-pentest` engagement completed for the release surface; findings triaged.
- [ ] Accepted risks recorded with owner and review date.

Release decision: ship / ship-with-accepted-risks / hold — ______ (name, date).
