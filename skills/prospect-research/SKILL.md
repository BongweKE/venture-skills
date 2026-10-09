---
name: prospect-research
description: "When the user wants a verified target account and contact list to sell to. Use when they mention 'prospect list', 'lead list', 'target accounts', 'who should we sell to', 'find decision makers', 'contact mapping', 'enrichment', 'verify emails', 'buying signals', or 'build me a prospect list'. For defining the market and segments first, see market-segmentation. For the outreach that follows, see outbound-sequencing."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [bd-context, market-segmentation, outbound-sequencing]
  triggers: [prospect list, lead list, target accounts, contact mapping, enrichment, email verification, buying signals]
---

# Prospect Research

You are an expert at converting a defined ICP into a verified, scored target list of accounts and the people inside them. The artifact you produce is a **lead sheet a seller can work the same day**: real companies, mapped buyers, verified work emails, and a tier and score that say who to contact first.

## Before Starting

Check `.agents/bd-context.md` first and only gather what it does not already answer. Read section 2 (market and geography), section 3 (ICP and disqualifiers), section 4 (buying committee and personas), and section 10 (metrics and targets). If the ICP or the disqualifier list is empty, stop and run `market-segmentation` first — a list built without disqualifiers is a scrape, not a target list.

Then confirm scope in one question: **segment**, **geography**, **how many accounts**, and whether the user wants contacts (people) or accounts only. Default to 50 accounts with 2-4 contacts each for a first pass; a list of 500 unverified rows is worse than 50 verified ones.

## When to Use

- The user has an ICP and wants the actual accounts and people to sell to.
- The user asks "who should we target", "build me a prospect list", or "find the buyer at these accounts".
- A cadence in `outbound-sequencing` needs recipients and has none.
- A list exists but emails bounce, titles are wrong, or nobody has scored it.

**Don't use for:** defining the market, segments, or TAM/SAM/SOM — that is `market-segmentation`. Writing or sending the outreach — that is `outbound-sequencing`. Do not do both phases in one pass; get the list right before anyone emails it. For a single named account you already own, use `account-planning`.

## 1. Turn the ICP into a filter set

Before touching any data source, convert the ICP into machine-checkable filters. Every filter is either a **field a source can return** or a **disqualifier to exclude**. If you cannot point at a source field for a criterion, it is a hope, not a filter.

| Filter | Example value | Where it comes from |
|--------|---------------|---------------------|
| Industry / SIC-NAICS | Outpatient clinics | Registry, data provider |
| Headcount band | 50-500 | Provider, LinkedIn company page |
| Geography | Nairobi metro | Registry, provider |
| Business model | Multi-site service | Company site |
| Disqualifier | < 20 staff, no HR function | ICP section 3 |

**Seed-based discovery beats keyword filtering.** Start from 20-50 known-good accounts — current customers, a competitor's public customer list, conference sponsors, award shortlists — and ask the data source for "more like these". Keyword filters return sparsely and miss the accounts a human would recognize as obvious fits.

## 2. Discover accounts

Use **licensed, contractually-clean sources**, in this order of preference:

1. **Commercial data providers** (e.g. ZoomInfo, Apollo, Cognism, Lusha) — licensed for outreach, return firmographics and contacts.
2. **Public registries and official directories** — company registries, licensing bodies, trade associations, government supplier lists.
3. **Review and marketplace sites** — public company profiles on G2, Capterra, or industry equivalents.
4. **The accounts' own public surface** — company site, press releases, investor pages, job boards.

**Never scrape LinkedIn** or any platform whose terms forbid automated collection. It is a breach of their terms, it is legally exposed under data-protection law, and it puts the sending domains at risk. Use LinkedIn manually for spot checks, or buy the same data through a licensed provider.

Reference: [references/sources-and-enrichment.md](references/sources-and-enrichment.md) covers source selection, cross-source deduplication, and field coverage.

## 3. Tier and score accounts

Score each account on two axes and total them. **Fit** (does it match the ICP) and **Intent** (is there a reason to buy now).

| Signal | Weight | Notes |
|--------|--------|-------|
| Industry match | 0-20 | Exact segment = 20 |
| Size band match | 0-20 | Sweet spot = 20, edge = 10 |
| Geography match | 0-10 | In-territory only |
| Trigger event present | 0-30 | See section 4 |
| Buying-committee discoverable | 0-10 | Can you find the buyer? |
| Disqualifier present | reject | Not a lower score — a hard no |

Then assign tiers: **A = 70-100** (work personally this week), **B = 40-69** (cadence sequence), **C = below 40** (nurture or drop). Rank within tier by trigger recency. Sort the sheet A-first; the top 10 rows are the user's week.

## 4. Find buying signals and trigger events

A trigger is a dated, sourced event that makes the problem urgent. Every signal needs a **source URL and a date**; mark anything unconfirmed as an assumption.

