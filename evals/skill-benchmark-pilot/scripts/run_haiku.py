#!/usr/bin/env python3
"""Bounded multi-model check: does the with-vs-without effect hold on a
materially weaker subject model (Haiku) for a small, category-spanning
sample? Reuses existing scenarios (no new scenario-design cost). n=3 per
condition, 4 skills. Sonnet stays the grader throughout, kept separate from
the subject model to avoid the self-check problem this project's own
proving-claims skill warns about."""
import hashlib
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPO_ROOT = BASE.parents[2]
DATA_DIR = BASE.parent / "data" / "multi-model-check"
RUNS_DIR = DATA_DIR / "runs"
WORK_DIR = BASE / "work"
SKILLS_ROOT = REPO_ROOT / "skills"
ALL_TASKS = json.loads((BASE.parent / "data" / "all-skills-pilot" / "all_skill_tasks.json").read_text())
GATE1_TASKS = json.loads((BASE.parent / "data" / "gate1-hard-case-pilot" / "gate1_tasks.json").read_text())

SAMPLE = [
    ("learning-from-experience", "round1"),
    ("staying-on-mission", "round1"),
    ("proving-claims", "gate1"),
    ("creating-change-records", "gate1"),
]
SUBJECT_MODEL = "claude-haiku-4-5"
TOOLS = "Read,Glob,Grep"
MAX_BUDGET_USD = "0.30"
# Isolation/session flags that also shape what the subject model can do --
# named here (not inlined in cmd below) so the hash and the actual command
# are built from the exact same list and can never drift apart, the same
# fix already applied to TOOLS/MAX_BUDGET_USD.
HARNESS_FLAGS = ["--safe-mode", "--no-session-persistence"]
TRIALS = 3


def extract_skill_body(skill_name):
    text = (SKILLS_ROOT / skill_name / "SKILL.md").read_text()
    parts = re.split(r"^---$", text, flags=re.MULTILINE)
    return "---".join(parts[2:]).strip()


def scenario_for(skill, source):
    return ALL_TASKS[skill]["scenario_prompt"] if source == "round1" else GATE1_TASKS[skill]["scenario_prompt"]


def input_spec_hash(skill, source, condition):
    """Fingerprint of everything that determines the subject-model call's
    output besides its own randomness: the scenario prompt, the skill body
    (with_skill only), the subject model, the condition, and the harness
    settings (--tools, --max-budget-usd, HARNESS_FLAGS). A persisted run
    file is only reused if this matches -- an edited scenario, SKILL.md, or
    harness config must force a fresh call even if the old output file is
    still sitting on disk from before the change."""
    scenario = scenario_for(skill, source)
    skill_body = extract_skill_body(skill) if condition == "with_skill" else ""
    return hashlib.sha256(
        f"{scenario}::{skill_body}::{SUBJECT_MODEL}::{condition}::{TOOLS}::{MAX_BUDGET_USD}::"
        f"{'::'.join(HARNESS_FLAGS)}".encode()
    ).hexdigest()


def run_one(skill, source, condition, trial):
    scenario = scenario_for(skill, source)
    cwd = WORK_DIR / f"{skill}_{condition}_{trial}"
    cwd.mkdir(parents=True, exist_ok=True)
    cmd = ["claude", "-p", "--output-format", "json", "--model", SUBJECT_MODEL,
           "--tools", TOOLS, "--max-budget-usd", MAX_BUDGET_USD, *HARNESS_FLAGS]
    if condition == "with_skill":
        cmd += ["--append-system-prompt", extract_skill_body(skill)]
    out_path = RUNS_DIR / f"{skill}__{condition}__trial{trial}.json"
    spec_hash = input_spec_hash(skill, source, condition)
    if out_path.exists():
        existing = json.loads(out_path.read_text())
        if existing.get("_input_spec_sha256") == spec_hash:
            return existing
    try:
        proc = subprocess.run(cmd, input=scenario, capture_output=True, text=True, cwd=str(cwd), timeout=180)
        record = json.loads(proc.stdout.strip())
    except subprocess.TimeoutExpired:
        record = {"type": "error", "error": "timeout"}
    except json.JSONDecodeError:
        record = {"type": "error", "error": "non-json output", "stdout": proc.stdout[:2000], "stderr": proc.stderr[:2000]}
    record["_skill"] = skill
    record["_condition"] = condition
    record["_trial"] = trial
    record["_input_spec_sha256"] = spec_hash
    out_path.write_text(json.dumps(record, indent=2))
    return record


def main():
    jobs = []
    for skill, source in SAMPLE:
        for cond in ["with_skill", "without_skill"]:
            for trial in range(1, TRIALS + 1):
                jobs.append((skill, source, cond, trial))
    failures = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(run_one, *j): j for j in jobs}
        for fut in as_completed(futs):
            j = futs[fut]
            rec = fut.result()
            is_error = rec.get("type") == "error" or rec.get("is_error")
            if is_error:
                failures += 1
            print(j, "->", "ERR" if is_error else "ok", rec.get("total_cost_usd"))
    if failures:
        print(f"{failures}/{len(jobs)} job(s) recorded an error -- see the persisted "
              f"error rows in {RUNS_DIR}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
