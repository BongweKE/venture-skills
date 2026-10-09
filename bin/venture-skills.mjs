#!/usr/bin/env node
/**
 * venture-skills CLI.
 *
 * Zero runtime dependencies. Reads the repo it ships in, so `npx venture-skills`
 * and a local `node bin/venture-skills.mjs` behave identically.
 *
 * Commands
 *   list [--suite <s>] [--json]      authored skills in this repo
 *   info <skill>                     one skill's frontmatter and files
 *   get <skill> [--out <dir>]        print a skill, or copy it somewhere
 *   registry [--json]                curated third-party sources, with licence
 *   install [--runtime <r>] [--dry-run]
 *   doctor                           check each runtime can see the skills
 *   help
 */
import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, statSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const REPO = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const SKILLS = join(REPO, "skills");
const HOME = homedir();

const RUNTIMES = {
  hermes: { path: join(HOME, ".hermes/skills"), categorize: true },
  opencode: { path: join(HOME, ".config/opencode/skills") },
  antigravity: { path: join(HOME, ".gemini/antigravity-cli/plugins/venture-skills/skills") },
  vibe: { path: join(HOME, ".vibe/skills") },
};

// ---------------------------------------------------------------- frontmatter

/**
 * Minimal frontmatter reader. Our SKILL.md frontmatter is deliberately simple
 * (scalars plus one nested metadata block), so a full YAML parser would be
 * dependency weight for nothing. Anything it cannot read confidently returns
 * null and the caller reports it, rather than guessing.
 */
export function parseFrontmatter(text) {
  if (!text.startsWith("---")) return null;
  const end = text.indexOf("\n---", 3);
  if (end === -1) return null;
  const fm = text.slice(3, end);
  const out = {};
  let nested = null;
  for (const rawLine of fm.split("\n")) {
    const line = rawLine.replace(/\s+$/, "");
    if (!line.trim() || line.trim().startsWith("#")) continue;
    const indent = line.length - line.trimStart().length;
    const m = /^([A-Za-z0-9_-]+):\s*(.*)$/.exec(line.trim());
    if (indent === 0) {
      nested = null;
      if (!m) return null;
      const [, key, value] = m;
      if (value === "") {
        nested = {};
        out[key] = nested;
      } else {
        out[key] = unquote(value);
      }
    } else if (nested && m) {
      const [, key, value] = m;
      nested[key] = value === "" ? [] : parseValue(value);
    } else if (nested && /^-\s+/.test(line.trim())) {
      const last = Object.keys(nested).pop();
      if (last && Array.isArray(nested[last])) {
        nested[last].push(unquote(line.trim().replace(/^-\s+/, "")));
      }
    }
  }
  return out;
}

function unquote(v) {
  const t = v.trim();
  if (t.length > 1 && (t[0] === '"' || t[0] === "'") && t[t.length - 1] === t[0]) {
    return t.slice(1, -1);
  }
  return t;
}

/**
 * Scalar or flow sequence. Our skills write lists as `related-skills: [a, b]`,
 * which is valid YAML that a scalar-only reader silently turns into a string.
 */
function parseValue(v) {
  const t = v.trim();
  if (t.startsWith("[") && t.endsWith("]")) {
    return t
      .slice(1, -1)
      .split(",")
      .map((x) => unquote(x))
      .filter((x) => x !== "");
  }
  return unquote(t);
}

export function readSkill(dir) {
  const file = join(dir, "SKILL.md");
  if (!existsSync(file)) return null;
  const text = readFileSync(file, "utf8");
  const fm = parseFrontmatter(text);
  if (!fm) return null;
  return {
    dir,
    name: fm.name ?? null,
    description: fm.description ?? "",
    license: fm.license ?? null,
    suite: fm.metadata?.suite ?? "uncategorized",
    version: fm.metadata?.version ?? null,
    chars: text.length,
    files: listFiles(dir),
  };
}

