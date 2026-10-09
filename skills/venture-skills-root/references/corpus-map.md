# Corpus map: where venture-skills hands off

venture-skills owns the WHY and the WHAT. The wider installed corpus owns the
HOW. This map records the handoff points so a stage skill never re-teaches craft
that already has a better home.

Every skill named here is present in the live corpus of the four runtimes. The
machine-readable list of cross-link targets is `catalog/known-skills.public.txt`
(committed) merged with `catalog/known-skills.local.txt` (generated locally,
gitignored — it is a snapshot of one machine and is never published).

## UI and UX

Load at: stage 8 (product-discovery), stage 10 (prd-to-system-design), and
whenever a requirement is about how something looks, reads or feels.

- `baseline-ui` - the default visual and interaction baseline before styling.
- `improve-ui` - raising an existing screen to a considered standard.
- `fixing-accessibility` - concrete a11y defects on a real interface.
- `wcag-audit-patterns` - systematic WCAG 2.2 audit method.
- `design-system-patterns` - tokens, theming, component API shape.
- `interaction-design` - state, motion, feedback, micro-interactions.
- `responsive-design` - layout across viewports; container queries.
- `visual-design-foundations` - type, colour, spacing, iconography.
- `fixing-metadata` - titles, descriptions, social cards.
- `create-design-md` - authoring the design token spec.

Handoff rule: a PRD names the *user-visible outcome and its acceptance
criteria*. It does not specify pixels. Pass the outcome to these skills.

## Marketing and growth

Load at: stage 3 (value-proposition-and-pricing), stage 4 (demand), and for any
question about traffic, conversion or lifecycle that is not a sales motion.

- `revops` - lead lifecycle, routing, scoring, handoff to sales.
- `cro` - conversion rate work on a specific funnel step.
- `seo-audit` - technical and content search diagnostics.
- `content-strategy` - what to publish, for whom, in what order.
- `analytics` - measurement plan, events, definitions.
- `attribution` - which channel gets credit, and its limits.
- `marketing-psychology` - why a message lands or does not.
- `ab-testing` - designing an experiment that can actually conclude.
- `brand-landingpage` - brand-first page construction.
- `social-publishing` - scheduling and publishing across platforms.
- `kpi-dashboard-design` - metric hierarchy for a dashboard.
- `data-storytelling` - turning analysis into a decision.

Handoff rule: `outbound-sequencing` is a one-to-one sales motion. If the channel
is one-to-many (search, content, ads, lifecycle email), it is these skills, not
that one.

## Support and customer journey

Load at: stage 7 (qbr-and-renewal), stage 13 (sop-to-automation), stage 14
(launch-readiness), and for any post-sale interaction.

- `incident-runbook-templates` - the runbook a responder actually follows.
- `on-call-handoff-patterns` - context transfer between shifts.
- `postmortem-writing` - blameless analysis that changes something.
- `email-inbox-triage` - prioritising an inbound queue safely.
- `meeting-action-items` - decisions, owners, deadlines from notes.
- `document-to-action-items` - obligations and deadlines from contracts.
- `customer-research` - interview and synthesis method.
- `churn-prevention` - cancellation flows and save motions.
- `team-communication-protocols` - structured messaging between people.

Handoff rule: stage 14 requires a support path for everything being launched. If
the feature can fail for a user, a runbook and a ticket route must exist before
go-live, and they come from this category.

## Engineering and security

Load at: stage 10 (prd-to-system-design), stage 11 (security-by-design), stage
12 (feature-traceability), and for all implementation.

- `system-design-theory` - distributed design, scaling, trade-offs.
- `architecture-decision-records` - recording and superseding decisions.
- `api-design-principles` - REST and GraphQL interface design.
- `microservices-patterns` - boundaries, contracts, failure isolation.
- `before-you-build` - pre-build product and feature risk review.
- `postgresql-table-design` - schema, keys, constraints, indexes.
- `sql-optimization-patterns` - query plans and indexing strategy.
- `test-driven-development` - RED-GREEN-REFACTOR discipline.
- `e2e-testing-patterns` - browser-level verification.
- `deployment-pipeline-design` - staged pipelines and approval gates.
- `stride-analysis-patterns` - systematic threat enumeration.
- `threat-mitigation-mapping` - threats to controls, with coverage.
- `security-requirement-extraction` - turning threats into requirements.
- `source-code-security-audit` - auditing a codebase for real defects.
- `tob-supply-chain-risk-auditor` - third-party and dependency risk.
- `web-pentest` - authorised application penetration testing.
- `secrets-management` - secret storage, rotation, CI hygiene.

Handoff rule: `security-by-design` produces the threat model and the required
controls *as requirements*. It never writes the control. `secrets-management`
writes the control; `security-requirement-extraction` is the bridge between the
two when the threat model is large.

## The two-way rule

Cross-linking runs in both directions.

- A stage skill names the corpus skill that implements its artifact.
- When a corpus skill is used and it surfaces a commercial consequence (a cost, a
  compliance obligation, a segment that cannot be served, a launch blocker), that
  consequence is written back into the relevant stage artifact, not silently
  absorbed.

That second direction is what stops this suite from being a one-time planning
exercise. A threat model that finds an unbudgeted control is a change to the
PRD. A CRO test that changes the promise is a change to positioning.
