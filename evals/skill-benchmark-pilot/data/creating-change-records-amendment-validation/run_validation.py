#!/usr/bin/env python3
import hashlib
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPO_ROOT = BASE.parents[3]
RUNS_DIR = BASE / "runs"
WORK_DIR = BASE / "work"
SKILL_PATH = REPO_ROOT / "skills" / "creating-change-records" / "SKILL.md"
GATE1_TASKS = json.loads((BASE.parent / "gate1-hard-case-pilot" / "gate1_tasks.json").read_text())
SCENARIO = GATE1_TASKS["creating-change-records"]["scenario_prompt"]
TOOLS = "Read,Glob,Grep"
MAX_BUDGET_USD = "0.30"
# Isolation/session flags that also shape what the subject model can do --
# named here (not inlined in cmd below) so the hash and the actual command
# are built from the exact same list and can never drift apart, the same
# fix already applied to TOOLS/MAX_BUDGET_USD.
HARNESS_FLAGS = ["--safe-mode", "--no-session-persistence"]
TRIALS = 3

def extract_skill_body():
    text = SKILL_PATH.read_text()
    parts = re.split(r"^---$", text, flags=re.MULTILINE)
    return "---".join(parts[2:]).strip()

def input_spec_hash(model):
    """Fingerprint of everything that determines the subject-model call's
    output besides its own randomness: the scenario prompt, the skill body,
    the model under test, and the harness settings (--tools,
    --max-budget-usd, HARNESS_FLAGS). A persisted run file is only reused
    if this matches -- an edited scenario, SKILL.md, or harness config
    must force a fresh call even if the old output file is still sitting
    on disk from before the change."""
    skill_body = extract_skill_body()
    return hashlib.sha256(
        f"{SCENARIO}::{skill_body}::{model}::{TOOLS}::{MAX_BUDGET_USD}::"
        f"{'::'.join(HARNESS_FLAGS)}".encode()
    ).hexdigest()

def run_one(model, trial):
    cwd = WORK_DIR / f"{model}_{trial}"
    cwd.mkdir(parents=True, exist_ok=True)
    cmd = ["claude", "-p", "--output-format", "json", "--model", model,
           "--tools", TOOLS, "--max-budget-usd", MAX_BUDGET_USD, *HARNESS_FLAGS,
           "--append-system-prompt", extract_skill_body()]
    out_path = RUNS_DIR / f"{model}__with_skill__trial{trial}.json"
    spec_hash = input_spec_hash(model)
    if out_path.exists():
        existing = json.loads(out_path.read_text())
        # Never treat a cached ERROR record as a hit, even with a matching
        # hash -- a transient failure must always be retried on the next
        # invocation, not replayed forever until someone manually deletes
        # the file.
        if (existing.get("_input_spec_sha256") == spec_hash
                and existing.get("type") != "error" and not existing.get("is_error")):
            return existing
    try:
        proc = subprocess.run(cmd, input=SCENARIO, capture_output=True, text=True, cwd=str(cwd), timeout=180)
        record = json.loads(proc.stdout.strip())
    except subprocess.TimeoutExpired:
        record = {"type": "error", "error": "timeout"}
    except json.JSONDecodeError:
        record = {"type": "error", "error": "non-json output", "stdout": proc.stdout[:2000], "stderr": proc.stderr[:2000]}
    record["_model"] = model
    record["_trial"] = trial
    record["_input_spec_sha256"] = spec_hash
    out_path.write_text(json.dumps(record, indent=2))
    return record

def main():
    jobs = []
    for model in ["claude-sonnet-5", "claude-haiku-4-5"]:
        for trial in range(1, TRIALS + 1):
            jobs.append((model, trial))
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