function listFiles(dir, base = dir) {
  const out = [];
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) out.push(...listFiles(p, base));
    else out.push(p.slice(base.length + 1));
  }
  return out.sort();
}

export function allSkills() {
  if (!existsSync(SKILLS)) return [];
  return readdirSync(SKILLS)
    .filter((n) => statSync(join(SKILLS, n)).isDirectory())
    .map((n) => readSkill(join(SKILLS, n)))
    .filter(Boolean)
    .sort((a, b) => a.name.localeCompare(b.name));
}

// -------------------------------------------------------------------- registry

export function registrySources() {
  const f = join(REPO, "registry/sources.json");
  if (!existsSync(f)) return [];
  return JSON.parse(readFileSync(f, "utf8")).sources.filter((s) => s.enabled !== false);
}

// ------------------------------------------------------------------- commands

const C = process.stdout.isTTY
  ? { dim: "\x1b[2m", bold: "\x1b[1m", off: "\x1b[0m", green: "\x1b[32m", red: "\x1b[31m" }
  : { dim: "", bold: "", off: "", green: "", red: "" };

function flag(args, name, fallback = null) {
  const i = args.indexOf(`--${name}`);
  return i === -1 ? fallback : (args[i + 1] && !args[i + 1].startsWith("--") ? args[i + 1] : true);
}

function cmdList(args) {
  let skills = allSkills();
  const suite = flag(args, "suite");
  if (suite) skills = skills.filter((s) => s.suite === suite);
  if (flag(args, "json")) {
    console.log(JSON.stringify(skills.map(({ dir, ...s }) => s), null, 2));
    return 0;
  }
  const bySuite = skills.reduce((acc, s) => ((acc[s.suite] ??= []).push(s), acc), {});
  for (const [name, group] of Object.entries(bySuite)) {
    console.log(`\n${C.bold}${name}${C.off} ${C.dim}(${group.length})${C.off}`);
    for (const s of group) {
      console.log(`  ${s.name.padEnd(30)} ${C.dim}${s.description.slice(0, 72)}${C.off}`);
    }
  }
  console.log(`\n${skills.length} skills. Use \`venture-skills info <name>\` for detail.`);
  return 0;
}

function cmdInfo(args) {
  const name = args.find((a) => !a.startsWith("--"));
  const s = allSkills().find((x) => x.name === name);
  if (!s) {
    console.error(`${C.red}no such skill:${C.off} ${name ?? "(none given)"}`);
    return 1;
  }
  console.log(`${C.bold}${s.name}${C.off}  ${C.dim}${s.suite}${C.off}`);
  console.log(`\n${s.description}\n`);
  console.log(`${C.dim}version${C.off}  ${s.version ?? "n/a"}`);
  console.log(`${C.dim}license${C.off}  ${s.license ?? "n/a"}`);
  console.log(`${C.dim}size${C.off}     ${s.chars} chars`);
  console.log(`${C.dim}path${C.off}     ${s.dir}`);
  console.log(`\n${C.dim}files${C.off}\n${s.files.map((f) => `  ${f}`).join("\n")}`);
  return 0;
}

function cmdGet(args) {
  const name = args.find((a) => !a.startsWith("--"));
  const s = allSkills().find((x) => x.name === name);
  if (!s) {
    console.error(`${C.red}no such skill:${C.off} ${name ?? "(none given)"}`);
    return 1;
  }
  const out = flag(args, "out");
  if (out && out !== true) {
    const dest = join(resolve(String(out)), s.name);
    rmSync(dest, { recursive: true, force: true });
    mkdirSync(dirname(dest), { recursive: true });
    cpSync(s.dir, dest, { recursive: true });
    console.log(`${C.green}copied${C.off} ${s.name} -> ${dest}`);
    return 0;
  }
  console.log(readFileSync(join(s.dir, "SKILL.md"), "utf8"));
  return 0;
}

