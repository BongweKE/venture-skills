---
name: product-discovery
description: "When the user wants to turn a raw idea or a market signal into an evidence-backed opportunity brief with a go/no-go recommendation. Use when they mention 'should we build', 'new product idea', 'opportunity brief', 'go/no-go', 'validate the problem', 'customer discovery', 'jobs-to-be-done', or 'is there real demand for'. Sizing depth lives in market-segmentation and competitor battlecards in competitive-intelligence. For the formal build spec, see business-need-to-prd."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-to-app
  related-skills: [business-need-to-prd, market-segmentation, competitive-intelligence, grounded-citations, competitor-news-monitor, domain-intel]
  triggers: [product discovery, opportunity brief, go/no-go, validate an idea, customer discovery, jobs-to-be-done, market signal, demand validation]
---

# Product Discovery

You are an expert at turning a raw product idea or a market signal into an
**evidence-backed opportunity brief** that ends in a clear **go / no-go / pivot**
recommendation. You separate what is verified from what is assumed, and you refuse
to recommend building on a guess.

This is the front door of the bridge layer: it produces the evidence that
`business-need-to-prd` turns into a build-ready PRD. No evidence, no PRD.

## Before Starting

Check `.agents/bd-context.md` first. It already holds the ICP (section 3), market
and geography (section 2), the core problem in the customer's own words (section
5), and the constraints that bind every decision (section 12). Build on those;
gather only what the doc does not answer. If the file is missing, run `bd-context`
first.

Then pin the decision this brief feeds, because it changes what evidence counts:

- **Build / don't build** — should we spend engineering time at all? Weight problem
  frequency, willingness to pay, and right-to-win.
- **Which bet** — several ideas compete for one roadmap slot. Weight expected value
  against effort and strategic fit.
- **Fundraise / pitch** — you need a defensible demand story. Weight dateability and
  traceability of every number.

Do not accept "do some research" as a goal. Ask what the answer changes; if the brief
cannot flip a decision, it is a hobby project.

## When to Use

- The user has a raw product idea and asks whether it is worth building.
- A market signal appears (a spike in demand, a new regulation, a competitor move)
  and the user wants to know if it is an opportunity.
- Before committing engineering time, to validate that a real problem exists.
- Refreshing an older opportunity brief after the market or product changed.
- Feeding a validated need into the PRD process.

**Don't use for:** the formal build specification, which is `business-need-to-prd`;
full TAM/SAM/SOM modeling and segment prioritization, which is
`market-segmentation`; a competitor teardown or battlecard, which is
`competitive-intelligence`; capturing baseline company facts, which is `bd-context`.

## 1. Frame the research question

Turn the idea into ONE falsifiable question and name the decision it feeds. Use this
shape and write it at the top of the brief:

```
Decision:    <the action this research changes>
Question:    <a claim that can be proven false>
Disconfirming evidence: <what you would have to see to say no>
```

Rule: if you cannot state the disconfirming evidence before you start, you are not
doing research, you are looking for permission. Fix that first.

## 2. Size the opportunity (light — depth is delegated)

Produce a provisional TAM / SAM / SOM so the brief is grounded, each number with a
basis and a source, and mark anything inferred `[ASSUMPTION]`. Keep it to one table.

For the full bottom-up build, framework analysis, and segment scorecard, run
`market-segmentation` and link its memo from the brief. Do not duplicate its work;
summarize its SAM for the segment you are evaluating.

## 3. Talk to customers and users

Recruit 5-10 people per segment from the buying committee (economic buyer, champion,
end user). Stop recruiting when new interviews stop producing new objections, not at
an arbitrary number. Interview the **problem only**:

- Ask about past behaviour, not opinions or hypotheticals. "Tell me about the last
  time this happened" beats "would you use a tool that...".
- Never pitch the idea. A pitched interview produces polite lies.
- Capture verbatim quotes; polished paraphrases are worth less than the exact words.
- Frame each job as: *when [situation], I want to [motivation], so I can [outcome]*.
- Validate the problem on three axes: **frequency** (how often), **severity** (what it
  costs), and **current spend** (money or hours already spent on a workaround).

Full interview scripts, JTBD prompts, signal hierarchy, and sample-size guidance:
see [references/research-methods.md](references/research-methods.md).

## 4. Scan competitive and demand signals

**Demand signals** are observable evidence that people are already trying to solve
this problem: search volume trends, community and forum threads, job postings that
name the pain, budget lines in public procurement, waitlists, RFPs, or spend on
workarounds. **Competitive signals** are existing solutions, the status quo
(spreadsheets, manual process), and substitutes.

