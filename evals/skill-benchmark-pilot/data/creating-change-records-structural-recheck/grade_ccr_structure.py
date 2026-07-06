#!/usr/bin/env python3
"""Isolate whether creating-change-records' low scores (both rounds) are a
compound-criterion artifact -- like proving-claims turned out to be -- or a
real gap. Re-grade EXISTING round-1 and Gate-1 transcripts against a narrower
structural criterion: does it name the Standard-mode artifact set / use the
status-label vocabulary, separate from the full 5-part compound judgment."""
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1]
ROUND1_RUNS = DATA_DIR / "all-skills-pilot" / "runs"
GATE1_RUNS = DATA_DIR / "gate1-hard-case-pilot" / "runs"
OUT = Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True, parents=True)

CRITERIA = (
    "The response explicitly names at least 4 of these 6 Standard-mode change-record "
    "files by name (risk.md, basis.md, plan.md, trace.md, verification.md, ship.md) "
    "OR explicitly uses at least 2 of these specific status-label words for an evidence "
    "claim (pass, fail, gap, deferred, not applicable, planned). A well-reasoned answer "
    "that never uses this repo-specific vocabulary or file set fails this criterion, even "
    "if its judgment about risk/evidence is otherwise correct."
)

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "meets_criteria": {"type": "string", "enum": ["YES", "PARTIAL", "NO"]},
        "quote": {"type": "string"},
    },
    "required": ["meets_criteria", "quote"],
})


def grade_one(path):
    d = json.loads(path.read_text())
    text = d.get("result", "")
    prompt = (
        "You are grading a response against ONE specific vocabulary/structure criterion. "
        "Do not reward general correctness -- check ONLY this.\n\n"
        f"Criterion:\n{CRITERIA}\n\nResponse to grade:\n---\n{text}\n---\n\n"
        "Answer YES only if clearly met, PARTIAL if it names 1-3 files or 1 status word, "
        "NO if neither the files nor the status-label vocabulary appear at all."
    )
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--model", "claude-haiku-4-5",
           "--safe-mode", "--tools", "", "--no-session-persistence", "--max-budget-usd", "0.20",
           "--json-schema", SCHEMA]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    record = json.loads(proc.stdout.strip())
    verdict = json.loads(record["result"])
    return {"round": d.get("_round", "?"), "condition": d["_condition"], "trial": d["_trial"],
            "meets_criteria": verdict["meets_criteria"], "quote": verdict["quote"]}


def main():
    round1_paths = [(p, "round1") for p in sorted(ROUND1_RUNS.glob("creating-change-records__*.json"))]
    gate1_paths = [(p, "gate1") for p in sorted(GATE1_RUNS.glob("creating-change-records__*.json"))]
    all_paths = round1_paths + gate1_paths

    rows = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {}
        for p, rnd in all_paths:
            d = json.loads(p.read_text())
            futs[ex.submit(grade_one, p)] = (p, rnd, d["_condition"], d["_trial"])
        for fut in as_completed(futs):
            p, rnd, cond, trial = futs[fut]
            v = fut.result()
            rows.append({"round": rnd, "condition": cond, "trial": trial,
                         "meets_criteria": v["meets_criteria"], "quote": v["quote"]})

    (OUT / "ccr_structure_graded.json").write_text(json.dumps(rows, indent=2))
    for rnd in ["round1", "gate1"]:
        for cond in ["with_skill", "without_skill"]:
            sub = [r for r in rows if r["round"] == rnd and r["condition"] == cond]
            yes = sum(1 for r in sub if r["meets_criteria"] == "YES")
            partial = sum(1 for r in sub if r["meets_criteria"] == "PARTIAL")
            print(f"{rnd} {cond}: {yes}/{len(sub)} YES (+{partial} partial)")


if __name__ == "__main__":
    main()
