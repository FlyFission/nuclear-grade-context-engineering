#!/usr/bin/env python3
"""Gate 3 for proving-claims: re-grade the EXISTING Gate 1 transcripts against a
structural-completeness criterion instead of a decision-correctness criterion.

Diagnosis from AMENDMENT_VALIDATION.md-style manual read: both conditions already
reach the right DECISION (self-check != independent evidence). The skill's own
Outputs section demands something neither condition was ever scored on: a
structured claim-to-evidence artifact with named status labels. This reuses the
same 10 transcripts (no new generation cost) with a new grading pass.
"""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1]
GATE1_RUNS = DATA_DIR / "gate1-hard-case-pilot" / "runs"
OUT = Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True, parents=True)

CRITERIA = (
    "The response presents its claims as structured claim-to-evidence rows (a table, "
    "or clearly labeled per-claim entries -- not just free-flowing prose) AND assigns "
    "at least one material claim one of the skill's specific status labels "
    "(pass, fail, gap, deferred, not applicable, or planned) AND explicitly separates, "
    "for at least one claim, what is verified/fact from what is merely the actor's own "
    "source-claim/assertion. A well-reasoned prose answer that reaches the right "
    "conclusion but never structures claims into labeled rows with status tags fails "
    "this criterion, even if it is otherwise excellent."
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
    if d.get("type") == "error" or d.get("is_error"):
        return {"condition": d["_condition"], "trial": d["_trial"], "error": True}
    text = d.get("result", "")
    prompt = (
        "You are grading a response against ONE specific structural criterion. "
        "Do not reward general correctness or reasoning quality -- check ONLY whether "
        "this exact structural requirement is met.\n\n"
        f"Criterion:\n{CRITERIA}\n\nResponse to grade:\n---\n{text}\n---\n\n"
        "Answer YES only if clearly and explicitly met, PARTIAL if partially structured "
        "(e.g. has status labels but no clear per-claim rows, or vice versa), NO if the "
        "response is plain prose with no claim-to-evidence structure at all."
    )
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--model", "claude-haiku-4-5",
           "--safe-mode", "--tools", "", "--no-session-persistence", "--max-budget-usd", "0.20",
           "--json-schema", SCHEMA]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        record = json.loads(proc.stdout.strip())
        verdict = json.loads(record["result"])
    except Exception as e:
        return {"condition": d["_condition"], "trial": d["_trial"], "error": True,
                "grader_error": True, "grader_quote": str(e)[:200]}
    return {"condition": d["_condition"], "trial": d["_trial"],
            "meets_criteria": verdict["meets_criteria"], "quote": verdict["quote"]}


def main():
    paths = sorted(GATE1_RUNS.glob("proving-claims__*.json"))
    rows = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(grade_one, p): p for p in paths}
        for fut in as_completed(futs):
            rows.append(fut.result())
    (OUT / "structure_graded.json").write_text(json.dumps(rows, indent=2))
    for cond in ["with_skill", "without_skill"]:
        sub = [r for r in rows if r["condition"] == cond and not r.get("error")]
        yes = sum(1 for r in sub if r["meets_criteria"] == "YES")
        partial = sum(1 for r in sub if r["meets_criteria"] == "PARTIAL")
        print(f"{cond}: {yes}/{len(sub)} YES (+{partial} partial)")
    for r in sorted((r for r in rows if not r.get("error")), key=lambda r: (r["condition"], r["trial"])):
        print(r["condition"], r["trial"], r["meets_criteria"], "|", r["quote"][:180])

    failures = sum(1 for r in rows if r.get("error"))
    if failures:
        print(f"\n{failures}/{len(rows)} row(s) recorded a subject-run or grader error -- "
              f"see the excluded rows in structure_graded.json", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
