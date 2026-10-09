#!/usr/bin/env python3
"""Deploy the business-development skill suite into four agent runtimes.

One source of truth (`skills/` in this repo) is installed into every runtime that
should see it, so the skills are identical everywhere and drift is detectable.

Targets
  hermes       ~/.hermes/skills/business-development/<name>/        copy
  opencode     ~/.config/opencode/skills/<name>/                   copy
  antigravity  ~/.gemini/antigravity-cli/plugins/bd-skills/skills/ copy (+ plugin.json + manifest entry)
  vibe         ~/.vibe/skills/<name>  ->  ./skills/<name>          symlink

Usage
  python3 deploy.py              # install / update all targets
  python3 deploy.py --check      # read-only: report drift, exit 1 if any
  python3 deploy.py --dry-run    # show what would change
  python3 deploy.py --target hermes opencode

Each target gets a `.bd-skills-manifest.json` recording the source path and
sha256 of every deployed file, so `--check` can prove a deployed copy still
matches the source it came from (supply-chain / update-drift hygiene).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
SRC = REPO / "skills"
MANIFEST = ".bd-skills-manifest.json"

HOME = Path.home()
TARGETS = {
    "hermes": {"path": HOME / ".hermes/skills/business-development", "mode": "copy"},
    "opencode": {"path": HOME / ".config/opencode/skills", "mode": "copy"},
    "antigravity": {
        "path": HOME / ".gemini/antigravity-cli/plugins/bd-skills/skills",
        "mode": "copy",
        "plugin_dir": HOME / ".gemini/antigravity-cli/plugins/bd-skills",
    },
    "vibe": {"path": HOME / ".vibe/skills", "mode": "symlink"},
}

PLUGIN_JSON = {
    "$schema": "https://antigravity.google/schemas/v1/plugin.json",
    "name": "bd-skills",
    "description": "Business-development agent store: 13 sales & commercial skills.",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def dir_files(d: Path) -> dict[str, str]:
    """Relative-path -> sha256 for every file under d."""
    out: dict[str, str] = {}
    for p in sorted(d.rglob("*")):
        if p.is_file():
            out[str(p.relative_to(d))] = sha256(p)
    return out


def source_skills() -> list[Path]:
    return sorted(d for d in SRC.iterdir() if d.is_dir() and (d / "SKILL.md").is_file())


def deploy_copy(skill: Path, dest_root: Path, dry: bool) -> str:
    dest = dest_root / skill.name
    if dry:
        return "update" if dest.exists() else "new"
    if dest.is_symlink() or dest.is_file():
        dest.unlink()
    elif dest.is_dir():
        shutil.rmtree(dest)
    shutil.copytree(skill, dest)
    return "ok"


def deploy_symlink(skill: Path, dest_root: Path, dry: bool) -> str:
    dest = dest_root / skill.name
    if dest.is_symlink() and dest.resolve() == skill.resolve():
        return "ok"
    if dry:
        return "update" if dest.exists() or dest.is_symlink() else "new"
    if dest.is_symlink() or dest.is_file():
        dest.unlink()
    elif dest.is_dir():
        shutil.rmtree(dest)
    os.symlink(skill.resolve(), dest)
    return "ok"


def write_manifest(dest_root: Path, dry: bool) -> None:
    skills = source_skills()
    data = {
        "source": str(SRC),
        "suite": "business-development",
        "synced": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "skill_count": len(skills),
        "skills": {s.name: {"skill_md_sha256": sha256(s / "SKILL.md")} for s in skills},
    }
    if dry:
        return
    dest_root.mkdir(parents=True, exist_ok=True)
    (dest_root / MANIFEST).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def ensure_antigravity_plugin(dry: bool) -> None:
    pd = TARGETS["antigravity"].get("plugin_dir")
    if not pd:
        return
    pj = pd / "plugin.json"
    if pj.is_file():
        return
    if dry:
        print(f"  would write {pj}")
        return
    pd.mkdir(parents=True, exist_ok=True)
    pj.write_text(json.dumps(PLUGIN_JSON, indent=2) + "\n", encoding="utf-8")
    print(f"  wrote {pj}")

    # Register the plugin in Antigravity's import manifest if present.
    manifest = pd.parent / "import_manifest.json"
    if not manifest.is_file():
        return
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return
    imports = data.setdefault("imports", [])
    if any(i.get("name") == "bd-skills" for i in imports):
        return
    imports.append({
        "name": "bd-skills",
        "source": "local-install",
        "importedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "components": ["installed"],
    })
    manifest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"  registered bd-skills in {manifest}")


def do_deploy(names: list[str], dry: bool) -> int:
    skills = source_skills()
    if not skills:
        print("no skills found — run validate.py first", file=sys.stderr)
        return 1
    print(f"deploying {len(skills)} skills to: {', '.join(names)}"
          + ("  [dry-run]" if dry else ""))
    for tname in names:
        t = TARGETS[tname]
        root: Path = t["path"]
        print(f"\n[{tname}] {root}  ({t['mode']})")
        counts: dict[str, int] = {}
        for s in skills:
            try:
                status = (deploy_copy if t["mode"] == "copy" else deploy_symlink)(s, root, dry)
            except OSError as e:
                print(f"  ! {s.name}: {e}")
                counts["error"] = counts.get("error", 0) + 1
                continue
            counts[status] = counts.get(status, 0) + 1
        write_manifest(root, dry)
        print(f"  {counts}")
        if tname == "antigravity":
            ensure_antigravity_plugin(dry)
    return 0


def do_check(names: list[str]) -> int:
    skills = source_skills()
    problems = 0
    for tname in names:
        t = TARGETS[tname]
        root: Path = t["path"]
        print(f"\n[{tname}] {root}")
        if not root.is_dir():
            print("  ! target directory missing")
            problems += 1
            continue
        for s in skills:
            dest = root / s.name
            if not (dest.exists() or dest.is_symlink()):
                print(f"  ! missing: {s.name}")
                problems += 1
                continue
            if dest.is_symlink():
                if dest.resolve() != s.resolve():
                    print(f"  ! wrong symlink target: {s.name} -> {dest.resolve()}")
                    problems += 1
                continue
            src_files = dir_files(s)
            dst_files = dir_files(dest) if dest.is_dir() else {}
            if src_files != dst_files:
                diff = sorted(set(src_files) ^ set(dst_files)) or [
                    f for f in src_files if src_files[f] != dst_files.get(f)
                ]
                print(f"  ! drifted: {s.name} ({', '.join(diff)})")
                problems += 1
        if problems == 0:
            print("  all skills in sync")
    if problems:
        print(f"\n{problems} drift issue(s) — run `python3 deploy.py` to fix")
        return 1
    print("\nall targets in sync")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="read-only drift report")
    ap.add_argument("--dry-run", action="store_true", help="show what would change")
    ap.add_argument("--target", nargs="+", choices=sorted(TARGETS), default=sorted(TARGETS))
    args = ap.parse_args()
    if not SRC.is_dir():
        sys.exit(f"missing {SRC}")
    return do_check(args.target) if args.check else do_deploy(args.target, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
