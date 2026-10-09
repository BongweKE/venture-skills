# The linking model

This is the document that explains the design decision the rest of the repository
depends on. If you read one file here, read this one.

## The problem with a big skill collection

An agent with 600 installed skills is not better than an agent with 20. Past a
certain size, a skill collection degrades in three specific ways:

1. **Duplicate triggers.** Two skills both look relevant to "write a pricing
   page", so the agent picks one arbitrarily. Whichever it picks, the other's
   knowledge is lost.
2. **No notion of sequence.** Skills describe capabilities, not order. An agent
   asked to "build the onboarding flow we sold to clinics" has no way to know
   that positioning must precede the PRD.
3. **No notion of obligation.** Nothing in a capability list says that a feature
   without a named business owner and a measurable outcome should not be built.

venture-skills is designed around those three failure modes rather than added to
a pile.

## The WHY and the HOW

The central rule: **a skill belongs to exactly one of two layers, and they never
duplicate each other.**

| | venture-skills | the wider corpus |
|---|---|---|
| Owns | WHY and WHAT | HOW |
| Answers | should we, for whom, at what price, which requirement, what risk, is it ready | how to build it, how it should look, how to secure the implementation |
| Artifacts | briefs, battlecards, PRDs, threat models, traceability matrices, launch gates | code, schemas, components, pipelines, tests |
| Fails if | it restates engineering craft | it invents business justification |

A stage skill that needs a "how" **names the corpus skill** rather than
describing the craft. This is enforced culturally, not mechanically: the
authoring rules forbid re-teaching, and `references/corpus-map.md` records the
handoff point for each stage.

## Sequence: the chain

Twenty-one skills are arranged as a fifteen-stage chain, and each stage consumes
the artifact the previous stage wrote.

```
 0 bd-context
      |
 1 market-segmentation -> 2 competitive-intelligence -> 3 value-proposition-and-pricing
      |
 4 prospect-research -> outbound-sequencing
      |
 5 discovery-call -> objection-handling
      |
 6 proposal-and-quote
      |
 7 account-planning / pipeline-forecast / qbr-and-renewal / win-loss-review
      |
 ==== the commercial half ends, the delivery half begins ====
      |
 8 product-discovery          <- the handoff point
      |
 9 business-need-to-prd
      |
10 prd-to-system-design -> 11 security-by-design
      |
12 feature-traceability, 13 sop-to-automation
      |
14 launch-readiness
```

The chain is **iterative, not a waterfall**. Later stages routinely invalidate
earlier ones, and `references/routing-table.md` names the common loops:

- a repeated loss reason sends you back to segmentation or positioning;
- a threat the spec did not budget for sends you back to the PRD;
- a failed launch gate sends you back to whichever stage owns the gate.

Deciding *when to loop back* is the actual skill being taught. A linear reading
of the chain produces the same rigid, unusable process that waterfall planning
produces.

## Obligation: the entry rule

`feature-traceability` holds the only rule in this repository that can block
work: **no feature enters the backlog without a named business owner, a
measurable outcome, and an acceptance test.**

That rule is what makes the WHY/HOW split real rather than decorative. Without
it, the chain is a planning exercise that ends the moment implementation starts.

It is enforced by inspection rather than by tooling, because correctness here is
a judgement about a specific feature, not a property a linter can read.

## The three linking mechanisms

1. **The router** (`venture-skills-root`). Task to stage. Loaded first, then the
   agent loads exactly one stage skill. This solves duplicate triggers by
   providing a single arbitration point.
2. **The corpus map** (`references/corpus-map.md`). Stage to HOW-skill. This
   solves the restatement problem by making the handoff explicit.
3. **The catalog** (`catalog/known-skills.txt`). The generated list of every
   skill name installed across the four runtimes. The validator uses it to check
   that a cross-reference resolves, so a skill cannot point at a corpus skill
   that does not exist.

## Both directions

Linking is not one-way delegation. When a corpus skill is used and it surfaces a
commercial consequence, that consequence is written **back** into the stage
artifact:

- a threat model that finds an unbudgeted control is a change to the PRD;
- a conversion test that changes the promise is a change to positioning;
- a support runbook that needs a new admin action is a change to the requirements;
- a data-retention obligation is a change to the launch gate.

Without the return path, the commercial half of the chain is a one-time document
that goes stale the moment engineering starts.

## What this buys you

An agent working from this suite can answer, for any piece of work:

- Which business question does this serve, and which artifact says so?
- What has to be true before this can be built?
- Which existing skill implements the how?
- What must be true before this can ship?
- If this changes, which earlier decision has to be revisited?

That is the difference between an agent that writes code and an agent that was
briefed.
