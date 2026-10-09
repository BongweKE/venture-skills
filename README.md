# venture-skills

Business, product and engineering skills for AI coding agents.

Give your agent a business brief before it writes code. venture-skills teaches it
to work from market evidence, business need, SOPs, system design and security
requirements, and to hand the actual engineering craft to the skills you already
have installed.

Works with **Hermes**, **OpenCode**, **Antigravity CLI** and **Mistral Vibe**.
Every runtime reads the same open `SKILL.md` format, so these skills are authored
once and deployed to all four.

```bash
npx venture-skills list
npx venture-skills install          # deploy to every runtime it can find
npx venture-skills doctor           # verify each runtime can see every skill
```

## The problem this solves

Most agent skills teach craft: how to write a component, how to design a schema,
how to configure CI. Those are largely solved, and you probably already have
good ones installed.

What is usually missing is the layer above: deciding *what* is worth building and
*why*, in terms an engineering team can act on. Without it, an agent produces
plausible code that satisfies the prompt and answers no business question. The
feature ships, nobody uses it, and no one can say which KPI it was meant to move.

venture-skills fills that gap. It is a chain of fifteen stages carrying a
commercial intent through to a launched, defensible system, with an artifact
written at every stage.

## The chain

| # | Stage | Skill |
|---|-------|-------|
| 0 | Foundation | `bd-context` |
| 1 | Market | `market-segmentation` |
| 2 | Competition | `competitive-intelligence` |
| 3 | Offer | `value-proposition-and-pricing` |
| 4 | Demand | `prospect-research`, `outbound-sequencing` |
| 5 | Conversation | `discovery-call`, `objection-handling` |
| 6 | Commitment | `proposal-and-quote` |
| 7 | Land and grow | `account-planning`, `pipeline-forecast`, `qbr-and-renewal`, `win-loss-review` |
| 8 | Product | `product-discovery` |
| 9 | Specification | `business-need-to-prd` |
| 10 | System design | `prd-to-system-design` |
| 11 | Trust | `security-by-design` |
| 12 | Traceability | `feature-traceability` |
| 13 | Automation | `sop-to-automation` |
| 14 | Release | `launch-readiness` |

Stages 0 to 7 decide what is worth building and what it is worth. Stages 8 to 14
turn that decision into a specified, threat-modelled, traceable, launchable
system. Start at `venture-skills-root`: it routes you to the right stage and
names the skills to load for the *how*.

## Interlinking: the WHY and the HOW

This repository deliberately does not re-teach engineering, design, security or
growth craft. Those skills exist, they are better than anything this repo could
restate, and duplicating them creates routing ambiguity that makes agents worse.

The division is explicit:

- **venture-skills owns the WHY and the WHAT.** Which segment, which offer, which
  price, which requirement, which risk, which release gate.
- **The wider corpus owns the HOW.** How to type the API, how to lay out the
  screen, how to write the migration, how to configure the pipeline.

Every stage skill names the corpus skills that implement its artifact, and the
link runs both ways: when using a corpus skill surfaces a commercial
consequence, that consequence is written back into the relevant stage artifact.

- `skills/venture-skills-root/references/routing-table.md` maps tasks to skills,
  including re-entry loops for when a later stage invalidates an earlier one.
- `skills/venture-skills-root/references/corpus-map.md` maps the four corpus
  categories (UI/UX, marketing, support journey, engineering and security) to the
  stages that hand off to them.

## Curated skills and attribution

A separate curated layer installs high-value third-party skills that complement
this suite: architecture, threat modelling, SLOs, ADRs, business metrics,
full-stack patterns, UX and marketing.

**We do not vendor other people's work.** Curated skills are fetched from their
upstream repositories at install time by `scripts/install-external.py`, pinned to
a revision, and installed alongside our own. Every source is recorded in
`registry/sources.json` with its licence and rationale, and attribution is
generated into [`CREDITS.md`](CREDITS.md).

Skills this suite already covers are deliberately excluded from import, so two
skills never compete for the same trigger.

## Install

```bash
# everything the CLI can find
npx venture-skills install

# or one runtime
npx venture-skills install --runtime opencode
npx venture-skills install --runtime hermes --dry-run
```

Manual install is just a copy. Each skill is a directory containing `SKILL.md`
plus optional `references/` and `templates/`:

| Runtime | Path |
|---|---|
| Hermes | `~/.hermes/skills/<suite>/<name>/` |
| OpenCode | `~/.config/opencode/skills/<name>/` |
| Antigravity CLI | `~/.gemini/antigravity-cli/plugins/venture-skills/skills/<name>/` |
| Mistral Vibe | `~/.vibe/skills/<name>/` |

Antigravity also gets a `plugin.json` and an entry in its `import_manifest.json`.
The Python deployer is the richer installer (it registers the Antigravity plugin
and records a source hash per deployed file so drift is detectable); the Node CLI
covers the plain copy case.

## Repository layout

```
skills/           21 authored skills (the product)
bin/              the CLI, zero dependencies
registry/         curated third-party sources + generated attribution
catalog/          the cross-link registry of every installed skill name
scripts/          validate, deploy, install-external, gen-known-skills, gen-credits
tests/            format, CLI and registry contracts
docs/             architecture and the linking model
```

## Development

```bash
python3 scripts/validate.py       # authoring spec: structure, size, links, emoji, cross-links
npm test                          # format, CLI and registry contracts
npm run credits                   # regenerate CREDITS.md from the registry
python3 scripts/deploy.py         # push skills into the four runtimes
python3 scripts/deploy.py --check # drift: has a runtime copy diverged?
npm run catalog                   # regenerate the installed-corpus registry
```

`python3 scripts/validate.py` is the gate. It enforces the authoring rules in
[`AGENTS.md`](AGENTS.md): frontmatter fields, name format, description length,
size limits, section order, resolvable links and resolvable cross-references.

Never edit a deployed copy in a runtime directory. Edit `skills/` here and
re-deploy.

## Licence

MIT for everything in `skills/`, `bin/`, `scripts/` and `tests/`. Curated
third-party skills remain under their own upstream licences — see
[`CREDITS.md`](CREDITS.md) and [`NOTICE.md`](NOTICE.md).
