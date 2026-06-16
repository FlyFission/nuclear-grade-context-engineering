"""Optional MCP server exposing Nuclear-grade's checks as callable tools.

Install the extra to use it:  pip install "nuclear-grade[mcp]"
Run (stdio transport):        python -m nuclear_grade.mcp_server

This wraps the SAME logic the CLI uses (it does not shell out): it sets up and
reports on evidence records. It does not decide engineering adequacy, safety,
security, compliance, or verification and validation.

Token note: an MCP server's tool schemas load into the model's context every
session whether used or not. The skills (see `ng install`) are leaner; reach for
this only when a tool must CALL the checks rather than read the skills.

The four tool functions are module-level and import nothing from `mcp`, so they
can be unit-tested without the optional dependency installed; only `build_server`
needs the `mcp` package.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from nuclear_grade.cli import (
    MODE_FILES,
    collect_doctor_failures,
    packet_health,
    template_root_for,
)
from nuclear_grade.ng_validate import detect_packet_mode, validate_packet


def validate_change_record(packet_path: str) -> str:
    """Structurally validate a change-record packet directory.

    Checks that required sections are present, the placeholder marker is gone,
    internal links resolve, and evidence statuses are set. Returns OK or the list
    of structural gaps. It does not judge whether the code is correct, safe,
    secure, or compliant.
    """

    result = validate_packet(Path(packet_path))
    if result.ok:
        return f"OK: {packet_path} is structurally complete."
    gaps = "\n".join(f"- {message}" for message in result.messages)
    return f"FAILED: {packet_path}\n{gaps}"


def doctor(repo_path: str = ".") -> str:
    """Check that a repo or workspace is set up for Nuclear-grade.

    Returns OK, or the list of installation/health problems found.
    """

    failures = collect_doctor_failures(Path(repo_path).resolve())
    if not failures:
        return "OK: Nuclear-grade doctor found no problems."
    return "FAILED: Nuclear-grade doctor\n" + "\n".join(f"- {failure}" for failure in failures)


def status(repo_path: str = ".") -> str:
    """List change-record packets and their health (ok / closed / scaffold / invalid)."""

    changes = Path(repo_path).resolve() / ".nuclear" / "changes"
    if not changes.exists():
        return "No .nuclear/changes directory found."
    packets = sorted(path for path in changes.iterdir() if path.is_dir())
    if not packets:
        return "No active packets found."
    return "\n".join(f"{p.name}: {detect_packet_mode(p)}  [{packet_health(p)}]" for p in packets)


def new_change_record(slug: str, mode: str = "quick", repo_path: str = ".") -> str:
    """Scaffold a new change-record packet (mode: quick, standard, cm, golden-path).

    Writes the empty templates; a human then fills and approves them. Refuses to
    overwrite an existing packet.
    """

    if mode not in MODE_FILES:
        return f"unknown mode: {mode} (choose from {', '.join(MODE_FILES)})"
    repo = Path(repo_path).resolve()
    changes_dir = (repo / ".nuclear" / "changes").resolve()
    packet = (changes_dir / slug).resolve()
    if packet == changes_dir or not packet.is_relative_to(changes_dir):
        return f"invalid slug: {slug!r} (must stay under .nuclear/changes)"
    if packet.exists():
        return f"already exists: {packet}"
    templates = template_root_for(repo, mode)
    # Copy directly (not via the CLI's apply_writes) because a stdio MCP server
    # must keep stdout clean for the JSON-RPC protocol.
    packet.mkdir(parents=True, exist_ok=True)
    for name in MODE_FILES[mode]:
        source = templates / mode / name
        if not source.exists():
            return f"missing template: {source}"
        shutil.copyfile(source, packet / name)
    return f"created {mode} packet: {packet} ({', '.join(MODE_FILES[mode])})"


def build_server():
    """Construct the FastMCP server with the Nuclear-grade tools registered.

    Imports `mcp` lazily so the module stays importable (and testable) without the
    optional dependency.
    """

    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as exc:  # pragma: no cover - only hit without the extra
        raise SystemExit(
            'The MCP server needs the optional "mcp" dependency. '
            'Install it with:  pip install "nuclear-grade[mcp]"'
        ) from exc

    server = FastMCP("nuclear-grade")
    for tool in (validate_change_record, doctor, status, new_change_record):
        server.tool()(tool)
    return server


def main() -> int:
    build_server().run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
