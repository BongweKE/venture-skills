# Market Sizing: TAM, SAM, SOM

Build bottom-up by default. Top-down is a sanity check, never the headline. A number
without a basis and a source is a liability in any deck.

## Definitions

- **TAM (Total Addressable Market)** — everyone who could conceivably buy this category
  with any product, in your geography, at full penetration.
- **SAM (Serviceable Addressable Market)** — the slice you can actually serve with today's
  product, price, geography, and compliance posture.
- **SOM (Serviceable Obtainable Market)** — the share you can realistically win in 24-36
  months given sales capacity and competition.

## Bottom-up build (default)

1. **Count the buyers.** Start from a registry, an industry database, or a bottom-up
   estimate from a known population. State the exact count and its source.
   - `buyers = <count>` [source: <registry / DB / survey>, accessed YYYY-MM]
2. **Segment the count.** Break the total into the segments from the segmentation memo, or
   the tiers you sell into, so each number is defensible on its own.
3. **Attach a value.** Multiply by the realistic annual contract value (ACV), not the list
   price if you discount. `ACV = <amount>` [source: price sheet / closed-won average].
4. **Compute.**
   - `TAM = total buyers x ACV`
   - `SAM = serviceable buyers x ACV` (apply geography/product/compliance filters)
   - `SOM = SAM x realistic share`, where share is derived from a capacity model:
     `share <= (reps x quota x win rate) / SAM` over the period.
5. **Show the arithmetic inline.** `SAM = 1,200 clinics x KES 840k = KES 1.01B`.

Example skeleton:

```
Buyers (SAM)      = 1,200 clinics          [source: <registry>, 2024]
ACV (Roster tier) = KES 840,000 / yr       [source: price sheet]
SAM               = 1,200 x 840,000 = KES 1.008B
SOM (yr 3)        = 3 reps x KES 60M quota x 0.9 = KES 162M (~16% of SAM)
```

## Top-down cross-check

Compute it once, only to check the bottom-up figure:

- `TAM = total market spend x addressable share` or `population x penetration x price`.
- If top-down and bottom-up differ by more than roughly 30%, find the discrepancy before
  you publish either number. The gap is usually in buyer count or in ACV.

## Sanity checks

- Does your 3-year SOM exceed your sales capacity (reps x quota)? If yes, you are promising
  a market you cannot service.
- Is SAM more than about a third of TAM? If yes, you probably have not filtered for what
  you can actually sell (geography, compliance, product gaps).
- Does the SOM imply a market share that no comparable company holds? If yes, you are
  selling fiction.
- Does each number survive "says who"? Every count and every ACV needs a source or an
  explicit `[ASSUMPTION]`.

## Common inflation traps

1. **TAM as the headline.** Investors and boards discount it. Lead with SAM and SOM.
2. **Percent-of-market share.** "We will win 5% of a $2B market" is a hunch, not a plan.
   Tie SOM to capacity.
3. **List price instead of realized ACV.** Discounts, churn, and seat expansion change the
   real number.
4. **Unfiltered TAM.** Including geographies you cannot serve or buyer types you disqualify
   inflates the number and destroys credibility on the first question.
5. **Mixing sources across years.** A 2019 buyer count with a 2024 price is not a number.
   Date everything.
6. **No growth view.** A single static figure hides whether the segment is rising or dying;
   add a growth rate and its source.

## Output contract

Return a small table: segment, TAM, SAM, SOM, basis + source, growth rate. Mark every
assumption `[ASSUMPTION]`. Feed the SAM column into the segment scorecard.
