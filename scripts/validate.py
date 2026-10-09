#!/usr/bin/env python3
"""Validate every skill in skills/ against the Agent Skills spec + repo rules.

Enforces the hard rules in AGENTS.md section 3. Exit 0 = all pass, 1 = failures.

Usage:
  python3 scripts/validate.py            # validate all skills
  python3 scripts/validate.py <name>...  # validate only the named skills
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML required: python3 -m pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
CATALOG = ROOT / "catalog"
# Committed allowlist of public skill names this repo cross-references.
KNOWN_PUBLIC = CATALOG / "known-skills.public.txt"
# Generated snapshot of this machine's full corpus. Gitignored: it reveals the
# author's private projects, so it is never published.
KNOWN_LOCAL = CATALOG / "known-skills.local.txt"


def _load_known_external() -> set[str]:
    """Cross-link targets: public allowlist merged with the local snapshot.

    The public file is always present, so a fresh clone and CI validate the same
    way. The local file is merged when it exists, which is what lets a developer
    machine cross-reference every skill it actually has installed.
    """
    out: set[str] = set()
    for path in (KNOWN_PUBLIC, KNOWN_LOCAL):
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                out.add(line)
    return out


KNOWN_EXTERNAL = _load_known_external()

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PORTABLE_FIELDS = {"name", "description", "license", "compatibility", "metadata"}
MAX_NAME = 64
MAX_DESC = 1024
MAX_BODY = 20_000
MAX_LINES = 500
# Common emoji blocks — crude but catches the raw-emoji rule.
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F0FF"
    "\U00002190-\U000021FF\U00002B00-\U00002BFF\U0000FE0F]"
)
LINK_RE = re.compile(r"\((references/[^)]+)\)")


def fail(errors: list[str], skill: str, msg: str) -> None:
    errors.append(f"{skill}: {msg}")


def validate_skill(skill_dir: Path, all_names: set[str], errors: list[str]) -> None:
    name = skill_dir.name
    f = skill_dir / "SKILL.md"
    if not f.is_file():
        return fail(errors, name, "missing SKILL.md")

    raw = f.read_text(encoding="utf-8")

    # 4. frontmatter at byte 0, closes properly
    if not raw.startswith("---"):
        return fail(errors, name, "frontmatter does not start at byte 0")
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return fail(errors, name, "frontmatter not closed with ---")
    fm_text, body = parts[1], parts[2]
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        return fail(errors, name, f"frontmatter YAML error: {e}")
    if not isinstance(fm, dict):
        return fail(errors, name, "frontmatter is not a YAML mapping")

    # 1. name present + matches directory
    if "name" not in fm:
        return fail(errors, name, "missing required field: name")
    if fm["name"] != name:
        fail(errors, name, f"name '{fm['name']}' != directory '{name}'")

    # 2. name format
    if not isinstance(fm["name"], str) or not NAME_RE.match(fm["name"]):
        fail(errors, name, "name violates ^[a-z0-9]+(-[a-z0-9]+)*$")
    if len(str(fm.get("name", ""))) > MAX_NAME:
        fail(errors, name, f"name > {MAX_NAME} chars")

    # 3. description
    desc = fm.get("description")
    if not isinstance(desc, str) or not desc.strip():
        fail(errors, name, "missing or empty description")
    elif len(desc) > MAX_DESC:
        fail(errors, name, f"description {len(desc)} chars > {MAX_DESC}")

    # 5. non-empty body
    if not body.strip():
        fail(errors, name, "empty body after frontmatter")

    # 6. portable fields only
    extra = set(fm) - PORTABLE_FIELDS
    if extra:
        fail(errors, name, f"non-portable frontmatter fields: {sorted(extra)}")

    # 7. size limits
    if len(raw) > MAX_BODY:
        fail(errors, name, f"SKILL.md {len(raw)} chars > {MAX_BODY}")
    if raw.count("\n") + 1 > MAX_LINES:
        fail(errors, name, f"SKILL.md > {MAX_LINES} lines")

    # 8. no raw emoji
    m = EMOJI_RE.search(raw)
    if m:
        fail(errors, name, f"raw emoji found: {m.group()!r}")

    # 9. references links resolve
    for rel in LINK_RE.findall(raw):
        if not (skill_dir / rel).is_file():
            fail(errors, name, f"broken reference link: {rel}")

    # 10. related-skills resolve in-repo or against the installed-corpus registry
    meta = fm.get("metadata") or {}
    related = meta.get("related-skills") or []
    if isinstance(related, str):
        related = [related]
    for r in related:
        if r not in all_names and r not in KNOWN_EXTERNAL:
            fail(errors, name, f"related-skill unresolved (not in repo or cross-link registry): {r}")

    # structure sanity (warnings, not hard failures)
    for req in ("## Before Starting", "## When to Use", "## Common Pitfalls"):
        if req not in raw:
            fail(errors, name, f"missing required section: {req}")


def main() -> int:
    if not SKILLS.is_dir():
        sys.exit(f"no skills/ dir at {SKILLS}")
    dirs = sorted(d for d in SKILLS.iterdir() if d.is_dir())
    wanted = set(sys.argv[1:])
    if wanted:
        dirs = [d for d in dirs if d.name in wanted]
        missing = wanted - {d.name for d in dirs}
        if missing:
            sys.exit(f"unknown skill(s): {sorted(missing)}")

    all_names = {d.name for d in SKILLS.iterdir() if d.is_dir()}
    errors: list[str] = []
    for d in dirs:
        validate_skill(d, all_names, errors)

    print(f"validated {len(dirs)} skill(s)")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors:
            print(f"  ! {e}")
        return 1
    print("all skills pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
