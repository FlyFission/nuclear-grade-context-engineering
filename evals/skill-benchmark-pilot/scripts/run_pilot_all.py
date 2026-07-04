#!/usr/bin/env python3
"""Run with-skill vs without-skill trials for every skill in all_skill_tasks.json."""
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).parent
RUNS_DIR = BASE / "runs_all"
WORK_DIR = BASE / "work_all"
SKILLS_ROOT = Path("/home/user/nuclear-grade-context-engineering/skills")
TASKS = json.loads((BASE / "all_skill_tasks.json").read_text())

CONDITIONS = ["with_skill", "without_skill"]
TRIALS = 3
MODEL = "claude-sonnet-5"
MAX_BUDGET_USD = "0.50"
MAX_WORKERS = 8


def extract_skill_body(skill_name: str) -> str:
    text = (SKILLS_ROOT / skill_name / "SKILL.md").read_text()
    parts = re.split(r"^---$", text, flags=re.MULTILINE)
    # parts[0] = '', parts[1] = frontmatter, parts[2:] = body
    return "---".join(parts[2:]).strip()


def run_one(skill: str, condition: str, trial: int) -> dict:
    scenario = TASKS[skill]["scenario_prompt"]
    cwd = WORK_DIR / f"{skill}_{condition}_{trial}"
    cwd.mkdir(parents=True, exist_ok=True)

    cmd = [
        "claude", "-p",
        "--output-format", "json",
        "--model", MODEL,
        "--safe-mode",
        "--tools", "",
        "--no-session-persistence",
        "--max-budget-usd", MAX_BUDGET_USD,
    ]
    if condition == "with_skill":
        cmd += ["--append-system-prompt", extract_skill_body(skill)]

    out_path = RUNS_DIR / f"{skill}__{condition}__trial{trial}.json"
    if out_path.exists():
        return json.loads(out_path.read_text())

    try:
        proc = subprocess.run(
            cmd, input=scenario, capture_output=True, text=True,
            cwd=str(cwd), timeout=180,
        )
        stdout = proc.stdout.strip()
        record = json.loads(stdout)
    except subprocess.TimeoutExpired:
        record = {"type": "error", "error": "timeout"}
    except json.JSONDecodeError:
        record = {"type": "error", "error": "non-json output", "stdout": proc.stdout[:2000], "stderr": proc.stderr[:2000]}

    record["_skill"] = skill
    record["_condition"] = condition
    record["_trial"] = trial
    out_path.write_text(json.dumps(record, indent=2))
    return record


def main():
    RUNS_DIR.mkdir(exist_ok=True)
    WORK_DIR.mkdir(exist_ok=True)

    jobs = []
    for skill in TASKS:
        for condition in CONDITIONS:
            for trial in range(1, TRIALS + 1):
                jobs.append((skill, condition, trial))

    print(f"Total jobs: {len(jobs)}", file=sys.stderr)
    done = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(run_one, *job): job for job in jobs}
        for fut in as_completed(futures):
            job = futures[fut]
            done += 1
            try:
                rec = fut.result()
                status = "ERR" if rec.get("type") == "error" or rec.get("is_error") else "ok"
            except Exception as e:
                status = f"EXC:{e}"
            print(f"[{done}/{len(jobs)}] {job} -> {status}", file=sys.stderr)

    print("Done.", file=sys.stderr)


if __name__ == "__main__":
    main()
