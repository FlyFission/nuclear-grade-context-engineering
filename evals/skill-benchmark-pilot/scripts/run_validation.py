#!/usr/bin/env python3
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPO_ROOT = BASE.parents[2]
DATA_DIR = BASE.parent / "data" / "briefing-an-agent-amendment-validation"
RUNS_DIR = DATA_DIR / "runs"
WORK_DIR = BASE / "work"
SKILLS_ROOT = REPO_ROOT / "skills"
TASKS = json.loads((DATA_DIR / "task.json").read_text())
TRIALS = 5
MODEL = "claude-sonnet-5"

def extract_skill_body(skill_name):
    text = (SKILLS_ROOT / skill_name / "SKILL.md").read_text()
    parts = re.split(r"^---$", text, flags=re.MULTILINE)
    return "---".join(parts[2:]).strip()

def run_one(task_key, skill_name, condition, trial):
    scenario = TASKS[task_key]["scenario_prompt"]
    cwd = WORK_DIR / f"{task_key}_{condition}_{trial}"
    cwd.mkdir(parents=True, exist_ok=True)
    cmd = ["claude", "-p", "--output-format", "json", "--model", MODEL,
           "--safe-mode", "--tools", "Read,Glob,Grep", "--no-session-persistence",
           "--max-budget-usd", "0.50"]
    if condition == "with_skill":
        cmd += ["--append-system-prompt", extract_skill_body(skill_name)]
    out_path = RUNS_DIR / f"{task_key}__{condition}__trial{trial}.json"
    if out_path.exists():
        return json.loads(out_path.read_text())
    try:
        proc = subprocess.run(cmd, input=scenario, capture_output=True, text=True, cwd=str(cwd), timeout=180)
        record = json.loads(proc.stdout.strip())
    except subprocess.TimeoutExpired:
        record = {"type": "error", "error": "timeout"}
    except json.JSONDecodeError:
        record = {"type": "error", "error": "non-json output", "stdout": proc.stdout[:2000], "stderr": proc.stderr[:2000]}
    record["_task"] = task_key
    record["_condition"] = condition
    record["_trial"] = trial
    out_path.write_text(json.dumps(record, indent=2))
    return record

def main():
    RUNS_DIR.mkdir(exist_ok=True)
    WORK_DIR.mkdir(exist_ok=True)
    jobs = []
    for cond in ["with_skill", "without_skill"]:
        for trial in range(1, TRIALS+1):
            jobs.append(("briefing-an-agent-true-niche", "briefing-an-agent", cond, trial))
    failures = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(run_one, *j): j for j in jobs}
        for fut in as_completed(futs):
            j = futs[fut]
            rec = fut.result()
            is_error = rec.get("type") == "error" or rec.get("is_error")
            if is_error:
                failures += 1
            print(j, "->", "ERR" if is_error else "ok")
    if failures:
        print(f"{failures}/{len(jobs)} job(s) recorded an error -- see the persisted "
              f"error rows in {RUNS_DIR}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
