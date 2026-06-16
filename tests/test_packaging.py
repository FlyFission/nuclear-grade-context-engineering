import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _config() -> dict:
    return tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))


def test_console_entry_point_uses_namespaced_package():
    config = _config()

    assert config["project"]["scripts"]["nuclear-grade"] == "nuclear_grade.cli:main"


def test_build_backend_is_hatchling():
    config = _config()

    assert config["build-system"]["build-backend"] == "hatchling.build"


def test_wheel_force_includes_top_level_resources():
    config = _config()

    force_include = config["tool"]["hatch"]["build"]["targets"]["wheel"]["force-include"]
    assert force_include["templates"] == "nuclear_grade/_bundled/templates"
    assert force_include["skills"] == "nuclear_grade/_bundled/skills"
    assert force_include["commands"] == "nuclear_grade/_bundled/commands"


def test_wheel_packages_only_namespaced_package():
    config = _config()

    packages = config["tool"]["hatch"]["build"]["targets"]["wheel"]["packages"]
    assert packages == ["nuclear_grade"]


def test_version_is_stamped():
    config = _config()

    assert config["project"]["version"] == "0.6.0"


def _version_line(rel_path: str) -> str:
    text = (ROOT / rel_path).read_text(encoding="utf-8")
    line = next(line for line in text.splitlines() if line.startswith("version:"))
    return line.split(":", 1)[1].strip().strip('"')


def test_all_version_mirrors_track_pyproject():
    # pyproject is the source of truth; guard every mirror so a bump can't drift
    # one of them (this caught nuclear-grade.yaml and CITATION.cff lagging once).
    expected = _config()["project"]["version"]
    assert _version_line("nuclear-grade.yaml") == expected, "nuclear-grade.yaml version out of sync"
    assert _version_line("CITATION.cff") == expected, "CITATION.cff version out of sync"
