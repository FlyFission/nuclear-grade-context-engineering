#!/usr/bin/env python3
"""Run every installed coding agent on both tracks of the challenge, then rebuild the results.

    python challenge-results/run-all.py --trials 5
    python challenge-results/run-all.py --agents claude-code,opencode --trials 5 --model claude-code=<model-id>

For each agent in agents.json whose CLI is on PATH (or each one named with --agents),
this runs `run.py` on the task-only track and the house-rules track, the same number
of trials each, then runs `build.py` so RESULTS.md, the scoreboard page and the badge
match the run files. Agents whose CLI is missing are listed and skipped.

Run it inside a throwaway container or VM: the agent commands in agents.json let the
agent act without asking, and the scorer runs code the agent wrote. Stdlib only.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from run import TRACKS, load_agents  # noqa: E402


def installed(entry: dict) -> bool:
    return shutil.which(entry["command"][0]) is not None


def parse_models(values: list[str]) -> dict[str, str]:
    models: dict[str, str] = {}
    for value in values:
        agent, sep, model = value.partition("=")
        if not sep or not agent or not model:
            raise SystemExit(f"--model takes agent=model-id, got {value!r}")
        models[agent] = model
    return models


def plan(agents: dict[str, dict], wanted: list[str] | None) -> tuple[list[str], list[str]]:
    """Return (agents to run, agents skipped because their CLI is missing)."""

    if wanted:
        unknown = [name for name in wanted if name not in agents]
        if unknown:
            raise SystemExit(f"unknown agent(s): {', '.join(unknown)}; known: {', '.join(sorted(agents))}")
        names = wanted
    else:
        names = sorted(agents)
    run = [name for name in names if installed(agents[name])]
    skipped = [name for name in names if name not in run]
    return run, skipped


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run every installed agent on both challenge tracks.")
    parser.add_argument("--agents", default="", help="comma-separated agent ids (default: every installed one)")
    parser.add_argument("--model", action="append", default=[], help="agent=model-id, repeatable")
    parser.add_argument("--trials", type=int, default=5, help="runs per agent per track (default 5)")
    parser.add_argument("--timeout", type=int, default=1800, help="seconds per run before it is stopped")
    parser.add_argument("--agents-file", type=Path, default=HERE / "agents.json")
    parser.add_argument("--dry-run", action="store_true", help="show what would run, then stop")
    args = parser.parse_args(argv)
    agents = load_agents(args.agents_file)
    wanted = [name.strip() for name in args.agents.split(",") if name.strip()] or None
    models = parse_models(args.model)
    to_run, skipped = plan(agents, wanted)
    for name in skipped:
        print(f"skip {name}: `{agents[name]['command'][0]}` is not on PATH")
    if not to_run:
        print("no installed agents to run")
        return 1
    for name in to_run:
        for track in TRACKS:
            command = [
                sys.executable, str(HERE / "run.py"), "--agent", name, "--track", track,
                "--trials", str(args.trials), "--timeout", str(args.timeout),
                "--agents-file", str(args.agents_file),
            ]
            if models.get(name):
                command += ["--model", models[name]]
            print("$ " + " ".join(command), flush=True)
            if not args.dry_run:
                subprocess.run(command, check=False)
    if args.dry_run:
        return 0
    return subprocess.run([sys.executable, str(HERE / "build.py")], check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
