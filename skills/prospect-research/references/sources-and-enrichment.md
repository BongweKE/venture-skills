# Sources and Enrichment

Detail for `prospect-research` sections 2, 6 and 7. Read this when you are
choosing where data comes from or filling gaps in a list you already have.

## Source categories

| Category | Examples | Strength | Watch-outs |
|----------|----------|----------|-----------|
| Commercial providers | ZoomInfo, Apollo, Cognism, Lusha | Coverage + contacts, licensed for outreach | Overlapping records; stale after ~a year; check licence permits contact |
| Public registries | Company registries, licensing bodies, association member lists | Authoritative, legally clean | Firmographics only, rarely emails |
| Review / marketplace sites | G2, Capterra, sector equivalents | Reveals stack, size, and stated pain | Public profiles only; do not bulk-extract governed data |
| Company public surface | Site, press, investor pages, job boards | Fresh triggers, real language | Manual effort; do not scrape where terms forbid |
| Manual LinkedIn lookup | Human reading a profile | Confirms a title in seconds | Manual only — never automated collection |

## Waterfall enrichment

For each missing field, try sources cheapest-first and stop at the first hit:

1. Field already in your provider of record?
2. Try the primary provider's other modules.
3. Try a second provider for that field only.
4. Fall back to public registry / company site (manual).
5. If still missing, leave blank and mark `unmapped` — never guess.

Two providers disagreeing on firmographics is a `confidence: low` flag, not a coin flip.

## Deduplication

- Normalise `domain` (lowercase, strip `www`, strip path). Dedup accounts on the
  **registered domain**, not the display name — "Acme Ltd" and "Acme Limited" are one account.
- Dedup contacts on **(normalised domain + normalised name)**; a person moving to a
  new domain is a new row, not an update.
- Keep the row from the source with the highest confidence; merge triggers.

## Field coverage targets

Before shipping a sheet, check coverage:

- Firmographics (industry, size, geography): 100% — these drive the score.
- Mapped buying committee: at least the economic buyer for every tier-A account.
- Verified email: as high as the segment allows; never ship `unknown` as `valid`.
- Trigger: present for every tier-A account, or explain why not.
