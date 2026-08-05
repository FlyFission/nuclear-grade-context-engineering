import json
from pathlib import Path

import pytest

from nuclear_grade.skill_catalog import (
    CatalogError,
    load_catalog,
    load_yaml_projections,
)

ROOT = Path(__file__).resolve().parents[1]


def _write_skill(root: Path, name: str, bucket: str = "skills") -> str:
    rel = f"{bucket}/{name}/SKILL.md"
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\nname: {name}\ndescription: demo\n---\n\n# Demo\n", encoding="utf-8")
    return rel


def _write_catalog(root: Path, entries: list[dict]) -> None:
    (root / "skill-catalog.json").write_text(
        json.dumps({"schema_version": 1, "skills": entries}, indent=2) + "\n",
        encoding="utf-8",
    )


def test_repository_catalog_is_complete_and_matches_compatibility_projections():
    catalog = load_catalog(ROOT)
    projected_skills, projected_commands = load_yaml_projections(ROOT)

    assert len(catalog.entries) == 29
    assert {entry.id for entry in catalog.promoted} == set(projected_skills)
    assert catalog.command_map == projected_commands
    assert {entry.id for entry in catalog.model_routable} == {entry.id for entry in catalog.promoted}
    assert all(entry.status == "promoted" for entry in catalog.entries)
    assert len(catalog.profile("core")) == 8
    assert catalog.profile("core")[0].id == "using-nuclear-grade"


def test_catalog_rejects_beta_skill_in_plugin_discoverable_promoted_path(tmp_path):
    rel = _write_skill(tmp_path, "candidate")
    _write_catalog(
        tmp_path,
        [
            {
                "id": "candidate",
                "path": rel,
                "status": "beta",
                "invocation": "model",
                "role": "discipline",
                "command": None,
            }
        ],
    )

    with pytest.raises(CatalogError, match="beta.*skills/"):
        load_catalog(tmp_path)


def test_catalog_rejects_deprecated_skill_without_replacement(tmp_path):
    rel = _write_skill(tmp_path, "old", "skills-deprecated")
    _write_catalog(
        tmp_path,
        [
            {
                "id": "old",
                "path": rel,
                "status": "deprecated",
                "invocation": "user",
                "role": "reference",
                "command": None,
            }
        ],
    )

    with pytest.raises(CatalogError, match="replacement"):
        load_catalog(tmp_path)


def test_catalog_rejects_duplicate_ids_and_commands(tmp_path):
    first = _write_skill(tmp_path, "one")
    second = _write_skill(tmp_path, "two")
    _write_catalog(
        tmp_path,
        [
            {
                "id": "one",
                "path": first,
                "status": "promoted",
                "invocation": "both",
                "role": "discipline",
                "command": "ng-same",
            },
            {
                "id": "one",
                "path": second,
                "status": "promoted",
                "invocation": "both",
                "role": "discipline",
                "command": "ng-same",
            },
        ],
    )

    with pytest.raises(CatalogError, match="duplicate skill id"):
        load_catalog(tmp_path)


def test_catalog_rejects_unknown_enum_and_missing_skill_path(tmp_path):
    _write_catalog(
        tmp_path,
        [
            {
                "id": "missing",
                "path": "skills/missing/SKILL.md",
                "status": "production",
                "invocation": "automatic",
                "role": "helper",
                "command": None,
            }
        ],
    )

    with pytest.raises(CatalogError) as exc:
        load_catalog(tmp_path)

    message = str(exc.value)
    assert "invalid status" in message
    assert "invalid invocation" in message
    assert "invalid role" in message
    assert "missing skill file" in message


def test_catalog_rejects_promoted_folder_not_registered(tmp_path):
    rel = _write_skill(tmp_path, "registered")
    _write_skill(tmp_path, "orphan")
    _write_catalog(
        tmp_path,
        [
            {
                "id": "registered",
                "path": rel,
                "status": "promoted",
                "invocation": "model",
                "role": "discipline",
                "command": None,
            }
        ],
    )

    with pytest.raises(CatalogError, match="unregistered promoted skill folder.*orphan"):
        load_catalog(tmp_path)
