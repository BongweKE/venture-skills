# BD Skills — business development for AI agents

A portable suite of 13 **Agent Skills** covering the full business-development
motion — from market definition through prospecting, deal execution, and
post-sale expansion — written to the [Agent Skills specification](https://agentskills.io)
so the *same* skills load in every agent you run.

Author: BongweKE · License: MIT · Source of truth for four runtimes.

## Why a suite, not a pile of prompts

Business development fails in predictable places: an undefined ICP, outreach that
was never personalised, a proposal that argues price instead of value, and a
pipeline whose forecast nobody trusts. Each skill in this suite owns one of those
failure points end to end and produces a concrete artifact.

The suite shares one foundation document — `.agents/bd-context.md` — written and
maintained by `bd-context`. Every other skill reads it first, so you state your
company, ICP, and pricing **once** and never repeat yourself.

## The skills

| Skill | Use it when you need to… |
|-------|--------------------------|
| `bd-context` | Write/update the shared foundation doc (company, ICP, pricing, proof) |
| `market-segmentation` | Refine ICP, size the market (TAM/SAM/SOM), prioritise segments, run SWOT/Porter/PESTEL |
| `competitive-intelligence` | Teardown competitors and build battlecards |
| `value-proposition-and-pricing` | Sharpen positioning, build an ROI business case, design packaging/pricing |
| `prospect-research` | Turn the ICP into a verified, scored target list |
| `outbound-sequencing` | Design cold-email / LinkedIn / call cadences and write the copy |
| `discovery-call` | Prep and run discovery; capture MEDDPICC; send the follow-up |
| `proposal-and-quote` | Assemble a proposal, SOW, or quote |
| `objection-handling` | Answer objections; plan the negotiation |
| `pipeline-forecast` | Define stage gates, clean the CRM, build a forecast |
| `account-planning` | Build a strategic account plan and expansion path |
| `qbr-and-renewal` | Run a QBR; renew and expand; save at-risk accounts |
| `win-loss-review` | Debrief a won or lost deal and find the pattern |

## Install

```bash
python3 scripts/validate.py      # check every skill against the spec
python3 deploy.py                # install into all four runtimes
python3 deploy.py --check        # read-only: report drift
python3 deploy.py --target hermes opencode
```

| Runtime | Discovery path | Deploy mode |
|---------|----------------|-------------|
| Hermes Agent | `~/.hermes/skills/business-development/` | copy |
| OpenCode | `~/.config/opencode/skills/` | copy |
| Antigravity CLI | `~/.gemini/antigravity-cli/plugins/bd-skills/skills/` | copy |
| Mistral Vibe | `~/.vibe/skills/` | symlink |

Antigravity also gets a `plugin.json` and an entry in its `import_manifest.json`.

Deployment is idempotent and a `.bd-skills-manifest.json` records the source hash
of every deployed file, so `--check` can prove a deployed copy still matches the
source it came from. Never edit a deployed copy — edit `skills/` here and re-deploy.

## Repository layout

```
bd-skills/
├── AGENTS.md              # authoring spec: hard rules, structure, style guide
├── README.md
├── VERSIONS.md            # suite changelog
├── skills/<name>/         # SKILL.md + optional references/ templates/ scripts/
├── scripts/validate.py    # open-standard validator
└── deploy.py              # installs skills/ into the four runtimes
```

## Design rules

Every skill follows the rules in [`AGENTS.md`](AGENTS.md): portable frontmatter
(`name`, `description`, `license`, `metadata`), a description that leads with the
trigger in its first 57 characters, a fixed body structure, concrete artifacts
over abstract advice, and no fabricated facts — anything inferred is labelled an
assumption, and customer references are never invented.

## Credits

Architecture inspired by the open agent-skills ecosystem, in particular
[`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills)
(the shared-context foundation pattern) and the
[Agent Skills specification](https://agentskills.io).
