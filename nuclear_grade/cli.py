"""Nuclear-grade command-line helper.

This tool sets up and checks evidence records for a change. It does not decide
engineering adequacy, safety, security, compliance, or verification and validation.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nuclear_grade.efficacy import run_all as run_efficacy
from nuclear_grade.ng_validate import (
    PLACEHOLDER_MARKER,
    detect_packet_mode,
    has_closure_note,
    validate_packet,
)
from nuclear_grade.tokens import (
    build_report,
    check_budgets,
    cost_per_signal,
    load_budgets,
    phrase_frequency,
)

PACKAGE_DIR = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_DIR.parent
BUNDLED_ROOT = PACKAGE_DIR / "_bundled"


def _resolve_resource_root(name: str) -> Path:
    """Return the directory holding bundled resources ('templates', 'skills', 'commands').

    Prefers the repo-relative path when running from a source checkout; falls back
    to the wheel-bundled copy under nuclear_grade/_bundled/.
    """

    repo_path = REPO_ROOT / name
    if repo_path.is_dir():
        return repo_path
    bundled = BUNDLED_ROOT / name
    return bundled


SKILLS = _resolve_resource_root("skills")
COMMANDS = _resolve_resource_root("commands")

QUICK_FILES = ("risk.md", "proof.md")
STANDARD_FILES = ("risk.md", "basis.md", "plan.md", "trace.md", "verification.md", "ship.md")
CM_FILES = ("controlled-items.md", "change-impact.md", "baseline.md", "variance.md", "opex.md")
GOLDEN_PATH_FILES = (
    "questioning-attitude.md",
    "spec.md",
    "turnover.md",
    "self-check.md",
    "decision.md",
)
OPTIONAL_FILES = ("standard/supplier-trust.md",)
MODE_FILES = {
    "quick": QUICK_FILES,
    "standard": STANDARD_FILES,
    "cm": CM_FILES,
    "golden-path": GOLDEN_PATH_FILES,
}
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
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
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

MODE_DEFAULT_BLOCK = {
    "quick": "## Selected mode\n\n- **Mode:** Quick\n",
    "standard": "## Selected mode\n\n- **Mode:** Standard\n",
}

CHARTER_TEMPLATE = (
    "# Charter\n\n"
    "**Version:** 1.0.0\n"
    "**Ratified:** <date>\n"
    "**Last amended:** <date>\n\n"
    "The lasting, non-negotiable rules for how work is done here, no matter the change. "
    "A mission anchor says what one change is for; the charter says how every change must be carried out. "
    "It is advisory in the tooling, but it is the standard a reviewer and an agent are expected to hold. Apply it in proportion to the stakes.\n\n"
    "## Articles\n\n"
    "1. Ownership: one named person owns each change and its evidence.\n"
    "2. Face facts: report what is actually true, not what you hoped would be true.\n"
    "3. Rising standards: never let a slip become the new normal; a small erosion is a finding.\n"
    "4. Formality: follow the procedure; if you must deviate, write it down and decide it out loud, never in silence.\n"
    "5. Technical depth: the owner understands the details, not just the summary.\n"
    "6. Honest reporting: bad news travels up fast and unchanged.\n"
    "7. Questioning attitude: challenge the assumptions before you act.\n"
    "8. Evidence over persuasion: every claim carries reproducible evidence or a labeled gap.\n"
    "9. Graded rigor: match the controls to the stakes.\n"
    "10. Baseline discipline: the approved version is written down, and changes to it are controlled.\n\n"
    "## Amendment log\n\n"
    "- 1.0.0 (<date>): Initial charter.\n\n"
    "This charter records principles for engineering review. It does not create compliance, formal "
    "V&V, safety, security, certification, or regulatory adequacy.\n"
)

MISSION_TEMPLATE = (
    "# Workspace mission anchor\n\n"
    "The lasting goal this workspace serves. Each change record names its own "
    "`## Mission anchor`; this file is the goal those changes trace back up to. Restate it after any "
    "context reset so the goal survives even when the context is lost.\n\n"
    "- Objective: <the lasting goal this workspace serves>\n"
    "- Success criteria: <what you can observe that proves the goal is met>\n"
    "- Non-goals / forbidden directions: <what is clearly out of scope and off-limits>\n\n"
    "This anchor records intent for engineering review. It does not create compliance, formal V&V, "
    "safety, security, certification, or regulatory adequacy.\n"
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
            "Nuclear-grade helper. Checks whether evidence is visible. It does not decide "
            "engineering adequacy, safety, compliance, or formal V&V."
        )
    )
    subcommands = parser.add_subparsers(dest="command", required=True)

    init_parser = subcommands.add_parser("init", help="Initialize .nuclear workspace files.")
    init_parser.add_argument("repo", nargs="?", default=".", type=Path)
    init_parser.add_argument("--dry-run", action="store_true")
    init_parser.add_argument("--yes", action="store_true", help="Overwrite managed files when needed.")
    init_parser.set_defaults(handler=handle_init)

    new_parser = subcommands.add_parser("new", help="Create a packet (quick, standard, cm, or golden-path).")
    new_parser.add_argument("slug")
    new_parser.add_argument(
        "--mode",
        required=True,
        choices=("quick", "standard", "cm", "golden-path"),
    )
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

    migrate_parser = subcommands.add_parser(
        "migrate",
        help="Insert a `## Selected mode` block into a legacy packet's risk.md.",
    )
    migrate_parser.add_argument("packet", type=Path)
    migrate_parser.add_argument(
        "--default",
        choices=("quick", "standard"),
        default=None,
        help="Mode to record when it cannot be inferred (default: auto).",
    )
    migrate_parser.set_defaults(handler=handle_migrate)

    eval_parser = subcommands.add_parser(
        "eval",
        help="Score worked-example artifacts for the decision signals they claim to teach.",
    )
    eval_parser.add_argument("repo", nargs="?", default=".", type=Path)
    eval_parser.set_defaults(handler=handle_eval)

    tokens_parser = subcommands.add_parser(
        "tokens",
        help="Audit prose token cost and enforce per-file token budgets.",
    )
    tokens_parser.add_argument("repo", nargs="?", default=".", type=Path)
    tokens_parser.set_defaults(handler=handle_tokens)

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
                "Change records live in `changes/<slug>/`.\n\n"
                "This workspace stores evidence for engineering review. It does not "
                "create compliance, formal V&V, safety, security, or regulatory adequacy.\n"
            ),
        ),
        PlannedWrite(repo / ".nuclear" / "charter.md", content=CHARTER_TEMPLATE),
        PlannedWrite(repo / ".nuclear" / "mission.md", content=MISSION_TEMPLATE),
    ]
    return apply_writes(writes, dry_run=args.dry_run, overwrite=args.yes)


def handle_new(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    packet = repo / ".nuclear" / "changes" / args.slug
    files = MODE_FILES[args.mode]
    templates = template_root_for(repo, args.mode)
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


def handle_migrate(args: argparse.Namespace) -> int:
    packet = args.packet.resolve()
    if not packet.is_dir():
        print(f"packet is not a directory: {packet}", file=sys.stderr)
        return 2

    risk = packet / "risk.md"
    if not risk.exists():
        print(f"missing risk.md: {risk}", file=sys.stderr)
        return 2

    text = risk.read_text(encoding="utf-8")
    if "## Selected mode" in text:
        print(f"already declares mode: {risk}")
        return 0

    inferred = args.default or infer_mode_from_files(packet)
    block = MODE_DEFAULT_BLOCK[inferred]

    new_text = _insert_mode_block(text, block)
    risk.write_text(new_text, encoding="utf-8")
    print(f"migrated: {risk} (inferred Mode: {inferred.capitalize()})")
    print("Edit risk.md to override if the inferred mode is wrong.")
    return 0


def infer_mode_from_files(packet: Path) -> str:
    standard_signals = ("basis.md", "plan.md", "trace.md", "verification.md", "ship.md")
    return "standard" if any((packet / name).exists() for name in standard_signals) else "quick"


def _insert_mode_block(text: str, block: str) -> str:
    """Insert the mode block after the first H1, or at top if no H1 is present."""

    lines = text.splitlines(keepends=True)
    insert_index = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_index = i + 1
            break

    head = "".join(lines[:insert_index])
    tail = "".join(lines[insert_index:])
    separator = "\n" if head and not head.endswith("\n\n") else ""
    return f"{head}{separator}\n{block}\n{tail}"


def template_root_for(repo: Path, mode: str) -> Path:
    repo_templates = repo / "templates"
    required = MODE_FILES[mode]
    if all((repo_templates / mode / name).exists() for name in required):
        return repo_templates
    bundled_templates = BUNDLED_ROOT / "templates"
    if all((bundled_templates / mode / name).exists() for name in required):
        return bundled_templates
    return REPO_ROOT / "templates"


def handle_list(args: argparse.Namespace) -> int:
    print("Modes: quick, standard, cm, golden-path")
    print("Quick files: " + ", ".join(QUICK_FILES))
    print("Standard files: " + ", ".join(STANDARD_FILES))
    print("Activated CM files: " + ", ".join(CM_FILES))
    print("Golden path files: " + ", ".join(GOLDEN_PATH_FILES))
    print("Optional files: " + ", ".join(OPTIONAL_FILES))
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

    # ok and closed are terminal states; only scaffold and invalid need attention.
    needs_attention = 0
    for packet in packets:
        health = packet_health(packet)
        if health not in ("ok", "closed"):
            needs_attention += 1
        print(f"{packet.name}: {detect_packet_mode(packet)}  [{health}]")

    if needs_attention:
        print(
            f"\n{needs_attention} packet(s) need attention. "
            "A scaffold packet is an unfilled draft; an invalid packet fails validation. "
            "Fill it, or close it with a rationale, or delete it -- do not leave it half-done."
        )
    return 0


def packet_health(packet: Path) -> str:
    """Classify a packet for `status`: ok, closed, scaffold (untouched draft), or invalid.

    A packet that validates is ok. A packet deliberately abandoned with a recorded
    rationale carries a `NUCLEAR-GRADE-CLOSED:` closure note and is a terminal
    state, so it is reported as closed and not counted as needing attention -- the
    closure check comes first because an abandoned packet may still hold the
    placeholder marker. A bare marker or a prose mention does not count, so a packet
    cannot be suppressed without recording why it was dropped. A scaffold
    still carries the placeholder marker, so it is an unfilled draft rather than a
    wrong one. Anything else that fails validation is invalid. The marker tests read
    the actual markers from the packet files (not the validator's message text) so
    health tracks behavior rather than wording.
    """

    if validate_packet(packet).ok:
        return "ok"
    texts = [md_file.read_text(encoding="utf-8") for md_file in packet.glob("*.md")]
    if any(has_closure_note(text) for text in texts):
        return "closed"
    if any(PLACEHOLDER_MARKER in text for text in texts):
        return "scaffold"
    return "invalid"


def handle_eval(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    try:
        results = run_efficacy(repo)
    except (OSError, ValueError, KeyError, TypeError) as error:
        # ValueError covers json.JSONDecodeError; KeyError/TypeError cover a
        # malformed case (missing "name", non-list "signals", and so on).
        print(f"eval: could not load eval cases under {repo / 'evals' / 'cases'}: {error}")
        return 1
    if not results:
        print(f"No eval cases found under {repo / 'evals' / 'cases'}.")
        return 0

    failures = 0
    for result in results:
        if not result.ok:
            failures += 1
        print(
            f"{result.case.id} {result.case.title}: "
            f"{result.present_count}/{result.total} signals [{result.status}]"
        )
        for signal in result.signals:
            if not signal.present:
                print(f"    - missing: {signal.name}")

    total = sum(result.total for result in results)
    present = sum(result.present_count for result in results)
    print(
        f"\nDecision-signal coverage: {present}/{total} across "
        f"{len(results)} worked example(s)."
    )
    print(
        "Coverage means the artifact names the decision element; it is not proof "
        "the element is adequately handled, safe, secure, or compliant."
    )
    if failures:
        print(f"{failures} case(s) missing required signals.")
        return 1
    return 0


def handle_tokens(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    report = build_report(repo)
    budgets = load_budgets(repo)

    skills = sorted(report.of_kind("skill"), key=lambda f: f.body_tokens, reverse=True)
    print("Skill token cost (description = always-loaded, body = on-invocation):")
    print(f"  {'description':>11}  {'body':>6}  skill")
    for skill in skills:
        print(f"  {skill.description_tokens:>11}  {skill.body_tokens:>6}  {skill.name}")
    print(
        f"\nSkill totals: descriptions {report.skill_description_total} tokens "
        f"(always loaded), bodies {report.skill_body_total} tokens "
        f"(loaded only when the skill fires)."
    )

    commands = report.of_kind("command")
    if commands:
        worst = max(commands, key=lambda f: f.body_tokens)
        print(
            f"Commands: {len(commands)} cards, "
            f"{sum(c.body_tokens for c in commands)} tokens total, "
            f"largest {worst.body_tokens} ({worst.name})."
        )
    print(f"All measured prose: {report.total} tokens.")

    per_signal = cost_per_signal(repo)
    if per_signal:
        print("\nWorked-example cost per decision signal (tokens / signal):")
        for case_id, cost in sorted(per_signal.items()):
            print(f"  {case_id}: {cost:.0f}")

    disclaimer_total, disclaimer_files = phrase_frequency(repo, "does not create")
    print(
        f"\nAssurance disclaimer 'does not create ...': {disclaimer_total} occurrences "
        f"across {disclaimer_files} files."
    )
    if report.repeated_blocks:
        print("Repeated prose blocks (>=3 files):")
        for block in report.repeated_blocks:
            print(f"  {block.file_count} files x {block.block_tokens} tokens: \"{block.excerpt[:60]}...\"")

    violations = check_budgets(report, budgets)
    if violations:
        print("\nFAILED: token budget")
        for violation in violations:
            print(f"- {violation}")
        return 1
    print("\nOK: token budget")
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
    if not looks_like_distribution_repo(repo):
        return collect_workspace_failures(repo)

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

    for name in OPTIONAL_FILES:
        if not (repo / "templates" / name).exists():
            failures.append(f"missing template: templates/{name}")

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


def looks_like_distribution_repo(repo: Path) -> bool:
    return (repo / "nuclear-grade.yaml").exists() or all(
        (repo / path).exists()
        for path in ("templates", "skills", "commands")
    )


def collect_workspace_failures(repo: Path) -> list[str]:
    failures: list[str] = []
    if sys.version_info < (3, 11):
        failures.append("Python 3.11 or newer is required")
    if not repo.exists():
        failures.append(f"repo path does not exist: {repo}")
        return failures
    if not (repo / ".nuclear").is_dir():
        failures.append("missing initialized workspace: .nuclear")
    if not (repo / ".nuclear" / "changes").is_dir():
        failures.append("missing packet directory: .nuclear/changes")
    if not (repo / ".nuclear" / "README.md").exists():
        failures.append("missing workspace guide: .nuclear/README.md")
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