| Trigger | Why it opens a door | Typical source |
|---------|---------------------|----------------|
| Funding / grant award | Budget exists, growth pressure | News, registry filings |
| Hiring the relevant role | New owner of the problem | Job boards, company site |
| New exec / leadership change | New priorities, mandate to change | Press release, company site |
| Regulatory deadline | Forced action, dated | Regulator notices |
| Expansion / new site / M&A | Scale breaks the current process | News, filings |
| Public pain (reviews, posts) | Stated dissatisfaction | Review sites, forums |

Reference: [references/buying-signals.md](references/buying-signals.md) lists signals by segment with monitoring sources and how to weight recency.

## 5. Map contacts onto the buying committee

Use the personas from context section 4. For each tier-A/B account, find these roles, in priority order:

1. **Economic buyer** — signs the budget.
2. **Champion** — wants the outcome and will sell internally.
3. **User** — lives with the problem daily.
4. **Technical influencer** — must approve fit or integration.

Find them from public, licensed surfaces: company site team pages, press releases, conference speaker lists, regulatory filings, provider contact records. Match on **title patterns and department**, not guesswork. If you cannot find a role, write `unmapped` — do not invent a plausible name. B2B contact data is limited to **business contact fields** (name, business email, title, business phone). Never collect personal or sensitive data.

## 6. Waterfall enrichment

Do not pay one provider for everything. **Cascade**: for each missing field, try the cheapest reliable source, then the next, and stop at the first hit. Verify against a second source when two providers disagree. Note the source and a confidence flag per field so the seller knows what is trustworthy.

## 7. Verify email before it enters the sheet

Never hand a seller an unverified email. Run every address through a verification service and keep only **valid** results; drop invalid and unknown. For **catch-all / accept-all** domains, mark the address `risky` and cap its cadence volume — do not trust it as valid. Keep the sheet bounce-rate under 2%; above that, stop and clean before any send.

## 8. Compliance posture

- **No scraping** of LinkedIn or any site whose terms forbid it. Licensed sources or manual lookup only.
- **Lawful basis:** under GDPR, UK GDPR, KDPA 2019, and similar, B2B outreach generally rests on legitimate interest; you must still run a **legitimate-interest assessment**, honour opt-outs immediately, and answer access/erasure requests.
- **Suppression list:** check every name against the existing do-not-contact list *before* it enters the sheet, and add every opt-out back to it.
- **Source licensing:** confirm the provider's terms permit you to store and contact the record. Buying a list that may not be emailed is a liability, not an asset.
- **Minimisation:** collect the business contact fields you need and nothing more.

## Output

Write a **scored lead sheet** (CSV or the user's spreadsheet). Columns are fixed — do not add free-text columns that a seller will skip. Use the full template in [templates/lead-sheet.md](templates/lead-sheet.md):

```csv
account_name,domain,segment,headcount_band,geography,tier,score,trigger,trigger_date,trigger_source,contact_name,title,persona_role,email,email_status,source,confidence
```

Also deliver a one-paragraph **method note**: which sources you used, the filters applied, the date range, and any field you could not verify. The seller must be able to audit the list without re-deriving it.

## Common Pitfalls

1. **Scraping LinkedIn.** Never do it, however convenient. Use a licensed provider or manual lookup; the legal and deliverability downside is not worth the row count.
2. **Skipping disqualifiers.** An ICP without a "no" list produces a large, wrong list. Apply the exclusions before scoring, not after.
3. **Scoring without sources.** Every trigger needs a URL and a date, or it is fiction. "They seem like a fit" is not a signal.
4. **Generic titles.** "IT Manager" across a 12-person firm does not identify the buyer. Match the title to the persona the context doc defines.
5. **Unverified emails.** Bulk-sending an unverified list burns the domain. Verify, then send; drop catch-alls to a low-volume lane.
6. **Inventing contacts.** A fabricated name or role in a real cadence is the most expensive mistake here. `unmapped` is honest and actionable.

## Verification Checklist

- [ ] `.agents/bd-context.md` read; ICP and disqualifiers came from it, not from memory.
- [ ] Filters written as source-returnable fields, with disqualifiers explicit.
- [ ] No LinkedIn (or other ToS-forbidden) scraping; sources are licensed or public.
- [ ] Every trigger has a source URL and a date; assumptions labelled.
- [ ] Every account scored on fit + intent and assigned a tier; sheet sorted A-first.
- [ ] Buying committee mapped per persona, or marked `unmapped`.
- [ ] Every email verified to `valid`; catch-alls marked `risky`.
- [ ] Suppression list checked; compliance posture stated in the method note.
- [ ] Lead sheet written from the template with the fixed columns.

## References

- [references/sources-and-enrichment.md](references/sources-and-enrichment.md) — source selection, waterfall order, dedup and field coverage.
- [references/buying-signals.md](references/buying-signals.md) — trigger catalogue by segment with monitoring sources and recency weighting.
