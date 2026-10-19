"""Tool runner for the toy file agent.

Every tool call goes through ``ToolRunner.run``, which enforces
``app/agent_config.json``:

- a tool must be listed in ``allowed_tools`` and registered in ``TOOLS``;
- a tool that needs the network runs only when ``network`` is true;
- file paths must stay inside the configured ``workspace`` folder.

Other code constructs ``ToolRunner(config, root)``, calls ``run(name, **kwargs)``,
and catches ``ToolDenied``. Keep that interface compatible.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG = APP_DIR / "agent_config.json"


class ToolDenied(Exception):
    """Raised when a tool call is outside what the config allows."""


@dataclass(frozen=True)
class Tool:
    handler: Callable[..., object]
    needs_network: bool = False


def load_config(path: Path = DEFAULT_CONFIG) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


class ToolRunner:
    def __init__(self, config: dict, root: Path | None = None) -> None:
        self.config = config
        self.root = Path(root) if root is not None else APP_DIR.parent
        self.workspace = (self.root / config["workspace"]).resolve()

    def run(self, name: str, **kwargs: object) -> object:
        if name not in self.config.get("allowed_tools", []):
            raise ToolDenied(f"tool not allowed by config: {name}")
        tool = TOOLS.get(name)
        if tool is None:
            raise ToolDenied(f"unknown tool: {name}")
        if tool.needs_network and self.config.get("network") is not True:
            raise ToolDenied(f"tool needs network access and network is off: {name}")
        return tool.handler(self, **kwargs)

    def resolve(self, relative: str) -> Path:
        target = (self.workspace / relative).resolve()
        if not target.is_relative_to(self.workspace):
            raise ToolDenied(f"path escapes the workspace: {relative}")
        return target


def _read_file(runner: ToolRunner, path: str) -> str:
    return runner.resolve(path).read_text(encoding="utf-8")


def _write_file(runner: ToolRunner, path: str, content: str) -> int:
    target = runner.resolve(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return len(content)


TOOLS: dict[str, Tool] = {
    "read_file": Tool(_read_file),
    "write_file": Tool(_write_file),
}
