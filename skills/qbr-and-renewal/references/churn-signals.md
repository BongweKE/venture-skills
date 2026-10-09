# Churn-Risk Signals

Detail for Step 5 of `qbr-and-renewal`. Load this when scoring an account's health and choosing a save play.

## How to use

For each signal, record what you observed, the date, the source, and whether it is new or worsening. Classify the account:

- **Green** — no red signals, no more than one amber, health score 8+.
- **Amber** — one red signal, or three or more amber, or a falling trend over two periods.
- **Red** — two or more red signals, or any single signal below marked critical.

A single red signal overrides a healthy score. The point of the list is to catch a falling account before it tells you it is leaving.

## Signals by category

### Relationship

| Signal | Weight | Notes |
|---|---|---|
| Champion left or changed roles | Red (critical) | The most predictive single signal in B2B. Re-map immediately. |
| Executive sponsor silent > 90 days | Red | Your air cover is gone. |
| Single-thread relationship (only your contact) | Amber | Fragile by construction. |
| New economic buyer or reorg | Amber | Budget ownership reset; re-earn it. |
| Meetings repeatedly postponed or downgraded | Amber | Access is closing. |

### Adoption and usage

| Signal | Weight | Notes |
|---|---|---|
| Active seats falling period over period | Red | Falling, not merely low — a trend. |
| Usage drop > 30% in a quarter | Red | Find out why before the QBR. |
| Feature depth stalled at login-only | Amber | Not embedded in a workflow. |
| Key integration switched off | Amber | The product stopped mattering to a process. |
| Training or onboarding never completed | Amber | Adoption debt from day one. |

### Support and experience

| Signal | Weight | Notes |
|---|---|---|
| Open P1 or repeated P1s | Red | Trust eroding in real time. |
| Escalation trend rising over two periods | Red | Fixing speed, not the underlying defect. |
| Named dissatisfaction from a user group | Amber | Discontent spreads before it churns. |
| Ticket volume high but resolution slow | Amber | Cost and frustration both rising. |

### Commercial

| Signal | Weight | Notes |
|---|---|---|
| Renewal date inside notice window with no plan | Red | Process risk alone can churn an account. |
| Payment late or disputed | Amber to Red | Finance friction often precedes cancellation. |
| Budget cut or freeze announced | Amber | May force a downgrade conversation. |
| Procurement ran a competitive evaluation | Red | Assume active alternatives. |

### Value and outcomes

| Signal | Weight | Notes |
|---|---|---|
| Customer cannot name the value received | Red | Renewal will be decided on price. |
| No documented outcomes this period | Amber | Nothing to defend the invoice with. |
| Goal posts moved and success was never re-baselined | Amber | They are measuring something you are not delivering. |

## Reading the pattern

- **Trend beats level.** A 60% adoption that is climbing is safer than an 80% that is falling.
- **Silence is a signal.** The quiet account is not the happy account; it is often the disengaged one.
- **Finance moves before sales knows.** Late payment precedes cancellation more often than a stated complaint.
- **One relationship is one point of failure.** Weight single-thread heavily even when the score looks fine.

## From signal to save play

| Dominant signal | Primary save play |
|---|---|
| Champion / sponsor loss | Executive reset |
| Low or falling adoption | Adoption rescue |
| Value not landing | Value gap re-scope |
| Budget or price pressure | Commercial relief (trade, not discount) |
| Competitive evaluation | Value gap plus a differentiated proof point |

Escalate anything classified Red to `account-planning` so the account's strategy is rewritten, not just patched at the next meeting.
