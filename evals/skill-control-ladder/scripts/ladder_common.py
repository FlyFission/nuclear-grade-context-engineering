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
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
LADDER_DIR = BASE.parent
REPO_ROOT = BASE.parents[2]
SKILLS_ROOT = REPO_ROOT / "skills"

PILOT_DATA = LADDER_DIR.parent / "skill-benchmark-pilot" / "data" / "all-skills-pilot"
PILOT_RUNS = PILOT_DATA / "runs"
TASKS = json.loads((PILOT_DATA / "all_skill_tasks.json").read_text())

RUNS_DIR = LADDER_DIR / "data" / "runs"
COMPRESSIONS_PATH = LADDER_DIR / "data" / "compressed_skills.json"
GRADED_PATH = LADDER_DIR / "data" / "graded.json"

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
REUSABLE_FROM_PILOT = {"C0_bare": "without_skill", "C4_full_skill": "with_skill"}


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
