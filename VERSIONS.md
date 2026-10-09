# Versions

Suite-level changelog. The shared `x.y.z` number follows: **x** = restructure,
**y** = new skill added, **z** = update to an existing skill. Per-skill versions
live in each `SKILL.md` under `metadata.version`.

## 1.0.0

Initial release of the business-development suite — 13 skills:

- `bd-context` — foundation document `.agents/bd-context.md`
- `market-segmentation` — ICP, TAM/SAM/SOM, segment prioritisation, frameworks
- `competitive-intelligence` — teardowns and battlecards
- `value-proposition-and-pricing` — positioning, ROI business case, packaging/pricing
- `prospect-research` — verified, scored target lists
- `outbound-sequencing` — multi-touch cadences and copy
- `discovery-call` — call prep, MEDDPICC, follow-up
- `proposal-and-quote` — proposals, SOWs, quotes
- `objection-handling` — objection library and negotiation planning
- `pipeline-forecast` — stage gates, CRM hygiene, forecast model
- `account-planning` — strategic account plans and expansion
- `qbr-and-renewal` — QBRs, renewals, churn saves
- `win-loss-review` — post-decision debriefs and pattern synthesis

Tooling: `scripts/validate.py` (open-standard validator), `deploy.py` (installs
the suite into Hermes, OpenCode, Antigravity CLI, and Mistral Vibe).
