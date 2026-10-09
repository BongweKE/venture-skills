# Notice on scope of the MIT licence

The MIT licence in [`LICENSE`](LICENSE) covers the material authored in this
repository:

- `skills/` — the 21 venture-skills skills
- `bin/` — the CLI
- `scripts/` — the tooling
- `tests/` — the test suite
- the documentation (`README.md`, `AGENTS.md`, `docs/`, `catalog/`)

It does **not** cover curated third-party skills.

Third-party skills listed in `registry/sources.json` remain the property of their
authors and stay under their own upstream licences. They are never vendored into
this repository: `scripts/install-external.py` fetches them from the upstream
repository at install time. Their licences and attribution are recorded in
[`CREDITS.md`](CREDITS.md) and `registry/installed.json`.

If you are the author of a curated source and want your credit changed, or want
your work removed from the registry, open an issue. Attribution requests are
handled first.
