/**
 * Skill format contract tests.
 *
 * These deliberately re-implement the rules enforced by scripts/validate.py in
 * a second language. A skill file is the product of this repository, so if the
 * two checkers ever disagree, one of them has a bug and we want to know before
 * a runtime silently refuses to load a skill.
 */
import { test } from "node:test";
import assert from "node:assert/strict";
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { parseFrontmatter } from "../bin/venture-skills.mjs";

const REPO = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const SKILLS = join(REPO, "skills");
const KNOWN = join(REPO, "catalog/known-skills.txt");

const NAME_RE = /^[a-z0-9]+(-[a-z0-9]+)*$/;
const PORTABLE = new Set(["name", "description", "license", "compatibility", "metadata"]);
const EMOJI_RE = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{1F000}-\u{1F0FF}\u{2190}-\u{21FF}\u{2B00}-\u{2BFF}\u{FE0F}]/u;

const dirs = readdirSync(SKILLS).filter((n) => statSync(join(SKILLS, n)).isDirectory());
const names = new Set(dirs);
const known = new Set(
  readFileSync(KNOWN, "utf8")
    .split("\n")
    .map((l) => l.trim())
    .filter((l) => l && !l.startsWith("#"))
);

test("skills directory is not empty", () => {
  assert.ok(dirs.length >= 20, `expected at least 20 skills, found ${dirs.length}`);
});

for (const name of dirs) {
  const dir = join(SKILLS, name);
  const file = join(dir, "SKILL.md");
  const raw = existsSync(file) ? readFileSync(file, "utf8") : "";

  test(`${name}: SKILL.md exists and parses`, () => {
    assert.ok(existsSync(file), "missing SKILL.md");
    assert.ok(raw.startsWith("---"), "frontmatter must start at byte 0");
    const fm = parseFrontmatter(raw);
    assert.ok(fm, "frontmatter must parse");
  });

  test(`${name}: frontmatter contract`, () => {
    const fm = parseFrontmatter(raw);
    assert.ok(fm, "frontmatter must parse");
    assert.equal(fm.name, name, "name must equal the directory name");
    assert.match(fm.name, NAME_RE, "name must be lowercase-hyphenated");
    assert.ok(fm.name.length <= 64, "name must be at most 64 chars");
    assert.ok(typeof fm.description === "string" && fm.description.trim(), "description required");
    assert.ok(fm.description.length <= 1024, "description must be at most 1024 chars");
    for (const key of Object.keys(fm)) {
      assert.ok(PORTABLE.has(key), `non-portable frontmatter field: ${key}`);
    }
  });

  test(`${name}: description is routing-safe`, () => {
    const fm = parseFrontmatter(raw);
    // Runtimes index a truncated opening of the description; the first ~57
    // characters must stand alone as a trigger.
    const head = fm.description.slice(0, 57);
    assert.ok(head.length >= 20, "description opening is too short to route on");
    assert.ok(/^[A-Z]/.test(fm.description), "description should open with a capitalised trigger");
  });

  test(`${name}: body and size limits`, () => {
    const body = raw.split("---", 3)[2] ?? "";
    assert.ok(body.trim().length > 0, "body must not be empty");
    assert.ok(raw.length <= 20000, `SKILL.md is ${raw.length} chars, limit is 20000`);
    assert.ok(raw.split("\n").length <= 500, "SKILL.md must be at most 500 lines");
  });

  test(`${name}: no raw emoji`, () => {
    const m = EMOJI_RE.exec(raw);
    assert.equal(m, null, `raw emoji found: ${m?.[0]} (use text or Material Symbols instead)`);
  });

  test(`${name}: required sections present in order`, () => {
    const order = ["## Before Starting", "## When to Use", "## Common Pitfalls"];
    let cursor = -1;
    for (const section of order) {
      const at = raw.indexOf(section);
      assert.ok(at !== -1, `missing required section: ${section}`);
      assert.ok(at > cursor, `section out of order: ${section}`);
      cursor = at;
    }
  });

  test(`${name}: reference and template links resolve`, () => {
    for (const m of raw.matchAll(/\((references\/[^)]+|templates\/[^)]+)\)/g)) {
      assert.ok(existsSync(join(dir, m[1])), `broken link: ${m[1]}`);
    }
  });

  test(`${name}: related-skills resolve`, () => {
    const fm = parseFrontmatter(raw);
    const related = fm?.metadata?.["related-skills"] ?? [];
    const list = Array.isArray(related) ? related : [related];
    for (const r of list) {
      assert.ok(
        names.has(r) || known.has(r),
        `related-skill does not resolve in-repo or in catalog/known-skills.txt: ${r}`
      );
    }
  });
}
