# Funnel analytics — detail

Reference for `pipeline-forecast`. Load when computing conversion, weighting the
pipeline, or diagnosing where the forecast leaks. Core steps live in `SKILL.md`.

## 1. Pull the raw data

For every deal closed in the period (won or lost), capture: entry stage, exit stage,
entry date, close date, amount, source, segment, and loss reason. Compute only from
closed deals — open deals have no outcome yet and bias the numbers.

## 2. Stage-to-stage conversion

For each boundary N -> N+1:

```
conversion(N->N+1) = deals that reached N+1 / deals that reached N
```

- Use deals that *entered* stage N, not all deals, so a deal that skipped a stage
  cannot inflate the rate.
- The stage with the lowest conversion is the bottleneck. Put coaching and
  inspection there, not evenly across the funnel.
- A conversion above ~90% usually means the stage is not a real gate — tighten or
  merge it.

## 3. Win rate

```
win rate = wins / (wins + losses)
```

- Split by segment, source, and deal size; a blended win rate hides which motion
  works.
- Exclude disqualified and duplicate deals — they are not losses you can learn from.
- Track "no-decision" losses separately; in many funnels the biggest competitor is
  inertia, not a rival.

## 4. Cycle time

```
average cycle = mean(close date - first qualified date)
```

- Measure per stage and end-to-end; per-stage time shows where deals actually stall.
- Compare to `bd-context` §9 typical cycle length. A rising cycle with a flat win rate
  means qualification is loosening, not that the market slowed.

## 5. Weighted forecast

```
weighted pipeline = sum over open deals of (amount x stage probability)
```

Set stage probability from the user's own history: for deals that reached stage N,
the share that eventually closed won. That is the honest weight for stage N. Textbook
defaults are a starting point only when no history exists yet:

| Stage | Typical starting weight |
|-------|-------------------------|
| Discovery | 0.10 |
| Solution fit | 0.20 |
| Validation | 0.35 |
| Proposal | 0.50 |
| Negotiation | 0.65 |
| Commit | 0.90 |

Report weighted pipeline alongside commit and best case — never instead of them.

## 6. Coverage ratio

```
coverage = open qualified pipeline / period target
```

Healthy default is **3x** for a mature funnel, higher (4-5x) when win rates are low
or cycles are long. A gap means the fix is pipeline generation, not closing tactics.

## 7. Pipeline velocity

```
velocity = (qualified opportunities x avg deal size x win rate) / cycle length
```

Velocity expresses revenue per unit time and is the retrodicted rate of the funnel.
If velocity x remaining periods < target, the quarter is short regardless of how the
CRM feels. Raise velocity by improving any one factor — more qualified opps, higher
win rate, bigger deals, or shorter cycles — but measure one change at a time.

## 8. Worked example

Inputs (period): 40 qualified opportunities, average deal 200,000, win rate 25%,
average cycle 60 days.

```
velocity = (40 x 200,000 x 0.25) / 60 = 33,333 per day
over a 90-day quarter = 3,000,000
```

If the target is 4,000,000, the funnel is short by 1,000,000 — a coverage and win-rate
problem, not a discounting problem. Levers: raise qualified opps to ~53, lift win rate
to ~33%, or cut the cycle. Pick the lever the bottleneck stage points to.

## 9. Cohort and trend reads

- **Cohort by entry month:** track win rate of deals that entered in each month to
  separate a weak pipeline from a weak season.
- **Trend, not snapshot:** read conversion and velocity over at least three periods;
  a single period is noise.
- **Segment split:** the best funnel read is per segment — the motion that wins SME
  deals rarely wins enterprise ones.
