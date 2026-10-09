# ROI Business-Case Calculator Outline

Build the case in money, bottom-up from the client's own volumes. Mark every input
`[CLIENT]` (client-supplied) or `[ASSUMPTION]` (yours, with a source or a range). Never
present a modeled number as a measured one. Lead with the conservative case.

## 1. Baseline (the client's status quo)

| Input | Value | Basis |
|-------|-------|-------|
| Volume of work per period (transactions, records, payouts) | | `[CLIENT]` |
| Hours spent on the process per period | | `[CLIENT]` |
| Loaded hourly cost (salary + overhead / hours) | | `[CLIENT]` or `[ASSUMPTION]` |
| Error / rework rate and cost per error | | `[CLIENT]` |
| Penalty, interest, or fine exposure per period | | `[CLIENT]`, cite the rule |
| Revenue leaked / churn attributable | | `[ASSUMPTION]` with a range |

## 2. Cost of inaction (annualized)

Compute the cost of doing nothing. This is usually the strongest number in the case.

```
Manual labour cost      = hours/period x loaded rate x periods
Error / rework cost     = errors/period x cost per error x periods
Penalty / risk cost     = exposure/period x periods (weighted by probability)
Revenue / churn cost    = leaked revenue (state the assumption)
                         -----------------------------------------
Cost of inaction (yr)   = sum of the above
```

Mark any line built on an assumption `[ASSUMPTION]` and give it a range.

## 3. Value created (the delta)

Measure against the client's baseline, not against zero.

| Value driver | Conservative | Base | Aggressive | Basis |
|--------------|--------------|------|------------|-------|
| Hours saved x loaded rate | | | | `[ASSUMPTION]` % saved |
| Errors / penalties avoided | | | | `[CLIENT]` rates |
| Revenue protected / gained | | | | `[ASSUMPTION]` |
| Risk reduction (weighted) | | | | `[ASSUMPTION]` |
| **Total annual benefit** | | | | |

## 4. Return and payback

| Metric | Value |
|--------|-------|
| Annual price (subscription + one-off) | |
| Year-1 net benefit (benefit - price) | |
| Payback period (months) | `price / (monthly benefit)` |
| 3-year ROI ratio | `(3-yr benefit - 3-yr cost) / 3-yr cost` |
| Net present value (state the discount rate) | |

## 5. 3-year cash-flow view

| | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|
| Benefit (conservative) | | | |
| Cost | | | |
| Net | | | |
| Cumulative | | | |

## 6. Sensitivity

- Which single input moves the payback most? Show `if <input> varies +/- 25%`.
- State the break-even value on the most sensitive input.
- If the conservative case does not clear the client's hurdle, say so plainly.

## 7. Sources and assumptions register

List every `[ASSUMPTION]`, its value or range, and what would confirm it. List every
`[CLIENT]` input and who supplied it. This register is what makes the case defensible in a
negotiation — an unaudited ROI is the first thing a CFO attacks.
