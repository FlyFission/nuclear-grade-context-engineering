import re
from pathlib import Path

from nuclear_grade.cli import (
    DECISION_CONTRACT_LABELS,
    DECISION_TIER_PATTERN,
    DECISION_TIERS,
)

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SKILLS_INDEX = ROOT / "SKILLS.md"
CATALOG = ROOT / "nuclear-grade.yaml"
SKILL_EVALUATION = ROOT / "docs" / "05-reference" / "skill-evaluation.md"

# Frontmatter contract: name + description are required; license and compatibility
# are optional supported fields (Anthropic skill-creator convention).
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "compatibility"}
# Name format: lowercase, hyphen-separated, starts with a letter, no consecutive
# or trailing dashes. No length cap (existing names exceed 32 chars).
SKILL_NAME_PATTERN = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")

EXPECTED_SKILLS = {
    "questioning-attitude",
    "using-nuclear-grade",
    "choosing-what-to-control",
    "checking-what-a-change-affects",
    "recording-a-known-good-version",
    "rating-change-risk",
    "creating-change-records",
    "briefing-an-agent",
    "handing-off-work",
    "double-checking-before-acting",
    "proving-claims",
    "checking-release-readiness",
    "learning-from-experience",
    "vetting-outside-code-and-models",
    "checking-source-claims",
    "checking-legal-and-safety-wording",
    "staying-on-mission",
    "reviewing-code-quality",
    "stress-testing-agent-changes",
    "recording-what-an-agent-did",
    "breaking-down-the-work",
    "organizing-project-folders",
    "closing-stale-packets",
    "deciding-who-decides",
    "declaring-intent",
    "responding-to-incidents",
    "tracking-deficiencies",
}

REQUIRED_SECTIONS = (
    "## Overview",
    "## Decision contract",
    "## When to Use",
    "## When Not to Use",
    "## Inputs",
    "## Process",
    "## Outputs",
    "## Verification",
    "## Escalation",
    "## Common Rationalizations",
    "## Red Flags",
    "## Source-lineage note",
)


def read_frontmatter(text: str) -> dict[str, str]:
    assert text.startswith("---\n")
    end = text.index("\n---", 4)
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def test_expected_skill_folders_exist():
    found = {path.name for path in SKILLS_DIR.iterdir() if path.is_dir()}

    assert found == EXPECTED_SKILLS


def test_every_skill_has_valid_agent_operable_contract():
    for skill_name in EXPECTED_SKILLS:
        skill_file = SKILLS_DIR / skill_name / "SKILL.md"
        text = skill_file.read_text(encoding="utf-8")
        frontmatter = read_frontmatter(text)

        assert {"name", "description"} <= set(frontmatter) <= ALLOWED_FRONTMATTER_KEYS
        assert frontmatter["name"] == skill_name
        assert SKILL_NAME_PATTERN.match(skill_name), f"{skill_name} is not a valid skill name"

        description = frontmatter["description"]
        lowered = description.lower()
        # Rich, high-triggering descriptions: what it does, when to trigger, and an
        # explicit negative clause. No fixed-prefix mandate; generous length band.
        assert 80 <= len(description) <= 500, f"{skill_name} description length {len(description)}"
        # An explicit negative clause sharpens triggering and curbs over-triggering.
        assert any(
            marker in lowered for marker in ("do not use", "not for", "skip when", "avoid when")
        ), f"{skill_name} description must include a negative clause (e.g. 'Do not use for ...')"
        # Single-line YAML scalar safety: no colon-space, which strict loaders misparse.
        assert ": " not in description, f"{skill_name} description must not contain a colon-space"
        assert len(text.splitlines()) <= 500

        for section in REQUIRED_SECTIONS:
            assert section in text, f"{skill_name} missing {section}"


def test_every_skill_declares_a_decision_contract():
    """Charter Art. 11: name the decision the evidence must support. Every skill is a
    control in that loop, so it must emit -- in a compact receipt -- the claim checked,
    the artifact observed, the decision affected (with a block/warn/observe tier), the
    failure class, and the next action. The lint checks the receipt is present and
    well-formed, not that the named decision is the honest one (that is human
    judgment). See docs/05-reference/skill-authoring-contract.md."""
    for skill_name in EXPECTED_SKILLS:
        text = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")

        assert "## Decision contract" in text, f"{skill_name} missing decision contract"
        for label in DECISION_CONTRACT_LABELS:
            assert label in text, f"{skill_name} decision contract missing {label}"
        match = DECISION_TIER_PATTERN.search(text)
        assert match, (
            f"{skill_name} decision affected must start with one of {DECISION_TIERS}"
        )
        assert match.group(1).lower() in DECISION_TIERS


def test_skills_index_lists_every_skill_folder():
    index = SKILLS_INDEX.read_text(encoding="utf-8")

    for skill_name in EXPECTED_SKILLS:
        assert f"skills/{skill_name}/SKILL.md" in index


def test_catalog_lists_every_skill_folder():
    catalog = CATALOG.read_text(encoding="utf-8")

    for skill_name in EXPECTED_SKILLS:
        assert f"  - {skill_name}" in catalog


def test_skill_evaluation_prompts_cover_every_skill():
    evaluation = SKILL_EVALUATION.read_text(encoding="utf-8")

    for skill_name in EXPECTED_SKILLS:
        heading = f"### `{skill_name}`"
        assert heading in evaluation
        block = evaluation.split(heading, 1)[1].split("\n### `", 1)[0]
        assert block.count("Should trigger:") >= 3
        assert block.count("Should not trigger:") >= 2


def test_using_nuclear_grade_forces_classification_and_trip_wire():
    """The router must force a spoken risk classification (a declaration of intent)
    and MUST-promote the cheap 'it's only small' traps; guard that directive
    behavior against silent regression. See
    .nuclear/changes/directive-dispatcher-skill/."""
    # Case-insensitive so a capitalization tweak does not fail the contract,
    # while the classify-first move and the trip-wire must stay present.
    text = (SKILLS_DIR / "using-nuclear-grade" / "SKILL.md").read_text(encoding="utf-8").lower()

    assert "classify first" in text, "router must lead with a mandatory classification"
    assert "declaration of intent" in text, "classification is a declaration, not a permission request"
    assert "standard-plus" in text and "must" in text, "router must MUST-promote, not merely suggest"

    traps = ("authentication", "dependency manifest", "model id", ".github/", "public wording", "migration")
    missing = [trap for trap in traps if trap not in text]
    assert len(traps) - len(missing) >= 5, f"dispatcher trip-wire missing traps: {missing}"
