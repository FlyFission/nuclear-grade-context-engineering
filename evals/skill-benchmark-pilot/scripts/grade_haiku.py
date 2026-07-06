#!/usr/bin/env python3
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE.parent / "data" / "multi-model-check"
ALL_TASKS = json.loads((BASE.parent / "data" / "all-skills-pilot" / "all_skill_tasks.json").read_text())
GATE1_TASKS = json.loads((BASE.parent / "data" / "gate1-hard-case-pilot" / "gate1_tasks.json").read_text())

CRITERIA_SOURCE = {
    "learning-from-experience": ("round1", ALL_TASKS),
    "staying-on-mission": ("round1", ALL_TASKS),
    "proving-claims": ("gate1", GATE1_TASKS),
    "creating-change-records": ("gate1", GATE1_TASKS),
}

# creating-change-records uses the corrected, scope-limited criterion (see
# Task 7 / PR #63 reconciliation), not the original compound Gate 1 criterion.
CCR_CORRECTED_CRITERIA = (
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


def criteria_for(skill):
    if skill == "creating-change-records":
        return CCR_CORRECTED_CRITERIA
    source, tasks = CRITERIA_SOURCE[skill]
    return tasks[skill]["pass_criteria"]


def grade_one(path):
    d = json.loads(path.read_text())
    skill = d["_skill"]
    if d.get("type") == "error" or d.get("is_error"):
        return {"skill": skill, "condition": d["_condition"], "trial": d["_trial"], "error": True}
    criteria = criteria_for(skill)
    text = d.get("result", "")
    prompt = (
        "You are grading a response against ONE specific pass criterion. "
        "Do not reward general competence or tone -- check ONLY whether "
        "this exact criterion is explicitly satisfied.\n\n"
        f"Pass criterion:\n{criteria}\n\nResponse to grade:\n---\n{text}\n---\n\n"
        "Answer YES only if clearly and explicitly met, PARTIAL if hinted at but "
        "incomplete, NO if absent."
    )
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--model", "claude-sonnet-5",
           "--safe-mode", "--tools", "", "--no-session-persistence", "--max-budget-usd", "0.20",
           "--json-schema", SCHEMA]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        record = json.loads(proc.stdout.strip())
        verdict = json.loads(record["result"])
    except Exception as e:
        return {"skill": skill, "condition": d["_condition"], "trial": d["_trial"], "error": True,
                "grader_error": True, "grader_quote": str(e)[:200]}
    return {"skill": skill, "condition": d["_condition"], "trial": d["_trial"],
            "meets_criteria": verdict["meets_criteria"], "quote": verdict["quote"]}


def main():
    paths = sorted((DATA_DIR / "runs").glob("*.json"))
    rows = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(grade_one, p): p for p in paths}
        for fut in as_completed(futs):
            rows.append(fut.result())
    (DATA_DIR / "haiku_graded.json").write_text(json.dumps(rows, indent=2))
    skills = sorted(set(r["skill"] for r in rows))
    for skill in skills:
        for cond in ["with_skill", "without_skill"]:
            sub = [r for r in rows if r["skill"] == skill and r["condition"] == cond and not r.get("error")]
            yes = sum(1 for r in sub if r["meets_criteria"] == "YES")
            partial = sum(1 for r in sub if r["meets_criteria"] == "PARTIAL")
            print(f"{skill:28s} {cond:15s} {yes}/{len(sub)} YES (+{partial}p)")


if __name__ == "__main__":
    main()
