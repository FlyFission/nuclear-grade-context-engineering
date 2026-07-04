#!/usr/bin/env python3
"""Bounded multi-model check: does the with-vs-without effect hold on a
materially weaker subject model (Haiku) for a small, category-spanning
sample? Reuses existing scenarios (no new scenario-design cost). n=3 per
condition, 4 skills. Sonnet stays the grader throughout, kept separate from
the subject model to avoid the self-check problem this project's own
proving-claims skill warns about."""
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).parent
RUNS_DIR = BASE / "runs"
WORK_DIR = BASE / "work"
SKILLS_ROOT = Path("/home/user/nuclear-grade-context-engineering/skills")
ALL_TASKS = json.loads(Path("/home/user/nuclear-grade-context-engineering/evals/skill-benchmark-pilot/data/all-skills-pilot/all_skill_tasks.json").read_text())
GATE1_TASKS = json.loads(Path("/home/user/nuclear-grade-context-engineering/evals/skill-benchmark-pilot/data/gate1-hard-case-pilot/gate1_tasks.json").read_text())

SAMPLE = [
    ("learning-from-experience", "round1"),
    ("staying-on-mission", "round1"),
    ("proving-claims", "gate1"),
    ("creating-change-records", "gate1"),
]
SUBJECT_MODEL = "claude-haiku-4-5"
TRIALS = 3


def extract_skill_body(skill_name):
    text = (SKILLS_ROOT / skill_name / "SKILL.md").read_text()
    parts = re.split(r"^---$", text, flags=re.MULTILINE)
    return "---".join(parts[2:]).strip()


def scenario_for(skill, source):
    return ALL_TASKS[skill]["scenario_prompt"] if source == "round1" else GATE1_TASKS[skill]["scenario_prompt"]


def run_one(skill, source, condition, trial):
    scenario = scenario_for(skill, source)
    cwd = WORK_DIR / f"{skill}_{condition}_{trial}"
    cwd.mkdir(parents=True, exist_ok=True)
    cmd = ["claude", "-p", "--output-format", "json", "--model", SUBJECT_MODEL,
           "--safe-mode", "--tools", "Read,Glob,Grep", "--no-session-persistence",
           "--max-budget-usd", "0.30"]
    if condition == "with_skill":
        cmd += ["--append-system-prompt", extract_skill_body(skill)]
    out_path = RUNS_DIR / f"{skill}__{condition}__trial{trial}.json"
    if out_path.exists():
        return json.loads(out_path.read_text())
    proc = subprocess.run(cmd, input=scenario, capture_output=True, text=True, cwd=str(cwd), timeout=180)
    record = json.loads(proc.stdout.strip())
    record["_skill"] = skill
    record["_condition"] = condition
    record["_trial"] = trial
    out_path.write_text(json.dumps(record, indent=2))
    return record


def main():
    jobs = []
    for skill, source in SAMPLE:
        for cond in ["with_skill", "without_skill"]:
            for trial in range(1, TRIALS + 1):
                jobs.append((skill, source, cond, trial))
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(run_one, *j): j for j in jobs}
        for fut in as_completed(futs):
            j = futs[fut]
            rec = fut.result()
            print(j, "->", "ERR" if rec.get("is_error") else "ok", rec.get("total_cost_usd"))


if __name__ == "__main__":
    main()
