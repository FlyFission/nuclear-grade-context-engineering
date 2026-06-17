#!/usr/bin/env python3
"""Validate the Codex plugin manifest and print exact Codex install guidance.

This is a repo-side helper, not a Codex installer. Codex's own plugin/skill
mechanism does the installing; this script only (1) checks that
`.codex-plugin/plugin.json` is shaped the way Codex plugin validation expects
and the way the skills it points at actually exist, and (2) prints the precise
install + restart steps a Codex user runs.

Usage:
    python tools/install-codex.py            # validate, then print install guidance
    python tools/install-codex.py --check    # validate only (CI/test friendly)

Exit status is non-zero when validation fails.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"

# Top-level fields and the Python type Codex plugin validation expects for each.
REQUIRED_FIELDS: dict[str, type | tuple[type, ...]] = {
    "name": str,
    "version": str,
    "description": str,
    "author": dict,
    "homepage": str,
    "repository": str,
    "license": str,
    "keywords": list,
    "skills": str,
    "interface": dict,
}

REQUIRED_INTERFACE_FIELDS: dict[str, type | tuple[type, ...]] = {
    "displayName": str,
    "developerName": str,
    "category": str,
    "capabilities": list,
    "defaultPrompt": list,
}

# Verified against the Codex manifest loader (codex_core_plugins::manifest):
# it rejects an interface.defaultPrompt entry longer than 128 characters with
# "prompt must be at most 128 characters" and drops that prompt. Keep every
# starter prompt under the limit so none is silently ignored.
DEFAULT_PROMPT_MAX_CHARS = 128

# Keys whose presence would imply a Codex-native capability this plugin does not
# actually ship. Skills are the only exported surface (see Codex install docs).
UNSUPPORTED_KEYS = ("agents", "commands", "hooks", "mcpServers", "apps")


def validate_manifest(manifest: dict, root: Path = ROOT) -> list[str]:
    """Return a list of validation errors; an empty list means the manifest is valid."""
    errors: list[str] = []

    for field, expected in REQUIRED_FIELDS.items():
        if field not in manifest:
            errors.append(f"missing required field: {field}")
        elif not isinstance(manifest[field], expected):
            name = expected.__name__ if isinstance(expected, type) else "/".join(t.__name__ for t in expected)
            errors.append(f"field {field} must be {name}, got {type(manifest[field]).__name__}")

    author = manifest.get("author")
    if isinstance(author, dict) and not author.get("name"):
        errors.append("author object must include a name")

    interface = manifest.get("interface")
    if isinstance(interface, dict):
        for field, expected in REQUIRED_INTERFACE_FIELDS.items():
            if field not in interface:
                errors.append(f"interface missing required field: {field}")
            elif not isinstance(interface[field], expected):
                name = expected.__name__ if isinstance(expected, type) else "/".join(t.__name__ for t in expected)
                errors.append(f"interface field {field} must be {name}, got {type(interface[field]).__name__}")
        prompts = interface.get("defaultPrompt")
        if isinstance(prompts, list):
            if len(prompts) > 3:
                errors.append(f"interface.defaultPrompt should hold at most 3 prompts, got {len(prompts)}")
            for index, prompt in enumerate(prompts):
                if isinstance(prompt, str) and len(prompt) > DEFAULT_PROMPT_MAX_CHARS:
                    errors.append(
                        f"interface.defaultPrompt[{index}] is {len(prompt)} chars; "
                        f"Codex ignores prompts longer than {DEFAULT_PROMPT_MAX_CHARS}"
                    )

    for key in UNSUPPORTED_KEYS:
        if key in manifest:
            errors.append(
                f"unsupported top-level key '{key}': Codex install exports skills only; "
                "agents/commands/hooks/mcpServers/apps are not packaged here"
            )

    skills = manifest.get("skills")
    if isinstance(skills, str):
        skills_dir = (root / skills).resolve()
        if not skills_dir.is_dir():
            errors.append(f"skills points at a missing directory: {skills}")
        else:
            missing = [
                child.name
                for child in sorted(skills_dir.iterdir())
                if child.is_dir() and not (child / "SKILL.md").is_file()
            ]
            if missing:
                errors.append(f"skill folders without SKILL.md: {', '.join(missing)}")

    if "[TODO:" in json.dumps(manifest):
        errors.append("manifest still contains a [TODO: placeholder")

    return errors


GUIDANCE = """\
Codex plugin install — what to run and what to expect
=====================================================

1. Install the plugin from this repository (Codex's self-serve plugin
   directory is still rolling out; verify the exact installer syntax against
   https://developers.openai.com/codex/plugins):

       $skill-installer install nuclear-grade from \\
         https://github.com/FlyFission/nuclear-grade-context-engineering

   Or copy the skills directly from a checkout:

       python tools/ng.py install codex          # Core set
       python tools/ng.py install codex --full   # all skills

2. Start a NEW Codex thread (or restart Codex) so it re-scans its skills
   directory and picks up the new SKILL.md descriptions.

3. Use the skills by describing your task — e.g. "I'm about to change auth" —
   and Codex pulls in the matching skill on its own. No slash command needed.

What Codex install gives you:   the skills/ catalog (auto-surfaced by description).
What it does NOT give you:      agents/, commands/, templates/, .nuclear/, or the
                                ng CLI. The flagship skill is a router that points
                                at those repo-local files, so for the full workflow
                                clone the repo. See the Codex section of
                                INTEGRATIONS.md.
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="validate the manifest only; print no install guidance")
    args = parser.parse_args(argv)

    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"FAIL: no Codex manifest at {MANIFEST_PATH}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"FAIL: {MANIFEST_PATH} is not valid JSON: {exc}", file=sys.stderr)
        return 1

    errors = validate_manifest(manifest)
    if errors:
        print(f"FAIL: {MANIFEST_PATH} is not a valid Codex plugin manifest:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"OK: {MANIFEST_PATH.relative_to(ROOT)} is a valid Codex plugin manifest.")
    if not args.check:
        print()
        print(GUIDANCE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
