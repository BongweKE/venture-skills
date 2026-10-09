# Launch readiness checklist — template

Fill top to bottom. Every line needs evidence (a link, a query result, a test run — not a
verbal assurance), a verifier, and a status. A failed Product, Security, Privacy, or Data
line is a hard stop until fixed or formally waived.

**Release:** [name / ticket]  **Owner:** [name]  **Date:** [YYYY-MM-DD]
**Feature traceability row:** [FT-xxx]  **KPI it must move:** [metric]

## 1. Product

| # | Item | Evidence | Verifier | Status |
|---|------|----------|----------|--------|
| 1.1 | All acceptance criteria pass on the release candidate | [test-run link] | [name] | pass/fail/waived |
| 1.2 | Acceptance test maps to the traceability row | [row link] | [name] | |
| 1.3 | Known limitations listed | [link] | [name] | |

## 2. Security

| # | Item | Evidence | Verifier | Status |
|---|------|----------|----------|--------|
| 2.1 | Controls from `security-by-design` deployed | [control list] | [name] | |
| 2.2 | Control tests pass | [scan/audit link] | [name] | |
| 2.3 | Auth, session, and secret handling unchanged or verified | [link] | [name] | |

## 3. Privacy / compliance

| # | Item | Evidence | Verifier | Status |
|---|------|----------|----------|--------|
| 3.1 | Data map covers the feature's new data | [data map] | [name] | |
| 3.2 | Retention and deletion defined | [note] | [name] | |
| 3.3 | Statutory deadlines respected (`bd-context` §12) | [link] | [name] | |

## 4. Operations

| # | Item | Evidence | Verifier | Status |
|---|------|----------|----------|--------|
| 4.1 | Dashboard shows the new path | [dashboard] | [name] | |
| 4.2 | Alert fires on failure (tested) | [alert] | [name] | |
| 4.3 | Runbook exists and is current | [runbook] | [name] | |
| 4.4 | Rollback tested on the production path | [drill note] | [name] | |

## 5. Support

| # | Item | Evidence | Verifier | Status |
|---|------|----------|----------|--------|
| 5.1 | User documentation published | [doc] | [name] | |
| 5.2 | Escalation path reaches an on-call owner | [path] | [name] | |
| 5.3 | Known issues published to support | [link] | [name] | |

## 6. Data migration / backfill

| # | Item | Evidence | Verifier | Status |
|---|------|----------|----------|--------|
| 6.1 | Migration dry-run on a copy | [run link] | [name] | |
| 6.2 | Row counts verified before/after | [counts] | [name] | |
| 6.3 | Backfill reversible | [note] | [name] | |

## 7. Go-to-market

| # | Item | Evidence | Verifier | Status |
|---|------|----------|----------|--------|
| 7.1 | Pricing configured in product and billing | [config] | [name] | |
| 7.2 | Sales enablement note ready | [note] | [name] | |
| 7.3 | Internal and customer comms scheduled | [plan] | [name] | |

## Go/no-go decision

- Outcome: **go / conditional go / no-go**
- Decision owner: [name]  **Time:** [timestamp]
- Evidence reviewed: [links]
- Conditions (if conditional): [list with owners and dates]
- Blockers (if no-go): [list with owners and dates]

## Waivers

| Item | Who accepted the risk | Why | Date |
|------|-----------------------|-----|------|
| [item] | [name] | [reason] | [date] |
