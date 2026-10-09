---
name: bd-context
description: "When the user wants to set up or update their business-development context, or mentions 'BD context', 'sales context', 'company context', 'who do we sell to', 'our ICP', 'value proposition', 'positioning', 'pricing model', 'sales motion', or is starting any BD/sales task and no context doc exists yet. Run this first — it writes `.agents/bd-context.md`, the foundation document every other business-development skill reads so the user never repeats themselves."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [market-segmentation, value-proposition-and-pricing, competitive-intelligence]
  triggers: [bd context, sales context, company context, ICP, positioning, value proposition]
---

# Business Development Context

You maintain the shared context document that every other skill in this suite
reads before it does anything. Your job is to turn scattered knowledge — repo,
website, pitch decks, the user's head — into one accurate, versioned file at
`.agents/bd-context.md`.

This skill is the reason the other twelve skills can be short: they assume the
commercial reality is already written down.

## Before Starting

Check for an existing `.agents/bd-context.md`. Also check these legacy locations
and offer to move the file to the canonical path if found:

- `.claude/bd-context.md`
- `bd-context.md` (repo root)
- `docs/bd-context.md`

**If it exists:** read it, summarize what is captured, and show its current
**Version** and the last few **Changelog** entries. Ask which sections to update
and gather only those. Never rewrite the whole doc to change one section.

**If it does not exist:** do not interview from a blank page. Offer:

1. **Auto-draft (recommended).** Read the repo and public surface — README,
   landing/marketing copy, `package.json`/`pyproject.toml`, pricing pages, the
   about page, any pitch or investor material — and draft a V1 of every section
   you can fill. Present it and ask only "what is wrong, what is missing?"
2. **Interview.** Walk the sections below one at a time, conversationally. Do not
   dump all questions at once.

Prefer auto-draft. It is faster and the user corrects better than they recall.

## When to Use

- The user is starting any BD, sales, or go-to-market task and no context doc exists.
- The user says the company's positioning, pricing, or ICP has changed.
- A sibling skill (prospecting, proposals, battlecards) reads the context and finds
  it missing or stale.

**Don't use for:** building a target list, writing outreach, or a specific deal —
those are `prospect-research`, `outbound-sequencing`, and `discovery-call`. This
skill only writes the foundation they consume.

## Sections to Capture

Write exactly these twelve sections, in this order. Omit a section only if it is
genuinely inapplicable, and say so in the doc rather than leaving it blank.

### 1. Company and business model
- One-line description; what the company does in 2–3 sentences.
- Category (the "shelf" buyers search on) and business model (SaaS, services,
  marketplace, usage-based).
- Stage, headcount, funding, and the single most important goal this quarter.

### 2. Market and geography
- Primary and secondary markets; countries/regions served.
- Currency and payment rails in play (e.g. KES + M-PESA/PesaLink, USD + card).
- Regulatory or compliance constraints that shape deals (data-protection regime,
  licensing, procurement rules).

### 3. Ideal Customer Profile (ICP)
- Firmographics: industry, size (headcount/revenue), geography, business model.
- The trigger that makes a company buy *now*.
- **Disqualifiers** — the clearest way to lose money is to sell to the wrong buyer.
  List them explicitly.

### 4. Buying committee and personas
For each role in the buying decision — economic buyer, champion, user, technical
influencer, blocker (for consumer products, just the buyer):
- What they are measured on; their pain; the value you promise *them*.
- Their most likely objection.

### 5. Problems and pain
- The core problem before you existed, in the customer's own words.
- Why current workarounds fall short.
- What the problem costs (money, hours, risk) — quantify where possible.

### 6. Value propositions and differentiators
- 2–4 value props, each in the form: *for [persona], we [capability] so they can
  [outcome], unlike [alternative].*
- The one differentiator you would defend in a competitive deal.
- Proof points: metrics, case results, guarantees. Mark anything unverified.

### 7. Offer, packaging, and pricing
- Tiers/packages, price points, and what changes between them.
- Discount and prepayment policy; onboarding or setup fees; minimums.
- Unit economics guardrails (floor price, approval thresholds).

### 8. Competitive landscape
- Direct, secondary, and status-quo ("do nothing / spreadsheet") competitors.
- For each: how you win, how you lose.
- Link to `competitive-intelligence` output if battlecards exist.

### 9. Sales motion and stages
- Motion (self-serve, sales-led, product-led, channel/partner).
- Deal stages in order, with the exit criterion for each.
- Typical cycle length and ACV/contract size.

### 10. Metrics and targets
- Current and target: pipeline value, win rate, cycle length, ACV, NRR/churn,
  CAC. Mark current-actual vs target.
- The one number leadership watches.

### 11. Proof and references
- Named or anonymized customers willing to be referenced, and what each will say.
- Never invent a logo or a quote. If the user has no reference customers, write
  "none yet" — a fabricated reference is the most expensive mistake in this doc.

### 12. Constraints and non-negotiables
- Legal, ethical, or brand rules that bind every deal (e.g. "never gate a
  statutory deadline behind a paywall", "no deductions from employee pay").
- Anything the sales team must never promise.

## Output

Write `.agents/bd-context.md`. Use this skeleton:

```markdown
# BD Context — <Company>

**Version:** 1.0.0
**Updated:** <YYYY-MM-DD>
**Owner:** <name>

## 1. Company and business model
…

## 12. Constraints and non-negotiables
…

---

## Changelog
- <YYYY-MM-DD> — v1.0.0 — initial context created from <sources>.
```

Rules for the file:

- Push for **verbatim customer language** in sections 5 and 6 — exact phrases make
  outreach and proposals resonate; polished paraphrases do not.
- Mark every unverified claim `[UNVERIFIED]` inline. Do not launder a guess into a fact.
- On any substantive save, bump the version (major = repositioning/pricing change,
  minor = new section or offer, patch = corrections) and add a changelog line.
  Downstream skills read this file; a silent change breaks their assumptions.

## Common Pitfalls

1. **Interviewing from scratch when a repo exists.** The codebase already contains
   the positioning. Auto-draft first; the user corrects faster than they recall.
2. **Leaving disqualifiers empty.** An ICP with no "who we say no to" is not an ICP;
   it is a wish. Force the user to name at least three disqualifiers.
3. **Inventing proof.** Never write a customer logo or quote that was not supplied.
   "None yet" is a valid and useful entry.
4. **Writing a brochure instead of a brief.** This file is consumed by agents, not
   buyers. Short, factual, specific. Cut adjectives.
5. **Silent edits.** Changing pricing or ICP without bumping the version and
   changelog leaves sibling skills reasoning on a stale premise.
6. **Filling every section even when unknown.** An honest "TBD" beats a plausible
   fiction — the fiction gets quoted back in a real proposal.

## Verification Checklist

- [ ] `.agents/bd-context.md` exists at the canonical path (legacy copies moved).
- [ ] All twelve sections present, or explicitly marked inapplicable.
- [ ] Sections 3 and 4 include disqualifiers and per-persona objections.
- [ ] Section 6 value props follow the *for / we / so they can / unlike* form.
- [ ] Section 7 states price points and approval guardrails.
- [ ] Section 11 contains no fabricated references.
- [ ] Unverified claims marked `[UNVERIFIED]`.
- [ ] Version and changelog updated on this save.
