/**
 * Registry integrity tests.
 *
 * Curating other people's work carries an obligation: the attribution must be
 * complete and must not drift from the registry that drives the installer.
 */
import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { existsSync, readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const REPO = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const sources = JSON.parse(readFileSync(join(REPO, "registry/sources.json"), "utf8")).sources;
const enabled = sources.filter((s) => s.enabled !== false);

test("every source records a licence and a reason", () => {
  for (const s of sources) {
    assert.ok(s.repo, "every source needs a repo");
    assert.match(s.repo, /^[\w.-]+\/[\w.-]+$/, `${s.repo} is not owner/name`);
    assert.ok(s.license, `${s.repo} must record its upstream licence`);
    assert.ok(s.why && s.why.length > 20, `${s.repo} must explain why it is curated`);
  }
});

test("include and exclude do not overlap", () => {
  for (const s of enabled) {
    const overlap = (s.include ?? []).filter((n) => (s.exclude ?? []).includes(n));
    assert.deepEqual(overlap, [], `${s.repo} both includes and excludes: ${overlap.join(", ")}`);
  }
});

test("curated skills do not collide with skills this repo authors", () => {
  const out = execFileSync("node", [join(REPO, "bin/venture-skills.mjs"), "list", "--json"], {
    encoding: "utf8",
  });
  const ours = new Set(JSON.parse(out).map((s) => s.name));
  for (const s of enabled) {
    for (const n of s.include ?? []) {
      assert.ok(!ours.has(n), `"${n}" is both authored here and curated from ${s.repo} - routing ambiguity`);
    }
  }
});

test("no duplicate skill across sources", () => {
  const seen = new Map();
  for (const s of enabled) {
    for (const n of s.include ?? []) {
      assert.ok(!seen.has(n), `"${n}" curated from both ${seen.get(n)} and ${s.repo}`);
      seen.set(n, s.repo);
    }
  }
});

test("attribution files exist and match the registry", () => {
  assert.ok(existsSync(join(REPO, "CREDITS.md")), "CREDITS.md must exist");
  assert.ok(existsSync(join(REPO, "registry/installed.json")), "registry/installed.json must exist");
  // --check exits non-zero when the generated files are stale.
  execFileSync("node", [join(REPO, "scripts/gen-credits.mjs"), "--check"], { encoding: "utf8" });
});

test("installed.json records the same sources as sources.json", () => {
  const installed = JSON.parse(readFileSync(join(REPO, "registry/installed.json"), "utf8"));
  assert.equal(installed.sources.length, enabled.length);
  for (const s of installed.sources) {
    assert.match(s.url, /^https:\/\/github\.com\//, "attribution must link upstream");
    assert.ok(s.license, `${s.repo} missing licence in installed.json`);
  }
});
