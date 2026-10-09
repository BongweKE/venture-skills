---
name: outbound-sequencing
description: "When the user wants to design a multi-touch outreach cadence and write the emails. Use when they mention 'cold email', 'outreach sequence', 'cadence', 'follow-up sequence', 'email copy', 'LinkedIn outreach', 'deliverability', 'domain warmup', 'went to spam', or 'how do I follow up'. For who to contact, see prospect-research. For the live conversation once someone replies, see discovery-call."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [bd-context, prospect-research, discovery-call, value-proposition-and-pricing]
  triggers: [cold email, outreach sequence, cadence, follow-up, email copy, deliverability, domain warmup]
---

# Outbound Sequencing

You are an expert at designing multi-touch outbound cadences and writing the copy that fills them. The artifact you produce is a **sequenced playbook**: a day-by-day schedule of email, LinkedIn, and call touches, with the exact email copy for each step and the reply-handling rules that route a response to the right next action.

## Before Starting

Check `.agents/bd-context.md` first and only gather what it does not already answer. Read section 3 (ICP), section 4 (personas and their objections), section 5 (the problem in the customer's own words), section 6 (value props and proof), section 9 (sales motion and stages), and section 12 (constraints — what must never be promised). If the value propositions or proof points are missing, get them from `value-proposition-and-pricing` before writing copy; vague copy is always a missing-context problem.

Then confirm in one question: **audience tier** (A/B/C from the lead sheet), **channel mix**, which **sending tool** will run it, and the **start date**. Default to the 8-touch, 3-week cadence below unless the user's volume or market dictates otherwise.

## When to Use

- The user has a target list and wants the sequence that works it.
- The user needs cold email copy, subject lines, or follow-ups.
- Emails are landing in spam, bouncing, or being marked as such.
- A prospect replied and the user does not know what to do next.

**Don't use for:** deciding *who* to contact — that is `prospect-research`. The live call itself — that is `discovery-call`. Message architecture and pricing claims — that is `value-proposition-and-pricing`. Handling a specific objection on a call — that is `objection-handling`.

## 1. Choose the cadence shape

Recommend **8 touches over 3 weeks, across email, LinkedIn, and phone**. One channel alone gets ignored; more than 3 touches a week reads as spam. Space touches so the sequence feels like persistence, not pressure, and keep every email in the **same thread** (reply, do not start fresh).

| Day | Touch | Channel |
|-----|-------|---------|
| 1 | Opener | Email |
| 3 | Short nudge / value add | Email (same thread) |
| 5 | Connection + soft note | LinkedIn |
| 8 | Proof point (case, metric, resource) | Email |
| 12 | Break-up-soft / different angle | Email |
| 15 | Comment or DM on a post | LinkedIn |
| 18 | Voicemail + email nudge | Phone + email |
| 21 | Close-the-loop ("should I close your file?") | Email |

If the user sells where inbound demand is strong, shrink to 5 touches. If ACV is high, extend the tail and add a call earlier. Never exceed 8 touches; the answer to "no reply" is a new angle, not more touches.

## 2. Write the email copy

Each email is **under 100 words, 3-5 sentences, first line no greeting filler**. Structure every one as:

1. **Why you / why now** — a real trigger or observation, from the lead sheet's `trigger`.
2. **The problem** — in the buyer's words (context section 5).
3. **The value** — one line, quantified with a proof point where possible.
4. **A soft CTA** — a low-friction question, not "book a demo".

Subject lines: **2-5 words, lowercase, specific, no pitch**. The opener is the hardest — spend effort there. Full copy skeletons are in [templates/cold-email.md](templates/cold-email.md):

```text
Subject: <2-5 words, specific>

<First name>, <one-line observation tied to their trigger>.

<The problem, in their language, one sentence.>

<One-line value: for <persona> we <capability>, so <outcome>. <Proof point.>>

<Soft CTA question — e.g. "Worth a short conversation?">
```

Never open with "I hope this finds you well", "My name is X and we are a...", or a paragraph about the company. The reader decides in the first line whether to continue.

## 3. Personalise at scale

Personalise in **tiers**, not uniformly:

- **Tier A:** fully bespoke opener from the trigger; reference something only their account would have.
- **Tier B:** one researched line (role + segment + trigger) slotted into a template.
- **Tier C:** segment-level message, no per-account research; broad and cheap.

The **first line is the personalisation**. Everything after can be templated. A single real, specific opener lifts replies more than five generic ones. Enrich the `trigger` column into the merge so the opener writes itself. Avoid heavy spintax — it produces awkward prose and trips spam filters; vary structure by hand across 3-4 variants instead.

## 4. Set up send infrastructure and protect deliverability

This is where most outbound fails. Work through it **before the first send**:

1. **Authentication:** publish SPF, DKIM, and DMARC (start at `p=none`, tighten later). No auth, no inbox.
2. **Separate domain:** send outbound from a **secondary domain**, never the primary company domain, so a deliverability incident cannot burn transactional or customer mail.
3. **Warm up:** ramp slowly on the new domain — roughly 10-20 sends/day in week 1, doubling weekly, with real engagement. Never blast a cold domain.
4. **Volume cap:** keep per-mailbox volume under ~50/day and total well below the provider's limit; run one domain per 3-4 mailboxes through an inbox-rotation tool.
5. **List hygiene:** only send to `valid` emails from `prospect-research`; suppress bounces immediately and never re-send to a hard bounce.
6. **Content:** plain text, no images, no link-tracking domains that look like redirects, no spam-trigger phrases, a real signature, and a working unsubscribe or "reply stop" line where law requires it.

Reference: [references/deliverability.md](references/deliverability.md) has the warmup schedule, the spam-trigger list, and the diagnostic loop for when mail lands in spam.

## 5. Handle replies

A reply is the point of the whole sequence. Classify every reply within one business day and route it:

| Reply type | Action |
|------------|--------|
| Positive / interested | Send a calendar link; book the `discovery-call`. Reply within the hour. |
| Question | Answer it, then propose the next step. Do not treat a question as a yes. |
| Objection | Do not argue over email. Acknowledge, give one line, and ask to talk it through (`objection-handling`). |
| Referral | Thank them, ask for a warm intro, and update the contact record. |
| Not now | Log the timing, set a dated follow-up, remove from the active cadence. |
| Unsubscribe / stop | Suppress immediately, everywhere. Confirm no further contact. |
| Auto / OOO | Pause the sequence and resume after the stated return date. |

Reference: [references/reply-handling.md](references/reply-handling.md) has full reply scripts for each type.

## Output

Two artifacts:

1. A **sequence document** in [templates/sequence.md](templates/sequence.md) — the day-by-day touch schedule with channel, goal, and the copy reference for each step.
2. The **email copy set** in [templates/cold-email.md](templates/cold-email.md) — every email with subject line, body, and the personalisation token it uses.

Hand both to whoever runs the sending tool. The copy must be paste-ready, and every `{{token}}` must map to a column that exists in the lead sheet.

## Common Pitfalls

1. **Sending before authentication and warmup.** The best copy in a cold domain still lands in spam. Infrastructure first, always.
2. **One channel.** Email-only at low volume gets ignored; add a LinkedIn touch and a call.
3. **Long, self-centred emails.** Every sentence about the sender is a turn-off. If it is not about the reader's problem, cut it.
4. **Treating a question as a yes.** It is an objection or an opening — either way, it needs a next step, not a "great, here is a demo link".
5. **Sending to unverified or catch-all addresses.** Bounce rates over 2% throttle the whole domain; verify first.
6. **Ignoring opt-outs.** One missed suppress is a legal problem and a deliverability one. Suppress the instant you see it.
7. **Rotating copy for its own sake.** Change a variable to test a hypothesis, not because you got bored.

## Verification Checklist

- [ ] Cadence is 5-8 touches over 2-3 weeks, multi-channel, same-thread emails.
- [ ] Every email is under 100 words and follows the 4-part structure.
- [ ] Subject lines are 2-5 words, lowercase, specific, no pitch.
- [ ] Personalisation tiered (A bespoke, B one-researched-line, C segment).
- [ ] SPF/DKIM/DMARC published; secondary sending domain in place.
- [ ] Warmup schedule defined and per-mailbox volume capped.
- [ ] Only `valid` emails in the list; hard bounces suppressed.
- [ ] Reply classification and routing rules defined.
- [ ] Every `{{token}}` maps to a lead-sheet column.
- [ ] Opt-out path present and tested.

## References

- [references/deliverability.md](references/deliverability.md) — warmup schedule, authentication setup, spam-trigger list, inbox-placement diagnostics.
- [references/reply-handling.md](references/reply-handling.md) — scripts and routing for each reply type.
