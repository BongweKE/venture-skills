# Product Discovery Research Methods

Deep detail behind the SKILL.md workflow: how to interview, how to validate a
problem, how to scan demand signals, and how to grade evidence. Read the relevant
section only; the SKILL.md is the workflow.

## 1. Framing a falsifiable research question

A discovery effort is only as good as its question. Convert the idea into a claim
that could be proven false, and name the decision it feeds.

- Bad: "Is there a market for a rota tool?" (unfalsifiable, no decision attached)
- Good: "Do clinic administrators who plan rotas manually lose more than 20 hours a
  month to it, and would they reallocate existing budget to fix it?" (falsifiable;
  the answer changes whether we build)

Write down the **disconfirming evidence** first. If the answer is "we would still
build anyway", the research is theatre — stop and be honest about that.

## 2. Problem interviews (The Mom Test discipline)

The single biggest source of bad discovery data is asking people to predict their
own future behaviour. Follow these rules:

1. **Talk about their life, not your idea.** Never describe the product. A described
   idea earns compliments, not truth.
2. **Ask about the past, not the hypothetical.** "Walk me through the last time you
   did this" beats "would you use...".
3. **Ask for specifics, not opinions.** "How much did that cost you last month?" not
   "is that annoying?".
4. **Watch what they do, not what they say.** A workaround, a spreadsheet, a paid
   tool — behaviour is evidence; enthusiasm is not.
5. **Cut off compliments.** "That's a cool idea" is a stop signal, not data.

### Interview script (30 minutes)

- Warm-up: "What does a normal Monday look like in your role?" (context)
- Problem probe: "Tell me about the last time <the problem> happened. What did you
  do? Who else was involved? How long did it take?"
- Cost probe: "What did that cost you — time, money, or a mistake you had to fix?"
- Workaround probe: "How do you handle it today? Show me, if you can."
- Trigger probe: "What made you actually go looking for a fix last time?" (or: "Why
  haven't you fixed it yet?")
- Close: "Who else should I talk to about this?" (referral compounding)

Do not ask "would you buy", "how much would you pay", or "do you like this idea".

## 3. Jobs-to-be-done framing

Capture the job, not the feature request. Use the Job Story form:

```
When <situation>, I want to <motivation>, so I can <expected outcome>.
```

Example:

```
When a nurse calls in sick two hours before a night shift,
I want to find a qualified replacement fast,
so I can keep the ward within safe staffing ratios.
```

Each interview yields zero to two job stories. Cluster them across interviews; the
cluster that recurs most is the strongest signal of a shared job.

## 4. Problem validation: the three axes

A problem is worth solving when all three axes are strong:

| Axis | Question | Weak | Strong |
|------|----------|------|--------|
| Frequency | How often does it occur? | Annual | Daily / weekly |
| Severity | What does it cost when it happens? | Mild annoyance | Money, safety, legal risk |
| Current spend | What do they already spend to cope? | Nothing | Budget line, paid tool, staff hours |

Rule of thumb: high frequency + low severity is a feature; low frequency + high
severity is an incident; high frequency + high severity + existing spend is a
business. Aim for the third.

## 5. Demand-signal scanning

Demand signals are observable traces of people already trying to solve the problem.
Gather at least two independent ones before treating demand as real.

| Signal class | Where to look | What counts |
|--------------|---------------|-------------|
| Search | Public keyword-trend tools | Rising, sustained volume for problem terms |
| Community | Forums, groups, review sites | Repeated threads naming the pain |
| Labour | Job postings | Roles hired to do the manual work |
| Money | Procurement portals, tender listings | Budget allocated to the problem |
| Competition | Vendor landscape | Funded competitors = proven demand |
| Workaround | Marketplaces | Paid spreadsheets, consultants, ad-hoc tools |

Use the installed tooling where it fits:

- `competitor-news-monitor` — track a named company's material news over time
  (funding, launches, pivots) as a demand and competitive signal.
- `domain-intel` — passive domain/technical reconnaissance when you need to profile
  a prospective buyer's or competitor's public surface.
- `grounded-citations` — capture each source as a citation so the brief stays
  auditable and every claim carries a URL.

Record **source + access date** for every signal. A signal without provenance is a
rumour.

## 6. Evidence grading

Every claim gets a status and a confidence level. Do not blur them.

| Status | Meaning | Allowed in brief |
|--------|---------|------------------|
| Verified | A cited source proves it | Yes, with source |
| Assumption | You believe it, no source yet | Yes, marked `[ASSUMPTION]` |
| Refuted | A source disproves it | Yes — record it, do not bury it |

Confidence is High / Medium / Low, driven by source quality (primary interview >
public signal > secondhand claim) and sample size. Three interviews is a hint; ten
that agree is a pattern.

## 7. Sample size and recruiting

- Recruit 5-10 people per segment from the buying committee, not just end users.
- Stop when three consecutive interviews surface nothing new (saturation), not at a
  fixed number chosen in advance.
- Recruit via: existing customers, referrals from interviews, communities where the
  segment gathers, and outbound to a named list (`prospect-research` can build one).
- Bias check: are you only talking to friendly contacts? Deliberately include one
  disconfirming voice per round.

## 8. Bias traps

1. **Confirmation bias** — you hear what you want. Fix: pre-commit to disconfirming
   evidence.
2. **Leading questions** — "don't you hate...?" Fix: open, past-tense, behavioural.
3. **Friendly-sample bias** — only fans answer. Fix: seek a skeptic each round.
4. **False consensus** — one loud forum equals a market. Fix: two independent
   signals, and check repetition.
5. **Survivorship** — you interview users, not the people who tried and quit. Fix:
   ask for churned or lapsed users.
6. **Sunk-cost framing** — the team already "knows" it is good. Fix: the brief's job
   is to try to kill the idea; if it survives, it is genuinely stronger.

## 9. Output contract

Feed into the brief's evidence table: one row per claim, with `Status`, `Source`
(URL + date), and `Confidence`. The brief is only as trustworthy as its weakest
load-bearing row. Apply the go/no-go rule from SKILL.md section 5 against these rows.
