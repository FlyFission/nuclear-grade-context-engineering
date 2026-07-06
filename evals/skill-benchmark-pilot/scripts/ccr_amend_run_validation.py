#!/usr/bin/env python3
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPO_ROOT = BASE.parents[2]
RUNS_DIR = BASE / "runs"
WORK_DIR = BASE / "work"
SKILL_PATH = REPO_ROOT / "skills" / "creating-change-records" / "SKILL.md"
GATE1_TASKS = json.loads((BASE.parent / "data" / "gate1-hard-case-pilot" / "gate1_tasks.json").read_text())
SCENARIO = GATE1_TASKS["creating-change-records"]["scenario_prompt"]
TRIALS = 3

def extract_skill_body():
    text = SKILL_PATH.read_text()
    parts = re.split(r"^---$", text, flags=re.MULTILINE)
    return "---".join(parts[2:]).strip()

def run_one(model, trial):
    cwd = WORK_DIR / f"{model}_{trial}"
    cwd.mkdir(parents=True, exist_ok=True)
    cmd = ["claude", "-p", "--output-format", "json", "--model", model,
           "--safe-mode", "--tools", "Read,Glob,Grep", "--no-session-persistence",
           "--max-budget-usd", "0.30", "--append-system-prompt", extract_skill_body()]
    out_path = RUNS_DIR / f"{model}__with_skill__trial{trial}.json"
    if out_path.exists():
        return json.loads(out_path.read_text())
    proc = subprocess.run(cmd, input=SCENARIO, capture_output=True, text=True, cwd=str(cwd), timeout=180)
    record = json.loads(proc.stdout.strip())
    record["_model"] = model
    record["_trial"] = trial
    out_path.write_text(json.dumps(record, indent=2))
    return record

def main():
    jobs = []
    for model in ["claude-sonnet-5", "claude-haiku-4-5"]:
        for trial in range(1, TRIALS + 1):
            jobs.append((model, trial))
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(run_one, *j): j for j in jobs}
        for fut in as_completed(futs):
            j = futs[fut]
            rec = fut.result()
            print(j, "->", "ERR" if rec.get("is_error") else "ok", rec.get("total_cost_usd"))

if __name__ == "__main__":
    main()
