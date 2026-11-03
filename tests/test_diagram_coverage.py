"""The skill figures must show every skill in the catalog.

The skill map silently fell behind the catalog once (it showed 22 of 31 skills).
These checks keep the catalog figure and the full skill map in step with
``nuclear-grade.yaml``, so a skill cannot be added, merged, or removed without
the pictures that explain the skills following it.
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _catalog_skills() -> set[str]:
    text = (ROOT / "nuclear-grade.yaml").read_text(encoding="utf-8")
    section = text.split("skills:", 1)[1].split("commands:", 1)[0]
    return {line.strip()[2:].strip() for line in section.splitlines() if line.strip().startswith("- ")}


def _diagrams():
    spec = importlib.util.spec_from_file_location("ng_build_diagrams", ROOT / "tools" / "build_diagrams.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_catalog_figure_lists_every_skill_once():
    families = _diagrams().SKILL_FAMILIES
    names = [name for _, skills in families for name, _ in skills]
    assert len(names) == len(set(names)), "a skill appears in two families"
    assert set(names) == _catalog_skills()


def test_full_skill_map_shows_every_skill():
    module = _diagrams()
    on_map = {"using-nuclear-grade", "questioning-attitude", "rating-change-risk", "creating-change-records",
              "proving-claims", "checking-release-readiness", "controlling-approved-versions",
              "learning-from-experience", "checking-what-a-change-affects"}
    for chains in module.FULL_OVERLAYS.values():
        for chain in chains:
            on_map.update(label for label, _ in chain)
    assert on_map == _catalog_skills()
    svg = (ROOT / "docs" / "assets" / "diagrams" / "skill-map.svg").read_text(encoding="utf-8")
    shown = set(re.findall(r">([a-z]+(?:-[a-z]+)+)</text>", svg))
    assert _catalog_skills() <= shown, f"rebuild diagrams: missing {sorted(_catalog_skills() - shown)}"
