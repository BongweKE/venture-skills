# AGENTS.md — business-development skills: authoring specification

Guidelines for humans and AI agents working in this repository.

## 1. What this repo is

Portable **Agent Skills** for business development, sales, and commercial
operations, written to the [Agent Skills specification](https://agentskills.io)
(agentskills.io → `skill-name/SKILL.md`). One source of truth, deployed to four
agent runtimes:

| Runtime | Discovery path | Deploy mode |
|---------|----------------|-------------|
| Hermes Agent | `~/.hermes/skills/business-development/<name>/` | copy |
| OpenCode | `~/.config/opencode/skills/<name>/` | copy |
| Antigravity CLI | `~/.gemini/antigravity-cli/plugins/bd-skills/skills/<name>/` | copy |
| Mistral Vibe | `~/.vibe/skills/<name>/` | symlink |

Run `python3 deploy.py` to install; `python3 deploy.py --check` to detect drift.
Never hand-edit a deployed copy — edit `skills/` here and re-deploy.

## 2. Repository layout

```
bd-skills/
├── AGENTS.md                 # this spec
├── README.md                 # human-facing overview
├── VERSIONS.md               # suite changelog
├── skills/                   # Agent Skills (open standard) — the source of truth
│   └── <skill-name>/
│       ├── SKILL.md          # required
│       ├── references/       # optional — detail loaded on demand
│       ├── templates/        # optional — reusable output artifacts
│       └── scripts/          # optional — executable helpers
├── scripts/validate.py       # open-standard validator (run before every deploy)
└── deploy.py                 # installs skills/ into the four runtimes
```

## 3. Hard rules (machine-checked by `scripts/validate.py`)

1. File is `<skill-dir>/SKILL.md`; **`name` must equal the directory name exactly**.
2. `name` matches `^[a-z0-9]+(-[a-z0-9]+)*$`, 1–64 chars, no leading/trailing hyphen, no `--`.
3. `description` is 1–1024 chars and non-empty.
4. Frontmatter starts at byte 0 (`---`), closes with `\n---\n`, parses as a YAML mapping.
5. Body after frontmatter is non-empty.
6. **Portable frontmatter only**: `name`, `description`, `license`, `compatibility`,
   `metadata`. Hermes tolerates more fields, but the portable core is the intersection
   every runtime reads — extra top-level keys are validator errors.
7. `SKILL.md` ≤ 500 lines and ≤ 20,000 chars. Over that, move detail to `references/`.
8. No raw emoji anywhere in `SKILL.md` (renders inconsistently across runtimes).
9. Every `references/…` link in `SKILL.md` resolves to a file that exists.
10. Every skill name in `metadata.related-skills` exists in this repo.

## 4. Frontmatter template

```yaml
---
name: <skill-name>
description: "When the user wants <outcome>. Use when they mention <trigger>, <trigger>, <trigger>. For <adjacent task>, see <sibling-skill>."
license: MIT
metadata:
  version: 1.0.0
  author: BongweKE
  suite: business-development
  related-skills: [sibling-a, sibling-b]
  triggers: [short, keyword, list]
---
```

### Writing the `description` (this is the whole trigger burden)

At startup only `name` + `description` load. Hermes renders the skill index
truncated to **57 characters**, so the opening clause must carry the core trigger
on its own. Rules:

- Start with `When the user wants …` (an outcome, not a feature).
- Name the concrete triggers a user would actually type ("MEDDPICC", "battlecard",
  "cold email", "churn", "forecast").
- End with the boundary: `For <adjacent>, see <sibling>.` This is how the agent
  picks between near-miss skills.
- Keep under 1024 chars; aim for 200–400.

## 5. Required body structure

Every `SKILL.md` follows this skeleton. Sections may be added between them, but
these eight always appear, in this order:

```
# <Title>

<One-two sentence role statement: "You are an expert at …" + the concrete
outcome this skill produces.>

## Before Starting
Check `.agents/bd-context.md` first … only gather what it does not already answer.

## When to Use
- bullet triggers
- **Don't use for:** counter-triggers that route to a sibling skill.

## <Workflow sections>
Phased, numbered. Decision rules ("if X, do Y"). Tables for reference data.

## Output
The concrete artifact, with a template in a fenced block (or templates/<file>).

## Common Pitfalls
1. Numbered mistake → fix.

## Verification Checklist
- [ ] Checkbox items.
```

Add `## References` last **only** when `references/*.md` files exist.

## 6. Style guide

- **Second person, active voice.** "Score every candidate against the ICP checklist."
- **Defaults, not menus.** When several approaches exist, recommend ONE and say why.
  Do not hand the agent a buffet.
- **Procedures over declarations.** "Run X, check Y, if Z do W" beats "handle this well".
- **Evidence discipline.** Never assert a market, competitor, or deal fact without a
  source. Label anything inferred as an assumption. Cite URLs inline.
- **No filler.** No "Great question", no restating the title, no explanation of what a
  proposal is. Every paragraph must justify its token cost: would the agent get this
  wrong without it? If no, cut it.
- **Formatting.** H2 for sections, H3 for subsections. Bold key terms. Tables for
  reference data. Fenced blocks for templates and commands. No emoji.
- **Length.** Short paragraphs (2–4 sentences). Bullets and numbered lists liberally.

## 7. Progressive disclosure

`SKILL.md` is the router + core workflow. Push depth into `references/`:

- `references/<topic>.md` — one topic per file, linked from `SKILL.md`.
- `templates/<name>.md` — a reusable artifact the skill fills in (battlecard,
  proposal, QBR deck outline).
- `scripts/<name>.py` — self-contained; document dependencies in a docstring.

Keep links one level deep. A skill with no `references/` is fine if the body is
genuinely complete.

## 8. The suite (names are fixed — siblings cross-reference by these)

| Skill | Produces | Reads context |
|-------|----------|---------------|
| `bd-context` | `.agents/bd-context.md` — the shared foundation doc | writes it |
| `market-segmentation` | ICP, TAM/SAM/SOM, segment priority, framework analysis | yes |
| `competitive-intelligence` | competitor teardown, battlecards | yes |
| `prospect-research` | verified target account + contact list | yes |
| `outbound-sequencing` | multi-touch cadence, copy, deliverability setup | yes |
| `discovery-call` | call plan, question bank, MEDDPICC capture, follow-up | yes |
| `value-proposition-and-pricing` | messaging, ROI business case, packaging/pricing | yes |
| `proposal-and-quote` | proposal / SOW / quote | yes |
| `objection-handling` | objection library, negotiation plan | yes |
| `pipeline-forecast` | stage-gate model, CRM hygiene, forecast, funnel analytics | yes |
| `account-planning` | key-account plan, whitespace, expansion path | yes |
| `qbr-and-renewal` | QBR deck, renewal plan, churn-risk play | yes |
| `win-loss-review` | post-decision debrief, pattern analysis | yes |

## 9. Workflow for adding or changing a skill

1. Read 2 peer skills in `skills/` to match tone and structure.
2. Draft with `write_file` into `skills/<name>/SKILL.md` (+ `references/` if needed).
3. `python3 scripts/validate.py` — must pass.
4. Bump `metadata.version` on any shipped change; update `VERSIONS.md`.
5. `python3 deploy.py` to install into the four runtimes.
6. `git add -A && git commit` on the working branch.

## 10. Versioning

- **Per-skill**: `metadata.version` in `SKILL.md`, semantic (minor = new capability or
  description triggers; patch = fixes and clarifications).
- **Suite**: `VERSIONS.md` headings carry an `x.y.z` shared number (x = restructure,
  y = new skill, z = update to an existing skill).
