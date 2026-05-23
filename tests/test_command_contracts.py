from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMANDS_DIR = ROOT / "commands"
COMMANDS_INDEX = ROOT / "COMMANDS.md"
CATALOG = ROOT / "nuclear-grade.yaml"

EXPECTED_COMMANDS = {
    "ng-question.md",
    "ng-classify.md",
    "ng-new.md",
    "ng-cm-items.md",
    "ng-impact.md",
    "ng-baseline.md",
    "ng-context-pack.md",
    "ng-prove.md",
    "ng-ship-review.md",
    "ng-source-check.md",
    "ng-legal-check.md",
}

REQUIRED_SECTIONS = (
    "## Purpose",
    "## Use when",
    "## Do not use when",
    "## Inputs",
    "## Prompt text",
    "## Files created or modified",
    "## Expected outputs",
    "## Verification command",
    "## Failure modes",
    "## Legal/assurance boundary note",
)


def test_expected_command_cards_exist():
    found = {path.name for path in COMMANDS_DIR.glob("*.md")}

    assert found == EXPECTED_COMMANDS


def test_every_command_card_has_required_sections():
    for command_name in EXPECTED_COMMANDS:
        text = (COMMANDS_DIR / command_name).read_text(encoding="utf-8")

        for section in REQUIRED_SECTIONS:
            assert section in text, f"{command_name} missing {section}"

        assert "slash command" not in text.lower()
        assert "portable command prompt" in text.lower()


def test_commands_index_lists_every_command_card():
    index = COMMANDS_INDEX.read_text(encoding="utf-8")

    for command_name in EXPECTED_COMMANDS:
        assert f"commands/{command_name}" in index


def test_catalog_lists_every_command_card():
    catalog = CATALOG.read_text(encoding="utf-8")

    for command_name in EXPECTED_COMMANDS:
        assert f"  - {command_name}" in catalog
