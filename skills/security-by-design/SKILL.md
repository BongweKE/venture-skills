---
name: security-by-design
description: "When the user wants to design security and privacy controls into a system before and during the build. Use when they mention 'threat model', 'STRIDE', 'abuse case', 'security requirements', 'privacy by design', 'data classification', 'auth model', 'authorization rules', 'data-scoping', 'secrets management', 'security acceptance criteria', 'security gate', or a pre-launch security checklist. References web-pentest and requesting-code-review for testing and review, and supabase for row-level security. For exploitation testing, see web-pentest."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-to-app
  related-skills: [web-pentest, requesting-code-review, supabase, prd-to-system-design, feature-traceability, launch-readiness, system-design-theory]
  triggers: [threat model, STRIDE, abuse case, security requirements, privacy by design, data classification, authorization rules, secrets management, security acceptance criteria, security gate]
---

# Security and Privacy by Design

You produce the security and privacy controls a system must have while it is being designed and built — before there is a running exploit to test. Your outputs are a threat model, per-story security acceptance criteria, a pre-build gate, and a pre-launch control checklist. You do not re-teach testing or exploitation: `web-pentest` finds the holes, `requesting-code-review` gates the code, `supabase` implements row-level security, and this skill decides what must be true for the design to be safe.

## Before Starting

Check `.agents/bd-context.md` first and only gather what it does not already answer: section 2 (market, currency and payment rails, the regulatory and data-protection regime, licensing), section 12 (legal, ethical, and brand non-negotiables), and any data-sensitivity note in section 1. Then confirm: the data-protection regime that applies, the system design or feature list you are protecting (if a design exists, read it — ideally the output of `prd-to-system-design`), and who the tenants and data subjects are (multi-tenant? consumer? employee data?). If the regime is unknown, treat it as strict and mark it `[ASSUMED]`.

## When to Use

- A design or PRD exists and the user wants the security and privacy requirements before building.
- The user asks for a threat model, abuse cases, or security acceptance criteria.
- The user is defining an auth/authorization model, including data-scoping or row-level rules.
- The user needs a pre-build security gate or a pre-launch control checklist.
- The user is handling personal or regulated data and needs retention and subject-rights controls.

**Don't use for:** offensive testing or exploiting a running app — that is `web-pentest`. Reviewing a diff or PR for security before commit — that is `requesting-code-review`. Implementing Postgres/Supabase row-level security syntax — that is `supabase`. Deep resilience and consistency theory — that is `system-design-theory`. Final go/no-go acceptance for a launch — that is `launch-readiness`.

## 1. Classify data and map the flows

- Classify every data element: **Public / Internal / Confidential / Regulated-personal / Regulated-sensitive**. Health, financial, and biometric data default to the highest tier.
- Map the data flow: source, processor, store, consumers, egress. Mark every **trust boundary** — browser to server, service to service, tenant to tenant, system to third party. Every boundary is where a control must sit.
- If a data-protection law applies, record the **lawful basis** and **purpose** for each personal-data element. Purpose and retention are design inputs, not paperwork.

Output: a classification table and a flow sketch inside the threat model ([templates/threat-model.md](templates/threat-model.md)).

## 2. Threat-model per trust boundary (STRIDE)

Apply STRIDE at each boundary as a table, one row per threat. Per-element prompts and controls: [references/control-catalogue.md](references/control-catalogue.md).

| STRIDE | Question at the boundary | Typical control |
|--------|--------------------------|-----------------|
| Spoofing | Can identity be faked? | MFA, signed tokens, service auth |
| Tampering | Can data or requests be altered in flight? | TLS, integrity checks, input validation |
| Repudiation | Can an actor deny an action? | Audit log, non-repudiable events |
| Information disclosure | Can data leak across a boundary? | Least privilege, data-scoping, encryption |
| Denial of service | Can the boundary be exhausted? | Rate limits, quotas, timeouts |
| Elevation of privilege | Can a lower role gain higher rights? | Authorization checks, RLS, separation of duties |

- For each threat record: likelihood times impact, the control, and the **residual risk**. A threat you cannot mitigate becomes an accepted risk with a named owner — never a silent omission.
- Run the model against the design's NFRs: an availability target implies DoS controls; a multi-tenant model implies isolation controls.

## 3. Enumerate abuse cases

For each user story or functional requirement, write the abuse case: who misuses this, to what end, and what the system must refuse. Abuse cases become the negative tests that `web-pentest` and `requesting-code-review` later check. Cover at minimum: cross-tenant privilege escalation, IDOR / object-reference tampering, mass assignment, payment or credit manipulation, and enumeration or rate abuse.

## 4. Define the authentication and authorization model

- **Authentication:** default to the platform's managed identity with MFA available; never build password storage yourself. State session lifetime, token type, and revocation path.
- **Authorization:** decide the model explicitly. **Default: role-based access control with attribute scoping per tenant** — tenant scope is a first-class column on every tenant-owned row. Add policy checks only where roles are insufficient.
- **Data-scoping / row-level rules:** for every table holding tenant or user data, "a principal may only touch rows in its scope" must be enforced at the **data layer**, not only in application code. For Postgres/Supabase implement this as row-level security and let `supabase` own the syntax, policy testing, and `auth.uid()` patterns — do not re-derive them here.
- Produce a **permission matrix**: role times resource times action, with a scope column. It is an acceptance artifact, not a footnote.

