---
name: win-loss-review
description: "When the user wants to run a post-decision debrief after a deal is won or lost. Use when they mention \"win-loss\", \"win/loss review\", \"lost deal analysis\", \"deal post-mortem\", \"why did we lose\", \"buyer interview\", \"decision criteria scoring\", \"loss reasons\", or \"win themes\". For the deal process being reviewed, see discovery-call. For prospective competitive positioning, see competitive-intelligence. For the pipeline metrics behind these deals, see pipeline-forecast."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [discovery-call, competitive-intelligence, pipeline-forecast]
  triggers: [win-loss, win loss review, lost deal analysis, deal post-mortem, why did we lose, buyer interview, decision criteria scoring, loss reasons, win themes]
---

# Win Loss Review

You are an expert at running disciplined post-decision debriefs on won and lost deals. The output is a `<deal>-win-loss-debrief.md` per deal and a `<period>-win-loss-report.md` that synthesizes patterns across deals and feeds them back into the ICP and messaging.

## Before Starting

Read `.agents/bd-context.md` first (ICP, personas, value props, competitive landscape, sales stages). Only gather what it does not answer.

Then, for each deal under review, pull and source:

1. The CRM record: stage history, amounts, dates, close reason.
2. Call notes and recordings; email threads with the buying committee.
3. The proposal or quote sent, and any competitive material.
4. The discovery or qualification capture from `discovery-call`, if it exists.
5. Buyer-side and rep-side accounts of the decision (interview them; see Step 3).

Evidence discipline: separate three things and never blend them — **what the buyer said**, **what the rep believes**, and **what the data shows**. Label beliefs as beliefs. The point of the review is the gap between those three.

## When to Use

- A deal was won or lost and the team wants to know why.
- Building a quarterly or periodic win/loss pattern report.
- A repeated loss reason is suspected and needs proving.
- Feeding real decision criteria back into the ICP or messaging.

**Don't use for:** running the deal process being reviewed — that is `discovery-call`. Prospective competitive positioning or battlecards — that is `competitive-intelligence`. The pipeline metrics that selected these deals — that is `pipeline-forecast`.

## Step 1 — Select the deals

Do not review every deal; review the ones that teach something. Default sample per cycle:

- Every loss above the context's mid-deal value.
- Every win against a named competitor.
- Every "no decision" deal above the same threshold (the most under-studied outcome).
- Any deal the rep is confused about.

Aim for 8-15 deals per cycle; below that, patterns are noise. Record the sample and the population it came from so the report can state its own limits.

## Step 2 — Reconstruct the timeline

Build the deal's factual arc before interpreting it:

| Date | Event | Source |
|---|---|---|
| … | first contact, demo, proposal, competitor entered, silence, decision | CRM / email / call note |

Mark the decision date and count the days of silence before it. Long unexplained silences usually hide a competitor or an internal blocker — note them.

## Step 3 — Interview the buyer

Use [references/interview-method.md](references/interview-method.md). Interview the buyer separately from the rep and never in the rep's presence. Ask what actually decided it, who was involved, what almost changed their mind, and what they told their boss. Record verbatim phrasing — exact words feed messaging.

## Step 4 — Debrief the internal team

Run a short internal debrief (rep, SE, and anyone who touched the deal) with the same discipline: what did we believe, what did we miss, and at which gate. Keep it blameless or people will shade the truth. Capture disagreements; do not resolve them by vote.

## Step 5 — Score the decision criteria

List the criteria the buyer actually used (price, fit, integration, trust, risk, references, timing) and score performance on each, win or loss:

| Decision criterion | Weight | Our score | Winner's score / bar | Evidence |
|---|---|---|---|---|
| | | | | |

The weighted gap names the real cause. If a score cannot be evidenced, mark it `[ASSUMPTION]` and flag it for the next cycle.

## Step 6 — Root-cause the outcome

Take the top-weighted gap and run "five whys" until you reach a cause you can change — a process, a message, or a qualification rule — not a person or bad luck. Classify the root cause as one of: qualification, discovery, value/messaging, pricing, product gap, competitive, or no-decision. A loss with no changeable root cause is a product signal — route it, do not bury it.

## Step 7 — Synthesize patterns

Across the sample, count root causes and weigh them by deal value, not deal count. Look for:

- The recurring loss reason that contradicts the ICP's assumed buying trigger.
- The win theme that appears in every won deal (your real differentiator).
- The competitor that keeps showing up, and the stage at which it appears.

Each pattern produces one recommendation with an owner and a destination (ICP, messaging, qualification, roadmap, or battlecard).

## Step 8 — Close the loop

Write the recommendations into the artifacts they change: ICP in `.agents/bd-context.md` or `market-segmentation`, messaging in `value-proposition-and-pricing`, battlecards in `competitive-intelligence`, qualification gates in `pipeline-forecast`. A win/loss report nobody acts on is the most expensive report a team can write.

## Output

1. `<deal>-win-loss-debrief.md` per deal from [templates/win-loss-debrief.md](templates/win-loss-debrief.md).
2. `<period>-win-loss-report.md` from [templates/win-loss-report.md](templates/win-loss-report.md): sample and limits, root-cause counts weighted by value, win themes, competitor appearances, and owned recommendations.

## Common Pitfalls

1. **Reviewing only losses.** Wins reveal the differentiator and the repeatable play; skip them and you learn half the story.
2. **Interviewing the buyer with the rep present.** The buyer softens; you get politeness, not data.
3. **Blending buyer, rep, and data into one "reason".** Keep them separate and show the gaps between them.
4. **Stopping at "price".** Price is a symptom; run the five whys to a changeable cause.
5. **Counting deals instead of weighting by value.** Ten small losses can matter less than one large one.
6. **A report with no owner or destination.** Every recommendation names who changes what, or it is not a recommendation.
7. **Blaming a person.** Blame shuts down honesty and hides the process cause underneath.

## Verification Checklist

- [ ] Sample documented with its population and stated limits.
- [ ] Timeline reconstructed from sources with the decision date marked.
- [ ] Buyer and internal interviews run separately; verbatim buyer phrasing captured.
- [ ] Decision criteria scored with weights and evidence; assumptions labelled.
- [ ] Root cause traced to a changeable cause and classified.
- [ ] Patterns weighted by deal value; each has an owner and a destination artifact.
- [ ] Buyer, rep, and data kept distinct throughout.
- [ ] Debrief and report written to their `<deal>-` and `<period>-` files.

## References

- [Interview method](references/interview-method.md)
- [Win/loss debrief template](templates/win-loss-debrief.md)
- [Win/loss report template](templates/win-loss-report.md)
