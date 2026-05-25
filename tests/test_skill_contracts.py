from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SKILLS_INDEX = ROOT / "SKILLS.md"
CATALOG = ROOT / "nuclear-grade.yaml"
SKILL_EVALUATION = ROOT / "docs" / "05-reference" / "skill-evaluation.md"

EXPECTED_SKILLS = {
    "questioning-attitude",
    "using-nuclear-grade",
    "identifying-controlled-items",
    "screening-change-impact",
    "baselining-configuration",
    "classifying-change-risk",
    "creating-change-packets",
    "packing-agent-context",
    "proving-claims",
    "reviewing-ship-readiness",
    "checking-source-lineage",
    "checking-license-and-assurance-boundaries",
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

        assert frontmatter["name"] == skill_name
        assert frontmatter["description"].startswith("Use when")
        assert len(frontmatter["description"]) >= 90
        assert len(frontmatter["description"]) <= 180
        assert " then " not in frontmatter["description"].lower()
        assert " step " not in frontmatter["description"].lower()

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
