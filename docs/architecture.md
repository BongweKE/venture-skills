# Architecture

How venture-skills is put together, and why.

## One source of truth, four runtimes

Hermes, OpenCode, Antigravity CLI and Mistral Vibe all read the same open
`SKILL.md` format, but from different directories. Rather than maintaining four
copies, `skills/` is the only place a skill is edited, and deployment fans it out:

```
                    skills/<name>/SKILL.md
                             |
        +--------------------+--------------------+
        |            |               |            |
     hermes      opencode      antigravity      vibe
     (copy)       (copy)         (copy)       (symlink)
```

- Hermes groups skills into category directories, so each skill lands under a
  directory named after its `metadata.suite`.
- Antigravity needs a `plugin.json` and an entry in `import_manifest.json`;
  `scripts/deploy.py` writes both, idempotently.
- Vibe gets symlinks, so edits in the repository are live without re-deploying.
- Every target receives a `.venture-skills-manifest.json` recording the source
  path and a sha256 per deployed file, so `deploy.py --check` can prove a
  deployed copy still matches the source it came from.

Editing a deployed copy is always a mistake. `--check` exists to catch it.

## Why skills are content, not code

A skill is a markdown document with YAML frontmatter. The only executable parts of
this repository are the tooling around them. That keeps the product reviewable by
non-engineers, diffable, and portable across any runtime that adopts the format.

The frontmatter is restricted to `name`, `description`, `license` and `metadata`.
Anything else would be runtime-specific and would break portability.

## The registry and the attribution model

Curated third-party skills live in `registry/sources.json`, not in `skills/`.

We do not vendor other people's work. `scripts/install-external.py` shallow-clones
each source, selects only the named skills, validates them, and installs them
alongside our own. `vendor/` is gitignored.

Attribution is generated, never hand-written: `scripts/gen-credits.mjs` renders
`CREDITS.md` and `registry/installed.json` from the registry. A test fails the
build if the committed files are stale, because a hand-maintained credits file
drifts the moment a source is added.

Every curated source records its real upstream licence. The MIT in this
repository's LICENSE covers `skills/`, `bin/`, `scripts/` and `tests/` only, and
the LICENSE says so explicitly.

### Curation rule: exclude the overlap

When a curated source contains a skill that this repository already authors, it is
excluded. Two skills competing for the same trigger degrade routing, because the
agent has to choose between near-duplicates. `tests/registry.test.mjs` fails if a
curated name collides with an authored one, or if two sources offer the same name.

## The two checkers

Skill format is enforced twice, in two languages:

- `scripts/validate.py` (PyYAML) is the authoring gate, and the one contributors
  run and CI blocks on.
- `tests/skills.test.mjs` (Node) re-implements the same rules.

That redundancy is deliberate. A skill file is the product of this repository; if
the two checkers disagree, one has a bug, and we want to know before a runtime
silently refuses to load a skill. The Node checker has already caught one real
defect the Python one missed: flow-style YAML sequences
(`related-skills: [a, b]`) parsed as strings by a scalar-only reader.

## Verification commands

```bash
python3 scripts/validate.py       # authoring spec
npm test                          # format, CLI, registry contracts
python3 scripts/deploy.py --check # runtime drift
node scripts/gen-credits.mjs --check   # attribution freshness
python3 scripts/gen-known-skills.py --check   # catalog freshness
node bin/venture-skills.mjs doctor     # can each runtime see every skill
```
