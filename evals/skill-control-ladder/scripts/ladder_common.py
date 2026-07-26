#!/usr/bin/env python3
"""Shared definitions for the control-ladder experiment.

The existing `skill-benchmark-pilot` compares a loaded skill against a bare
prompt with nothing appended. That measures skill-versus-nothing. This module
defines the intermediate arms needed to measure skill-versus-*prompting*, which
is a different and harder question: how much of a skill's measured effect is the
specific knowledge it carries, versus the mere presence of any structured
instruction in the system prompt?

Every arm is run through the identical harness configuration (model, tool
allowlist, budget cap, isolation flags). The ONLY thing that varies between arms
is the text appended to the system prompt. That is what makes the between-arm
deltas attributable to prompt content rather than to harness differences.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
LADDER_DIR = BASE.parent
REPO_ROOT = BASE.parents[2]
SKILLS_ROOT = REPO_ROOT / "skills"

PILOT_DATA = LADDER_DIR.parent / "skill-benchmark-pilot" / "data" / "all-skills-pilot"
PILOT_RUNS = PILOT_DATA / "runs"

# Scenario pools. `v1` is the pilot's original pool, inherited unchanged so its
# 150 valid transcripts stay adoptable. `hard` is the pre-calibrated replacement
# pool for the scenarios where v1 hit the ceiling and could not measure anything.
#
# Selected by the NG_LADDER_POOL environment variable so that run/grade/analyze
# all read the same pool from one place; passing it per-script would let a run
# and its grading silently disagree about which scenarios they refer to.
POOL = os.environ.get("NG_LADDER_POOL", "v1")
_POOLS = {
    "v1": {
        "tasks": PILOT_DATA / "all_skill_tasks.json",
        "runs": LADDER_DIR / "data" / "runs",
        "graded": LADDER_DIR / "data" / "graded.json",
        "report": LADDER_DIR / "REPORT.md",
        # Only v1 shares the pilot's scenarios, so only v1 may adopt its transcripts.
        "adopt_pilot": True,
    },
    "hard": {
        "tasks": LADDER_DIR / "data" / "hard-pool" / "selected_tasks.json",
        "runs": LADDER_DIR / "data" / "hard-pool" / "runs",
        "graded": LADDER_DIR / "data" / "hard-pool" / "graded.json",
        "report": LADDER_DIR / "REPORT-hard.md",
        "adopt_pilot": False,
    },
}
if POOL not in _POOLS:
    raise SystemExit(f"unknown NG_LADDER_POOL={POOL!r}; expected one of {sorted(_POOLS)}")

_CFG = _POOLS[POOL]
TASKS_PATH = _CFG["tasks"]
TASKS = json.loads(TASKS_PATH.read_text()) if TASKS_PATH.exists() else {}
RUNS_DIR = _CFG["runs"]
GRADED_PATH = _CFG["graded"]
REPORT_PATH = _CFG["report"]
ADOPT_PILOT = _CFG["adopt_pilot"]

COMPRESSIONS_PATH = LADDER_DIR / "data" / "compressed_skills.json"

# Held identical to the skill-benchmark-pilot all-skills run so that its cached
# C0/C4 transcripts remain valid members of this ladder rather than a separate,
# non-comparable batch. Changing any of these invalidates that reuse -- the hash
# check in run_ladder.py enforces it rather than trusting this comment.
MODEL = "claude-sonnet-5"
TOOLS = "Read,Glob,Grep"
MAX_BUDGET_USD = "0.50"
HARNESS_FLAGS = ["--safe-mode", "--no-session-persistence"]
TRIALS = 3
MAX_WORKERS = 8

# The "simple prompting" bar. Deliberately strong and deliberately generic: it
# is the SAME text for all 27 skills and contains no domain vocabulary from any
# of them. A skill that cannot beat this is not carrying knowledge the model
# lacks -- it is re-deriving a general instruction to be careful, which one
# reusable sentence already supplies at a fraction of the token cost.
#
# Writing this arm weakly (e.g. "be thorough") would inflate every skill's
# measured effect, which is the exact failure this experiment exists to detect.
GENERIC_NUDGE = (
    "Before you answer, think like a careful senior reviewer accountable for the "
    "outcome. Identify what is missing, unstated, or assumed; what could go wrong "
    "and who would be affected; who needs to approve, be informed, or own the "
    "risk; and what evidence would actually back any claim you make. State the "
    "gaps, risks, and non-obvious consequences explicitly rather than leaving "
    "them implicit, and say plainly when something should not proceed as-is. "
    "Be specific and concrete rather than general."
)

ARMS = ("C0_bare", "C1_generic_nudge", "C2_description_only", "C3_compressed", "C4_full_skill")

ARM_LABELS = {
    "C0_bare": "bare prompt (nothing appended)",
    "C1_generic_nudge": "generic skill-agnostic reviewer nudge",
    "C2_description_only": "skill name + frontmatter description only",
    "C3_compressed": "skill compressed to <=5 imperative bullets",
    "C4_full_skill": "full SKILL.md body",
}

# Arms whose transcripts are byte-identical in construction to an existing
# skill-benchmark-pilot condition, and may therefore be reused instead of
# re-spent -- but only when the recorded input-spec hash still matches.
REUSABLE_FROM_PILOT = (
    {"C0_bare": "without_skill", "C4_full_skill": "with_skill"} if ADOPT_PILOT else {}
)


GRADER_MODEL = "claude-haiku-4-5-20251001"
# Bump when the grading prompt's wording changes, so a wording-only edit
# invalidates cached rows the same way a criteria or model change already does.
PROMPT_VERSION = "v1"

_GRADE_SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "meets_criteria": {"type": "string", "enum": ["YES", "PARTIAL", "NO"]},
        "quote": {"type": "string"},
    },
    "required": ["meets_criteria", "quote"],
})

# Wording frozen to match skill-benchmark-pilot/scripts/grade_pilot_all.py. Every
# consumer (final grading, candidate screening) calls THIS function rather than
# its own copy: a screening pass that graded even slightly differently from the
# final pass would select scenarios against one standard and measure them against
# another, and the resulting difficulty calibration would be meaningless.
_GRADE_PROMPT = (
    "You are grading a response against ONE specific pass criterion. "
    "Do not reward general competence, tone, or thoroughness — check ONLY whether "
    "this exact criterion is explicitly satisfied.\n\n"
    "Pass criterion:\n{criteria}\n\n"
    "Response to grade:\n---\n{text}\n---\n\n"
    "Answer YES only if the criterion is clearly and explicitly met, "
    "PARTIAL if it is hinted at but not explicit or is materially incomplete, "
    "NO if it is absent."
)


def blind_grade(criteria: str, text: str) -> dict:
    """Grade one response against one criterion. The grader is never told the
    arm, the skill, or that a comparison is running -- it sees only these two
    strings."""
    import subprocess  # local: keeps this module import-safe for non-running uses

    cmd = [
        "claude", "-p", _GRADE_PROMPT.format(criteria=criteria, text=text),
        "--output-format", "json",
        "--model", GRADER_MODEL,
        "--safe-mode",
        "--tools", "",
        "--no-session-persistence",
        "--max-budget-usd", "0.20",
        "--json-schema", _GRADE_SCHEMA,
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return json.loads(json.loads(proc.stdout.strip())["result"])
    except Exception as e:  # noqa: BLE001 -- surfaced as an ERROR verdict row
        return {"meets_criteria": "ERROR", "quote": f"{type(e).__name__}: {e}"[:200]}


def run_subject(scenario: str, appended: str, cwd: Path) -> dict:
    """One subject-model call under the ladder's fixed harness configuration."""
    import subprocess

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
        proc = subprocess.run(cmd, input=scenario, capture_output=True, text=True,
                              cwd=str(cwd), timeout=180)
        return json.loads(proc.stdout.strip())
    except subprocess.TimeoutExpired:
        return {"type": "error", "error": "timeout"}
    except Exception as e:  # noqa: BLE001
        return {"type": "error", "error": f"{type(e).__name__}: {e}"}


