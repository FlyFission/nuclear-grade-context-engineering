#!/usr/bin/env python3
"""Re-grade creating-change-records' existing Gate 1 transcripts against a
criterion corrected for PR #63's clarified scope: this skill owns the packet
shell/required-files/links, NOT mode choice (rating-change-risk's job) or
evidence-adequacy judgment (proving-claims' job). My original Gate 1 criterion
conflated all three. This isolates just the file-naming dimension, using
literal filenames (unambiguous tokens) rather than common English words
(the source of the false-positive bug in the earlier recheck attempt)."""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1]
GATE1_RUNS = DATA_DIR / "gate1-hard-case-pilot" / "runs"
OUT = Path(__file__).resolve().parent

CRITERIA = (
    "Under a corrected scope where this skill owns only the change-record packet "
    "shell (required files and how they link), NOT the mode-choice decision "
    "(Quick vs Standard) and NOT the evidence-adequacy judgment (whether tests are "
    "sufficient) -- the response passes if it explicitly names at least 4 of these "
    "6 Standard-mode files as the required packet structure: risk.md, basis.md, "
    "plan.md, trace.md, verification.md, ship.md. It does NOT need to also argue "
    "why Standard mode applies, or independently judge whether the linter tests "
    "are sufficient evidence -- only naming the correct file/link structure is "
    "being checked here."
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
        "Do not reward general correctness -- check ONLY whether the required file "
        "names appear as the named packet structure.\n\n"
        f"Criterion:\n{CRITERIA}\n\nResponse to grade:\n---\n{text}\n---\n\n"
        "Answer YES if 4+ of the 6 files are explicitly named, PARTIAL if 1-3 are "
        "named, NO if none of the 6 specific filenames appear."
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
    paths = sorted(GATE1_RUNS.glob("creating-change-records__*.json"))
    rows = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(grade_one, p): p for p in paths}
        for fut in as_completed(futs):
            rows.append(fut.result())
    (OUT / "ccr_corrected_scope_graded.json").write_text(json.dumps(rows, indent=2))
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
              f"see the excluded rows in ccr_corrected_scope_graded.json", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