function cmdRegistry(args) {
  const sources = registrySources();
  if (flag(args, "json")) {
    console.log(JSON.stringify(sources, null, 2));
    return 0;
  }
  for (const s of sources) {
    const count = (s.include ?? []).length;
    console.log(`\n${C.bold}${s.repo}${C.off}  ${C.dim}${s.license ?? "see repo"}${C.off}`);
    console.log(`  ${s.why}`);
    console.log(`  ${C.dim}${count} curated skill(s)${C.off}`);
  }
  console.log(`\nFull attribution in CREDITS.md.`);
  return 0;
}

function cmdInstall(args) {
  const target = flag(args, "runtime", "all");
  const dry = Boolean(flag(args, "dry-run"));
  const names = String(target) === "all" ? Object.keys(RUNTIMES) : [String(target)];
  for (const n of names) {
    if (!RUNTIMES[n]) {
      console.error(`${C.red}unknown runtime:${C.off} ${n}`);
      return 1;
    }
  }
  const skills = allSkills();
  for (const n of names) {
    const rt = RUNTIMES[n];
    if (!existsSync(rt.path) && !dry) mkdirSync(rt.path, { recursive: true });
    let ok = 0;
    for (const s of skills) {
      const dest = join(rt.categorize ? join(rt.path, s.suite) : rt.path, s.name);
      if (dry) {
        console.log(`  would write ${dest}`);
        ok++;
        continue;
      }
      rmSync(dest, { recursive: true, force: true });
      mkdirSync(dirname(dest), { recursive: true });
      cpSync(s.dir, dest, { recursive: true });
      ok++;
    }
    console.log(`${C.green}${n}${C.off} ${ok} skill(s) -> ${rt.path}`);
  }
  return 0;
}

function cmdDoctor() {
  const skills = allSkills();
  const suites = [...new Set(skills.map((s) => s.suite))];
  console.log(`${C.bold}repo${C.off}       ${skills.length} skills across ${suites.length} suite(s)`);
  let bad = 0;
  for (const n of Object.keys(RUNTIMES)) {
    const rt = RUNTIMES[n];
    let found = 0;
    for (const s of skills) {
      const candidates = [
        join(rt.categorize ? join(rt.path, s.suite) : rt.path, s.name),
        join(rt.path, s.name),
      ];
      if (candidates.some((c) => existsSync(join(c, "SKILL.md")))) found++;
    }
    const mark = found === skills.length ? `${C.green}ok${C.off}` : `${C.red}${found}/${skills.length}${C.off}`;
    console.log(`  ${n.padEnd(12)} ${mark} ${C.dim}${rt.path}${C.off}`);
    if (found !== skills.length) bad++;
  }
  if (!existsSync(join(REPO, "catalog/known-skills.public.txt"))) {
    console.log(
      `  ${C.dim}catalog/known-skills.public.txt missing - run scripts/gen-known-skills.py --public${C.off}`
    );
  }
  return bad ? 1 : 0;
}

function usage() {
  console.log(`${C.bold}venture-skills${C.off} - business, product and engineering skills for AI coding agents

${C.bold}usage${C.off}
  venture-skills list [--suite <suite>] [--json]
  venture-skills info <skill>
  venture-skills get <skill> [--out <dir>]
  venture-skills registry [--json]
  venture-skills install [--runtime ${Object.keys(RUNTIMES).join("|")}|all] [--dry-run]
  venture-skills doctor

${C.bold}runtimes${C.off} ${Object.keys(RUNTIMES).join(", ")}`);
  return 0;
}

export function main(argv) {
  const [cmd, ...args] = argv;
  switch (cmd) {
    case "list": case undefined: return cmdList(args);
    case "info": return cmdInfo(args);
    case "get": return cmdGet(args);
    case "registry": return cmdRegistry(args);
    case "install": return cmdInstall(args);
    case "doctor": return cmdDoctor();
    case "help": case "--help": case "-h": return usage();
    default:
      console.error(`${C.red}unknown command:${C.off} ${cmd}\n`);
      usage();
      return 1;
  }
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exit(main(process.argv.slice(2)));
}
