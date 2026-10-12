import json
import shutil
from pathlib import Path

from nuclear_grade.release import MANIFESTS, check_release, main

ROOT = Path(__file__).resolve().parents[1]
FILES = ("pyproject.toml", "CITATION.cff", "CHANGELOG.md", *MANIFESTS)


def copy_identity(tmp_path: Path) -> Path:
    for name in FILES:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    return tmp_path


def test_repository_release_identity_is_consistent():
    assert check_release(ROOT) == []


def test_tag_must_match_version(tmp_path):
    repo = copy_identity(tmp_path)
    assert any("tag" in problem for problem in check_release(repo, "v9.9.9"))
    assert main(["--repo", str(repo), "--tag", "v9.9.9"]) == 1


def test_manifest_drift_is_caught(tmp_path):
    repo = copy_identity(tmp_path)
    manifest = repo / MANIFESTS[0]
    data = json.loads(manifest.read_text(encoding="utf-8"))
    data["version"] = "0.0.1"
    manifest.write_text(json.dumps(data), encoding="utf-8")

    assert any(MANIFESTS[0] in problem for problem in check_release(repo))


def test_missing_changelog_section_and_date_mismatch_are_caught(tmp_path):
    repo = copy_identity(tmp_path)
    citation = repo / "CITATION.cff"
    citation.write_text(
        citation.read_text(encoding="utf-8").replace("date-released:", "date-released: \"1999-01-01\"\n#"),
        encoding="utf-8",
    )
    assert any("date-released" in problem for problem in check_release(repo))

    (repo / "CHANGELOG.md").write_text("# Changelog\n\n## [Unreleased]\n", encoding="utf-8")
    assert any("no dated" in problem for problem in check_release(repo))


def test_release_workflow_refuses_tags_off_the_default_branch():
    """Review finding: a tag on an unmerged commit would build and publish unreviewed code."""
    workflow = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
    ancestry = workflow.index("git merge-base --is-ancestor")
    assert "fetch-depth: 0" in workflow
    assert ancestry < workflow.index("python -m build")
    assert ancestry < workflow.index("python -m nuclear_grade.release --tag")


def test_pypi_publishes_only_after_the_github_release():
    """Review finding: pypi and github-release both needed only build, so they ran in parallel."""
    import yaml

    jobs = yaml.safe_load((ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8"))["jobs"]
    assert "github-release" in jobs["pypi"]["needs"]
