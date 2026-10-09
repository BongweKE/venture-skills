#!/usr/bin/env python3
"""Deploy the venture-skills suite into four agent runtimes.

One source of truth (`skills/` in this repo) is installed into every runtime that
should see it, so the skills are identical everywhere and drift is detectable.

Targets
  hermes       ~/.hermes/skills/<suite>/<name>/           copy (categorised by metadata.suite)
  opencode     ~/.config/opencode/skills/<name>/          copy
  antigravity  ~/.gemini/antigravity-cli/plugins/venture-skills/skills/<name>/
                                                          copy (+ plugin.json + manifest entry)
  vibe         ~/.vibe/skills/<name>  ->  ./skills/<name> symlink

Hermes groups skills into category directories, so each skill is placed under a
directory named after its `metadata.suite` (business-development, business-to-app).

Usage
  python3 deploy.py              # install / update all targets
  python3 deploy.py --check      # read-only: report drift, exit 1 if any
  python3 deploy.py --dry-run    # show what would change
  python3 deploy.py --target hermes opencode

Each target gets a `.venture-skills-manifest.json` recording the source path and
sha256 of every deployed file, so `--check` can prove a deployed copy still
matches the source it came from (supply-chain / update-drift hygiene).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "skills"
MANIFEST = ".venture-skills-manifest.json"

HOME = Path.home()
PLUGIN_NAME = "venture-skills"
TARGETS: dict[str, dict] = {
    "hermes": {"path": HOME / ".hermes/skills", "mode": "copy", "categorize": True},
    "opencode": {"path": HOME / ".config/opencode/skills", "mode": "copy"},
    "antigravity": {
        "path": HOME / f".gemini/antigravity-cli/plugins/{PLUGIN_NAME}/skills",
        "mode": "copy",
        "plugin_dir": HOME / f".gemini/antigravity-cli/plugins/{PLUGIN_NAME}",
    },
    "vibe": {"path": HOME / ".vibe/skills", "mode": "symlink"},
}

PLUGIN_JSON = {
    "$schema": "https://antigravity.google/schemas/v1/plugin.json",
    "name": PLUGIN_NAME,
    "description": "Business-development and business-to-app skills: 20 sales, product and engineering-bridge skills.",
}

# Layouts from earlier iterations that must not linger and shadow the current one.
LEGACY_PLUGIN_DIRS = [
    HOME / ".gemini/antigravity-cli/plugins/bd-skills",
    HOME / ".gemini/config/plugins/bd-skills",
]
LEGACY_MANIFEST = ".bd-skills-manifest.json"


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


def suite_of(skill: Path) -> str:
    """Read metadata.suite without a YAML dependency (our frontmatter is simple)."""
    try:
        text = (skill / "SKILL.md").read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "uncategorized"
    m = re.search(r"^\s{2,}suite:\s*([A-Za-z0-9._-]+)\s*$", text, re.M)
    return m.group(1) if m else "uncategorized"


def dest_root_for(target: dict, skill: Path) -> Path:
    """Where this skill's directory belongs for this target."""
    root: Path = target["path"]
    return root / suite_of(skill) if target.get("categorize") else root


def deploy_copy(skill: Path, dest_root: Path, dry: bool) -> str:
    dest = dest_root / skill.name
    if dry:
        return "update" if dest.exists() else "new"
    dest_root.mkdir(parents=True, exist_ok=True)
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
    dest_root.mkdir(parents=True, exist_ok=True)
    if dest.is_symlink() or dest.is_file():
        dest.unlink()
    elif dest.is_dir():
        shutil.rmtree(dest)
    os.symlink(skill.resolve(), dest)
    return "ok"


def migrate_legacy() -> None:
    """Remove plugin dirs, manifests and manifest entries from earlier layouts."""
    current_plugin = TARGETS["antigravity"].get("plugin_dir")
    for d in LEGACY_PLUGIN_DIRS:
        if d.exists() and d != current_plugin:
            shutil.rmtree(d, ignore_errors=True)
            print(f"  removed legacy plugin dir {d}")
    for target in TARGETS.values():
        stale = Path(target["path"]) / LEGACY_MANIFEST
        if stale.is_file():
            stale.unlink()
            print(f"  removed legacy manifest {stale}")
    im = HOME / ".gemini/antigravity-cli/import_manifest.json"
    if im.is_file():
        try:
            data = json.loads(im.read_text(encoding="utf-8"))
            before = len(data.get("imports", []))
            data["imports"] = [i for i in data.get("imports", []) if i.get("name") != "bd-skills"]
            if len(data["imports"]) != before:
                im.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
                print(f"  dropped bd-skills entry from {im}")
        except (OSError, json.JSONDecodeError):
            pass


