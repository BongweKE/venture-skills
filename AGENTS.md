# AGENTS.md — venture-skills authoring specification

Guidelines for humans and AI agents working in this repository.

## 1. What this repo is

Portable **Agent Skills** that make a coding agent work from business evidence,
business need, SOPs, system design and security requirements before it writes
code. Written to the [Agent Skills specification](https://agentskills.io)
(`<skill-name>/SKILL.md`). One source of truth, deployed to four agent runtimes:

| Runtime | Discovery path | Deploy mode |
|---------|----------------|-------------|
| Hermes Agent | `~/.hermes/skills/<suite>/<name>/` | copy |
| OpenCode | `~/.config/opencode/skills/<name>/` | copy |
| Antigravity CLI | `~/.gemini/antigravity-cli/plugins/venture-skills/skills/<name>/` | copy |
| Mistral Vibe | `~/.vibe/skills/<name>/` | symlink |

Run `python3 scripts/deploy.py` to install; `--check` to detect drift. Never
hand-edit a deployed copy — edit `skills/` here and re-deploy.

Two suites:

- **business-development** — the commercial chain (14 skills).
- **business-to-app** — the bridge from commercial intent to delivered software
  (7 skills).

`venture-skills-root` is the router. An agent reads it first, then loads exactly
one stage skill. See `docs/linking-model.md`.

## 2. Repository layout

```
venture-skills/
├── AGENTS.md                 # this spec
├── README.md                 # human-facing overview
├── CHANGELOG.md              # the changelog
├── VERSIONS.md               # versioning scheme + per-skill version table
├── CONTRIBUTING.md
├── CREDITS.md                # GENERATED — do not hand-edit
├── skills/                   # the product: Agent Skills (open standard)
│   └── <skill-name>/
│       ├── SKILL.md          # required
│       ├── references/       # optional — detail loaded on demand
│       ├── templates/        # optional — reusable output artifacts
│       └── scripts/          # optional — executable helpers
├── bin/venture-skills.mjs    # the CLI (zero dependencies)
├── registry/
│   ├── sources.json          # curated third-party sources (hand-edited)
│   └── installed.json        # GENERATED — do not hand-edit
├── catalog/
│   ├── CATALOG.md            # the cross-link map of the corpus
│   └── known-skills.txt      # GENERATED — installed skill names
├── scripts/
│   ├── validate.py           # authoring spec validator (the gate)
│   ├── deploy.py             # installs skills/ into the four runtimes
│   ├── install-external.py   # vendors curated third-party skills
│   ├── gen-known-skills.py   # regenerates catalog/known-skills.txt
│   └── gen-credits.mjs       # regenerates CREDITS.md + registry/installed.json
├── tests/                    # format, CLI and registry contracts
└── docs/                     # architecture, linking model
```

## 3. Hard rules (machine-checked by `scripts/validate.py`)

1. File is `<skill-dir>/SKILL.md`; **`name` must equal the directory name exactly**.
2. `name` matches `^[a-z0-9]+(-[a-z0-9]+)*$`, 1–64 chars, no leading/trailing hyphen, no `--`.
3. `description` is 1–1024 chars and non-empty.
4. Frontmatter starts at byte 0 (`---`), closes with `\n---\n`, parses as a YAML mapping.
5. Body after frontmatter is non-empty.
6. **Portable frontmatter only**: `name`, `description`, `license`, `compatibility`,
   `metadata`. Extra top-level keys are validator errors.
7. `SKILL.md` ≤ 500 lines and ≤ 20,000 chars. Over that, move detail to `references/`.
8. No raw emoji anywhere in `SKILL.md`. The validator's emoji range includes
   arrows (`U+2190–U+21FF`) and `U+2B00–U+2BFF`, so write `->` and `-`, never a
   glyph arrow.
9. Every `references/…` and `templates/…` link in `SKILL.md` resolves to a file
   that exists in the skill directory.
10. Every skill name in `metadata.related-skills` resolves **either** to a skill
    in this repo **or** to a name in `catalog/known-skills.txt`. The second
    option is how a skill cross-references the user's wider installed corpus.
11. Quote any `description` containing a colon followed by a space — unquoted
    `key: value: value` is a YAML error.

## 4. Frontmatter template

```yaml
---
name: <skill-name>
description: "When the user wants <outcome>. Use when they mention <trigger>, <trigger>, <trigger>. For <adjacent task>, see <sibling-skill>."
license: MIT
metadata:
  version: 1.0.0
  suite: business-development   # or business-to-app
  related-skills: [sibling-a, sibling-b]
  triggers: [short, keyword, list]
---
```

### Writing the `description` (this is the whole trigger burden)

At startup only `name` + `description` load. Runtimes render the skill index
truncated to about **57 characters**, so the opening clause must carry the core
trigger on its own. Rules:

- Start with `When the user wants …` (an outcome, not a feature).
- Name the concrete triggers a user would actually type ("MEDDPICC", "battlecard",
  "cold email", "churn", "forecast", "PRD", "threat model").
- End with the boundary: `For <adjacent>, see <sibling>.` This is how the agent
  picks between near-miss skills.
- Keep under 1024 chars; aim for 200–400.

## 5. Required body structure

Every `SKILL.md` follows this skeleton. Sections may be added between them, but
these always appear, in this order:

```
# <Title>

<One-two sentence role statement: the concrete outcome this skill produces.>

## Before Starting
Check `.agents/bd-context.md` first … gather only what it does not already answer.

## When to Use
- bullet triggers
- **Don't use for:** counter-triggers that route to a sibling skill.

## <Workflow sections>
Phased, numbered. Decision rules ("if X, do Y"). Tables for reference data.

## Output
The concrete artifact, with a template in a fenced block (or templates/<file>).

## Common Pitfalls
1. Numbered mistake -> fix.

## Verification Checklist
- [ ] Checkbox items.
```

Add `## References` last only when `references/*.md` files exist.

## 6. The linking rules (what makes this suite different)

These are as important as the format rules.

1. **Own the WHY and the WHAT only.** A skill decides *what* is worth building and
   *why*. It never teaches engineering, design, security or growth craft.
2. **Link, never restate.** When a skill needs a "how", name the corpus skill
   that implements it. `skills/venture-skills-root/references/corpus-map.md`
   records the handoff points.
3. **State the boundary.** Every skill's description ends with what it does not
   cover and which sibling owns it.
4. **No duplicate triggers.** Before adding a skill, check whether the corpus
   already covers it. Two skills competing for one trigger make agents worse.
   `tests/registry.test.mjs` enforces this for curated imports.
5. **Artifacts are files.** A stage produces a file under `.agents/`, not a
   paragraph in chat.

## 7. Style guide

- **Second person, active voice.** "Score every candidate against the ICP checklist."
- **Defaults, not menus.** Recommend ONE approach and say why. Do not hand the
  agent a buffet.
- **Procedures over declarations.** "Run X, check Y, if Z do W" beats "handle this well".
- **Evidence discipline.** Never assert a market, competitor or deal fact without a
  source. Label anything inferred as `[ASSUMPTION]` and state what would falsify it.
  **Never fabricate** a statistic, benchmark, quote, price, payment rail or
  credential. This is the single most important rule here.
- **Portable.** No company-specific pricing, geography, bank details or compliance
  specifics in a skill body. Those belong in the per-engagement `.agents/bd-context.md`.
- **No filler.** No "Great question", no restating the title, no explaining what a
  proposal is. Every paragraph must justify its token cost.
- **Formatting.** H2 for sections, H3 for subsections. Bold key terms. Tables for
  reference data. Fenced blocks for templates and commands. No emoji.

## 8. Progressive disclosure

`SKILL.md` is the router + core workflow. Push depth into `references/`:

- `references/<topic>.md` — one topic per file, linked from `SKILL.md`.
- `templates/<name>.md` — a reusable artifact the skill fills in.
- `scripts/<name>.py` — self-contained; document dependencies in a docstring.

Keep links one level deep. A skill with no `references/` is fine if the body is
genuinely complete.

## 9. The suite (names are fixed — siblings cross-reference by these)

**business-development** (commercial chain)

| Skill | Produces |
|-------|----------|
| `venture-skills-root` | route to the right stage; the WHY/HOW boundary |
| `bd-context` | `.agents/bd-context.md` — the shared foundation doc |
| `market-segmentation` | ICP, TAM/SAM/SOM, segment priority, framework analysis |
| `competitive-intelligence` | competitor teardown, battlecards |
| `value-proposition-and-pricing` | messaging, ROI business case, packaging/pricing |
| `prospect-research` | verified target account + contact list |
| `outbound-sequencing` | multi-touch cadence, copy, deliverability setup |
| `discovery-call` | call plan, question bank, MEDDPICC capture, follow-up |
| `objection-handling` | objection library, negotiation plan |
| `proposal-and-quote` | proposal / SOW / quote |
| `account-planning` | key-account plan, whitespace, expansion path |
| `pipeline-forecast` | stage-gate model, CRM hygiene, forecast, funnel analytics |
| `qbr-and-renewal` | QBR deck, renewal plan, churn-risk play |
| `win-loss-review` | post-decision debrief, pattern analysis |

**business-to-app** (the bridge)

| Skill | Produces |
|-------|----------|
| `product-discovery` | evidence-backed opportunity brief, go/no-go |
| `business-need-to-prd` | PRD with a non-negotiable KPI table |
| `prd-to-system-design` | design doc, ADRs, NFRs, build-vs-buy |
| `security-by-design` | threat model, control checklist, security acceptance criteria |
| `feature-traceability` | the living requirement-to-business-to-test matrix |
| `sop-to-automation` | process map, automate/assist/keep-human classification |
| `launch-readiness` | go/no-go gate, staged rollout, post-launch measurement |

## 10. Curated third-party sources

Curated skills live in `registry/sources.json` and are **never** vendored into
this repository. `scripts/install-external.py` shallow-clones each source,
selects only the named skills, and installs them alongside our own.

Rules:

- Record the real upstream `license`. Check it; do not assume MIT.
- Record `why` — what this source adds that we do not.
- **Exclude the overlap.** If a source has a skill this repo already authors,
  exclude it. Routing ambiguity is a defect, not a trade-off.
- Regenerate attribution after any change: `npm run credits`. `CREDITS.md` and
  `registry/installed.json` are generated; hand-editing them fails CI.

## 11. Workflow for adding or changing a skill

1. Read 2 peer skills in `skills/` to match tone and structure.
2. Draft with `write_file` into `skills/<name>/SKILL.md` (+ `references/` if needed).
3. `python3 scripts/validate.py` — must pass.
4. `npm test` — must be 0 failures.
5. Bump `metadata.version`; add a `CHANGELOG.md` entry for a shipped change, and
   update the table in `VERSIONS.md` if skills were added or removed.
6. `python3 scripts/deploy.py` to install into the four runtimes.
7. `node bin/venture-skills.mjs doctor` to prove every runtime sees every skill.
8. `git add -A && git commit` on the working branch.

If you touched the corpus or the registry, also run `npm run catalog` (or
`python3 scripts/gen-known-skills.py`) and `npm run credits`.

## 12. Versioning

- **Per-skill**: `metadata.version` in `SKILL.md`, semantic (minor = new
  capability or trigger; patch = fixes and clarifications).
- **Suite**: `package.json` version, with the scheme and per-skill table in
  `VERSIONS.md` and the changelog in `CHANGELOG.md`.

## 13. Reporting a problem with attribution

If you are the author of a curated source and want your credit changed or your
work removed, open an issue. Attribution requests are handled first.
