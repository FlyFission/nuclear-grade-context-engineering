"""Nuclear-grade command-line helper.

This tool sets up and checks evidence records for a change. It does not decide
engineering adequacy, safety, security, compliance, or verification and validation.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nuclear_grade import gen_commands
from nuclear_grade.efficacy import run_all as run_efficacy
from nuclear_grade.metrics import build_inventory
from nuclear_grade.ng_validate import (
    PLACEHOLDER_MARKER,
    check_internal_links,
    detect_packet_mode,
    has_closure_note,
    validate_packet,
)
from nuclear_grade.tokens import (
    build_report,
    check_budgets,
    cost_per_signal,
    count_tokens,
    load_budgets,
    phrase_frequency,
    split_frontmatter,
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
    "intent.md",
    "deficiency.md",
)
OPTIONAL_FILES = (
    "standard/supplier-trust.md",
    "standard/red-team.md",
    "standard/execution-trace.md",
    "standard/wbs.md",
    "standard/incident.md",
    "standard/stage-contract.md",
)
MODE_FILES = {
    "quick": QUICK_FILES,
    "standard": STANDARD_FILES,
    "cm": CM_FILES,
    "golden-path": GOLDEN_PATH_FILES,
}

# --- `ng install`: cross-tool skill distribution --------------------------------
# Skills auto-surface in each tool by their frontmatter `description` (the model
# picks them when a request matches); installing is just placing the same SKILL.md
# files where the tool looks for them. The lean `--core` profile ships the
# always-first router plus the Core 7 dispositions (see CORE.md); `--full` ships
# every skill under skills/*/.
CORE_SKILLS = (
    "using-nuclear-grade",  # the always-first router
    "questioning-attitude",
    "rating-change-risk",
    "proving-claims",
    "double-checking-before-acting",
    "staying-on-mission",
    "checking-release-readiness",
    "learning-from-experience",
)

INSTALL_TOOLS = ("codex", "claude", "cursor", "windsurf", "vscode")
TOOL_LABELS = {
    "codex": "Codex CLI",
    "claude": "Claude Code",
    "cursor": "Cursor",
    "windsurf": "Windsurf",
    "vscode": "VS Code + Copilot",
}
# Skill-directory paths confirmed against each tool's current docs (Codex, Claude
# Code, Cursor, Windsurf). VS Code's project path (.github/skills) is confirmed,
# but its user-scope path is a best-known default, so VS Code stays unverified:
# unverified tools print a "verify / override with --dest" note so a wrong default
# is obvious and recoverable rather than silently writing to the wrong place.
VERIFIED_TOOLS = frozenset({"codex", "claude", "cursor", "windsurf"})

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
    "CORE.md",
    "MAXIMS.md",
)
REQUIRED_SKILL_SECTIONS = (
    "## Overview",
    "## Decision contract",
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
# Command cards are generated from skills (see nuclear_grade/gen_commands.py), so
# the required-section contract is single-sourced there. When commands became
# generated, the card dropped from ten hand-authored sections to five projected
# ones; the dropped material (purpose, files, expected outputs, the verification
# command, failure modes, legal note) now lives in the skill the card points to.
REQUIRED_COMMAND_SECTIONS = gen_commands.REQUIRED_CARD_SECTIONS

# A skill's `## Decision contract` block is the compact receipt every run must emit:
# the claim checked, the artifact observed, the decision affected (with its tier), the
# failure class, and the next action. The labels are load-bearing -- a reviewer (and
# this lint) reads them to learn what running the skill could change. The tier keeps
# the control loop from becoming audit-the-audit: only `block` and `warn` are promoted
# into the operator receipt (`ng decisions`); `observe` stays in telemetry. Tiers are
# declarable, but a skill demoting itself to noise is not: a check that never moves a
# decision is surfaced by measurement (`ng eval`/`ng tokens`) over runs, because a
# guard inside the writable set is a suggestion the author can edit.
DECISION_CONTRACT_LABELS = (
    "**Claim checked:**",
    "**Artifact observed:**",
    "**Decision affected:**",
    "**Failure class:**",
    "**Next action:**",
)
DECISION_TIERS = ("block", "warn", "observe")
# Promoted into the operator receipt; the rest (observe) stays in telemetry.
DECISION_RECEIPT_TIERS = ("block", "warn")
DECISION_TIER_PATTERN = re.compile(
    r"\*\*Decision affected:\*\*\s*(block|warn|observe)\b", re.IGNORECASE
)
DECISION_TEXT_PATTERN = re.compile(r"\*\*Decision affected:\*\*\s*(.+)")

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

CI_WORKFLOW_TEMPLATE = """\
# Nuclear-grade change-record gate (rung 4 -- only with branch protection).
#
# The OUT-OF-BAND gate: it runs in CI and checks that change records are
# STRUCTURALLY complete. It does not decide engineering adequacy, safety,
# security, or compliance. The in-session skills (and any hooks) are rungs 1-3
# and advisory by doctrine; this workflow is the control that bites -- but only
# when branch protection makes it bite (see below).
#
# IMPORTANT: on a `pull_request` run this workflow executes from the PR's own
# code, so the same PR can edit this file (e.g. drop the validate step) while
# keeping the check name. The "the author cannot edit the check" property holds
# ONLY if branch protection requires this check, requires review, and restricts
# who can change `.github/workflows/` -- e.g. a CODEOWNERS rule on that path plus
# "require review from Code Owners". Without that, this gate is advisory.
#
# (This is why the trigger stays `pull_request` and NOT `pull_request_target`:
# the latter would run a fork PR's checkout in the base-branch context WITH a
# write token and secrets -- a privilege-escalation/exfil vector. The right fix
# for "the author controls this file" is branch protection, not a riskier trigger.)
#
# Hardening: the job runs with a read-only token (least privilege); the trigger
# is `pull_request`, so a fork PR never runs with a write token or repository
# secrets; and the job references none. Pin each action below to a full commit
# SHA for production immutability.
name: Nuclear-grade change records

