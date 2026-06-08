from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "agents"

# The PROVE pipeline: planner -> runner -> observer -> judge -> educator.
EXPECTED = {"planner", "runner", "observer", "judge", "educator"}


def _frontmatter(text: str) -> dict[str, str]:
    assert text.startswith("---\n"), "agent file needs YAML frontmatter"
    end = text.index("\n---", 4)
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def _tools(name: str) -> set[str]:
    fm = _frontmatter((AGENTS / f"{name}.md").read_text(encoding="utf-8"))
    return {t.strip() for t in fm.get("tools", "").split(",") if t.strip()}


def test_pipeline_agents_exist():
    found = {p.stem for p in AGENTS.glob("*.md") if p.stem != "README"}
    assert found == EXPECTED


def test_agent_frontmatter_is_valid():
    for name in EXPECTED:
        fm = _frontmatter((AGENTS / f"{name}.md").read_text(encoding="utf-8"))
        assert fm.get("name") == name, f"{name}.md name must match the filename"
        assert fm.get("description"), f"{name}.md needs a description"
        assert "tools" in fm, f"{name}.md must declare its tool authority"


def test_authority_split_is_encoded_in_tools():
    tools = {name: _tools(name) for name in EXPECTED}
    # Read-only verdict stage: cannot edit, write, or shell out.
    assert not ({"Bash", "Edit", "Write"} & tools["judge"]), "judge must be read-only"
    # Planner is read-only over product code (no Bash, no Edit); it may Write the packet.
    assert "Bash" not in tools["planner"] and "Edit" not in tools["planner"]
    # Observer gathers evidence (Bash) but cannot write product code.
    assert "Bash" in tools["observer"]
    assert "Edit" not in tools["observer"] and "Write" not in tools["observer"]
    # Runner is the only stage with build authority.
    assert {"Edit", "Write", "Bash"} <= tools["runner"]
    # Planner writes only the change packet: it must keep Write but never gets Bash/Edit.
    assert "Write" in tools["planner"], "planner needs Write to author the change packet"
    # Educator records baseline/lessons into .nuclear/ (Write) but runs no commands.
    assert "Write" in tools["educator"], "educator needs Write to record the baseline/lessons"
    assert "Bash" not in tools["educator"], "educator must not run commands"


def test_readme_carries_the_honesty_caveat():
    readme = (AGENTS / "README.md").read_text(encoding="utf-8")
    assert "permissionMode" in readme, "must document the plugin permissionMode limit (F6)"
    assert ".claude/agents/" in readme, "must point to where real confinement lives"
    assert "not a perimeter" in readme.lower()