## 5. Manage secrets and keys

- **Rule:** no secret, key, or token in source, config files, or logs. Use a managed secret store or environment injection; rotate on a schedule and on staff change.
- Classify keys (signing, encryption, API) and state who holds each. Encryption keys get their own lifecycle and must not sit beside the data they protect.
- State the encryption posture: in transit (TLS everywhere, internal traffic too) and at rest (platform-managed minimum; customer-managed where a contract demands it).

## 6. Handle input and output safely

- Validate input at every trust boundary — allow-list, type, length, range — and reject by default.
- Encode output per context (HTML, SQL, shell, URL); never rely on one global filter.
- Set safe defaults for uploads, redirects, and deserialization: deny external redirects and executable uploads unless explicitly required.
- These are design rules. The concrete testing belongs to `requesting-code-review` (static scan) and `web-pentest` (dynamic).

## 7. Assess dependency and supply-chain risk

- Pin dependencies and lockfiles; review new transitive dependencies before adding them.
- For each third-party service or library that touches sensitive data, record what data it receives, under what agreement, and the exit path.
- Watch for typosquatting, unmaintained packages, and install-time scripts. Prefer fewer, well-maintained dependencies.

## 8. Meet privacy obligations

- **Retention:** define a retention period per data class and an automated deletion or enforcement mechanism. "Forever" is a finding.
- **Subject rights:** design the export and erasure paths (access, portability, rectification, erasure) before launch — a right you cannot exercise is a violation.
- **Minimization:** collect only what a stated purpose needs; log audit events without logging personal payloads.
- **Breach:** state the detection and notification obligation (who, how fast) as a design requirement.
- Map each obligation to the regime named in `bd-context` section 2. Cite the statute; never assert a legal requirement without a source.

## 9. Write security acceptance criteria per user story

Attach security acceptance criteria to stories beside functional ones, in given-when-then form, so they are testable and traceable (feed them into `feature-traceability`). Example: "Given a user in tenant A, when they request a record owned by tenant B, then the API returns 404 and logs the attempt." Every abuse case from step 3 becomes at least one criterion.

## 10. Run the gates

- **Pre-build security gate** (before implementation starts): data classification, threat model, auth model, and permission matrix exist and are agreed. No gate, no build — record the sign-off.
- **Pre-launch control checklist** from [templates/control-checklist.md](templates/control-checklist.md): every control from the threat model is implemented, verified, and owned; secrets are out of code; data-scoping is tested; retention and subject-rights paths are exercised; logging and alerting are live. Pair the checklist with `requesting-code-review` (pre-commit scan) and a `web-pentest` engagement for independent verification.

## Output

Three artifacts:

1. A **threat model** from [templates/threat-model.md](templates/threat-model.md) — classification table, data-flow and trust boundaries, STRIDE rows, abuse cases, permission matrix.
2. **Security acceptance criteria** per user story (given-when-then), ready to attach to tickets.
3. A **pre-launch control checklist** from [templates/control-checklist.md](templates/control-checklist.md), with owners.

## Common Pitfalls

1. **Treating security as a post-build gate.** Controls designed after the schema is set cost a rewrite; model the boundary first.
2. **Threat-modeling once and filing it.** Re-run it for every new external interface or data class.
3. **App-layer-only authorization.** If one query forgets the scope filter, tenants leak — enforce scope at the data layer.
4. **Re-teaching RLS or exploitation.** Point to `supabase` and `web-pentest`; spend the tokens on the decision and the criteria.
5. **Secrets in config.** A key committed to a repo is already leaked; assume rotation.
6. **"Retention: forever."** An undefined retention period is a compliance finding, not a default.
7. **Asserting legal obligations without a source.** Cite the regime from `bd-context`; label assumptions.
8. **Unmitigated threats with no owner.** An accepted risk without a named owner is an orphaned risk.

## Verification Checklist

- [ ] Every data element classified; trust boundaries marked.
- [ ] STRIDE run at every boundary; each threat has a control, residual risk, and owner.
- [ ] Abuse cases written per story, covering cross-tenant access, IDOR, mass assignment, payment, and rate abuse.
- [ ] Authn/authz model chosen; permission matrix (role, resource, action, scope) written.
- [ ] Data-scoping / row-level rules specified per sensitive table, with `supabase` named as the implementation path.
- [ ] Secrets and keys: none in code, config, or logs; lifecycle and rotation stated.
- [ ] Input validation and context-aware output encoding specified as design rules.
- [ ] Dependencies pinned; third-party data flows and exit paths recorded.
- [ ] Retention, subject rights, minimization, and breach obligations mapped to the named regime with a source.
- [ ] Security acceptance criteria attached to each user story.
- [ ] Pre-build gate signed off; pre-launch checklist complete with owners and verification evidence.

## References

- [references/control-catalogue.md](references/control-catalogue.md) — control-by-boundary catalogue: what each control is, why it matters, how to verify it, and its STRIDE mapping.