on:
  pull_request:

permissions:
  contents: read

jobs:
  validate-change-records:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4  # pin to a full commit SHA for production

      - name: Set up Python
        uses: actions/setup-python@v5  # pin to a full commit SHA for production
        with:
          python-version: "3.12"

      - name: Install the validator
        # Pinned to the version that generated this workflow, so this required gate
        # stays reproducible (an unpinned install could change validation on a future
        # release with no repo change). Not on PyPI in your setup? Install from source
        # pinned to the same tag instead:
        #   pip install "nuclear-grade @ git+https://github.com/FlyFission/nuclear-grade-context-engineering@vNG_VERSION"
        run: |
          python -m pip install --upgrade pip
          python -m pip install "nuclear-grade==NG_VERSION"

      - name: Validate every change record
        shell: bash
        run: |
          set -euo pipefail
          shopt -s nullglob
          found=0
          for packet in .nuclear/changes/*/; do
            # Skip packets deliberately closed via the documented closure path
            # (a `NUCLEAR-GRADE-CLOSED: <rationale>` line). They are kept for audit
            # history; the validator still rejects their unfilled fields, so closing
            # a record -- not deleting it -- must not block this gate forever.
            if grep -rqE '^[[:space:]]*NUCLEAR-GRADE-CLOSED:[[:space:]]*[^[:space:]]' "$packet"; then
              echo "Skipping closed record: $packet"
              continue
            fi
            echo "Validating $packet"
            nuclear-grade validate "$packet"
            found=1
          done
          if [ "$found" -eq 0 ]; then
            echo "No open change records under .nuclear/changes/ -- nothing to validate."
          fi
"""


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

    scaffold_parser = subcommands.add_parser(
        "scaffold-ci",
        help="Write a hardened GitHub Actions workflow that validates change records (the rung-4 out-of-band gate).",
    )
    scaffold_parser.add_argument("repo", nargs="?", default=".", type=Path)
    scaffold_parser.add_argument("--dry-run", action="store_true")
    scaffold_parser.add_argument("--force", action="store_true", help="Overwrite an existing workflow file.")
    scaffold_parser.set_defaults(handler=handle_scaffold_ci)

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

    install_parser = subcommands.add_parser(
        "install",
        help="Install skills into a tool's skills directory so they auto-surface (codex, claude, cursor, windsurf, vscode).",
    )
    install_parser.add_argument("tool", choices=INSTALL_TOOLS)
    profile_group = install_parser.add_mutually_exclusive_group()
    profile_group.add_argument(
        "--core",
        dest="full",
        action="store_false",
        help="Install the lean Core set: the router + Core 7 (default).",
    )
    profile_group.add_argument(
        "--full",
        dest="full",
        action="store_true",
        help="Install every skill.",
    )
    install_parser.set_defaults(full=False)
    install_parser.add_argument(
        "--scope",
        choices=("user", "project"),
        default="user",
        help="user = available in every project (default); project = inside --repo.",
    )
    install_parser.add_argument("--repo", default=".", type=Path, help="Repo root for --scope project.")
    install_parser.add_argument("--dest", default=None, help="Override the destination skills directory.")
    install_parser.add_argument("--dry-run", action="store_true")
    install_parser.set_defaults(handler=handle_install)

    mcp_config_parser = subcommands.add_parser(
        "mcp-config",
        help="Print the MCP server config to register nuclear-grade's checks as tools (codex, claude, cursor, windsurf, vscode).",
    )
    mcp_config_parser.add_argument("tool", choices=INSTALL_TOOLS)
    mcp_config_parser.set_defaults(handler=handle_mcp_config)

    metrics_parser = subcommands.add_parser(
        "metrics",
        help="Count the repo's parts (skills, commands, docs, templates, records) for a before/after comparison.",
    )
    metrics_parser.add_argument("repo", nargs="?", default=".", type=Path)
    metrics_parser.set_defaults(handler=handle_metrics)

    gen_commands_parser = subcommands.add_parser(
        "gen-commands",
        help="Generate commands/*.md cards from skills/*/SKILL.md (the single source).",
    )
    gen_commands_parser.add_argument("repo", nargs="?", default=".", type=Path)
    gen_commands_parser.add_argument(
        "--check",
        action="store_true",
        help="Report drift between the cards and their skills instead of writing (for CI).",
    )
    gen_commands_parser.set_defaults(handler=handle_gen_commands)

    decisions_parser = subcommands.add_parser(
        "decisions",
        help="Operator receipt: the block/warn decision each skill can move (observe stays in telemetry).",
    )
    decisions_parser.add_argument("repo", nargs="?", default=".", type=Path)
    decisions_parser.add_argument(
        "--all",
        action="store_true",
        help="Also list observe-class skills held in telemetry, not just the promoted receipt.",
    )
    decisions_parser.set_defaults(handler=handle_decisions)

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


