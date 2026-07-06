#!/usr/bin/env python3
"""Run with-skill vs without-skill trials for reviewing-code-quality and save raw JSON."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPO_ROOT = BASE.parents[2]
DATA_DIR = BASE.parent / "data" / "reviewing-code-quality-pilot"
TASKS_DIR = DATA_DIR / "tasks"
RUNS_DIR = DATA_DIR / "runs"
WORK_DIR = BASE / "work"


def extract_skill_body() -> str:
    text = (REPO_ROOT / "skills" / "reviewing-code-quality" / "SKILL.md").read_text()
    parts = re.split(r"^---$", text, flags=re.MULTILINE)
    return "---".join(parts[2:]).strip()


SKILL_BODY = extract_skill_body()

TASKS = ["task1_thin_wrapper", "task2_shared_leak", "task3_clever_indirection"]
CONDITIONS = ["with_skill", "without_skill"]
TRIALS = 3
MODEL = "claude-sonnet-5"
TOOLS = ""
MAX_BUDGET_USD = "0.50"


def input_spec_hash(prompt_text: str, condition: str) -> str:
    """Fingerprint of everything that determines the subject-model call's
    output besides its own randomness: the task prompt, the skill body
    (with_skill only), the model, the condition, and the harness settings
    (--tools, --max-budget-usd) that shape what the model is even allowed to
    do. A persisted run file is only reused if this matches -- an edited
    task prompt, SKILL.md, or harness config must force a fresh call even
    if the old output file is still sitting on disk from before the change."""
    skill_body = SKILL_BODY if condition == "with_skill" else ""
    return hashlib.sha256(
        f"{prompt_text}::{skill_body}::{MODEL}::{condition}::{TOOLS}::{MAX_BUDGET_USD}".encode()
    ).hexdigest()


def run_one(task: str, condition: str, trial: int) -> dict:
    prompt_path = TASKS_DIR / f"{task}.txt"
    prompt_text = prompt_path.read_text()

    cwd = WORK_DIR / f"{task}_{condition}_{trial}"
    cwd.mkdir(parents=True, exist_ok=True)

    cmd = [
        "claude", "-p",
        "--output-format", "json",
        "--model", MODEL,
        "--safe-mode",
        "--tools", TOOLS,
        "--no-session-persistence",
        "--max-budget-usd", MAX_BUDGET_USD,
    ]
    if condition == "with_skill":
        cmd += ["--append-system-prompt", SKILL_BODY]

    out_path = RUNS_DIR / f"{task}__{condition}__trial{trial}.json"
    spec_hash = input_spec_hash(prompt_text, condition)
    if out_path.exists():
        existing = json.loads(out_path.read_text())
        if existing.get("_input_spec_sha256") == spec_hash:
            return existing

    print(f"Running {task} / {condition} / trial {trial} ...", file=sys.stderr)
    try:
        proc = subprocess.run(
            cmd, input=prompt_text, capture_output=True, text=True,
            cwd=str(cwd), timeout=180,
        )
    except subprocess.TimeoutExpired:
        record = {"type": "error", "error": "timeout", "_task": task, "_condition": condition, "_trial": trial,
                  "_input_spec_sha256": spec_hash}
        out_path.write_text(json.dumps(record, indent=2))
        return record

    stdout = proc.stdout.strip()
    try:
        record = json.loads(stdout)
    except json.JSONDecodeError:
        record = {"type": "error", "error": "non-json output", "stdout": stdout, "stderr": proc.stderr, "returncode": proc.returncode}

    record["_task"] = task
    record["_condition"] = condition
    record["_trial"] = trial
    record["_input_spec_sha256"] = spec_hash
    out_path.write_text(json.dumps(record, indent=2))
    return record


def main():
    RUNS_DIR.mkdir(exist_ok=True)
    WORK_DIR.mkdir(exist_ok=True)
    failures = 0
    total = 0
    for task in TASKS:
        for condition in CONDITIONS:
            for trial in range(1, TRIALS + 1):
                total += 1
                rec = run_one(task, condition, trial)
                if rec.get("type") == "error" or rec.get("is_error"):
                    failures += 1
    print("Done.", file=sys.stderr)
    if failures:
        print(f"{failures}/{total} job(s) recorded an error -- see the persisted "
              f"error rows in {RUNS_DIR}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
