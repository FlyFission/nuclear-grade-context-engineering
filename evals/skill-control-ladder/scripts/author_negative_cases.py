#!/usr/bin/env python3
"""Author false-positive scenarios: cases where each skill should NOT fire.

Why this is the missing term
----------------------------
Every measurement in this project so far is a trigger case, where firing the
skill is the right behavior. That measures benefit only. The failure mode that
actually degrades a skill library in production is the opposite one: the skill
fires on a trivial change and turns a one-line answer into a process ceremony.
A library can score well on every trigger case and still be net-negative in
daily use if it over-fires, and nothing here would have detected that.

Why the exclusions are a fair standard
--------------------------------------
The scenarios are not adversarial inventions. Every skill's frontmatter
`description` ends with its own "Do not use for ..." clause -- all 27 declare
one. This suite places each skill squarely inside the territory it declares out
of scope and checks whether it respects its own contract. Failing that is a
defect by the skill's own definition, not by a standard imposed here.

Scoring direction is INVERTED relative to the other pools
---------------------------------------------------------
Checks are phrased so that "met" means the response stayed proportionate to a
small task. So on this pool a HIGHER score is better behavior, and the finding
of interest is C4 scoring BELOW C1: that is the full skill causing unwarranted
ceremony that a generic careful-reviewer prompt did not.

Contamination control, unchanged: the author sees the skill's name and
description -- which is where the exclusion is declared, so it must be visible --
but never the SKILL.md body.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from ladder_common import LADDER_DIR, MAX_WORKERS, SKILLS_ROOT, skill_frontmatter

AUTHOR_MODEL = "claude-sonnet-5"
OUT_DIR = LADDER_DIR / "data" / "negative-pool"
TASKS_PATH = OUT_DIR / "selected_tasks.json"
RUBRICS_PATH = LADDER_DIR / "data" / "rubrics-negative.json"

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "scenario_prompt": {"type": "string"},
        "why_excluded": {"type": "string"},
        "checks": {
            "type": "array",
            "minItems": 4,
            "maxItems": 5,
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "check": {"type": "string"},
                    "weight": {"type": "string", "enum": ["core", "supporting"]},
                },
                "required": ["id", "check", "weight"],
            },
        },
    },
    "required": ["scenario_prompt", "why_excluded", "checks"],
})

INSTRUCTION = """\
You are writing a NEGATIVE test case for an AI assistant evaluation.

A reusable instruction document ("skill") exists for this topic area:

  {name}: {description}

Note the part of that description declaring when the skill should NOT be used:

  "{exclusion}"

Write ONE realistic scenario that falls SQUARELY inside that excluded territory \
-- a situation where invoking this skill's process would be disproportionate, \
and the right response is simply to help directly and briefly.

`scenario_prompt` requirements:
- A realistic short message from an engineer asking for help with something \
genuinely small, low-stakes, and easily reversible.
- It must be unambiguous that heavy process is not warranted. Do not smuggle in \
hidden stakes, production data, security implications, or irreversibility -- \
this is a genuine easy case, not a trap.
- Do not mention the skill, process, rigor, or ceremony. Write how a real \
person would write. 40-120 words, plain message, no headings.

`why_excluded`: one sentence on why this sits in the declared exclusion.

`checks`: 4-5 independent binary checks, each answerable YES/NO from the \
response alone. Phrase every check so that TRUE means the assistant behaved \
PROPORTIONATELY. For example:
- "The response directly answers the question / does the small thing asked."
- "The response does NOT require a formal written record, packet, or template \
before proceeding."
- "The response does NOT demand a separate human approval or sign-off for this \
change."
- "The response does NOT ask the user to complete a multi-step process before \
getting an answer."
Mark at least one "core". Do not reward tone, structure, or length. Judge only \
proportionality and whether the actual question was answered.
- `id` is a short unique lowercase slug.
"""


def exclusion_of(description: str) -> str | None:
    m = re.search(r"(Do not use[^.]*\.)", description)
    return m.group(1) if m else None


def author(skill: str) -> tuple[str, dict]:
    fm = skill_frontmatter(skill)
    description = fm.get("description", "")
    exclusion = exclusion_of(description)
    if not exclusion:
        raise RuntimeError(f"{skill}: no 'Do not use' clause to build a negative case from")
    prompt = INSTRUCTION.format(
        name=fm.get("name", skill), description=description, exclusion=exclusion
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
    out = json.loads(rec["result"])
    ids = [c["id"] for c in out["checks"]]
    if len(set(ids)) != len(ids):
        raise RuntimeError(f"{skill}: duplicate check ids {ids}")
    if not any(c["weight"] == "core" for c in out["checks"]):
        raise RuntimeError(f"{skill}: no core check")
    out["_exclusion"] = exclusion
    return skill, out


def main() -> int:
    skills = sorted(p.parent.name for p in SKILLS_ROOT.glob("*/SKILL.md"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tasks = json.loads(TASKS_PATH.read_text()) if TASKS_PATH.exists() else {}
    rubrics = json.loads(RUBRICS_PATH.read_text()) if RUBRICS_PATH.exists() else {}

    todo = [s for s in skills if s not in tasks and exclusion_of(
        skill_frontmatter(s).get("description", ""))]
    skipped = [s for s in skills
               if not exclusion_of(skill_frontmatter(s).get("description", ""))]
    if skipped:
        print(f"No exclusion declared, skipped: {', '.join(skipped)}", file=sys.stderr)
    if not todo:
        print("All negative cases authored.", file=sys.stderr)
        return 0

    print(f"Authoring negative cases for {len(todo)} skill(s)", file=sys.stderr)
    failures = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(author, s): s for s in todo}
        for fut in as_completed(futures):
            skill = futures[fut]
            try:
                skill, out = fut.result()
            except Exception as e:  # noqa: BLE001 -- reported, not swallowed
                failures.append(f"{skill}: {type(e).__name__}: {e}")
                continue
            tasks[skill] = {
                "scenario_prompt": out["scenario_prompt"],
                # Kept so grade_ladder.py (verdict path) still has a criterion,
                # though the rubric is the intended scoring route for this pool.
                "pass_criteria": (
                    "The response helps directly and proportionately with this small, "
                    "low-stakes request, without requiring a formal record, template, "
                    "separate approval, or multi-step process first."
                ),
                "_why_excluded": out["why_excluded"],
                "_exclusion": out["_exclusion"],
            }
            rubrics[skill] = {"checks": out["checks"], "_source_sha256": "negative-pool"}
            print(f"  ok {skill}: {len(out['checks'])} checks", file=sys.stderr)

    TASKS_PATH.write_text(json.dumps(dict(sorted(tasks.items())), indent=2) + "\n")
    RUBRICS_PATH.write_text(json.dumps(dict(sorted(rubrics.items())), indent=2) + "\n")
    print(f"Wrote {TASKS_PATH} and {RUBRICS_PATH}", file=sys.stderr)
    if failures:
        for f in failures:
            print(f"  FAIL {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
