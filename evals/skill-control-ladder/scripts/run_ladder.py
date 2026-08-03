#!/usr/bin/env python3
"""Run every (skill, arm, trial) cell of the control ladder.

Usage:
    python run_ladder.py                 # all arms, all skills
    python run_ladder.py --arms C1_generic_nudge C4_full_skill
    python run_ladder.py --skills questioning-attitude proving-claims
    python run_ladder.py --dry-run       # print the plan and estimated cost only

Cost control: C0 and C4 transcripts already exist in the skill-benchmark-pilot
data directory. Where their recorded input-spec hash still matches the current
scenario and SKILL.md, they are adopted here instead of re-spent. Where it does
not -- four skills were amended after the pilot ran -- they are re-run, because
adopting them would put superseded skill text into the C4 arm.
"""

from __future__ import annotations

import argparse
import json
import random
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from ladder_common import (
    ARMS,
    HARNESS_FLAGS,
    MAX_BUDGET_USD,
    MAX_WORKERS,
    MODEL,
    PILOT_RUNS,
    REPO_ROOT,
    REUSABLE_FROM_PILOT,
    RUNS_DIR,
    TASKS,
    TOOLS,
    TRIALS,
    append_text,
    ladder_spec_hash,
    load_compressions,
    pilot_spec_hash,
    run_path,
)

WORK_DIR = RUNS_DIR.parent / "work"
MEAN_COST_USD = 0.0436  # observed mean of the 162 existing pilot calls
SHUFFLE_SEED = 20260803  # fixed so the interleaved execution order is reproducible


def try_adopt_pilot(skill: str, arm: str, trial: int, spec_hash: str) -> dict | None:
    """Adopt an existing pilot transcript for C0/C4 when it is provably current.

    Returns None when there is nothing valid to adopt, which sends the cell to a
    live call. The hash compared here is the PILOT's formula, not the ladder's --
    the two differ by construction (the ladder's includes the arm id), so the
    pilot file's own recorded hash is the only sound thing to check it against.
    """
    condition = REUSABLE_FROM_PILOT.get(arm)
    if condition is None:
        return None
    src = PILOT_RUNS / f"{skill}__{condition}__trial{trial}.json"
    if not src.exists():
        return None
    try:
        rec = json.loads(src.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    if rec.get("type") == "error" or rec.get("is_error"):
        return None
    if rec.get("_input_spec_sha256") != pilot_spec_hash(skill, condition):
        return None  # stale: SKILL.md or scenario changed since the pilot ran
    rec["_skill"] = skill
    rec["_arm"] = arm
    rec["_trial"] = trial
    rec["_input_spec_sha256"] = spec_hash
    rec["_reused_from"] = str(src.relative_to(REPO_ROOT))
    return rec


def run_one(skill: str, arm: str, trial: int, compressions: dict[str, str]) -> dict:
    out_path = run_path(skill, arm, trial)
    spec_hash = ladder_spec_hash(skill, arm, compressions)

    if out_path.exists():
        try:
            existing = json.loads(out_path.read_text())
        except (json.JSONDecodeError, OSError):
            existing = {}
        # A cached ERROR row is never a hit: a transient timeout or proxy hiccup
        # must be retried on the next invocation, not replayed forever.
        if (existing.get("_input_spec_sha256") == spec_hash
                and existing.get("type") != "error" and not existing.get("is_error")):
            return existing

    adopted = try_adopt_pilot(skill, arm, trial, spec_hash)
    if adopted is not None:
        out_path.write_text(json.dumps(adopted, indent=2))
        return adopted

    appended = append_text(skill, arm, compressions)
    cwd = WORK_DIR / f"{skill}_{arm}_{trial}"
    cwd.mkdir(parents=True, exist_ok=True)

    cmd = [
        "claude", "-p",
        "--output-format", "json",
        "--model", MODEL,
        "--tools", TOOLS,
        "--max-budget-usd", MAX_BUDGET_USD,
        *HARNESS_FLAGS,
    ]
    if appended:
        cmd += ["--append-system-prompt", appended]

    try:
        proc = subprocess.run(
            cmd, input=TASKS[skill]["scenario_prompt"], capture_output=True,
            text=True, cwd=str(cwd), timeout=180,
        )
        record = json.loads(proc.stdout.strip())
    except subprocess.TimeoutExpired:
        record = {"type": "error", "error": "timeout"}
    except json.JSONDecodeError:
        record = {"type": "error", "error": "non-json output",
                  "stdout": proc.stdout[:2000], "stderr": proc.stderr[:2000]}
    except Exception as e:  # noqa: BLE001 -- persisted as a row, not swallowed
        record = {"type": "error", "error": f"{type(e).__name__}: {e}"}

    record["_skill"] = skill
    record["_arm"] = arm
    record["_trial"] = trial
    record["_input_spec_sha256"] = spec_hash
    out_path.write_text(json.dumps(record, indent=2))
    return record


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arms", nargs="*", default=list(ARMS), choices=list(ARMS))
    ap.add_argument("--skills", nargs="*", default=sorted(TASKS))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    unknown = sorted(set(args.skills) - set(TASKS))
    if unknown:
        print(f"No scenario defined for: {', '.join(unknown)}", file=sys.stderr)
        return 2

    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    compressions = load_compressions()
    if "C3_compressed" in args.arms:
        missing = sorted(set(args.skills) - set(compressions))
        if missing:
            print(f"C3 requested but no compression for: {', '.join(missing)}\n"
                  f"Run scripts/build_compressions.py first.", file=sys.stderr)
            return 2

    jobs = [(s, a, t) for s in args.skills for a in args.arms for t in range(1, TRIALS + 1)]
    # Seeded shuffle so arms are interleaved across the batch rather than executed
    # in per-skill blocks. If the serving backend drifts mid-run, block execution
    # would alias that drift onto whichever arm happened to run first; shuffling
    # spreads it across all arms instead. Seeded so the order is reproducible.
    random.Random(SHUFFLE_SEED).shuffle(jobs)

    if args.dry_run:
        cached = adoptable = fresh = 0
        for skill, arm, trial in jobs:
            spec_hash = ladder_spec_hash(skill, arm, compressions)
            p = run_path(skill, arm, trial)
            if p.exists() and json.loads(p.read_text()).get("_input_spec_sha256") == spec_hash:
                cached += 1
            elif try_adopt_pilot(skill, arm, trial, spec_hash) is not None:
                adoptable += 1
            else:
                fresh += 1
        print(f"cells={len(jobs)} cached={cached} adoptable_from_pilot={adoptable} "
              f"live_calls={fresh}")
        print(f"estimated new spend: ${fresh * MEAN_COST_USD:.2f} "
              f"(at the ${MEAN_COST_USD:.4f} mean of the 162 existing pilot calls)")
        return 0

    print(f"Total cells: {len(jobs)}", file=sys.stderr)
    done = failures = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(run_one, s, a, t, compressions): (s, a, t) for s, a, t in jobs}
        for fut in as_completed(futures):
            job = futures[fut]
            done += 1
            try:
                rec = fut.result()
                is_error = rec.get("type") == "error" or rec.get("is_error")
            except Exception as e:  # noqa: BLE001
                is_error, rec = True, {"error": str(e)}
            failures += bool(is_error)
            tag = "ERR" if is_error else ("reused" if rec.get("_reused_from") else "ok")
            print(f"[{done}/{len(jobs)}] {job} -> {tag}", file=sys.stderr)

    if failures:
        print(f"{failures}/{len(jobs)} cell(s) recorded an error -- see {RUNS_DIR}",
              file=sys.stderr)
        return 1
    print("Done.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
