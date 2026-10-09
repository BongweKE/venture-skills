/**
 * CLI contract tests. The CLI is the public interface of this package, so its
 * output shape is tested, not just its exit codes.
 */
import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const REPO = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const CLI = join(REPO, "bin/venture-skills.mjs");

function run(args) {
  return execFileSync("node", [CLI, ...args], { encoding: "utf8" });
}

test("list --json returns the full skill set with suites", () => {
  const skills = JSON.parse(run(["list", "--json"]));
  assert.ok(skills.length >= 20);
  const suites = new Set(skills.map((s) => s.suite));
  assert.ok(suites.has("business-development"), "expected the business-development suite");
  assert.ok(suites.has("business-to-app"), "expected the business-to-app suite");
  for (const s of skills) {
    assert.ok(s.name, "every skill needs a name");
    assert.ok(s.description, `${s.name} needs a description`);
  }
});

test("list --suite filters", () => {
  const bridge = JSON.parse(run(["list", "--suite", "business-to-app", "--json"]));
  assert.ok(bridge.length >= 7);
  assert.ok(bridge.every((s) => s.suite === "business-to-app"));
});

test("the router skill exists and is in the business-development suite", () => {
  const skills = JSON.parse(run(["list", "--json"]));
  const root = skills.find((s) => s.name === "venture-skills-root");
  assert.ok(root, "venture-skills-root must exist; it is the entry point");
  assert.equal(root.suite, "business-development");
});

test("info prints the skill and its files", () => {
  const out = run(["info", "venture-skills-root"]);
  assert.match(out, /venture-skills-root/);
  assert.match(out, /SKILL\.md/);
  assert.match(out, /references\/corpus-map\.md/);
});

test("info on an unknown skill fails non-zero", () => {
  assert.throws(() => run(["info", "no-such-skill"]), /Command failed|no such skill/);
});

test("get prints skill markdown to stdout", () => {
  const out = run(["get", "bd-context"]);
  assert.match(out, /^---/);
  assert.match(out, /name: bd-context/);
});

test("doctor reports every runtime", () => {
  const out = run(["doctor"]);
  for (const rt of ["hermes", "opencode", "antigravity", "vibe"]) {
    assert.match(out, new RegExp(rt), `doctor should mention ${rt}`);
  }
});

test("registry lists curated sources with licences", () => {
  const sources = JSON.parse(run(["registry", "--json"]));
  assert.ok(sources.length >= 2);
  for (const s of sources) {
    assert.ok(s.repo, "source needs a repo");
    assert.ok(s.license, `${s.repo} must record a licence`);
    assert.ok(Array.isArray(s.include) && s.include.length > 0, `${s.repo} needs curated skills`);
  }
});

test("help exits zero", () => {
  assert.match(run(["help"]), /venture-skills/);
});
