---
name: venture-skills-root
description: "Use when a business, product or go-to-market task needs routing: start here to pick the right venture-skills stage, then link to the wider skill corpus for the how."
license: MIT
metadata:
  suite: business-development
  version: 1.0.0
  layer: router
  related-skills:
    - bd-context
    - product-discovery
    - business-need-to-prd
    - prd-to-system-design
    - security-by-design
    - launch-readiness
    - market-segmentation
    - value-proposition-and-pricing
    - discovery-call
    - pipeline-forecast
    - system-design-theory
    - test-driven-development
    - web-pentest
---

# Venture Skills: the entry point

This suite exists to make a coding agent behave like it was briefed by a
business, not dropped into a codebase. It turns commercial intent into a
shipped, defensible product in a fixed chain of stages.

It is a chain, not a pile. Each stage consumes the artifact the previous stage
produced, and the artifact is a file on disk, not a paragraph in a chat.

Start here. Pick the stage. Load exactly one stage skill. Write the artifact.
Hand off.

## Before Starting

1. Check `.agents/bd-context.md`. If it exists, read it: it holds the venture's
   positioning, buyer, pricing model and constraints. Every stage skill assumes it.
2. If it does not exist, run the `bd-context` skill first. It writes that file.
   Do not guess at positioning, buyer, or pricing to work around its absence.
3. State the stage you are entering and the artifact you will produce, in one
   line, before doing work. If you cannot name the artifact, you have not
   picked the right stage yet.
4. Check whether the deliverable already exists. Stages are re-entrant: if
   `.agents/prd/checkout.md` exists and is current, revise it instead of
   restarting the chain.
5. Ask: is this actually a venture-skills question, or an engineering question?
   If the answer does not change based on market, buyer, pricing or risk, it is
   an engineering question. Use the wider corpus instead (see below).

## When to Use

Use this skill when:

- A request starts from a market, customer, revenue or compliance question and
  has to end in software.
