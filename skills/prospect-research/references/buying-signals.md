# Buying Signals and Trigger Events

Detail for `prospect-research` section 4. A trigger is a **dated, sourced event**
that makes the buyer's problem urgent. No URL and date means it is not a trigger.

## Weighting

- **Recency:** a trigger in the last 90 days scores full weight; 3-6 months scores
  half; older than 12 months is context, not a trigger.
- **Specificity:** an event naming the exact problem beats a generic growth signal.
- **Source quality:** a press release or filing beats a rumour; label the weak ones
  as assumptions.

## Catalogue by segment (adapt labels to the user's ICP)

| Segment type | Signal | Where to look |
|--------------|--------|---------------|
| Regulated services | New licence, inspection finding, compliance deadline | Regulator notices, association bulletins |
| High-growth | Funding round, grant, hiring spike | News, filings, job boards |
| Multi-site operations | New site, branch, or acquisition | News, filings, company site |
| Hiring-led | Job post for the role that owns the pain | Job boards, careers page |
| Leadership change | New exec with a mandate | Press release, company site |
| Tech adoption | Announced tool change or migration | Press, job posts citing the stack |
| Stated pain | Negative reviews, forum posts, public complaints | Review sites, sector forums |
| Cost pressure | Layoffs, procurement review, vendor consolidation | News, filings |

## Using a trigger in the sheet

- Record `trigger`, `trigger_date`, and `trigger_source` together.
- Score it (0-30) and sort tier-A rows by recency.
- Hand the trigger line to `outbound-sequencing` — it becomes the opening line of
  the first email, and the only personalisation signal the seller actually needs.

## Monitoring

For a standing list, re-check the highest-value sources monthly (news, filings,
job boards). Do not attempt continuous scraping. Set a quiet reminder rather than
polling a platform that forbids it.
