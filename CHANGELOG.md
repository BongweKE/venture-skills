# Changelog

Notable changes to venture-skills. Format follows Keep a Changelog; versions
follow Semantic Versioning. Per-skill versions live in each skill's
`metadata.version`.

## 1.0.0

First public release.

### Added

- **21 authored skills** in two suites.
  - `business-development` (14): the commercial chain, from context to retention.
    `bd-context`, `market-segmentation`, `competitive-intelligence`,
    `value-proposition-and-pricing`, `prospect-research`, `outbound-sequencing`,
    `discovery-call`, `objection-handling`, `proposal-and-quote`,
    `account-planning`, `pipeline-forecast`, `qbr-and-renewal`,
    `win-loss-review`, and `venture-skills-root`.
  - `business-to-app` (7): the bridge from commercial intent to delivered
    software. `product-discovery`, `business-need-to-prd`,
    `prd-to-system-design`, `security-by-design`, `feature-traceability`,
    `sop-to-automation`, `launch-readiness`.
- **`venture-skills-root`**, the router skill: a fifteen-stage chain, task-to-skill
  routing, re-entry loops, and the WHY/HOW division with the wider corpus.
- **Curated registry** (`registry/sources.json`) with generated attribution in
  `CREDITS.md`. Two sources: `wshobson/agents` (47 skills) and
  `coreyhaines31/marketingskills` (18 skills). Overlapping skills are excluded by
  design so no two skills compete for the same trigger.
- **CLI** (`bin/venture-skills.mjs`), zero runtime dependencies: `list`, `info`,
  `get`, `registry`, `install`, `doctor`.
- **Deploy tooling** for all four runtimes, with drift detection: `scripts/deploy.py`
  and `scripts/install-external.py`.
- **Catalog registry** (`catalog/known-skills.txt`) generated from the live
  corpora, used to validate cross-references between skills.
- **Tests**: 184 assertions covering skill format, CLI behaviour and registry
  integrity, plus a Python validator and a GitHub Actions workflow.

### Changed

- The suite was renamed from a business-development-only repository to
  `venture-skills` to reflect the business-to-app bridge layer.

### Notes

- `skills/` is MIT. Curated third-party skills keep their upstream licences and
  are never vendored into this repository.