def read_skill(skill: str) -> str:
    return (SKILLS_ROOT / skill / "SKILL.md").read_text()


def skill_body(skill: str) -> str:
    """Body after the YAML frontmatter -- identical extraction to the pilot's,
    so a reused C4 transcript and a freshly run one are built from the same
    string."""
    parts = re.split(r"^---$", read_skill(skill), flags=re.MULTILINE)
    return "---".join(parts[2:]).strip()


def skill_frontmatter(skill: str) -> dict[str, str]:
    """Parse the single-line `key: value` frontmatter without a YAML dependency
    (the shipped package keeps zero runtime deps, and this harness follows the
    same rule so it runs on a bare checkout)."""
    parts = re.split(r"^---$", read_skill(skill), flags=re.MULTILINE)
    out: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip()
    return out


def load_compressions() -> dict[str, str]:
    if not COMPRESSIONS_PATH.exists():
        return {}
    return json.loads(COMPRESSIONS_PATH.read_text())


def append_text(skill: str, arm: str, compressions: dict[str, str] | None = None) -> str:
    """The exact string appended to the system prompt for this (skill, arm).

    Returning "" means no `--append-system-prompt` flag is passed at all, which
    is what makes C0 identical to the pilot's `without_skill` condition rather
    than merely similar to it.
    """
    if arm == "C0_bare":
        return ""
    if arm == "C1_generic_nudge":
        return GENERIC_NUDGE
    if arm == "C2_description_only":
        fm = skill_frontmatter(skill)
        return f"{fm.get('name', skill)}: {fm.get('description', '')}".strip()
    if arm == "C3_compressed":
        compressions = load_compressions() if compressions is None else compressions
        if skill not in compressions:
            raise KeyError(
                f"no compression for {skill!r}; run scripts/build_compressions.py first"
            )
        return compressions[skill]
    if arm == "C4_full_skill":
        return skill_body(skill)
    raise ValueError(f"unknown arm {arm!r}")