- A request starts from a product idea and needs to become a specification.
- You must decide *which* of the twenty skills applies and you are not certain.
- A task spans stages (for example "build the client onboarding flow we sold
  them") and you need to decompose it into stages before starting.
- You need to know which existing skill in the corpus already covers the "how"
  so you do not re-invent it.

Do not use this skill when:

- The task is a pure refactor, bug fix or performance change with no change to
  who uses it, what it costs, or what risk it carries. Go straight to the
  engineering skills.
- A single stage skill is already obviously the answer. Load that one directly;
  routing through the router wastes context.
- The user has explicitly named the skill they want.

## The chain

| # | Stage | Skill | Artifact it writes |
|---|-------|-------|--------------------|
| 0 | Foundation | `bd-context` | `.agents/bd-context.md` |
| 1 | Market | `market-segmentation` | `.agents/market/segments.md` |
| 2 | Competition | `competitive-intelligence` | `.agents/market/battlecards.md` |
| 3 | Offer | `value-proposition-and-pricing` | `.agents/offer/positioning.md`, ROI case |
| 4 | Demand | `prospect-research`, `outbound-sequencing` | `.agents/pipeline/<account>.md` |
| 5 | Conversation | `discovery-call`, `objection-handling` | `.agents/discovery/<account>.md` |
| 6 | Commitment | `proposal-and-quote` | `.agents/proposals/<account>.md` |
| 7 | Land and grow | `account-planning`, `pipeline-forecast`, `qbr-and-renewal`, `win-loss-review` | `.agents/accounts/`, forecast, QBR packs |
| 8 | Product | `product-discovery` | `.agents/product/opportunity-brief.md` |
| 9 | Specification | `business-need-to-prd` | `.agents/prd/<feature>.md` |
| 10 | System design | `prd-to-system-design` | `.agents/design/<feature>.md` |
| 11 | Trust | `security-by-design` | `.agents/security/<feature>-threat-model.md` |
| 12 | Traceability | `feature-traceability` | `.agents/traceability.md` |
| 13 | Automation | `sop-to-automation` | `.agents/automation/<process>.md` |
| 14 | Release | `launch-readiness` | `.agents/launch/<feature>.md` |

Stages 0 to 7 are the commercial half: they decide what is worth building and
what it is worth. Stages 8 to 14 are the delivery half: they turn that decision
into a specified, threat-modelled, traceable, launchable system.

The two halves meet at stage 8. `product-discovery` is the handoff point where a
commercial question becomes an engineering brief. If you are building something
and cannot point to the stage 8 brief that justified it, stop and go back.

Full task-to-skill lookup, including edge cases and re-entry rules:
`references/routing-table.md`.

## Working with the wider corpus

This suite deliberately does not teach engineering, design or security craft.
Those skills already exist and are better than anything this repo could
restate. The rule is:

- **venture-skills owns the WHY and the WHAT.** Which segment, which offer, which
  price, which requirement, which risk, which release gate.
- **The wider corpus owns the HOW.** How to type the API, how to lay out the
  screen, how to write the migration, how to configure the pipeline.

When a stage skill needs a "how", it names the corpus skill to load rather than
describing the craft itself. Do not restate them.

The four categories you will link to most:

- **UI and UX**: `baseline-ui`, `improve-ui`, `fixing-accessibility`,
  `design-system-patterns`, `interaction-design`, `wcag-audit-patterns`,
  `responsive-design`, `visual-design-foundations`.
- **Marketing and growth**: `revops`, `cro`, `seo-audit`, `analytics`,
  `attribution`, `content-strategy`, `marketing-psychology`, `ab-testing`.
- **Support and customer journey**: `incident-runbook-templates`,
  `on-call-handoff-patterns`, `postmortem-writing`, `email-inbox-triage`,
  `meeting-action-items`, `customer-research`, `churn-prevention`,
  `team-communication-protocols`.
- **Engineering and security**: `system-design-theory`,
  `architecture-decision-records`, `api-design-principles`,
  `postgresql-table-design`, `test-driven-development`, `web-pentest`,
  `stride-analysis-patterns`, `threat-mitigation-mapping`,
  `source-code-security-audit`, `tob-supply-chain-risk-auditor`,
  `secrets-management`.

A fuller map, with the link point for each stage:
`references/corpus-map.md`.

## Golden rules

These apply at every stage, in every runtime, without exception.

1. **Never fabricate evidence.** Do not invent market sizes, growth rates,
   benchmark percentages, survey results or customer quotes. If a figure is not
   sourced, it does not go in. Label every non-sourced belief as `[ASSUMPTION]`
   and state what would falsify it.
2. **Never invent commercial facts.** No made-up prices, payment rails, bank
   accounts, registration numbers or certifications. If a stage needs one, it is
   an input you must obtain from the user.
3. **Stay portable.** These skills ship publicly. No company-specific pricing,
   geography or compliance detail belongs in a skill body; that lives in
   `.agents/bd-context.md` for the engagement at hand.
4. **Artifacts are files.** If a stage produces a decision, write it to the path
   in the chain table. A decision that exists only in chat is not a decision.
5. **One stage at a time.** Loading all twenty skills floods context and degrades
   routing. Load the stage you are in, plus `bd-context`.
6. **State the trade-off.** Every recommendation names what it costs, what it
   forecloses, and what would change your mind.

## Common Pitfalls

- **Skipping stage 0.** Working without `.agents/bd-context.md` produces
  generic, unfalsifiable output. Create it first.
- **Treating the chain as linear.** It is iterative. `win-loss-review` routinely
  sends you back to `market-segmentation`; `security-by-design` routinely sends
  you back to `prd-to-system-design`.
- **Doing the HOW.** Spending a stage's budget writing component code or SQL is
  a routing failure: hand that to the corpus skill and keep the stage artifact
  commercial or specification-level.
- **Re-inventing existing skills.** Before writing guidance, check whether a
  corpus skill already covers it. If it does, link instead.
- **Bundling stages.** "Give me positioning, pricing, a PRD and a threat model"
  is four stages. Do them in order; later ones depend on earlier artifacts.
- **Fabricating to fill a template.** A template with an unsourced number in it
  is worse than a template with an explicit `[ASSUMPTION]` and a validation
  plan.
- **Shipping without stage 14.** A feature that has no `launch-readiness`
  artifact is not ready, regardless of test coverage.

## If nothing fits

If the request is genuinely commercial but no stage matches, it is usually a
missing stage rather than a reason to improvise. Record the gap in
`.agents/bd-context.md` under "Open gaps", do the closest adjacent stage, and
say plainly that the chain does not cover it.

If the request is not commercial at all, this skill is the wrong one. Say so and
load the appropriate corpus skill.
