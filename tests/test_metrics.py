from pathlib import Path

from nuclear_grade.metrics import GENERATED_COMMAND_MARKER, build_inventory
from tests.test_ng_cli import ROOT, run_ng


def _write(path: Path, text: str = "# x\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_build_inventory_counts_a_synthetic_repo(tmp_path):
    # 2 skills, 3 commands, 3 template files across 2 modes, 2 root docs, 1 docs page.
    _write(tmp_path / "skills" / "alpha" / "SKILL.md", "---\nname: alpha\n---\n# Alpha\n")
    _write(tmp_path / "skills" / "beta" / "SKILL.md", "---\nname: beta\n---\n# Beta\n")
    for name in ("a", "b", "c"):
        _write(tmp_path / "commands" / f"ng-{name}.md")
    _write(tmp_path / "templates" / "quick" / "risk.md")
    _write(tmp_path / "templates" / "quick" / "proof.md")
    _write(tmp_path / "templates" / "standard" / "risk.md")
    _write(tmp_path / "README.md")
    _write(tmp_path / "CORE.md")
    _write(tmp_path / "docs" / "guide.md")

    inv = build_inventory(tmp_path)

    assert inv.skills == 2
    assert inv.commands == 3
    # The synthetic command files carry no generation marker, so they count as
    # hand-authored: the authored surface is all 5 objects.
    assert inv.generated_commands == 0
    assert inv.template_files == 3
    assert inv.template_modes == 2
    assert inv.root_docs == 2
    assert inv.docs_tree == 1
    assert inv.authored_surface == 5
    assert inv.commands_per_skill == 1.5
    # 2 SKILL.md + 3 commands + 3 templates + 2 root + 1 docs page.
    assert inv.markdown_total == 11


def test_inventory_matches_the_filesystem_on_this_repo():
    # No magic numbers: the inventory must equal an independent recount of the tree,
    # so the test stays correct as the teardown intentionally changes the counts.
    inv = build_inventory(ROOT)

    assert inv.skills == len(list((ROOT / "skills").glob("*/SKILL.md")))
    assert inv.commands == len(list((ROOT / "commands").glob("*.md")))
    assert inv.root_docs == len(list(ROOT.glob("*.md")))
    assert inv.skills > 0 and inv.commands > 0
    # Independent recount of generated cards (no magic numbers): a command is
    # generated when it carries the marker `ng gen-commands` writes.
    generated = sum(
        1
        for path in (ROOT / "commands").glob("*.md")
        if GENERATED_COMMAND_MARKER in path.read_text(encoding="utf-8")
    )
    assert inv.generated_commands == generated
    assert inv.authored_surface == inv.skills + inv.commands - inv.generated_commands
    # The teardown's headline: every command is now generated, so the only
    # hand-maintained skill/command objects left are the skills themselves.
    assert inv.generated_commands == inv.commands
    assert inv.authored_surface == inv.skills


def test_metrics_cli_runs_on_this_repo():
    result = run_ng("metrics", str(ROOT))

    assert result.returncode == 0, result.stderr
    assert "part inventory" in result.stdout
    assert "authored skill/command surface" in result.stdout
    assert "total markdown files" in result.stdout
