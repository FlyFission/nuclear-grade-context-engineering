from pathlib import Path

from nuclear_grade.cli import OPTIONAL_FILES

ROOT = Path(__file__).resolve().parents[1]
COMMANDS_DIR = ROOT / "commands"
COMMANDS_INDEX = ROOT / "COMMANDS.md"
CATALOG = ROOT / "nuclear-grade.yaml"

EXPECTED_COMMANDS = {
    "ng-question.md",
    "ng-classify.md",
    "ng-new.md",
    "ng-what-to-control.md",
    "ng-impact.md",
    "ng-baseline.md",
    "ng-context-pack.md",
    "ng-turnover.md",
    "ng-self-check.md",
    "ng-prove.md",
    "ng-ship-review.md",
    "ng-learn.md",
    "ng-trust-check.md",
    "ng-source-check.md",
    "ng-legal-check.md",
    "ng-drift-check.md",
    "ng-code-review.md",
    "ng-red-team.md",
    "ng-trace.md",
    "ng-breakdown.md",
    "ng-folders.md",
    "ng-close-packet.md",
    "ng-decide-authority.md",
    "ng-intent.md",
    "ng-incident.md",
    "ng-deficiency.md",
}

# Command cards are generated from their skills (nuclear_grade/gen_commands.py),
# so the card is a thin projection: five sections sourced from the skill, plus a
# generation lead and a pointer back to the skill for everything else. This is an
# independent copy of the public contract -- if the generator's section set
# changes, this guard should fail until the contract is reviewed.
REQUIRED_SECTIONS = (
    "## Use when",
    "## Do not use when",
    "## Inputs",
    "## Prompt text",
    "## Verification",
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


def test_catalog_optional_templates_match_cli():
    """The CLI's OPTIONAL_FILES tuple and the catalog's templates.optional list
    are two copies of one fact. Guard them so an optional template added to the
    catalog (but not the tuple) cannot silently drop out of `ng list`/`ng doctor`.
    """
    optional: list[str] = []
    in_block = False
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        if line.startswith("  optional:"):
            in_block = True
            continue
        if in_block:
            if line.lstrip().startswith("- "):
                optional.append(line.split("- ", 1)[1].strip())
            elif line.strip() and not line.startswith("    "):
                break

    assert optional, "could not parse templates.optional from nuclear-grade.yaml"
    assert set(optional) == set(OPTIONAL_FILES)
