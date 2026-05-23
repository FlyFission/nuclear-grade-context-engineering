import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_console_entry_point_uses_namespaced_package():
    config = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert config["project"]["scripts"]["nuclear-grade"] == "nuclear_grade.cli:main"


def test_package_discovery_is_explicitly_scoped():
    config = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    packages = config["tool"]["setuptools"]["packages"]["find"]
    assert packages["include"] == ["nuclear_grade*"]
    assert "skills*" in packages["exclude"]
    assert "commands*" in packages["exclude"]
    assert "templates*" in packages["exclude"]
