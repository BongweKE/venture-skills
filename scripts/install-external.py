#!/usr/bin/env python3
"""Install curated EXTERNAL skills into the four agent runtimes.

External skills are third-party, separately licensed works. This script keeps
them out of `skills/` (which is this repo's own authored, MIT content) and
installs them straight into each runtime, recording provenance so a later audit
can tell exactly which upstream commit each file came from.

Pipeline per source (external/sources.json):
  1. shallow-clone the repo into vendor/<owner>-<repo> (idempotent; --update to pull)
  2. walk it for SKILL.md, select by include/exclude name patterns
  3. validate each against the Agent Skills spec (name == dir, description, body)
  4. copy into vendor/installed/<name>/ with a provenance block appended
  5. deploy to hermes / opencode / antigravity (copy) and vibe (symlink)

Name collisions with your existing corpus are detected and SKIPPED, never
silently overwritten (--force to override).

Usage
  python3 scripts/install-external.py --list          # show the curated set
  python3 scripts/install-external.py --dry-run
  python3 scripts/install-external.py                 # install enabled sources
  python3 scripts/install-external.py --update        # re-clone, then install
  python3 scripts/install-external.py --source wshobson/agents
  python3 scripts/install-external.py --check         # drift report
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VENDOR = REPO / "vendor"
INSTALLED = VENDOR / "installed"
SOURCES = REPO / "registry" / "sources.json"
MANIFEST = ".ext-skills-manifest.json"

HOME = Path.home()
TARGETS = {
    "hermes": (HOME / ".hermes/skills", "copy"),
    "opencode": (HOME / ".config/opencode/skills", "copy"),
    "antigravity": (HOME / ".gemini/antigravity-cli/plugins/ext-skills/skills", "copy"),
    "vibe": (HOME / ".vibe/skills", "symlink"),
}
AG_PLUGIN_DIR = HOME / ".gemini/antigravity-cli/plugins/ext-skills"
AG_PLUGIN_JSON = {
    "$schema": "https://antigravity.google/schemas/v1/plugin.json",
    "name": "ext-skills",
    "description": "Curated third-party skills installed by venture-skills/scripts/install-external.py.",
}


def sh(cmd: list[str], cwd: Path | None = None) -> tuple[int, str]:
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_sources() -> list[dict]:
    data = json.loads(SOURCES.read_text(encoding="utf-8"))
    return data.get("sources", [])


def parse_fm(path: Path) -> tuple[dict, str]:
    import yaml
    raw = path.read_text(encoding="utf-8", errors="replace")
    if not raw.startswith("---"):
        return {}, raw
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}, raw
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception:
        fm = {}
    return (fm if isinstance(fm, dict) else {}), parts[2]


def clone(repo: str, ref: str, update: bool) -> Path | None:
    dest = VENDOR / repo.replace("/", "-")
    if dest.is_dir() and (dest / ".git").is_dir():
        if update:
            rc, out = sh(["git", "-C", str(dest), "fetch", "--depth", "1", "origin", ref])
            if rc:  # noqa: E501
                print(f"  ! fetch failed for {repo}: {out[:200]}")
                return dest
            sh(["git", "-C", str(dest), "reset", "--hard", f"origin/{ref}"])
        return dest
    VENDOR.mkdir(parents=True, exist_ok=True)
    rc, out = sh(["git", "clone", "--depth", "1", "--branch", ref,
                  f"https://github.com/{repo}.git", str(dest)])
    if rc:
        print(f"  ! clone failed for {repo}: {out[:200]}")
        return None
    return dest


def repo_sha(dest: Path) -> str:
    rc, out = sh(["git", "-C", str(dest), "rev-parse", "HEAD"])
    return out.strip() if rc == 0 else "unknown"


def discover(root: Path) -> dict[str, Path]:
    """skill name -> directory, for every SKILL.md under root."""
    out: dict[str, Path] = {}
    for p in root.rglob("SKILL.md"):
        if ".git" in p.parts:
            continue
        out[p.parent.name] = p.parent
    return out


def select(skills: dict[str, Path], include: list[str], exclude: list[str]) -> dict[str, Path]:
    def match(name: str, pats: list[str]) -> bool:
        return any(fnmatch.fnmatch(name, p) for p in pats)
    out = {}
    for n, d in sorted(skills.items()):
        if include and not match(n, include):
            continue
        if exclude and match(n, exclude):
            continue
        out[n] = d
    return out


def stage(name: str, src: Path, repo: str, sha: str, synced: str) -> tuple[bool, str]:
    """Copy a selected skill into vendor/installed/<name> with provenance."""
    dst = INSTALLED / name
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    for p in src.rglob("*"):
        if p.is_dir() or ".git" in p.parts:
            continue
        rel = p.relative_to(src)
        tgt = dst / rel
        tgt.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, tgt)

    skill_md = dst / "SKILL.md"
    fm, body = parse_fm(skill_md)
    if not fm.get("name") or not fm.get("description"):
        shutil.rmtree(dst, ignore_errors=True)
        return False, "missing name/description in frontmatter"
    if fm.get("name") != name:
        shutil.rmtree(dst, ignore_errors=True)
        return False, f"name '{fm.get('name')}' != directory '{name}'"
    if not body.strip():
        shutil.rmtree(dst, ignore_errors=True)
        return False, "empty body"

    note = (f"\n\n---\n\n*Vendored from `{repo}` @ `{sha[:12]}` ({synced}). "
            f"External, separately licensed content — see that repository for terms. "
            f"Do not edit here; re-run scripts/install-external.py to update.*\n")
    skill_md.write_text(skill_md.read_text(encoding="utf-8").rstrip() + note, encoding="utf-8")
    return True, "ok"


def existing_names() -> set[str]:
    """Names already present in a runtime, EXCLUDING skills this tool installed.

    Without the subtraction, a second run would report every previously vendored
    skill as a collision and refuse to update it.
    """
    names = set()
    for root in (HOME / ".hermes/skills", HOME / ".config/opencode/skills",
                 HOME / ".vibe/skills", HOME / ".agents/skills",
                 HOME / ".gemini/antigravity-cli/plugins/ext-skills/skills"):
        if root.is_dir():
            for p in root.iterdir():
                if p.is_dir() or p.is_symlink():
                    names.add(p.name)

    ours: set[str] = set()
    for root, _ in TARGETS.values():
        mf = root / MANIFEST
        if mf.is_file():
            try:
                ours |= set((json.loads(mf.read_text(encoding="utf-8")) or {}).get("skills", {}))
            except (OSError, json.JSONDecodeError):
                pass
    if INSTALLED.is_dir():
        ours |= {p.name for p in INSTALLED.iterdir() if p.is_dir()}
    return names - ours


def deploy(installed: list[str], dry: bool) -> dict:
    counts: dict[str, int] = {}
    for tname, (root, mode) in TARGETS.items():
        if dry:
            continue
        root.mkdir(parents=True, exist_ok=True)
        for n in installed:
            src = INSTALLED / n
            dst = root / n
            if dst.is_symlink() or dst.is_file():
                dst.unlink()
            elif dst.is_dir():
                shutil.rmtree(dst)
            if mode == "symlink":
                os.symlink(src.resolve(), dst)
            else:
                shutil.copytree(src, dst)
            counts[tname] = counts.get(tname, 0) + 1
    if not dry and installed:
        AG_PLUGIN_DIR.mkdir(parents=True, exist_ok=True)
        (AG_PLUGIN_DIR / "plugin.json").write_text(
            json.dumps(AG_PLUGIN_JSON, indent=2) + "\n", encoding="utf-8")
        register_antigravity_plugin()
    return counts


def register_antigravity_plugin() -> None:
    """Declare the plugin in Antigravity's import manifest.

    A plugin directory that is not registered is not loaded, so writing
    plugin.json alone is not enough. Mirrors what deploy.py does for the
    authored suite.
    """
    manifest = AG_PLUGIN_DIR.parent.parent / "import_manifest.json"
    if not manifest.is_file():
        print(f"  ! no import_manifest.json at {manifest} — plugin not registered")
        return
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        print(f"  ! unreadable import_manifest.json at {manifest} — plugin not registered")
        return
    imports = data.setdefault("imports", [])
    name = AG_PLUGIN_JSON["name"]
    if any(i.get("name") == name for i in imports):
        return
    imports.append({
        "name": name,
        "source": "local-install",
        "importedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "components": ["installed"],
    })
    manifest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"  registered {name} in {manifest}")


def write_manifest(installed: list[str]) -> None:
    """Merge into any existing manifest so repeated targeted runs stay cumulative."""
    for root, _ in TARGETS.values():
        if not root.is_dir():
            continue
        entry: dict = {}
        prior = root / MANIFEST
        if prior.is_file():
            try:
                entry = (json.loads(prior.read_text(encoding="utf-8")) or {}).get("skills", {})
            except (OSError, json.JSONDecodeError):
                entry = {}
        for n in installed:
            entry[n] = {"skill_md_sha256": sha256(INSTALLED / n / "SKILL.md")}
        data = {
            "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "note": "Curated third-party skills. Provenance per skill in its own SKILL.md footer.",
            "skills": entry,
        }
        try:
            prior.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        except OSError:
            pass


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="show the curated set")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--update", action="store_true", help="re-clone sources first")
    ap.add_argument("--check", action="store_true", help="drift report")
    ap.add_argument("--force", action="store_true", help="overwrite colliding names")
    ap.add_argument("--source", action="append", help="limit to one repo (repeatable)")
    args = ap.parse_args()

    sources = [s for s in load_sources() if s.get("enabled", True)]
    if args.source:
        sources = [s for s in sources if s["repo"] in args.source]
    if not sources:
        print("no sources selected")
        return 1

    if args.list:
        for s in sources:
            print(f"{s['repo']}  ({s.get('license','?')})  ref={s.get('ref','main')}")
            print(f"   {s.get('why','')[:150]}")
            for n in s.get("include", []):
                print(f"     - {n}")
        return 0

    installed, skipped, failed = [], [], []
    for s in sources:
        print(f"\n[{s['repo']}]")
        dest = clone(s["repo"], s.get("ref", "main"), args.update)
        if dest is None:
            failed.append((s["repo"], "clone failed"))
            continue
        sha = repo_sha(dest)
        found = discover(dest)
        picked = select(found, s.get("include", []), s.get("exclude", []))
        missing = [n for n in s.get("include", []) if n not in found]
        print(f"  discovered {len(found)} skills; selected {len(picked)}"
              + (f"; missing: {missing}" if missing else ""))

        collide = existing_names() - set(installed)
        for name, src in picked.items():
            if name in collide and not args.force:
                skipped.append((name, "name already installed in a runtime"))
                continue
            if args.dry_run:
                installed.append(name)
                continue
            ok, why = stage(name, src, s["repo"], sha, datetime.now(timezone.utc)
                            .strftime("%Y-%m-%d"))
            (installed if ok else failed).append(name if ok else (name, why))

    if args.dry_run:
        print(f"\n[dry-run] would install {len(installed)}: {', '.join(sorted(installed))}")
        return 0

    counts = deploy(installed, args.dry_run)
    write_manifest(installed)
    print(f"\ninstalled {len(installed)} external skills -> {counts}")
    if skipped:
        print(f"skipped {len(skipped)} (name collisions; use --force to override):")
        for n, why in skipped:
            print(f"   - {n}: {why}")
    if failed:
        print(f"failed {len(failed)}:")
        for item in failed:
            print(f"   - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
