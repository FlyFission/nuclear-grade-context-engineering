#!/usr/bin/env python3
"""Blind-grade every ladder transcript against its skill's pre-registered criterion.

Deliberately identical in grader model, prompt wording, and criterion text to
`skill-benchmark-pilot/scripts/grade_pilot_all.py`. That is the point: if the
ladder's grading differed at all, a C1-versus-C4 gap could be an artifact of
grading rather than of the arms, and the adopted C0/C4 transcripts could not be
pooled with the newly run ones.

Blinding: the grader sees the response text and the criterion only. It is never
told the arm, the skill name, or that a comparison is being run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from ladder_common import (
    ARMS,
    GRADED_PATH,
    MAX_WORKERS,
    TASKS,
    TRIALS,
    response_text,
    run_path,
)

GRADER_MODEL = "claude-haiku-4-5-20251001"
# Bump when the grading prompt's wording changes, so a wording-only edit
# invalidates cached rows the same way a criteria or model change already does.
PROMPT_VERSION = "v1"

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "meets_criteria": {"type": "string", "enum": ["YES", "PARTIAL", "NO"]},
        "quote": {"type": "string"},
    },
    "required": ["meets_criteria", "quote"],
})


def grading_spec_hash(skill: str) -> str:
    return hashlib.sha256(
        f"{TASKS[skill]['pass_criteria']}::{GRADER_MODEL}::{PROMPT_VERSION}".encode()
    ).hexdigest()


def grade(skill: str, text: str) -> dict:
    prompt = (
        "You are grading a response against ONE specific pass criterion. "
        "Do not reward general competence, tone, or thoroughness — check ONLY whether "
        "this exact criterion is explicitly satisfied.\n\n"
        f"Pass criterion:\n{TASKS[skill]['pass_criteria']}\n\n"
        f"Response to grade:\n---\n{text}\n---\n\n"
        "Answer YES only if the criterion is clearly and explicitly met, "
        "PARTIAL if it is hinted at but not explicit or is materially incomplete, "
        "NO if it is absent."
    )
    cmd = [
        "claude", "-p", prompt,
        "--output-format", "json",
        "--model", GRADER_MODEL,
        "--safe-mode",
        "--tools", "",
        "--no-session-persistence",
        "--max-budget-usd", "0.20",
        "--json-schema", SCHEMA,
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return json.loads(json.loads(proc.stdout.strip())["result"])
    except Exception as e:  # noqa: BLE001 -- surfaced as an ERROR verdict row
        return {"meets_criteria": "ERROR", "quote": f"{type(e).__name__}: {e}"[:200]}


def load_cache() -> dict:
    """Prior verdicts keyed by (skill, arm, trial).

    A row is reused only when BOTH the transcript's content hash and the grading
    inputs' hash still match, so neither a re-run transcript nor an edited
    criterion can silently keep an old verdict.
    """
    if not GRADED_PATH.exists():
        return {}
    try:
        rows = json.loads(GRADED_PATH.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    return {
        (r["skill"], r["arm"], r["trial"]): r
        for r in rows
        if r.get("verdict") != "ERROR" and r.get("_source_sha256") and r.get("_criteria_sha256")
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arms", nargs="*", default=list(ARMS), choices=list(ARMS))
    args = ap.parse_args()

    cache = load_cache()
    jobs, rows = [], []
    incomplete = []

    for skill in sorted(TASKS):
        for arm in args.arms:
            for trial in range(1, TRIALS + 1):
                p = run_path(skill, arm, trial)
                if not p.exists():
                    incomplete.append(f"{skill}/{arm}/trial{trial}: missing run file")
                    continue
                rec = json.loads(p.read_text())
                if rec.get("type") == "error" or rec.get("is_error"):
                    incomplete.append(f"{skill}/{arm}/trial{trial}: run recorded an error")
                    continue
                text = response_text(rec)
                src_hash = hashlib.sha256(text.encode()).hexdigest()
                crit_hash = grading_spec_hash(skill)
                hit = cache.get((skill, arm, trial))
                if (hit and hit["_source_sha256"] == src_hash
                        and hit["_criteria_sha256"] == crit_hash):
                    rows.append(hit)
                else:
                    jobs.append((skill, arm, trial, text, src_hash, crit_hash, rec))

    # Refuse to overwrite the checked-in results file from a partial batch:
    # every downstream statistic derives its denominator from this file, and a
    # truncated batch is indistinguishable from a complete one after the fact.
    if incomplete:
        print(f"Refusing to grade: {len(incomplete)} incomplete cell(s).", file=sys.stderr)
        for line in incomplete[:20]:
            print(f"  {line}", file=sys.stderr)
        if len(incomplete) > 20:
            print(f"  ... and {len(incomplete) - 20} more", file=sys.stderr)
        return 2

    print(f"cached={len(rows)} to_grade={len(jobs)}", file=sys.stderr)
    done = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {
            ex.submit(grade, j[0], j[3]): j for j in jobs
        }
        for fut in as_completed(futures):
            skill, arm, trial, _text, src_hash, crit_hash, rec = futures[fut]
            verdict = fut.result()
            done += 1
            rows.append({
                "skill": skill,
                "arm": arm,
                "trial": trial,
                "verdict": verdict.get("meets_criteria", "ERROR"),
                "quote": verdict.get("quote", ""),
                "cost_usd": rec.get("total_cost_usd"),
                "output_tokens": (rec.get("usage") or {}).get("output_tokens"),
                "input_tokens": (rec.get("usage") or {}).get("input_tokens"),
                "duration_api_ms": rec.get("duration_api_ms"),
                "_source_sha256": src_hash,
                "_criteria_sha256": crit_hash,
            })
            print(f"[{done}/{len(jobs)}] {skill}/{arm}/t{trial} -> "
                  f"{verdict.get('meets_criteria')}", file=sys.stderr)

    errors = [r for r in rows if r["verdict"] == "ERROR"]
    rows.sort(key=lambda r: (r["skill"], r["arm"], r["trial"]))
    GRADED_PATH.write_text(json.dumps(rows, indent=2) + "\n")
    print(f"Wrote {len(rows)} rows to {GRADED_PATH}", file=sys.stderr)
    if errors:
        print(f"{len(errors)} grading error(s) recorded", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
