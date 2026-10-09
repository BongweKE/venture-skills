# Versions

Suite-level changes are recorded in [`CHANGELOG.md`](CHANGELOG.md). This file
exists only to define the versioning scheme and to hold the per-skill version
table, so there is a single changelog to maintain.

## Scheme

The suite version is a single `x.y.z`:

- **x** — restructure: a skill added or removed, or the chain reordered.
- **y** — a new capability inside an existing skill that changes its routing or
  its output artifact.
- **z** — an edit that corrects or clarifies without changing routing or output.

Per-skill versions live in each `SKILL.md` under `metadata.version` and follow the
same logic for that skill alone. The suite version is what a runtime reports; the
per-skill version is what a contributor bumps in a pull request.

## Current

Suite version: **1.0.0**

| Suite | Skill | Version |
|---|---|---|
| business-development | `venture-skills-root` | 1.0.0 |
| business-development | `bd-context` | 1.0.0 |
| business-development | `market-segmentation` | 1.0.0 |
| business-development | `competitive-intelligence` | 1.0.0 |
| business-development | `value-proposition-and-pricing` | 1.0.0 |
| business-development | `prospect-research` | 1.0.0 |
| business-development | `outbound-sequencing` | 1.0.0 |
| business-development | `discovery-call` | 1.0.0 |
| business-development | `objection-handling` | 1.0.0 |
| business-development | `proposal-and-quote` | 1.0.0 |
| business-development | `account-planning` | 1.0.0 |
| business-development | `pipeline-forecast` | 1.0.0 |
| business-development | `qbr-and-renewal` | 1.0.0 |
| business-development | `win-loss-review` | 1.0.0 |
| business-to-app | `product-discovery` | 1.0.0 |
| business-to-app | `business-need-to-prd` | 1.0.0 |
| business-to-app | `prd-to-system-design` | 1.0.0 |
| business-to-app | `security-by-design` | 1.0.0 |
| business-to-app | `feature-traceability` | 1.0.0 |
| business-to-app | `sop-to-automation` | 1.0.0 |
| business-to-app | `launch-readiness` | 1.0.0 |
