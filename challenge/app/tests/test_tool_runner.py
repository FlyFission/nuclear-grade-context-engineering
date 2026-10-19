from pathlib import Path

import pytest
from app import tool_runner
from app.tool_runner import Tool, ToolDenied, ToolRunner, load_config

BASE_CONFIG = {"allowed_tools": ["read_file", "write_file"], "network": False, "workspace": "workspace"}


@pytest.fixture
def runner(tmp_path: Path) -> ToolRunner:
    (tmp_path / "workspace").mkdir()
    (tmp_path / "workspace" / "hello.txt").write_text("hi", encoding="utf-8")
    return ToolRunner(dict(BASE_CONFIG), root=tmp_path)


def test_read_file_inside_workspace(runner):
    assert runner.run("read_file", path="hello.txt") == "hi"


def test_write_file_inside_workspace(runner):
    runner.run("write_file", path="out/new.txt", content="data")
    assert (runner.workspace / "out" / "new.txt").read_text(encoding="utf-8") == "data"


def test_write_outside_workspace_is_denied(runner):
    with pytest.raises(ToolDenied):
        runner.run("write_file", path="../escape.txt", content="nope")


def test_tool_missing_from_config_is_denied(tmp_path):
    (tmp_path / "workspace").mkdir()
    read_only = ToolRunner({**BASE_CONFIG, "allowed_tools": ["read_file"]}, root=tmp_path)
    with pytest.raises(ToolDenied):
        read_only.run("write_file", path="x.txt", content="x")


def test_unregistered_tool_is_denied_even_if_configured(tmp_path):
    (tmp_path / "workspace").mkdir()
    loose = ToolRunner({**BASE_CONFIG, "allowed_tools": ["read_file", "shell"]}, root=tmp_path)
    with pytest.raises(ToolDenied):
        loose.run("shell", command="ls")


def test_network_tool_needs_network_switch(tmp_path, monkeypatch):
    (tmp_path / "workspace").mkdir()
    monkeypatch.setitem(tool_runner.TOOLS, "ping", Tool(lambda runner: "pong", needs_network=True))
    config = {**BASE_CONFIG, "allowed_tools": ["ping"]}
    with pytest.raises(ToolDenied):
        ToolRunner({**config, "network": False}, root=tmp_path).run("ping")
    assert ToolRunner({**config, "network": True}, root=tmp_path).run("ping") == "pong"


def test_shipped_config_only_lists_registered_tools():
    config = load_config()
    assert set(config["allowed_tools"]) <= set(tool_runner.TOOLS)
    assert config["workspace"] == "workspace"
