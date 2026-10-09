# Skill catalog: building software under business leadership

This is the linkage layer. It maps one continuous pipeline — *market evidence ->
business case -> product definition -> system design -> build -> verify -> ship
-> operate -> sell -> learn* — onto the concrete skills that serve each stage.

Three sources:

- **repo** — authored here (`skills/`). The business-development layer and the
  business-to-app bridge it owns.
- **installed** — skills already present in your agents across Hermes, OpenCode,
  Antigravity and Vibe. Generated into [`known-skills.txt`](known-skills.txt).
- **curated** — third-party skill sets vetted in
  [`../registry/sources.json`](../registry/sources.json), installed on demand by
  [`../scripts/install-external.py`](../scripts/install-external.py), credited in
  [`../CREDITS.md`](../CREDITS.md).

Every skill name below is checked against `known-skills.txt` by
`tests/catalog.test.mjs`. Do not cite a skill that is not installed; a catalog
that points at skills you do not have is worse than no catalog.

The rule this catalog enforces: **no stage starts without the artifact the
previous stage is supposed to produce.** Research without an opportunity brief is
a hobby; a feature without a KPI is a cost centre.

See [`../docs/linking-model.md`](../docs/linking-model.md) for why the layers are
split this way.

---

## The pipeline at a glance

| # | Stage | Question answered | Produces | Repo skill |
|---|-------|-------------------|----------|------------|
| 0 | Context | Who are we, who do we sell to, what binds us? | `.agents/bd-context.md` | `bd-context` |
| 1 | Market | Is there a market, and is it ours? | segmentation memo, segment scorecard | `market-segmentation` |
| 2 | Opportunity | Is *this* worth building, and why now? | opportunity brief, go/no-go | `product-discovery` |
| 3 | Define | What are we building and how do we know it worked? | PRD with KPIs | `business-need-to-prd` |
| 4 | Design | How will it be built, and how will it be safe? | design doc, ADRs, threat model | `prd-to-system-design`, `security-by-design` |
| 5 | Build | Implement it to a professional standard | working software | (installed; see Build) |
| 6 | Verify | Is it correct, tested, reviewed, secure? | test evidence, review record | (installed; see Verify) |
| 7 | Ship | Can we safely put this in front of customers? | readiness sign-off, rollout plan | `launch-readiness` |
| 8 | Operate | Does it keep running and keep matching the SOP? | runbooks, alerts, SOP compliance | `sop-to-automation` |
| 9 | Sell and grow | Does it win deals and retain accounts? | pipeline, proposals, QBRs | `competitive-intelligence`, `prospect-research`, `outbound-sequencing`, `discovery-call`, `proposal-and-quote`, `objection-handling`, `pipeline-forecast`, `account-planning`, `qbr-and-renewal` |
| 10 | Learn | Did the bet pay off, and what do we change? | win/loss themes, traceability review | `win-loss-review`, `feature-traceability` |

`feature-traceability` is the thread running through stages 1 to 10: every epic
keeps a live link back to the KPI, persona, SOP and control it exists to serve.

---

## Stage detail

### 0-1 Context and market

| Need | Use | Source |
|------|-----|--------|
| Write the foundation doc once | `bd-context` | repo |
| Size and rank segments, SWOT/Porter/PESTEL | `market-segmentation` | repo |
| Market and competitor evidence with citations | `grounded-citations`, `competitor-news-monitor`, `domain-intel` | installed |
| Market sizing arithmetic | `market-sizing-analysis` | curated |
| Competitor teardowns and battlecards | `competitive-intelligence` | repo |
| Competitive landscape framing | `competitive-landscape` | curated |
| Offer, packaging and price design | `value-proposition-and-pricing` | repo |
| Business-model and runway arithmetic | `startup-financial-modeling`, `startup-metrics-framework` | curated |

### 2-3 Opportunity and definition

