#!/usr/bin/env python3
"""Decompose each scenario's single compound criterion into independent binary checks.

Why
---
The hard pool graded 62% PARTIAL. A compound criterion ("must state X, meaning
Y") gives the grader no clean way to score a response that does one half well
and the other poorly, so it lands on PARTIAL, every arm converges on ~0.5, and
real differences are compressed out of view. The pool's null result is therefore
uninterpretable -- not because the skills did nothing, but because the instrument
has three levels of resolution and spends most of its time in the middle one.

A rubric of independent yes/no checks fixes this at the source:
  - No PARTIAL. Each check is observable and binary.
  - Resolution goes from 3 levels to N+1, so partial credit becomes *measured*
    rather than guessed at by the grader.
  - Variance rises, which is what a paired test needs to detect anything.

This re-grades transcripts that ALREADY EXIST. No new subject-model calls are
needed, so the higher-resolution measurement costs only grading.

Contamination control, unchanged from author_scenarios.py: the author sees the
scenario, its criterion, and its planted defect -- never the SKILL.md body. The
checks must be derivable from the scenario's own ground truth, not from a
skill's checklist, or the rubric would simply re-encode the skill and guarantee
the skill wins.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from ladder_common import LADDER_DIR, MAX_WORKERS, POOL, TASKS

AUTHOR_MODEL = "claude-sonnet-5"
MIN_CHECKS, MAX_CHECKS = 4, 6
OUT_PATH = LADDER_DIR / "data" / f"rubrics-{POOL}.json"

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "checks": {
            "type": "array",
            "minItems": MIN_CHECKS,
            "maxItems": MAX_CHECKS,
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "check": {"type": "string"},
                    "weight": {"type": "string", "enum": ["core", "supporting"]},
                },
                "required": ["id", "check", "weight"],
            },
        }
    },
    "required": ["checks"],
})

INSTRUCTION = """\
You are converting one compound grading criterion into a rubric of independent \
binary checks, for grading free-text responses to the scenario below.

SCENARIO GIVEN TO THE RESPONDER:
---
{scenario}
---

THE SINGLE COMPOUND CRITERION CURRENTLY USED:
{criteria}

{defect_line}
Write {lo}-{hi} INDEPENDENT checks that together capture what a correct response \
must do. Requirements:

- Each check must be answerable YES or NO by reading the response alone, with no \
judgement about degree. If a check could reasonably be answered "partially", \
split it into two checks or make it more specific.
- Checks must be INDEPENDENT: a response can satisfy any one without satisfying \
the others. Do not restate the same requirement in different words.
- Order them from most to least central.
- Mark `weight` as "core" if failing it means the response missed the actual \
problem, and "supporting" if it is a secondary quality that a good answer would \
also have.
- At least one check must be "core". Do not make everything core.
- Phrase each check as an observable statement about the response, e.g. \
"The response states that <specific thing>." Not "The response is thorough."
- Do NOT reward general competence, tone, structure, or length.
- `id` is a short lowercase slug, unique within this rubric.
"""


def author(skill: str) -> tuple[str, list[dict]]:
    task = TASKS[skill]
    defect = task.get("_planted_defect")
    defect_line = f"THE BURIED PROBLEM THE SCENARIO CONTAINS:\n{defect}\n\n" if defect else ""
    prompt = INSTRUCTION.format(
        scenario=task["scenario_prompt"],
        criteria=task["pass_criteria"],
        defect_line=defect_line,
        lo=MIN_CHECKS,
        hi=MAX_CHECKS,
    )
    cmd = [
        "claude", "-p", prompt,
        "--output-format", "json",
        "--model", AUTHOR_MODEL,
        "--safe-mode",
        "--tools", "",
        "--no-session-persistence",
        "--max-budget-usd", "0.40",
        "--json-schema", SCHEMA,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    rec = json.loads(proc.stdout.strip())
    if rec.get("is_error"):
        raise RuntimeError(f"{skill}: author error: {str(rec.get('result'))[:200]}")
    checks = json.loads(rec["result"])["checks"]
    ids = [c["id"] for c in checks]
    if len(set(ids)) != len(ids):
        raise RuntimeError(f"{skill}: duplicate check ids {ids}")
    if not any(c["weight"] == "core" for c in checks):
        raise RuntimeError(f"{skill}: no core check")
    return skill, checks


def source_hash(skill: str) -> str:
    """Fingerprint of the inputs the rubric is derived from, so an edited
    scenario or criterion regenerates its rubric instead of silently keeping a
    rubric that no longer matches what is being graded."""
    t = TASKS[skill]
    return hashlib.sha256(
        f"{t['scenario_prompt']}::{t['pass_criteria']}".encode()
    ).hexdigest()


def main() -> int:
    if not TASKS:
        print(f"No tasks for pool {POOL!r}.", file=sys.stderr)
        return 2
    existing = json.loads(OUT_PATH.read_text()) if OUT_PATH.exists() else {}
    todo = [s for s in TASKS
            if s not in existing or existing[s].get("_source_sha256") != source_hash(s)]
    if not todo:
        print(f"All rubrics current for pool {POOL!r}.", file=sys.stderr)
        return 0

    print(f"Authoring rubrics for {len(todo)} scenario(s) in pool {POOL!r}", file=sys.stderr)
    failures = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(author, s): s for s in todo}
        for fut in as_completed(futures):
            skill = futures[fut]
            try:
                skill, checks = fut.result()
            except Exception as e:  # noqa: BLE001 -- reported, not swallowed
                failures.append(f"{skill}: {type(e).__name__}: {e}")
                continue
            existing[skill] = {"checks": checks, "_source_sha256": source_hash(skill)}
            core = sum(1 for c in checks if c["weight"] == "core")
            print(f"  ok {skill}: {len(checks)} checks ({core} core)", file=sys.stderr)

    OUT_PATH.write_text(json.dumps(dict(sorted(existing.items())), indent=2) + "\n")
    print(f"Wrote {OUT_PATH}", file=sys.stderr)
    if failures:
        for f in failures:
            print(f"  FAIL {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
