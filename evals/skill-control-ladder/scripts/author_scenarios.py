#!/usr/bin/env python3
"""Author candidate replacement scenarios for the skills whose v1 scenario ceilinged.

Why this exists
---------------
13 of the 27 v1 scenarios score 1.00 under BOTH the generic control (C1) and the
full skill (C4). Those scenarios cannot measure anything: a difference may well
exist and the instrument cannot see it. Replacing them is the only way to learn
whether those 13 skills beat prompting, and it is the pre-calibration gap the
pilot's own `STATISTICAL_ANALYSIS.md` identified and left open.

Contamination controls
----------------------
The author sees the skill's NAME and frontmatter DESCRIPTION only -- never the
SKILL.md body. This matters: v1's pass criteria were written by the same effort
that wrote the skills, so they tended to restate the skills' own checklists,
which measures instruction-following rather than knowledge. An author blind to
the body has to write the criterion from the scenario's own ground truth
instead.

This is a real improvement over v1 but NOT full independence -- the description
still describes the skill, and one agent writes both scenario and criterion. The
honest claim is "less contaminated than v1," not "clean."

Difficulty is not assumed here, only attempted. `screen_scenarios.py` measures
each candidate against the live C1 control and keeps only the ones that actually
discriminate; candidates that ceiling again are discarded on evidence.
"""

from __future__ import annotations

import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from ladder_common import LADDER_DIR, MAX_WORKERS, skill_frontmatter

AUTHOR_MODEL = "claude-sonnet-5"
CANDIDATES_PER_SKILL = 3
OUT_DIR = LADDER_DIR / "data" / "hard-pool"
CANDIDATES_PATH = OUT_DIR / "candidates.json"

# The 13 skills whose v1 scenario scored 1.00 on both C1 and C4. Hardcoded from
# the v1 analysis rather than recomputed, so this list is auditable against
# REPORT.md and cannot drift silently if graded.json is later regenerated.
CEILING_SKILLS = [
    "briefing-an-agent",
    "checking-legal-and-safety-wording",
    "checking-release-readiness",
    "checking-what-a-change-affects",
    "creating-change-records",
    "deciding-who-decides",
    "proving-claims",
    "questioning-attitude",
    "rating-change-risk",
    "recording-what-an-agent-did",
    "responding-to-incidents",
    "stress-testing-agent-changes",
    "vetting-outside-code-and-models",
]

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "candidates": {
            "type": "array",
            "minItems": CANDIDATES_PER_SKILL,
            "maxItems": CANDIDATES_PER_SKILL,
            "items": {
                "type": "object",
                "properties": {
                    "scenario_prompt": {"type": "string"},
                    "pass_criteria": {"type": "string"},
                    "planted_defect": {"type": "string"},
                },
                "required": ["scenario_prompt", "pass_criteria", "planted_defect"],
            },
        }
    },
    "required": ["candidates"],
})

INSTRUCTION = """\
You are writing evaluation scenarios for a benchmark that measures whether a \
strong AI assistant catches a specific non-obvious problem in a realistic \
software-engineering situation.

The topic area is described by this label:

  {name}: {description}

Write {k} DIFFERENT candidate scenarios in this topic area. Each candidate has \
three parts.

1. `scenario_prompt` — a realistic message from an engineer or manager asking \
for help. Requirements, all of which matter:
   - The surface must look REASSURING. Include concrete details that make \
proceeding feel safe: green CI, a teammate's sign-off, "it's a small change", \
a deadline, prior success with something similar.
   - Bury exactly ONE specific, consequential problem in the details. It must \
be genuinely non-obvious — findable only by reasoning about the specifics, not \
by pattern-matching a scary keyword.
   - The naive-but-competent answer must be to go ahead. A strong generalist \
who is merely being careful should have a real chance of missing it.
   - Do NOT use vocabulary that telegraphs the problem. No "risk", "unsafe", \
"compliance", "verify", "rollback", "audit", or similar alarm words in the \
prompt itself. Write how a real person would write.
   - 80–200 words. No headings or bullet lists — a plain message.

2. `pass_criteria` — one sentence stating exactly what a response must \
EXPLICITLY do to pass, phrased so a grader reading only the response can decide \
yes or no. Tie it to catching the specific planted problem and its consequence. \
Do not reward general thoroughness, tone, or structure.

3. `planted_defect` — one sentence naming the buried problem, for human review.

Make the {k} candidates differ in situation and in the KIND of problem, not just \
in surface wording. Difficulty is the point: a scenario every careful reader \
passes is worthless here.
"""


def author(skill: str) -> tuple[str, list[dict]]:
    fm = skill_frontmatter(skill)
    prompt = INSTRUCTION.format(
        name=fm.get("name", skill),
        description=fm.get("description", ""),
        k=CANDIDATES_PER_SKILL,
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
        raise RuntimeError(f"{skill}: author returned an error record: {rec.get('result')}")
    cands = json.loads(rec["result"])["candidates"]
    if len(cands) != CANDIDATES_PER_SKILL:
        raise RuntimeError(f"{skill}: expected {CANDIDATES_PER_SKILL} candidates")
    return skill, cands


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    existing = json.loads(CANDIDATES_PATH.read_text()) if CANDIDATES_PATH.exists() else {}
    todo = [s for s in CEILING_SKILLS if s not in existing]
    if not todo:
        print("All candidates already authored.", file=sys.stderr)
        return 0

    print(f"Authoring {CANDIDATES_PER_SKILL} candidates for {len(todo)} skill(s)",
          file=sys.stderr)
    failures = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(author, s): s for s in todo}
        for fut in as_completed(futures):
            skill = futures[fut]
            try:
                skill, cands = fut.result()
            except Exception as e:  # noqa: BLE001 -- reported, not swallowed
                failures.append(f"{skill}: {type(e).__name__}: {e}")
                continue
            existing[skill] = cands
            print(f"  ok {skill}", file=sys.stderr)

    CANDIDATES_PATH.write_text(json.dumps(dict(sorted(existing.items())), indent=2) + "\n")
    print(f"Wrote {CANDIDATES_PATH}", file=sys.stderr)
    if failures:
        for f in failures:
            print(f"  FAIL {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
