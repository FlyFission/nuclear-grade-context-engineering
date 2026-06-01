from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PUBLIC_DOCS = (
    "README.md",
    "INSTALL.md",
    "QUICKSTART.md",
    "WORKFLOWS.md",
    "COMMANDS.md",
    "SKILLS.md",
    "EXAMPLES.md",
    "ROADMAP.md",
    "SUPPORT.md",
    "GOVERNANCE.md",
    "AGENTS.md",
    "CORE.md",
    "MAXIMS.md",
)

UNSAFE_RESIDUE = (
    "/" "mnt/",
    "/" "home/flyfission",
    "Her" "mes",
    "public" " push",
    "local" " uncommitted",
)

BOUNDARY_PHRASES = (
    "NQA-1 evidence",
    "NQA-1 record",
    "formal V&V",
    "formal verification and validation",
    "certified quality assurance program",
    "regulatory approval",
    "commercial-grade dedication package",
)

NEGATIVE_CONTEXT = (
    "not ",
    "no ",
    "does not ",
    "do not ",
    "without ",
    "never ",
)


def test_public_top_level_docs_exist():
    for public_doc in PUBLIC_DOCS:
        assert (ROOT / public_doc).exists(), f"missing {public_doc}"


def test_public_docs_contain_no_internal_residue():
    for public_doc in PUBLIC_DOCS:
        text = (ROOT / public_doc).read_text(encoding="utf-8")
        for unsafe in UNSAFE_RESIDUE:
            assert unsafe not in text, f"{public_doc} contains {unsafe}"


def test_boundary_phrases_are_only_used_in_negative_context():
    for public_doc in PUBLIC_DOCS:
        text = (ROOT / public_doc).read_text(encoding="utf-8")
        for line in text.splitlines():
            lowered = line.lower()
            for phrase in BOUNDARY_PHRASES:
                if phrase.lower() in lowered:
                    assert any(marker in lowered for marker in NEGATIVE_CONTEXT), (
                        f"{public_doc} has unbounded phrase: {line}"
                    )


def test_docs_readme_has_action_first_map():
    text = (ROOT / "docs" / "README.md").read_text(encoding="utf-8")

    assert "## Use the repo" in text
    assert "## Reference foundation" in text


def test_public_lifecycle_uses_questioning_attitude_golden_path():
    text = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn" in text


def test_baseline_is_late_lifecycle_state():
    text = (ROOT / "docs" / "02-operating-system" / "lifecycle.md").read_text(encoding="utf-8")

    assert "Decide -> Baseline -> Operate -> Learn" in text


def test_hpi_overlay_is_public_operating_doc():
    text = (
        ROOT / "docs" / "02-operating-system" / "hpi-overlays.md"
    ).read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "HPI for AI agents" in text
    assert "turn over cleanly" in text
    assert "No compliance claim is made" in text
    assert "HPI for AI agents" in readme


def test_golden_path_includes_hpi_microtool_templates():
    templates = ROOT / "templates" / "golden-path"

    assert (templates / "turnover.md").exists()
    assert (templates / "self-check.md").exists()


def test_skill_workflow_comparison_covers_catalog():
    comparison = (
        ROOT / "docs" / "03-worked-examples" / "skill-workflow-comparison" / "results-summary.md"
    ).read_text(encoding="utf-8")
    catalog = (ROOT / "nuclear-grade.yaml").read_text(encoding="utf-8")

    skills_section = catalog.split("skills:", 1)[1].split("commands:", 1)[0]
    skills = [
        line.strip().removeprefix("- ").strip()
        for line in skills_section.splitlines()
        if line.strip().startswith("- ")
    ]

    for skill in skills:
        assert f"`{skill}`" in comparison, f"comparison missing skill {skill}"
        skill_line = next(line for line in comparison.splitlines() if f"`{skill}`" in line)
        assert skill_line.count("U") >= 2, f"comparison must exercise {skill} in multiple trials"


def test_skill_workflow_comparison_covers_workflows():
    comparison = (
        ROOT / "docs" / "03-worked-examples" / "skill-workflow-comparison" / "results-summary.md"
    ).read_text(encoding="utf-8")

    workflows = (
        "Questioning attitude",
        "Quick change",
        "Standard change",
        "Controlled configuration",
        "Agent authority change",
        "Release readiness",
        "Source/legal check",
    )

    for workflow in workflows:
        assert workflow in comparison, f"comparison missing workflow {workflow}"
        workflow_line = next(line for line in comparison.splitlines() if f"| {workflow} |" in line)
        assert workflow_line.count("U") >= 2, f"comparison must exercise {workflow} in multiple trials"


def test_skill_workflow_comparison_has_inspectable_trial_records():
    trial_dir = ROOT / "docs" / "03-worked-examples" / "skill-workflow-comparison" / "trial-records"
    trials = sorted(trial_dir.glob("*.md"))

    assert len(trials) >= 12

    required_sections = (
        "## Scenario Facts",
        "## Simple Prompt Trial",
        "## Nuclear-Grade Trial",
        "## Scoring Rationale",
        "## Decision",
        "## Boundary Note",
    )

    for trial in trials:
        text = trial.read_text(encoding="utf-8")
        for section in required_sections:
            assert section in text, f"{trial.name} missing {section}"


def test_skill_workflow_comparison_scores_both_paths_for_each_trial():
    summary = (
        ROOT / "docs" / "03-worked-examples" / "skill-workflow-comparison" / "results-summary.md"
    ).read_text(encoding="utf-8")

    for index in range(1, 13):
        trial_id = f"U{index:02d}"
        simple_rows = [
            line for line in summary.splitlines()
            if line.startswith(f"| {trial_id} ") and "| Simple prompt |" in line
        ]
        nuclear_rows = [
            line for line in summary.splitlines()
            if line.startswith(f"| {trial_id} ") and "| Nuclear-grade |" in line
        ]
        assert simple_rows, f"missing simple-prompt score row for {trial_id}"
        assert nuclear_rows, f"missing Nuclear-grade score row for {trial_id}"
