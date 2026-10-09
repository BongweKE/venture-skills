---
name: discovery-call
description: "When the user wants to prepare for or run a discovery call with a prospect. Use when they mention 'discovery call', 'discovery questions', 'SPIN', 'gap selling', 'qualification call', 'MEDDPICC', 'needs analysis', 'call plan', 'call notes', or 'next steps'. For the proposal that follows, see proposal-and-quote. For handling pushback during or after the call, see objection-handling."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [bd-context, outbound-sequencing, objection-handling, proposal-and-quote, pipeline-forecast]
  triggers: [discovery call, discovery questions, SPIN, gap selling, MEDDPICC, call plan, call notes, next steps]
---

# Discovery Call

You are an expert at preparing and running discovery calls that qualify a deal and advance it. The artifacts you produce are a **call plan** (research, agenda, and a tailored question bank), **live call notes** structured to fill in as you talk, and a **follow-up email** that confirms the next step in the prospect's own words.

## Before Starting

Check `.agents/bd-context.md` first and only gather what it does not already answer. Read section 3 (ICP and disqualifiers), section 4 (personas, what they are measured on, and their likely objection), section 5 (the problem in the customer's words), section 6 (value props and proof), and section 9 (deal stages and exit criteria). If the persona's pain and metric are missing, the call becomes generic; get them from `value-proposition-and-pricing` first.

Then confirm in one question: **which account and deal**, **who is on the call and their roles**, **the current stage**, and **what was said in prior touches** (pull from the reply that booked it). Default to a 30-minute first call unless the user says otherwise.

## When to Use

- A call is booked and the user wants a plan, questions, or an agenda.
- The user wants to run a discovery or qualification call and capture it properly.
- The user finished a call and needs structured notes or a follow-up email.
- The user needs to map what is known and missing against MEDDPICC.

**Don't use for:** the proposal or pricing that follows — those are `proposal-and-quote` and `value-proposition-and-pricing`. Handling a specific objection in the moment — that is `objection-handling`. Stage-gating, CRM hygiene, or forecasting the deal afterwards — that is `pipeline-forecast`. The outreach that booked the call — that is `outbound-sequencing`.

## 1. Run pre-call research (30 minutes)

Build a one-page pre-read, not a dossier. Gather only what changes the call:

- **Three account facts:** what they do, size, and the trigger that made you talk (from the lead sheet).
- **Three persona hypotheses:** the contact's likely metric, their likely pain, and who else has to agree.
- **One explicit hypothesis to test:** write down the sentence you believe is true — e.g. "Their roster is manual and breaks at month-end" — and design a question that would disprove it.

Cite a source for each fact. If you cannot source it, label it an assumption and ask about it on the call rather than stating it as truth. Never open by reciting research back at the prospect; use it to ask better questions.

## 2. Open with an agenda and a contract

Spend the first two minutes on three things: who you are in one sentence, the agenda, and the outcome you both want. Then get permission.

```text
Thanks for the time. I have 30 minutes. My goal is to understand how
<problem> works for you today and whether we can help — not to pitch.
I would like to ask about <area 1>, <area 2>, and <area 3>, then leave
time for your questions. Anything you want to add before we start?
```

This single move distinguishes a discovery call from a demo and lets the prospect steer. If the prospect has a different agenda, take theirs first.

## 3. Work the question bank

Use **SPIN** to move from surface to pain, and **gap selling** to size the cost of inaction. Ask open questions, then stay quiet — the prospect should talk twice as much as you. Full bank in [references/question-bank.md](references/question-bank.md):

| Layer | Purpose | Example |
|-------|---------|---------|
| Situation | Establish facts | "Walk me through how <process> runs today." |
| Problem | Surface friction | "Where does that break or cost you most?" |
| Implication | Size the cost | "What does that failure cost you a month?" |
| Need-payoff | Let them state value | "If that were fixed, what changes for the team?" |
| Gap | Quantify current vs future | "Where should it be, and what is the gap?" |

**Decision rule:** do not move to the pitch until you can state the problem, its quantified cost, and who it hurts — in the prospect's own words. If you cannot, keep asking.

## 4. Capture notes live against MEDDPICC

Take notes in the structured template so nothing is reconstructed from memory. Capture **MEDDPICC** — Metrics, Economic buyer, Decision criteria, Decision process, Paper process, Identify pain, Champion, Competition. Full definitions, questions, and disqualify signals are in [references/meddpicc.md](references/meddpicc.md). Use the note template in [templates/call-notes.md](templates/call-notes.md):

```text
Account:            <name>          Date: <YYYY-MM-DD>
Attendees:          <name, role, persona>

Metrics:            <the number they care about, in their words>
Economic buyer:     <name/role, met? > 
Decision criteria:  <what they will judge on>
Decision process:   <steps, people, timeline>
Paper process:      <procurement, legal, security, signature path>
Identify pain:      <the problem + its quantified cost>
Champion:           <who, what they will do for us, evidence>
Competition:        <alternatives: named + status quo>
Gap / open Qs:      <what we still do not know>
Next step:          <action, owner, date>
```

**Verbatim matters.** Write their exact phrases for the pain and the metric; polished paraphrase loses the language that later closes the deal and sharpens the proposal.

## 5. Set the next step before the call ends

Never let a discovery call end with "I will send something over". Before the call closes, agree three things: **the next action**, **who owns it**, and **the date**. If a proposal or demo comes next, book the meeting that reviews it now. A discovery call without a dated next step did not advance the deal.

If the prospect is a poor fit against the ICP or disqualifiers, say so and close the loop — a clean disqualification saves the cycle.

## 6. Send the follow-up within two hours

Recap in the prospect's words, confirm the next step, and keep it under 150 words. Template in [templates/call-plan.md](templates/call-plan.md):

```text
Subject: <recap + next step, 3-5 words>

Hi <first name>,

Thanks for the time today. My take on what you said:
- <problem, in their words>
- <cost / impact, quantified as they stated it>
- <what "good" looks like to them>

Next step: <action> on <date>, with <people>. I will <what you owe them> by
<when>.

Anything I got wrong, reply and I will fix it.

<signature>
```

Then update the deal record: stage, MEDDPICC gaps, and the dated next step, so `pipeline-forecast` reads accurate data.

## Output

Three artifacts:

1. A **call plan** from [templates/call-plan.md](templates/call-plan.md) — research, hypothesis, agenda, and the tailored questions for this prospect.
2. **Live notes** from [templates/call-notes.md](templates/call-notes.md) — MEDDPICC-structured, verbatim where it matters.
3. A **follow-up email** built from the recap skeleton above; send within two hours.

## Common Pitfalls

1. **Pitching before discovering.** The moment you talk about your product before the problem is quantified, you have lost the room. Ask, then pitch.
2. **No explicit hypothesis.** Research with nothing to test becomes a recital. Write the one sentence you are trying to disprove.
3. **Paraphrasing the pain.** Capture their exact words. Paraphrase drops the language the prospect will recognise in the proposal.
4. **Reconstructing notes from memory.** Fill MEDDPICC live. Deals die from a blank champion field two weeks later.
5. **Ending without a dated next step.** "I will follow up" is not a next step. Action, owner, date — before the call ends.
6. **Ignoring the disqualifiers.** If the account fails the ICP or a hard disqualifier, say so and stop. A polite exit beats a long dead deal.
7. **A slow follow-up.** Two hours, not two days. The call is still warm; that is when the recap lands.

## Verification Checklist

- [ ] Pre-call one-pager has 3 account facts, 3 persona hypotheses, 1 testable hypothesis.
- [ ] Every research fact is sourced; unsourced items labelled assumptions.
- [ ] Agenda and outcome stated and agreed in the first two minutes.
- [ ] Questions span situation, problem, implication, need-payoff, and gap.
- [ ] Notes captured live against all eight MEDDPICC letters; gaps listed explicitly.
- [ ] Pain and metric captured verbatim.
- [ ] A dated next step with an owner agreed before the call ended.
- [ ] Follow-up email sent within two hours in the prospect's words.
- [ ] Deal record updated with stage, MEDDPICC gaps, and next step.

## References

- [references/meddpicc.md](references/meddpicc.md) — each letter: definition, the questions that fill it, and the signal that disqualifies.
- [references/question-bank.md](references/question-bank.md) — the full SPIN / gap-selling bank by persona and situation.
