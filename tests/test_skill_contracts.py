import re
from pathlib import Path

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
    "identifying-controlled-items",
    "screening-change-impact",
    "baselining-configuration",
    "classifying-change-risk",
    "creating-change-packets",
    "packing-agent-context",
    "turning-over-agent-work",
    "self-checking-agent-actions",
    "proving-claims",
    "reviewing-ship-readiness",
    "learning-from-opex",
    "checking-dependency-and-model-trust",
    "checking-source-lineage",
    "checking-license-and-assurance-boundaries",
    "controlling-mission-drift",
    "reviewing-code-quality",
    "red-teaming-agent-changes",
    "tracing-agent-execution",
    "decomposing-work-breakdown",
    "structuring-agentic-folders",
}

REQUIRED_SECTIONS = (
    "## Overview",
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
