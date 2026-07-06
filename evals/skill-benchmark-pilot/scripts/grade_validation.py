#!/usr/bin/env python3
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE.parent / "data" / "briefing-an-agent-amendment-validation"
TASKS = json.loads((DATA_DIR / "task.json").read_text())
SCHEMA = json.dumps({"type":"object","properties":{"meets_criteria":{"type":"string","enum":["YES","PARTIAL","NO"]},"quote":{"type":"string"}},"required":["meets_criteria","quote"]})

def grade_one(path):
    d = json.loads(path.read_text())
    task_key = d["_task"]
    if d.get("type") == "error" or d.get("is_error"):
        return {"condition": d["_condition"], "trial": d["_trial"], "error": True}
    criteria = TASKS[task_key]["pass_criteria"]
    prompt = (f"You are grading a response against ONE specific pass criterion. Do not reward general "
              f"competence or tone -- check ONLY whether this exact criterion is explicitly satisfied.\n\n"
              f"Pass criterion:\n{criteria}\n\nResponse to grade:\n---\n{d.get('result','')}\n---\n\n"
              f"Answer YES only if clearly and explicitly met, PARTIAL if hinted at but incomplete, NO if absent.")
    cmd = ["claude","-p",prompt,"--output-format","json","--model","claude-haiku-4-5",
           "--safe-mode","--tools","","--no-session-persistence","--max-budget-usd","0.20","--json-schema",SCHEMA]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        record = json.loads(proc.stdout.strip())
        verdict = json.loads(record["result"])
    except Exception as e:
        return {"condition": d["_condition"], "trial": d["_trial"], "error": True,
                "grader_error": True, "grader_quote": str(e)[:200]}
    return {"condition": d["_condition"], "trial": d["_trial"], "meets_criteria": verdict["meets_criteria"], "quote": verdict["quote"]}

def main():
    paths = sorted((DATA_DIR/"runs").glob("*.json"))
    rows = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(grade_one, p): p for p in paths}
        for fut in as_completed(futs):
            rows.append(fut.result())
    (DATA_DIR/"graded.json").write_text(json.dumps(rows, indent=2))
    for cond in ["with_skill","without_skill"]:
        sub = [r for r in rows if r["condition"]==cond and not r.get("error")]
        yes = sum(1 for r in sub if r["meets_criteria"]=="YES")
        partial = sum(1 for r in sub if r["meets_criteria"]=="PARTIAL")
        print(f"{cond}: {yes}/{len(sub)} YES (+{partial} partial)")
    for r in sorted((r for r in rows if not r.get("error")), key=lambda r:(r["condition"],r["trial"])):
        print(r["condition"], r["trial"], r["meets_criteria"], "|", r["quote"][:150])

    failures = sum(1 for r in rows if r.get("error"))
    if failures:
        print(f"\n{failures}/{len(rows)} row(s) recorded a subject-run or grader error -- "
              f"see the excluded rows in graded.json", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