| Need | Use | Source |
|------|-----|--------|
| Evidence-backed opportunity brief, go/no-go | `product-discovery` | repo |
| PRD with non-negotiable KPIs | `business-need-to-prd` | repo |
| Turn an SOP into requirements | `sop-to-automation` | repo |
| Pre-build product and feature risk review | `before-you-build` | curated |
| Context artifacts kept current | `context-driven-development` | curated |
| Metric hierarchy for a dashboard | `kpi-dashboard-design`, `data-storytelling` | curated |
| Customer research and synthesis | `customer-research` | curated |

### 4 Design and security

| Need | Use | Source |
|------|-----|--------|
| PRD to architecture, ADRs, NFRs | `prd-to-system-design` | repo |
| Deep systems-design theory (do not restate) | `system-design-theory` | installed |
| Diagrams | `architecture-diagram`, `excalidraw` | installed |
| Recording and superseding decisions | `architecture-decision-records` | curated |
| Architecture and service-boundary patterns | `architecture-patterns`, `microservices-patterns` | curated |
| API contract design | `api-design-principles`, `openapi-spec-generation` | curated |
| Threat model, controls, data classification | `security-by-design` | repo |
| Systematic threat enumeration | `stride-analysis-patterns`, `attack-tree-construction` | curated |
| Threats to controls mapping | `threat-mitigation-mapping`, `security-requirement-extraction` | curated |
| Data-layer design and row-level security | `supabase`, `supabase-postgres-best-practices`, `neon-postgres`, `postgresql-table-design` | installed + curated |
| Auth model design | `auth-implementation-patterns` | curated |
| Privacy and payment obligations | `gdpr-data-handling`, `pci-compliance` | curated |
| Payload contract and API shape debugging | `rest-graphql-debug` | installed |

### 5 Build

| Need | Use | Source |
|------|-----|--------|
| Plan the work in bite-sized tasks | `plan`, `writing-plans` | installed |
| De-risk an unknown before committing | `spike` | installed |
| Test-first discipline | `test-driven-development` | installed |
| Parallel agent execution of a plan | `subagent-driven-development` | installed |
| Frontend craft | `baseline-ui`, `improve-ui`, `vercel-react-best-practices`, `vercel-web-design-guidelines`, `design-md` | installed |
| Interaction and visual systems | `interaction-design`, `visual-design-foundations`, `design-system-patterns`, `tailwind-design-system`, `web-component-design` | curated |
| Responsive and accessible interfaces | `responsive-design`, `wcag-audit-patterns`, `fixing-accessibility`, `accessibility-compliance` | curated |
| Mobile platforms | `mobile-ios-design`, `mobile-android-design`, `flutter-*`, `dart-*`, `expo-*` | curated + installed |
| Backend and API implementation | `nodejs-backend-patterns`, `nextjs-app-router-patterns` | curated |
| Query and schema performance | `sql-optimization-patterns` | curated |
| Secret handling in code | `secrets-management` | curated |

### 6 Verify

| Need | Use | Source |
|------|-----|--------|
| Root-cause debugging before fixing | `systematic-debugging` | installed |
| Structured code review | `requesting-code-review`, `codebase-inspection` | installed |
| Security testing (exploitation) | `web-pentest`, `source-code-security-audit` | installed |
| Exploit-class deep dives | `idor-testing-methodology`, `jwt-attacks`, `oauth-oidc-attacks`, `saml-attacks`, `ssrf-testing`, `mass-assignment-method-tampering`, `business-logic-flaws` | installed |
| Supply-chain and audit tooling | `tob-supply-chain-risk-auditor`, `tob-semgrep`, `tob-codeql`, `tob-coverage-analysis` | installed |
| Exploratory QA of the running app | `dogfood`, `anthropic-webapp-testing` | installed |
| Browser-level verification | `e2e-testing-patterns` | curated |
| Accessibility conformance testing | `screen-reader-testing` | curated |
| Runtime debugging | `node-inspect-debugger`, `python-debugpy`, `rest-graphql-debug` | installed |
| Cleanup before merge | `simplify-code` | installed |

### 7 Ship