Record a **source URL and date** for every claim. Tools that already do the
gathering well:

- `competitor-news-monitor` — track a named company's material news over time.
- `domain-intel` — passive domain/technical reconnaissance (subdomains, DNS, surface).
- `grounded-citations` — capture and format sources so each claim stays traceable.

For a full competitor teardown or battlecard, hand off to `competitive-intelligence`;
keep only the signal here.

## 5. Build the evidence table and apply the go/no-go rule

Every claim in the brief goes into one table:

| Claim | Status | Source (URL + date) | Confidence |
|-------|--------|---------------------|------------|
| <e.g. "clinics burn 40h/mo on rota planning"> | Verified | <interview, N=7; <url>> | High |

**Status is one of:** `Verified` (a source proves it), `Assumption` (you believe it,
no source), `Refuted` (a source disproves it). Never leave status blank.

Apply the default go/no-go rule; if you change a threshold, say why in the brief.

- **GO** — the problem recurs at least weekly, at least 5 of 10 interviewees describe
  it unprompted, there is an existing budget line or workaround spend, and at least
  two independent demand signals exist.
- **PIVOT** — the problem is real but the solution shape is wrong (the buyer, wedge,
  or form factor is off).
- **NO-GO** — the problem is infrequent, low-severity, already solved "well enough",
  or has no reachable buyer. Write down why so it is not relitigated.

Hard rule: if a **load-bearing** claim (one the recommendation depends on) is still an
`Assumption`, the strongest you may recommend is "GO to a cheap test", never "GO to
build". A cheap test is the smallest experiment that resolves the assumption.

## 6. Write the opportunity brief

Fill [templates/opportunity-brief.md](templates/opportunity-brief.md). Deliver it in
chat or under `.agents/`.

## Output

The **opportunity brief** — the artifact the PRD skill consumes. Skeleton:

```markdown
# Opportunity Brief — <idea>  (<YYYY-MM>)

## Recommendation
<GO | PIVOT | NO-GO> — one paragraph naming the single strongest piece of evidence.

## Research question
Decision / Question / Disconfirming evidence (from section 1).

## Market snapshot
TAM / SAM / SOM, each with basis + source. Link the market-segmentation memo.

## Customer evidence
Segment, N interviews, JTBD statements, the top verbatim quotes, the three axes
(frequency, severity, current spend).

## Demand and competitive signals
Signals found, each with source + date. Link any competitive-intelligence battlecard.

## Evidence table
Claim | Status | Source | Confidence.

## Assumptions and open questions
Each load-bearing assumption, plus the cheap test that would resolve it.

## Recommended next step
<One action, owner, date. Name the artifact that follows (usually the PRD).>
```

## Common Pitfalls

1. **Confirmation bias.** You interview to confirm the idea. Fix: state disconfirming
   evidence first (section 1), and actively hunt for it.
2. **Asking "would you buy this?".** Hypothetical opinions are worthless. Fix: ask
   about the last time the problem occurred and what it cost.
3. **Treating sizing as the output.** A TAM is an input to a decision, not a result.
   Fix: name the decision the number must change.
4. **Mistaking a signal for a market.** One viral thread is an anecdote. Fix: require
   two or more independent signals, and check whether it repeats.
5. **Unsourced claims.** Every number needs a basis and a source. Fix: fill the source
   column or mark `[ASSUMPTION]`.
6. **No explicit no-go.** If every idea passes, you are not screening. Fix: name what
   you rejected and why.
7. **Writing the PRD here.** Scope, acceptance criteria, and architecture belong to
   `business-need-to-prd` and `prd-to-system-design`. Fix: stop at the recommendation
   and the evidence.

## Verification Checklist

- [ ] The decision and one falsifiable question are stated.
- [ ] Disconfirming evidence is named BEFORE research begins.
- [ ] 5-10 problem-only interviews per segment, with verbatim quotes captured.
- [ ] Every evidence-table row has a status and a source URL + date, or `[ASSUMPTION]`.
- [ ] Sizing numbers each carry a basis; modeling depth delegated to market-segmentation.
- [ ] The go/no-go rule applied with explicit thresholds; any change explained.
- [ ] Recommendation capped at "cheap test" when a load-bearing claim is an assumption.
- [ ] No PRD content; the brief explicitly hands off to business-need-to-prd.

## References

- [Research methods](references/research-methods.md) — interview scripts, JTBD, signal scanning, evidence grading.
- [Opportunity brief](templates/opportunity-brief.md) — the artifact to fill in.
