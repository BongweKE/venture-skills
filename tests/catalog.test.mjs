/**
 * Catalog integrity tests.
 *
 * The catalog and the router's reference docs all name skills. If one of them
 * names a skill that is not installed, an agent will load nothing and quietly
 * do the wrong thing. This repository shipped that bug once already: CATALOG.md
 * cited twenty-one skills from a plan that was never installed. This test is the
 * guard.
 *
 * Only backticked, skill-shaped tokens are checked, and non-skill tokens are
 * allowlisted explicitly rather than by a loose pattern.
 */
import { test } from "node:test";
import assert from "node:assert/strict";
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const REPO = resolve(dirname(fileURLToPath(import.meta.url)), "..");

const repoSkills = new Set(
  readdirSync(join(REPO, "skills")).filter((n) => statSync(join(REPO, "skills", n)).isDirectory())
);
const knownSkills = new Set(
  readFileSync(join(REPO, "catalog/known-skills.txt"), "utf8")
    .split("\n")
    .map((l) => l.trim())
    .filter((l) => l && !l.startsWith("#"))
);

// Tokens that look like skill names but are not.
const NOT_SKILLS = new Set([
  "venture-skills",
  "business-development",
  "business-to-app",
  "agent-skills",
  "related-skills",
  "material-symbols-outlined",
  "gen-known-skills",
  "install-external",
  "venture-skills-root",
  "venture-skills-manifest",
  "skills",
  "node",
  "npm",
  "npx",
  "git",
  "python3",
  // frontmatter field names, quoted in the authoring docs
  "name",
  "description",
  "license",
  "compatibility",
  "metadata",
  "version",
  "suite",
  "triggers",
  "why",
  "include",
  "exclude",
  "repo",
  "ref",
]);

// Naming families that are deliberately referenced as a prefix.
const GLOBS = [/^\w+-\*$/];

function docs() {
  const out = [join(REPO, "catalog/CATALOG.md"), join(REPO, "README.md"), join(REPO, "AGENTS.md")];
  for (const d of ["docs", "skills/venture-skills-root/references"]) {
    const p = join(REPO, d);
    if (!existsSync(p)) continue;
    for (const f of readdirSync(p)) {
      const full = join(p, f);
      if (statSync(full).isFile() && f.endsWith(".md")) out.push(full);
    }
  }
  return out.filter(existsSync);
}

function citedNames(text) {
  return new Set(
    [...text.matchAll(/`([a-z][a-z0-9-]{2,})`/g)].map((m) => m[1]).filter((t) => !t.includes("."))
  );
}

for (const file of docs()) {
  const text = readFileSync(file, "utf8");
  const rel = file.slice(REPO.length + 1);
  const names = [...citedNames(text)].filter(
    (n) => !NOT_SKILLS.has(n) && !GLOBS.some((g) => g.test(n))
  );

  test(`${rel}: every cited skill is installed`, () => {
    const missing = names.filter((n) => !repoSkills.has(n) && !knownSkills.has(n));
    assert.deepEqual(
      missing,
      [],
      `${rel} cites skills that are not installed: ${missing.join(", ")}. ` +
        `Either install them, or remove the reference.`
    );
  });
}

test("the router's corpus map cites only installed skills", () => {
  const p = join(REPO, "skills/venture-skills-root/references/corpus-map.md");
  assert.ok(existsSync(p), "the corpus map must exist; it carries the WHY/HOW handoffs");
  const text = readFileSync(p, "utf8");
  const names = [...citedNames(text)].filter((n) => !NOT_SKILLS.has(n));
  const missing = names.filter((n) => !repoSkills.has(n) && !knownSkills.has(n));
  assert.deepEqual(missing, [], `corpus-map cites uninstalled skills: ${missing.join(", ")}`);
});

test("every stage named in the router exists as a skill", () => {
  const text = readFileSync(join(REPO, "skills/venture-skills-root/SKILL.md"), "utf8");
  // The chain table names a skill per stage; each must be a real skill here.
  for (const m of text.matchAll(/`([a-z][a-z0-9-]{2,})`/g)) {
    const n = m[1];
    if (NOT_SKILLS.has(n) || n.includes(".")) continue;
    assert.ok(
      repoSkills.has(n) || knownSkills.has(n),
      `venture-skills-root references unknown skill: ${n}`
    );
  }
});
