#!/usr/bin/env python3
"""Run with-skill vs without-skill trials for every skill in all_skill_tasks.json."""
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPO_ROOT = BASE.parents[2]
DATA_DIR = BASE.parent / "data" / "gate1-hard-case-pilot"
RUNS_DIR = DATA_DIR / "runs"
WORK_DIR = BASE / "work"
SKILLS_ROOT = REPO_ROOT / "skills"
TASKS = json.loads((DATA_DIR / "gate1_tasks.json").read_text())

CONDITIONS = ["with_skill", "without_skill"]
TRIALS = 5
MODEL = "claude-sonnet-5"
MAX_BUDGET_USD = "0.50"
MAX_WORKERS = 8


def extract_skill_body(skill_name: str) -> str:
    text = (SKILLS_ROOT / skill_name / "SKILL.md").read_text()
    parts = re.split(r"^---$", text, flags=re.MULTILINE)
    # parts[0] = '', parts[1] = frontmatter, parts[2:] = body
    return "---".join(parts[2:]).strip()


def run_one(skill: str, condition: str, trial: int) -> dict:
    out_path = RUNS_DIR / f"{skill}__{condition}__trial{trial}.json"
    if out_path.exists():
        return json.loads(out_path.read_text())

    try:
        scenario = TASKS[skill]["scenario_prompt"]
        cwd = WORK_DIR / f"{skill}_{condition}_{trial}"
        cwd.mkdir(parents=True, exist_ok=True)

        cmd = [
            "claude", "-p",
            "--output-format", "json",
            "--model", MODEL,
            "--safe-mode",
            "--tools", "Read,Glob,Grep",
            "--no-session-persistence",
            "--max-budget-usd", MAX_BUDGET_USD,
        ]
        if condition == "with_skill":
            cmd += ["--append-system-prompt", extract_skill_body(skill)]

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
    except Exception as e:
        record = {"type": "error", "error": f"unexpected exception: {type(e).__name__}: {e}"}

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
    failures = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(run_one, *job): job for job in jobs}
        for fut in as_completed(futures):
            job = futures[fut]
            done += 1
            try:
                rec = fut.result()
                is_error = rec.get("type") == "error" or rec.get("is_error")
                status = "ERR" if is_error else "ok"
                if is_error:
                    failures += 1
            except Exception as e:
                status = f"EXC:{e}"
                failures += 1
            print(f"[{done}/{len(jobs)}] {job} -> {status}", file=sys.stderr)

    print("Done.", file=sys.stderr)
    if failures:
        print(f"{failures}/{len(jobs)} job(s) recorded an error -- see the persisted "
              f"error rows in {RUNS_DIR}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
