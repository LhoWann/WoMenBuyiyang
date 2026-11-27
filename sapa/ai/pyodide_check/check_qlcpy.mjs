// Run qlc_demo.questions inside Pyodide, as the browser will (proposal Section 4.3), and check every answer key
// against the facts of samples/class_means.py. qlcpy picks the asked variable and the wrong options at random,
// so the check runs several rounds instead of comparing text with desktop Python.
// Pyodide stays on 0.29.x (Python 3.13): qlcpy 1.0.18 imports ast.Num, which Python 3.14 (Pyodide 314.x) removed.
// Usage: npm install && node check_qlcpy.mjs [rounds]
import { readFileSync } from "node:fs";
import { loadPyodide } from "pyodide";

const ai = new URL("../", import.meta.url);
const rounds = Number(process.argv[2] ?? 10);
const declared = { iris: 6, df: 7, long_ones: 8, means: 9, best: 10 };
const seconds = (t) => ((performance.now() - t) / 1000).toFixed(1);

let t = performance.now();
const py = await loadPyodide();
console.log(`Pyodide ${py.version} loaded in ${seconds(t)} s`);

t = performance.now();
await py.loadPackage(["micropip", "pandas", "scikit-learn"]);
await py.pyimport("micropip").install("qlcpy==1.0.18");
console.log(`pandas, scikit-learn and qlcpy 1.0.18 installed in ${seconds(t)} s`);

py.FS.mkdirTree("/app/samples");
for (const f of ["qlc_demo.py", "samples/class_means.py"]) py.FS.writeFile(`/app/${f}`, readFileSync(new URL(f, ai)));
py.runPython(`import sys; sys.path.insert(0, "/app")`);
const generate = py.runPython(`
import json
from qlc_demo import SAMPLE, questions
lambda: json.dumps(questions(SAMPLE.read_text(encoding="utf-8"), "class_means(5.0)"))
`);

function wrongKeys(q) {
  const correct = q.options.filter((o) => o.correct).map((o) => String(o.answer));
  if (correct.length === 0) return ["no correct option"];
  if (q.type === "VariableNames") return correct.filter((a) => !(a in declared));
  if (q.type === "ParameterNames") return correct.filter((a) => a !== "min_length");
  if (q.type === "VariableDeclaration") {
    const name = q.question.match(/<em>(\w+)<\/em>/)?.[1];
    return correct.filter((a) => Number(a) !== declared[name]);
  }
  return [`unexpected type ${q.type}`];
}

const types = new Set();
let checked = 0;
const errors = [];
t = performance.now();
for (let r = 0; r < rounds; r++) {
  for (const q of JSON.parse(generate())) {
    types.add(q.type);
    checked++;
    for (const bad of wrongKeys(q)) errors.push(`[${q.type}] ${q.question.slice(0, 70)} -> ${bad}`);
  }
}
console.log(`${rounds} rounds, ${checked} questions in ${seconds(t)} s; types: ${[...types].join(", ")}`);
errors.forEach((e) => console.log(`WRONG KEY ${e}`));
const ok = errors.length === 0 && types.size === 3;
console.log(ok ? "PASS: qlcpy runs in Pyodide and every answer key is right" : "FAIL");
process.exitCode = ok ? 0 : 1;