def _validator_version() -> str:
    """The nuclear-grade version to pin the generated gate to, so a required check
    stays reproducible.

    Prefer the source checkout's ``pyproject.toml`` (guarded to *this* package): when
    ``scaffold-ci`` runs via the repo-local ``tools/ng.py`` wrapper, the checkout is the
    version actually being executed, whereas ``importlib.metadata`` reads whatever
    distribution is installed in the environment -- which may be an older wheel and would
    pin the gate to a stale validator. Fall back to installed metadata only when there is
    no matching checkout (e.g. the console script run from a wheel); otherwise return ""
    and the generator emits an unpinned install."""
    try:
        import tomllib

        pyproject = REPO_ROOT / "pyproject.toml"
        if pyproject.is_file():
            project = tomllib.loads(pyproject.read_text(encoding="utf-8")).get("project", {})
            if project.get("name") == "nuclear-grade" and project.get("version"):
                return str(project["version"])
    except Exception:
        pass
    try:
        from importlib.metadata import PackageNotFoundError, version

        try:
            return version("nuclear-grade")
        except PackageNotFoundError:
            return ""
    except Exception:
        return ""


def handle_scaffold_ci(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    pinned = _validator_version()
    content = CI_WORKFLOW_TEMPLATE
    if pinned:
        content = content.replace("nuclear-grade==NG_VERSION", f"nuclear-grade=={pinned}")
        content = content.replace("@vNG_VERSION", f"@v{pinned}")
    else:
        # No discoverable version: keep the workflow working, unpinned.
        content = content.replace("nuclear-grade==NG_VERSION", "nuclear-grade")
        content = content.replace("@vNG_VERSION", "@main")
    workflow = repo / ".github" / "workflows" / "nuclear-grade.yml"
    writes = [
        PlannedWrite(repo / ".github" / "workflows", is_dir=True),
        PlannedWrite(workflow, content=content),
    ]
    return apply_writes(writes, dry_run=args.dry_run, overwrite=args.force)


def _vscode_user_skills() -> Path:
    """VS Code + GitHub Copilot user-scope skills dir.

    Windows uses %APPDATA%\\github-copilot\\skills; elsewhere
    ~/.config/github-copilot/skills.
    """

    appdata = os.environ.get("APPDATA")
    if appdata:
        return Path(appdata) / "github-copilot" / "skills"
    return Path.home() / ".config" / "github-copilot" / "skills"


def install_dest(tool: str, scope: str, repo: Path) -> Path:
    """Resolve the skills directory a tool reads, for the requested scope.

    `user` scope installs once for every project; `project` scope installs inside
    one repo. Paths are each tool's documented skills location as of 2026-06.
    Codex/Claude/Cursor are doc-confirmed; Windsurf-user and VS Code paths are
    best-known. Override any of them with --dest.
    """

    home = Path.home()
    if tool == "codex":
        # Codex scans .agents/skills from the cwd up to the repo root (project)
        # and $HOME/.agents/skills (user). See developers.openai.com/codex/skills.
        return (repo / ".agents" / "skills") if scope == "project" else (home / ".agents" / "skills")
    if tool == "claude":
        return (repo / ".claude" / "skills") if scope == "project" else (home / ".claude" / "skills")
    if tool == "cursor":
        return (repo / ".cursor" / "skills") if scope == "project" else (home / ".cursor" / "skills")
    if tool == "windsurf":
        # Project: .windsurf/skills. User: ~/.codeium/windsurf/skills.
        return (repo / ".windsurf" / "skills") if scope == "project" else (home / ".codeium" / "windsurf" / "skills")
    if tool == "vscode":
        # VS Code + Copilot: project .github/skills (team-shared); user ~/.config/github-copilot/skills.
        return (repo / ".github" / "skills") if scope == "project" else _vscode_user_skills()
    raise ValueError(f"unknown tool: {tool}")


def handle_install(args: argparse.Namespace) -> int:
    if args.full:
        names = [path.parent.name for path in sorted(SKILLS.glob("*/SKILL.md"))]
        profile = "full"
    else:
        names = list(CORE_SKILLS)
        profile = "core"

    missing = [name for name in names if not (SKILLS / name / "SKILL.md").is_file()]
    if missing:
        print(f"missing source skills: {', '.join(sorted(missing))}", file=sys.stderr)
        return 2

    repo = args.repo.resolve()
    dest = Path(args.dest).expanduser().resolve() if args.dest is not None else install_dest(args.tool, args.scope, repo)

    # Reuse apply_writes for dry-run, parent creation, and copy. An install is an
    # update, so overwrite refreshes existing skill files when re-run.
    writes: list[PlannedWrite] = [PlannedWrite(dest, is_dir=True)]
    for name in names:
        skill_dir = SKILLS / name
        writes.append(PlannedWrite(dest / name, is_dir=True))
        for src in sorted(path for path in skill_dir.rglob("*") if path.is_file()):
            writes.append(PlannedWrite(dest / name / src.relative_to(skill_dir), source=src))

    code = apply_writes(writes, dry_run=args.dry_run, overwrite=True)
    if code != 0:
        return code

    # The honest always-on cost: the sum of the installed skills' descriptions,
    # which a routing agent reads every session whether or not a skill fires.
    standing = sum(
        count_tokens(split_frontmatter((SKILLS / name / "SKILL.md").read_text(encoding="utf-8"))[0])
        for name in names
    )
    label = TOOL_LABELS[args.tool]
    verb = "would install" if args.dry_run else "installed"
    print(f"\n{verb} {len(names)} skill(s) ({profile} profile) for {label} -> {dest}")
    print(f"always-on description cost: ~{standing} tokens (skill bodies load only when a skill fires)")
    if profile == "core":
        print("re-run with --full for all skills; re-run anytime to update.")
    if args.tool not in VERIFIED_TOOLS and args.dest is None:
        print(
            f"note: the {label} skills path is a best-known default; verify against the tool's "
            "current docs, or override with --dest <path>."
        )
    return 0


def _mcp_json(top_key: str) -> str:
    return (
        "{\n"
        f'  "{top_key}": {{\n'
        '    "nuclear-grade": {\n'
        '      "command": "python",\n'
        '      "args": ["-m", "nuclear_grade.mcp_server"]\n'
        "    }\n"
        "  }\n"
        "}\n"
    )


def handle_mcp_config(args: argparse.Namespace) -> int:
    """Print a ready-to-paste MCP server config for the chosen tool.

    Prints rather than edits: merging into a user's config file is theirs to do.
    The server needs the optional extra:  pip install "nuclear-grade[mcp]".
    """

    tool = args.tool
    if tool == "codex":
        path = "~/.codex/config.toml"
        snippet = (
            "[mcp_servers.nuclear_grade]\n"
            'command = "python"\n'
            'args = ["-m", "nuclear_grade.mcp_server"]\n'
        )
    else:
        path, top_key = {
            "claude": (".mcp.json (project) or ~/.claude.json (user)", "mcpServers"),
            "cursor": (".cursor/mcp.json (project) or ~/.cursor/mcp.json (user)", "mcpServers"),
            "windsurf": ("~/.codeium/windsurf/mcp_config.json", "mcpServers"),
            "vscode": (".vscode/mcp.json", "servers"),
        }[tool]
        snippet = _mcp_json(top_key)

    print(f"# Register nuclear-grade's checks as MCP tools for {TOOL_LABELS[tool]}.")
    print('# First install the optional extra:  pip install "nuclear-grade[mcp]"')
    print(f"# File: {path}")
    print(snippet, end="")
    if tool == "claude":
        print("# or run: claude mcp add nuclear-grade -- python -m nuclear_grade.mcp_server")
    print(
        "# Note: MCP tool schemas load into context every session (~1k tokens/tool); "
        "skills stay leaner -- prefer `ng install` unless your tool must CALL the checks."
    )
    return 0


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


def handle_metrics(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    inv = build_inventory(repo)

    rows = (
        (inv.skills, "skills", "skills/*/SKILL.md"),
        (inv.commands, "commands", "commands/*.md"),
        (inv.template_files, f"template files across {inv.template_modes} modes", "templates/**/*.md"),
        (inv.root_docs, "root docs", "*.md"),
        (inv.docs_tree, "docs/ reference tree", "docs/**/*.md"),
        (inv.change_record_files, f"change-record files in {inv.change_record_packets} packets", ".nuclear/**/*.md"),
        (inv.starter_kits, "starter kits", "starter-kit/*/"),
        (inv.agent_roles, "agent-role docs", "agents/*.md"),
    )
    print("Nuclear-grade part inventory (counts parts, not their quality or necessity):\n")
    print(f"  {'count':>6}  surface")
    print(f"  {'-' * 6}  {'-' * 7}")
    for count, label, source in rows:
        print(f"  {count:>6}  {label}  ({source})")

    print("\nDerived:")
    generated = (
        f", {inv.generated_commands} of {inv.commands} commands generated from skills"
        if inv.generated_commands
        else ""
    )
    print(
        f"  authored skill/command surface: {inv.authored_surface} hand-maintained objects"
        f"{generated} ({inv.commands_per_skill:.1f} command cards per skill)"
    )
    print(f"  self-contained prose files (skills+commands+templates+root+docs): {inv.prose_files}")
    print(f"  total markdown files: {inv.markdown_total}")

    print(
        "\nThis counts parts, not quality. A high count is not proof of waste; it is the "
        "surface a maintainer keeps in sync and a reader navigates."
    )
    return 0


def collect_skill_decisions(skills_dir: Path) -> list[tuple[str, str, str]]:
    """Return (tier, name, decision) for each skill's `## Decision contract` receipt.

    A skill with no readable tier is returned with an empty tier so the rollup shows
    the gap rather than hiding it; `ng doctor` is what fails the build on a malformed
    receipt. Rows sort block, then warn, then observe, then by name.
    """
    rows: list[tuple[str, str, str]] = []
    for skill_file in sorted(skills_dir.glob("*/SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        tier_match = DECISION_TIER_PATTERN.search(text)
        value_match = DECISION_TEXT_PATTERN.search(text)
        tier = tier_match.group(1).lower() if tier_match else ""
        decision = value_match.group(1).strip() if value_match else ""
        # The value leads with the tier token; strip it for the "which decision" view.
        if tier and decision.lower().startswith(tier):
            decision = decision[len(tier):].lstrip(" -–—").strip()
        rows.append((tier, skill_file.parent.name, decision))
    order = {"block": 0, "warn": 1, "observe": 2, "": 3}
    rows.sort(key=lambda row: (order.get(row[0], 3), row[1]))
    return rows


def handle_decisions(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    skills_dir = repo / "skills"
    if not skills_dir.exists():
        skills_dir = SKILLS
    rows = collect_skill_decisions(skills_dir)
    if not rows:
        print("no skills found", file=sys.stderr)
        return 2

    width = max(len(name) for _, name, _ in rows)

    def render(header: str, subset: list[tuple[str, str, str]]) -> None:
        print(header)
        print(f"  {'tier':<7}  {'skill':<{width}}  decision affected")
        for tier, name, decision in subset:
            shown = decision if len(decision) <= 60 else decision[:57] + "..."
            print(f"  {tier or '(none)':<7}  {name:<{width}}  {shown}")

    promoted = [row for row in rows if row[0] in DECISION_RECEIPT_TIERS]
    telemetry = [row for row in rows if row[0] == "observe"]
    missing = [name for tier, name, _ in rows if not tier]

    render("Operator receipt -- block and warn signals promoted from the skills:", promoted)

    block = sum(1 for tier, _, _ in rows if tier == "block")
    warn = sum(1 for tier, _, _ in rows if tier == "warn")
    print(
        f"\n{len(rows)} skills: {block} block, {warn} warn, {len(telemetry)} observe "
        f"-- {len(promoted)} promoted to the operator receipt, {len(telemetry)} in telemetry."
    )

    if telemetry and args.all:
        print()
        render("Telemetry -- observe signals, not promoted into the operator receipt:", telemetry)
    elif telemetry:
        print(f"Use `ng decisions --all` to list the {len(telemetry)} observe-class skill(s) in telemetry.")

    if missing:
        print(f"Missing a declarable tier (run `ng doctor`): {', '.join(missing)}")
    print(
        "\nTwo decisions stay separate: whether a skill should exist (evidence-based, "
        "see docs/05-reference/skill-evaluation.md) and the receipt it must emit. "
        "An 'observe' check that never moves a decision is a relocation candidate, "
        "never auto-deleted."
    )
    return 0


def handle_gen_commands(args: argparse.Namespace) -> int:
    repo = args.repo.resolve()
    if args.check:
        drifted = gen_commands.check(repo)
        if drifted:
            print("FAILED: commands/ is out of sync with skills/ -- run `ng gen-commands`:")
            for name in drifted:
                print(f"- {name}")
            return 1
        print("OK: every command card matches its skill.")
        return 0

    written = gen_commands.write(repo)
    print(f"Generated {len(written)} command card(s) from skills/ into commands/.")
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

    failures.extend(check_internal_links(repo, list(REQUIRED_PUBLIC_FILES)))
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
        # The decision-contract receipt must carry all five fields and a declarable
        # tier. The lint checks the receipt is present and well-formed; whether the
        # named decision is the honest one is human judgment, like every other
        # structural check here.
        if "## Decision contract" in text:
            for label in DECISION_CONTRACT_LABELS:
                if label not in text:
                    failures.append(f"{skill_file} decision contract missing {label}")
            if not DECISION_TIER_PATTERN.search(text):
                failures.append(
                    f"{skill_file} decision contract Decision affected must start "
                    f"with one of {', '.join(DECISION_TIERS)}"
                )
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