def write_manifest(dry: bool) -> None:
    skills = source_skills()
    data = {
        "source": str(SRC),
        "suite": "venture-skills",
        "synced": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "skill_count": len(skills),
        "skills": {
            s.name: {"suite": suite_of(s), "skill_md_sha256": sha256(s / "SKILL.md")}
            for s in skills
        },
    }
    if dry:
        return
    for target in TARGETS.values():
        root = Path(target["path"])
        if not root.is_dir():
            continue
        try:
            (root / MANIFEST).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        except OSError:
            pass


def ensure_antigravity_plugin(dry: bool) -> None:
    pd = TARGETS["antigravity"].get("plugin_dir")
    if not pd:
        return
    pj = pd / "plugin.json"
    if not pj.is_file():
        if dry:
            print(f"  would write {pj}")
        else:
            pd.mkdir(parents=True, exist_ok=True)
            pj.write_text(json.dumps(PLUGIN_JSON, indent=2) + "\n", encoding="utf-8")
            print(f"  wrote {pj}")

    # The manifest lives at the antigravity-cli root, i.e. two levels above the
    # plugin dir (.../antigravity-cli/import_manifest.json).
    manifest = pd.parent.parent / "import_manifest.json"
    if not manifest.is_file():
        print(f"  ! no import_manifest.json at {manifest} — plugin not registered")
        return
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        print(f"  ! unreadable import_manifest.json at {manifest} — plugin not registered")
        return
    imports = data.setdefault("imports", [])
    if any(i.get("name") == PLUGIN_NAME for i in imports):
        return
    if dry:
        print(f"  would register {PLUGIN_NAME} in {manifest}")
        return
    imports.append({
        "name": PLUGIN_NAME,
        "source": "local-install",
        "importedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "components": ["installed"],
    })
    manifest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"  registered {PLUGIN_NAME} in {manifest}")


def do_deploy(names: list[str], dry: bool) -> int:
    skills = source_skills()
    if not skills:
        print("no skills found — run validate.py first", file=sys.stderr)
        return 1
    print(f"deploying {len(skills)} skills to: {', '.join(names)}"
          + ("  [dry-run]" if dry else ""))
    if not dry:
        migrate_legacy()
    for tname in names:
        t = TARGETS[tname]
        print(f"\n[{tname}] {t['path']}  ({t['mode']})")
        counts: dict[str, int] = {}
        for s in skills:
            root = dest_root_for(t, s)
            try:
                status = (deploy_copy if t["mode"] == "copy" else deploy_symlink)(s, root, dry)
            except OSError as e:
                print(f"  ! {s.name}: {e}")
                counts["error"] = counts.get("error", 0) + 1
                continue
            counts[status] = counts.get(status, 0) + 1
        print(f"  {counts}")
        if tname == "antigravity":
            ensure_antigravity_plugin(dry)
    write_manifest(dry)
    return 0


def do_check(names: list[str]) -> int:
    skills = source_skills()
    problems = 0
    for tname in names:
        t = TARGETS[tname]
        print(f"\n[{tname}] {t['path']}")
        if not Path(t["path"]).is_dir():
            print("  ! target directory missing")
            problems += 1
            continue
        local = 0
        for s in skills:
            dest = dest_root_for(t, s) / s.name
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
            else:
                local += 1
        if local == len(skills):
            print(f"  all {local} skills in sync")
    if problems:
        print(f"\n{problems} drift issue(s) — run `python3 deploy.py` to fix")
        return 1
    print("\nall targets in sync")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="read-only drift report")
    ap.add_argument("--dry-run", action="store_true", help="show what would change")
    ap.add_argument("--target", nargs="+", choices=sorted(TARGETS), default=sorted(TARGETS))
    args = ap.parse_args()
    if not SRC.is_dir():
        sys.exit(f"missing {SRC}")
    return do_check(args.target) if args.check else do_deploy(args.target, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
