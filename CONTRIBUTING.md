# Contributing

Thanks for considering a contribution. This repository is small enough that one
rule matters more than process: **a skill is a product, and it has a contract.**

## Before you open a PR

```bash
python3 scripts/validate.py    # must print "all skills pass"
npm test                       # must be 0 failures
npm run credits                # if you touched registry/sources.json
```

CI runs exactly these. A PR that fails the validator will not be reviewed.

## The authoring contract

Full rules are in [`AGENTS.md`](AGENTS.md). The short version:

- Frontmatter contains only `name`, `description`, `license`, `metadata`.
  `name` must equal the directory name and match `^[a-z0-9]+(-[a-z0-9]+)*$`.
- The description opens with a routing trigger. Runtimes index a truncated
  opening of it, so the first ~57 characters must stand alone.
- Required sections appear in this order: `## Before Starting`,
  `## When to Use`, `## Common Pitfalls`.
- `SKILL.md` is between roughly 6,000 and 20,000 characters and under 500 lines.
- Every `(references/...)` and `(templates/...)` link must resolve to a file
  that exists in the skill directory.
- Every name in `metadata.related-skills` must resolve either to a skill in this
  repository or to a name in `catalog/known-skills.txt`.
- No raw emoji. The validator rejects them; use text or describe the icon.

## What makes a good skill here

**Write decisions, not tutorials.** A skill that explains what a forecast is has
failed. A skill that decides what makes a deal commit-grade, in order, with the
exceptions named, has succeeded.

**Never fabricate evidence.** No invented market sizes, growth rates, benchmark
percentages, survey results or customer quotes. Any non-sourced belief is labelled
`[ASSUMPTION]` with what would falsify it. This is the single most important rule
in the repository.

**Stay portable.** Skills ship publicly. No company-specific pricing, geography,
bank details or compliance specifics belong in a skill body; those live in the
per-engagement `.agents/bd-context.md`.

**Link instead of restating.** If a skill already exists for the *how*, name it.
See `skills/venture-skills-root/references/corpus-map.md`.

**State the boundary.** Each skill should say what it does *not* cover and which
sibling owns that instead. This is what keeps twenty-one skills from collapsing
into twenty-one overlapping ones.

## Adding a curated third-party source

Add it to `registry/sources.json` with:

- `repo` as `owner/name`
- `license` (the real upstream SPDX id; check it)
- `ref` to pin
- `why` explaining what it adds
- `include` with the specific skills to curate

Then run `npm run credits` and commit the regenerated `CREDITS.md` and
`registry/installed.json`. Tests fail if those drift from the registry.

**Curate, do not bulk-import.** If a source has a skill that overlaps one in
`skills/`, leave it out. Two skills competing for the same trigger make an agent
worse, not better. `tests/registry.test.mjs` enforces this.

## Reporting a problem with attribution

If you are the author of a curated source and want your credit changed, or want
your work removed, open an issue. Attribution requests are handled first.
