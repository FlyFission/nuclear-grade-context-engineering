"""The policy's glob matcher must stay identical to the PreToolUse gate's copy."""

import importlib.util
import json
from pathlib import Path

import pytest

from nuclear_grade.globmatch import glob_regex, match_any

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("ng_pre_tool_use_globs", ROOT / "hooks" / "pre_tool_use.py")
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)


def _policy_globs() -> list[str]:
    path = ROOT / ".nuclear" / "consequence-policy.json"
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [g for rule in data.get("rules", []) for g in (*rule.get("paths", []), *rule.get("exclude", []))]


@pytest.mark.parametrize("glob", [*gate.DENY_PATHS, *_policy_globs(), "**", "*.md", "docs/**.md",
                                  "docs/**/*.md", "a?c", "x.y", "[ab]", "~/.claude/**"])
def test_glob_regex_matches_the_gate_copy(glob):
    assert glob_regex(glob).pattern == gate._glob_regex(glob).pattern
    assert glob_regex(glob).flags == gate._glob_regex(glob).flags


def test_double_star_crosses_directories_and_single_star_does_not():
    assert match_any("docs/x.md", ["docs/**.md"]) == ["docs/**.md"]
    assert match_any("docs/a/b.md", ["docs/**.md"]) == ["docs/**.md"]
    assert match_any("docs/x.md", ["docs/**/*.md"]) == []  # the documented gotcha
    assert match_any("docs/a/b.md", ["docs/*.md"]) == []
    assert match_any("HOOKS/Gate.py", ["hooks/**"]) == ["hooks/**"]  # case-insensitive