def pilot_spec_hash(skill: str, condition: str) -> str:
    """Reproduces run_pilot_all.py's hash formula exactly, so a cached pilot
    transcript can be verified as still-current before this experiment adopts
    it. Four skills' SKILL.md files were amended after the pilot ran; without
    this check their `with_skill` transcripts would silently enter the ladder as
    a C4 arm built from superseded skill text."""
    body = skill_body(skill) if condition == "with_skill" else ""
    return hashlib.sha256(
        f"{TASKS[skill]['scenario_prompt']}::{body}::{MODEL}::{condition}::{TOOLS}::"
        f"{MAX_BUDGET_USD}::{'::'.join(HARNESS_FLAGS)}".encode()
    ).hexdigest()


def ladder_spec_hash(skill: str, arm: str, compressions: dict[str, str] | None = None) -> str:
    """Fingerprint of everything determining a ladder call's output besides the
    model's own sampling randomness. A run file is reused only on an exact
    match, so editing a SKILL.md, a scenario, a compression, or the nudge text
    forces a fresh call rather than replaying a stale transcript."""
    return hashlib.sha256(
        f"{TASKS[skill]['scenario_prompt']}::{append_text(skill, arm, compressions)}::"
        f"{MODEL}::{arm}::{TOOLS}::{MAX_BUDGET_USD}::{'::'.join(HARNESS_FLAGS)}".encode()
    ).hexdigest()


def run_path(skill: str, arm: str, trial: int) -> Path:
    return RUNS_DIR / f"{skill}__{arm}__trial{trial}.json"


def response_text(record: dict) -> str:
    return record.get("result", "") or ""
