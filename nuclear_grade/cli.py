"""Nuclear-grade command-line helper.

This CLI scaffolds and checks evidence packets. It does not decide engineering
adequacy, safety, security, compliance, or formal verification and validation.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nuclear_grade.ng_validate import detect_packet_mode, validate_packet


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
COMMANDS = ROOT / "commands"

QUICK_FILES = ("risk.md", "proof.md")
STANDARD_FILES = ("risk.md", "basis.md", "plan.md", "trace.md", "verification.md", "ship.md")
CM_FILES = ("controlled-items.md", "change-impact.md", "baseline.md", "variance.md", "opex.md")
GOLDEN_PATH_FILES = ("questioning-attitude.md", "spec.md", "decision.md")
REQUIRED_PUBLIC_FILES = (
    "README.md",
    "DISCLAIMER.md",
    "LICENSE",
    "INSTALL.md",
    "QUICKSTART.md",
    "WORKFLOWS.md",
    "SKILLS.md",
    "COMMANDS.md",
    "EXAMPLES.md",
    "ROADMAP.md",
    "SUPPORT.md",
    "GOVERNANCE.md",
    "AGENTS.md",
)
REQUIRED_SKILL_SECTIONS = (
    "## Overview",
    "## When to Use",
    "## When Not to Use",
    "## Inputs",
    "## Process",
    "## Outputs",
    "## Verification",
    "## Escalation",
    "## Common Rationalizations",
    "## Red Flags",
    "## Source-lineage note",
)
REQUIRED_COMMAND_SECTIONS = (
    "## Purpose",
    "## Use when",
    "## Do not use when",
    "## Inputs",
    "## Prompt text",
    "## Files created or modified",
    "## Expected outputs",
    "## Verification command",
    "## Failure modes",
    "## Legal/assurance boundary note",
)


@dataclass(frozen=True)
class PlannedWrite:
    path: Path
    content: str | None = None
    source: Path | None = None
    is_dir: bool = False


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.handler(args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Nuclear-grade helper. Checks evidence visibility; does not decide "
            "engineering adequacy, safety, compliance, or formal V&V."
        )
    )
    subcommands = parser.add_subparsers(dest="command", required=True)

    init_parser = subcommands.add_parser("init", help="Initialize .nuclear workspace files.")
    init_parser.add_argument("repo", nargs="?", default=".", type=Path)
    init_parser.add_argument("--dry-run", action="store_true")
    init_parser.add_argument("--yes", action="store_true", help="Overwrite managed files when needed.")
    init_parser.set_defaults(handler=handle_init)

    new_parser = subcommands.add_parser("new", help="Create a Quick or Standard change packet.")
    new_parser.add_argument("slug")
    new_parser.add_argument("--mode", required=True, choices=("quick", "standard"))
    new_parser.add_argument("--repo", default=".", type=Path)
    new_parser.add_argument("--force", action="store_true")
    new_parser.set_defaults(handler=handle_new)

    validate_parser = subcommands.add_parser("validate", help="Validate a change packet.")
    validate_parser.add_argument("packet", type=Path)
    validate_parser.set_defaults(handler=handle_validate)

    doctor_parser = subcommands.add_parser("doctor", help="Check repo installation health.")
    doctor_parser.add_argument("repo", nargs="?", default=".", type=Path)
    doctor_parser.set_defaults(handler=handle_doctor)

    list_parser = subcommands.add_parser("list", help="List modes, skills, commands, and templates.")
    list_parser.set_defaults(handler=handle_list)

    status_parser = subcommands.add_parser("status", help="List active packets and detected modes.")
    status_parser.add_argument("repo", nargs="?", default=".", type=Path)
    status_parser.set_defaults(handler=handle_status)

    return parser


def handle_init(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    writes = [
        PlannedWrite(repo / ".nuclear", is_dir=True),
        PlannedWrite(repo / ".nuclear" / "changes", is_dir=True),
        PlannedWrite(
            repo / ".nuclear" / "README.md",
            content=(
                "# Nuclear-grade workspace\n\n"
                "Change packets live in `changes/<slug>/`.\n\n"
                "This workspace records evidence for engineering review. It does not "
                "create compliance, formal V&V, safety, security, or regulatory adequacy.\n"
            ),
        ),
    ]
    return apply_writes(writes, dry_run=args.dry_run, overwrite=args.yes)


def handle_new(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    packet = repo / ".nuclear" / "changes" / args.slug
    files = QUICK_FILES if args.mode == "quick" else STANDARD_FILES
    templates = repo / "templates"
    writes = [PlannedWrite(packet, is_dir=True)]
    writes.extend(
        PlannedWrite(packet / name, source=templates / args.mode / name)
        for name in files
    )
    return apply_writes(writes, dry_run=False, overwrite=args.force)


def handle_validate(args: argparse.Namespace) -> int:
    result = validate_packet(args.packet)
    if result.ok:
        print(f"OK: {args.packet}")
        return 0

    print(f"FAILED: {args.packet}")
    for message in result.messages:
        print(f"- {message}")
    return 1


def handle_doctor(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    failures = collect_doctor_failures(repo)
    if failures:
        print("FAILED: Nuclear-grade doctor")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("OK: Nuclear-grade doctor")
    return 0


def handle_list(args: argparse.Namespace) -> int:
    print("Modes: quick, standard")
    print("Quick files: " + ", ".join(QUICK_FILES))
    print("Standard files: " + ", ".join(STANDARD_FILES))
    print("Activated CM files: " + ", ".join(CM_FILES))
    print("Golden path files: " + ", ".join(GOLDEN_PATH_FILES))
    print("Skills:")
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        print(f"- {path.parent.name}")
    print("Portable command prompts:")
    for path in sorted(COMMANDS.glob("*.md")):
        print(f"- {path.name}")
    return 0


def handle_status(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    changes = repo / ".nuclear" / "changes"
    if not changes.exists():
        print("No .nuclear/changes directory found.")
        return 0

    packets = sorted(path for path in changes.iterdir() if path.is_dir())
    if not packets:
        print("No active packets found.")
        return 0

    for packet in packets:
        print(f"{packet.name}: {detect_packet_mode(packet)}")
    return 0


def apply_writes(writes: list[PlannedWrite], dry_run: bool, overwrite: bool) -> int:
    for write in writes:
        if write.path.exists() and not write.is_dir and not overwrite:
            print(f"already exists: {write.path}", file=sys.stderr)
            return 2
        if write.source is not None and not write.source.exists():
            print(f"missing source file: {write.source}", file=sys.stderr)
            return 2

    for write in writes:
        if dry_run:
            action = "would create directory" if write.is_dir else "would create"
            print(f"{action}: {write.path}")
            continue

        if write.is_dir:
            write.path.mkdir(parents=True, exist_ok=True)
        elif write.source is not None:
            write.path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(write.source, write.path)
            print(f"created: {write.path}")
        else:
            write.path.parent.mkdir(parents=True, exist_ok=True)
            write.path.write_text(write.content or "", encoding="utf-8")
            print(f"created: {write.path}")
    return 0


def collect_doctor_failures(repo: Path) -> list[str]:
    failures: list[str] = []
    catalog = repo / "nuclear-grade.yaml"
    skills_dir = repo / "skills"
    commands_dir = repo / "commands"
    if sys.version_info < (3, 11):
        failures.append("Python 3.11 or newer is required")

    for public_file in REQUIRED_PUBLIC_FILES:
        if not (repo / public_file).exists():
            failures.append(f"missing public file: {public_file}")

    for mode, files in (
        ("quick", QUICK_FILES),
        ("standard", STANDARD_FILES),
        ("cm", CM_FILES),
        ("golden-path", GOLDEN_PATH_FILES),
    ):
        for name in files:
            if not (repo / "templates" / mode / name).exists():
                failures.append(f"missing template: templates/{mode}/{name}")

    if not catalog.exists():
        failures.append("missing nuclear-grade.yaml")

    if not skills_dir.exists():
        failures.append(f"missing skills directory: {skills_dir.name}")
    else:
        failures.extend(check_skill_contracts(skills_dir))

    if not commands_dir.exists():
        failures.append(f"missing commands directory: {commands_dir.name}")
    else:
        failures.extend(check_command_contracts(commands_dir))
    return failures


def check_skill_contracts(skills_dir: Path) -> list[str]:
    failures: list[str] = []
    for skill_file in sorted(skills_dir.glob("*/SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            failures.append(f"{skill_file} missing frontmatter")
        for section in REQUIRED_SKILL_SECTIONS:
            if section not in text:
                failures.append(f"{skill_file} missing {section}")
    return failures


def check_command_contracts(commands_dir: Path) -> list[str]:
    failures: list[str] = []
    for command_file in sorted(commands_dir.glob("*.md")):
        text = command_file.read_text(encoding="utf-8")
        for section in REQUIRED_COMMAND_SECTIONS:
            if section not in text:
                failures.append(f"{command_file} missing {section}")
    return failures


if __name__ == "__main__":
    raise SystemExit(main())
