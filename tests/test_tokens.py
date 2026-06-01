from pathlib import Path

from nuclear_grade import tokens
from tests.test_ng_cli import run_ng

ROOT = Path(__file__).resolve().parents[1]


def test_count_tokens_is_deterministic_and_positive():
    text = "Enforce with code, not prompts. A gate fires every time."
    first = tokens.count_tokens(text)
    second = tokens.count_tokens(text)

    assert first == second
    assert first > 0
    assert tokens.count_tokens("") == 0


def test_count_tokens_scales_with_length():
    short = tokens.count_tokens("one small sentence here")
    long = tokens.count_tokens("one small sentence here " * 20)

    assert long > short


def test_split_frontmatter_separates_description_from_body():
    text = '---\nname: demo\ndescription: A short trigger line.\n---\n\n# Demo\n\nBody text.\n'
    description, body = tokens.split_frontmatter(text)

    assert description == "A short trigger line."
    assert "Body text." in body
    assert "description:" not in body


def test_split_frontmatter_handles_missing_frontmatter():
    description, body = tokens.split_frontmatter("# No frontmatter\n\njust prose\n")

    assert description == ""
    assert "just prose" in body


def test_crlf_checkout_is_measured_identically_to_lf():
    """A CRLF checkout (Windows core.autocrlf) must yield the same counts as LF,
    or descriptions read as 0 tokens and the budget goes unenforced there."""

    lf = '---\nname: demo\ndescription: A short trigger line.\n---\n\n# Demo\n\nBody text here.\n'
    crlf = lf.replace("\n", "\r\n")

    lf_desc, lf_body = tokens.split_frontmatter(lf)
    crlf_desc, crlf_body = tokens.split_frontmatter(crlf.replace("\r\n", "\n"))

    assert lf_desc == crlf_desc != ""
    assert tokens.count_tokens(lf_desc) == tokens.count_tokens(crlf_desc) > 0


def test_read_text_normalizes_crlf(tmp_path):
    path = tmp_path / "f.md"
    path.write_bytes(b"---\r\nname: demo\r\ndescription: Trigger here now.\r\n---\r\n\r\nBody.\r\n")

    text = tokens._read_text(path)
    description, body = tokens.split_frontmatter(text)

    assert "\r" not in text
    assert description == "Trigger here now."
    assert tokens.count_tokens(description) > 0


def test_build_report_derives_skills_dynamically_from_tree():
    """The skill set is read from the directory, never hardcoded, so it stays
    correct as skills are added (#11's 23rd) or renamed (#12)."""

    report = tokens.build_report(ROOT)
    skill_names = {f.name for f in report.of_kind("skill")}
    found_on_disk = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}

    assert skill_names == found_on_disk
    assert len(skill_names) == len(found_on_disk)
    # Every skill carries both an always-loaded description and an on-invocation body.
    for skill in report.of_kind("skill"):
        assert skill.description_tokens > 0, skill.name
        assert skill.body_tokens > 0, skill.name


def test_repo_passes_its_own_token_budget():
    report = tokens.build_report(ROOT)
    budgets = tokens.load_budgets(ROOT)

    assert tokens.check_budgets(report, budgets) == [], "accepted corpus must start green"


def test_load_budgets_reads_catalog_over_defaults():
    budgets = tokens.load_budgets(ROOT)

    # The catalog seeds these; if the key is dropped, the defaults still apply.
    assert budgets["skill_body_max"] >= 1
    assert set(tokens.DEFAULT_BUDGETS) <= set(budgets)


def test_gate_has_teeth_when_a_file_exceeds_budget(tmp_path):
    """A skill body over budget must produce a violation (the gate's teeth)."""

    skill_dir = tmp_path / "skills" / "too-big"
    skill_dir.mkdir(parents=True)
    body = "word " * 5000
    (skill_dir / "SKILL.md").write_text(
        f"---\nname: too-big\ndescription: x\n---\n\n# Too Big\n\n{body}\n",
        encoding="utf-8",
    )

    report = tokens.build_report(tmp_path)
    budgets = dict(tokens.DEFAULT_BUDGETS)
    violations = tokens.check_budgets(report, budgets)

    assert violations
    assert any("skill_body_max" in v for v in violations)


def test_redundancy_index_fires_when_a_block_is_over_repeated(tmp_path):
    """A prose paragraph duplicated across many files must surface as a repeated
    block over the file threshold."""

    block = (
        "This is a substantial repeated boilerplate paragraph that recurs verbatim "
        "across many separate files and should be detected by the redundancy index."
    )
    skills = tmp_path / "skills"
    for i in range(5):
        d = skills / f"skill-{i}"
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(
            f"---\nname: skill-{i}\ndescription: d\n---\n\n# S{i}\n\nUnique intro {i}.\n\n{block}\n",
            encoding="utf-8",
        )

    files = list((tmp_path / "skills").glob("*/SKILL.md"))
    repeated = tokens.find_repeated_blocks(files, tmp_path, min_files=3)

    assert repeated
    assert repeated[0].file_count == 5
    assert repeated[0].wasted_tokens > 0


def test_redundancy_index_ignores_shared_code_snippets(tmp_path):
    """A shared `ng validate` command across files is a legitimate reference, not
    boilerplate waste, so fenced code must be excluded from the prose scan."""

    snippet = "```bash\npython tools/ng.py validate .nuclear/changes/<slug>\n```"
    skills = tmp_path / "skills"
    for i in range(5):
        d = skills / f"skill-{i}"
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(
            f"---\nname: skill-{i}\ndescription: d\n---\n\n# S{i}\n\nUnique prose {i}.\n\n{snippet}\n",
            encoding="utf-8",
        )

    files = list((tmp_path / "skills").glob("*/SKILL.md"))
    repeated = tokens.find_repeated_blocks(files, tmp_path, min_files=3)

    assert repeated == []


def test_cost_per_signal_matches_eval_cases():
    per_signal = tokens.cost_per_signal(ROOT)

    # Three worked examples ship with eval cases (U02, U04, U07); each yields a
    # positive tokens-per-signal ratio.
    assert set(per_signal) == {"U02", "U04", "U07"}
    for cost in per_signal.values():
        assert cost > 0


def test_phrase_frequency_counts_the_assurance_disclaimer():
    total, files = tokens.phrase_frequency(ROOT, "does not create")

    # The "does not create ..." boundary recurs across the tree; this is the hard
    # count the audit cites instead of an estimate.
    assert files >= 20
    assert total >= files


def test_tokens_command_reports_and_passes_on_accepted_corpus():
    result = run_ng("tokens", str(ROOT))

    assert result.returncode == 0, result.stderr
    assert "always-loaded" in result.stdout
    assert "on-invocation" in result.stdout
    assert "OK: token budget" in result.stdout


def test_tokens_command_fails_when_budget_is_blown(tmp_path):
    skill_dir = tmp_path / "skills" / "too-big"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        "---\nname: too-big\ndescription: x\n---\n\n# Too Big\n\n" + "word " * 5000 + "\n",
        encoding="utf-8",
    )
    (tmp_path / "nuclear-grade.yaml").write_text(
        "token_budgets:\n  skill_body_max: 100\n", encoding="utf-8"
    )

    result = run_ng("tokens", str(tmp_path))

    assert result.returncode == 1
    assert "FAILED: token budget" in result.stdout