| Need | Use | Source |
|------|-----|--------|
| Go/no-go gate, rollout, rollback triggers | `launch-readiness` | repo |
| Prove the deployed change is actually live | `deployed-change-verification` | installed |
| Deploy targets | `vercel-deploy-to-vercel`, `cloudflare-edge-deployments`, `railway-use-railway`, `google-cloud-run-basics`, `google-gke-basics` | installed |
| Staged pipelines and approval gates | `deployment-pipeline-design` | curated |
| Launch planning and comms | `launch`, `marketing-plan` | curated |

### 8 Operate and support

| Need | Use | Source |
|------|-----|--------|
| Turn the SOP into enforced workflow | `sop-to-automation` | repo |
| Service levels and error budgets | `slo-implementation` | curated |
| Incident runbooks | `incident-runbook-templates` | curated |
| Shift handoff and escalation | `on-call-handoff-patterns`, `team-communication-protocols` | curated |
| Blameless postmortems | `postmortem-writing` | curated |
| Inbound support triage | `email-inbox-triage` | installed |
| Commitments and deadlines out of documents | `document-to-action-items`, `meeting-action-items` | installed |
| Uptime and dependency watching | `site-availability-diagnosis`, `watchers`, `webhook-subscriptions` | installed |
| Ops documentation | `documentation-corpus-build` | installed |

### 9-10 Sell, grow, learn

The whole business-development layer applies here: `competitive-intelligence`,
`prospect-research`, `outbound-sequencing`, `discovery-call`,
`proposal-and-quote`, `objection-handling`, `pipeline-forecast`,
`account-planning`, `qbr-and-renewal`, `win-loss-review`.

Supporting curated skills: `revops`, `sales-enablement`, `cro`, `analytics`,
`attribution`, `seo-audit`, `content-strategy`, `site-architecture`,
`marketing-psychology`, `ab-testing`, `onboarding`, `churn-prevention`,
`emails`, `copywriting`, `brand-landingpage`, `social-publishing`,
`employment-contract-templates`.

Then `feature-traceability` closes the loop by re-checking that each shipped
feature moved the KPI it was justified by.

---

## "I want to do X" quick index

| I want to | Load |
|-----------|------|
| Know where to start | `venture-skills-root` |
| Set up my business context | `bd-context` |
| Decide whether an idea is worth building | `product-discovery` |
| Write a spec engineers can build from | `business-need-to-prd` |
| Convert a manual process into software | `sop-to-automation` |
| Turn a spec into architecture | `prd-to-system-design` |
| Make sure it is secure before I write code | `security-by-design` |
| Prove every feature earns its place | `feature-traceability` |
| Know if it is safe to go live | `launch-readiness` |
| Design the interface | `baseline-ui`, `interaction-design`, `design-system-patterns` |
| Make it accessible | `wcag-audit-patterns`, `fixing-accessibility` |
| Get more traffic or conversions | `cro`, `seo-audit`, `content-strategy`, `analytics` |
| Handle support and incidents | `incident-runbook-templates`, `on-call-handoff-patterns`, `email-inbox-triage` |
| Price and package it | `value-proposition-and-pricing` |
| Quote or propose it | `proposal-and-quote` |
| Plan and build it | `plan`, `writing-plans`, `test-driven-development`, `subagent-driven-development` |
| Review and harden it | `requesting-code-review`, `web-pentest`, `systematic-debugging` |
| Ship it | `launch-readiness`, `deployed-change-verification` |
| Sell it | `prospect-research` -> `outbound-sequencing` -> `discovery-call` -> `proposal-and-quote` |
| Keep and grow the account | `account-planning`, `qbr-and-renewal` |
| Learn why we won or lost | `win-loss-review` |

---

## Maintaining this catalog

1. `python3 scripts/gen-known-skills.py` — refresh `known-skills.txt` from the
   agents' live corpora after installing or removing skills.
2. Update the stage tables when a new repo skill lands.
3. `npm test` — `tests/catalog.test.mjs` fails if this file cites a skill that is
   not installed, or if it points at a `known-skills.txt` entry that has since
   disappeared.
4. `python3 scripts/validate.py` — every `related-skills` entry must resolve in
   this repo or in `known-skills.txt`.
5. `python3 scripts/deploy.py` — install into the four runtimes.
