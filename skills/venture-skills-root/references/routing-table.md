# Routing table

Task-to-skill lookup for the venture-skills suite. If a task matches more than
one row, do the rows in the order shown and write each artifact before starting
the next.

## By what the user asked for

| The user asks for | Load | Because |
|---|---|---|
| "Who should we sell to?" | `market-segmentation` | Decides segments and sizing before anything downstream. |
| "What are competitors doing?" | `competitive-intelligence` | Teardown and battlecards feed positioning. |
| "How do we price this?" | `value-proposition-and-pricing` | Pricing follows positioning, never precedes it. |
| "Write our positioning" | `bd-context`, then `value-proposition-and-pricing` | Positioning needs the foundation doc first. |
| "Find me leads" | `prospect-research` | Builds the qualified account list. |
| "Write a cold sequence" | `outbound-sequencing` | Needs the segment and offer from stages 1 and 3. |
| "Prep me for this call" | `discovery-call` | Produces the call plan and question set. |
| "They said it's too expensive" | `objection-handling` | Needs the pricing method and ROI case. |
| "Send them a proposal" | `proposal-and-quote` | Needs discovery notes. |
| "Plan the account" | `account-planning` | Stakeholder map and whitespace. |
| "Will we hit the number?" | `pipeline-forecast` | Commit logic and coverage. |
| "Prep the QBR" | `qbr-and-renewal` | Value recap, renewal plan. |
| "Why did we lose that deal?" | `win-loss-review` | Debrief, then feed findings back. |
| "Is this idea worth building?" | `product-discovery` | Opportunity brief with evidence and a kill criterion. |
| "Turn this into a spec" | `business-need-to-prd` | PRD with requirements and acceptance criteria. |
| "Design the system for this" | `prd-to-system-design` | Components, data, interfaces, failure modes. |
| "Is this secure?" | `security-by-design` | Threat model and controls, before code. |
| "Make sure we built what we promised" | `feature-traceability` | Requirement-to-artifact-to-test matrix. |
| "Automate this process" | `sop-to-automation` | Steps to triggers, guarantees, exception paths. |
| "Are we ready to launch?" | `launch-readiness` | Go/no-go with explicit gates. |
| "Where do I start?" | this skill | You are already here. |

## By artifact that already exists

Check `.agents/` before committing to a stage. Existing artifacts change the
routing:

| If this exists | And is current | Then |
|---|---|---|
| `.agents/bd-context.md` | yes | Skip stage 0; start at the stage you need. |
| `.agents/bd-context.md` | stale (pricing or buyer changed) | Re-run `bd-context` before anything downstream. |
| `.agents/market/segments.md` | yes | Skip stage 1; go to `competitive-intelligence` or the offer stage. |
| `.agents/offer/positioning.md` | yes | `value-proposition-and-pricing` becomes an update, not a rewrite. |
| `.agents/discovery/<account>.md` | yes | Go straight to `proposal-and-quote`. |
| `.agents/prd/<feature>.md` | yes | Start at `prd-to-system-design`. |
| `.agents/design/<feature>.md` | yes | Start at `security-by-design`, then `feature-traceability`. |
| `.agents/security/<feature>-threat-model.md` | yes | Controls are agreed; implementation may start. |

## Re-entry rules

The chain is iterative. These are the loops that happen most often, and what
triggers them.

- **Win to market.** `win-loss-review` finds a repeated loss reason, so you
  re-enter at `market-segmentation` or `value-proposition-and-pricing`. Do not
  patch the objection library and call it fixed.
- **Design to specification.** `prd-to-system-design` finds a requirement that
  cannot be satisfied safely or affordably, so you re-enter at
  `business-need-to-prd` to change the requirement rather than the design.
- **Threat to specification.** `security-by-design` finds a risk the spec did not
  budget for, so you re-enter at `business-need-to-prd` and add a requirement.
  Never leave a live threat model unaddressed in the PRD.
- **Launch to product.** `launch-readiness` fails a gate, so you re-enter at
  whichever stage owns the failed gate. A failed support gate goes back to
  `sop-to-automation`; a failed scope gate goes back to `business-need-to-prd`.
- **Discovery to offer.** `discovery-call` repeatedly hears the same buying
  criterion your positioning does not mention, so you re-enter at
  `value-proposition-and-pricing`.

## Decomposition

A request that names several stages at once is a decomposition task. Split it,
state the order, and run one stage per artifact. Example:

> "We want to sell to clinics, build the rota feature, and make sure it's
> compliant."

Decomposes to: `bd-context` (foundation) then `market-segmentation` (clinics as
a segment) then `value-proposition-and-pricing` (what compliance is worth to
them) then `product-discovery` (rota as an opportunity) then
`business-need-to-prd` then `prd-to-system-design` then `security-by-design`
(patient and staff data) then `launch-readiness`. Seven artifacts, in that order.

Do not attempt this in one pass. Each artifact is reviewed before the next begins.

## When the answer is a corpus skill, not a stage

| The user asks for | Do NOT use a stage skill | Use instead |
|---|---|---|
| "Add a column to the users table" | any | `postgresql-table-design` |
| "Write the API for this" | `prd-to-system-design` (already done) | `api-design-principles` |
| "Make the dashboard faster" | any | `sql-optimization-patterns` |
| "Fix the contrast on this page" | any | `fixing-accessibility`, `wcag-audit-patterns` |
| "Set up CI" | any | `deployment-pipeline-design` |
| "Write tests for this" | any | `test-driven-development` |
| "Patch this CVE in a dependency" | any | `source-code-security-audit`, `tob-supply-chain-risk-auditor` |
| "Get more traffic" | `outbound-sequencing` | `seo-audit`, `content-strategy`, `cro` |
| "Improve onboarding drop-off" | `outbound-sequencing` | `cro`, `onboarding`, `analytics` |
| "Handle this support ticket" | any | `email-inbox-triage`, `incident-runbook-templates` |

The test: if the answer would be the same for a different market, buyer, price
or risk profile, it is a corpus question, not a stage.
