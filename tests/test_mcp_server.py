"""Tests for the optional MCP server.

The four tool functions import nothing from `mcp`, so they run in CI without the
optional extra. Only `build_server` needs `mcp`, so that test is importorskip-guarded.
"""

import pytest

from nuclear_grade.mcp_server import (
    doctor,
    new_change_record,
    status,
    validate_change_record,
)
from tests.test_ng_validate import (
    COMMON_TAIL,
    add_decision_authority,
    minimal_quick_packet,
    minimal_standard_packet,
)


def test_validate_change_record_accepts_filled_packet(tmp_path):
    packet = minimal_quick_packet(tmp_path)

    assert validate_change_record(str(packet)).startswith("OK")


def test_validate_change_record_supports_strict_custody(tmp_path):
    packet = minimal_standard_packet(tmp_path)

    assert validate_change_record(str(packet), strict_custody=True).startswith("OK")


def test_validate_change_record_strict_flag_changes_legacy_packet_result(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    (packet / "verification.md").write_text(
        "# Verification\n\n## Result\n\n- Status: pass\n- Evidence: test\n" + COMMON_TAIL,
        encoding="utf-8",
    )

    assert validate_change_record(str(packet)).startswith("OK")
    strict = validate_change_record(str(packet), strict_custody=True)
    assert strict.startswith("FAILED")
    assert "missing required section: Evidence custody and coupling" in strict


def test_validate_change_record_supports_strict_authority(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    add_decision_authority(packet)

    assert validate_change_record(str(packet), strict_authority=True).startswith("OK")


def test_validate_change_record_strict_authority_requires_record(tmp_path):
    packet = minimal_standard_packet(tmp_path)

    strict = validate_change_record(str(packet), strict_authority=True)

    assert strict.startswith("FAILED")
    assert "missing required file: decision-authority.md" in strict


def test_new_then_validate_flags_unfilled_scaffold(tmp_path):
    message = new_change_record("demo", "quick", str(tmp_path))

    assert message.startswith("created")
    packet = tmp_path / ".nuclear" / "changes" / "demo"
    assert (packet / "risk.md").exists()
    # A freshly scaffolded packet still carries the placeholder marker.
    assert validate_change_record(str(packet)).startswith("FAILED")


def test_new_change_record_refuses_overwrite(tmp_path):
    assert new_change_record("demo", "quick", str(tmp_path)).startswith("created")
    assert new_change_record("demo", "quick", str(tmp_path)).startswith("already exists")


def test_new_change_record_rejects_unknown_mode(tmp_path):
    assert new_change_record("demo", "bogus", str(tmp_path)).startswith("unknown mode")


def test_new_change_record_rejects_path_traversal(tmp_path):
    # A slug that escapes .nuclear/changes must be refused before any write.
    message = new_change_record("../../../../etc/evil", "quick", str(tmp_path))

    assert message.startswith("invalid slug")


@pytest.mark.parametrize("slug", ["nested/packet", "nested\\packet", "C:\\outside", "", ".", ".."])
def test_new_change_record_requires_a_single_name(tmp_path, slug):
    assert new_change_record(slug, "quick", str(tmp_path)).startswith("invalid slug")
    assert list(tmp_path.iterdir()) == []


def test_new_change_record_rejects_redirected_changes_directory(tmp_path):
    repo = tmp_path / "repo"
    (repo / ".nuclear").mkdir(parents=True)
    outside = tmp_path / "outside"
    outside.mkdir()
    try:
        (repo / ".nuclear" / "changes").symlink_to(outside, target_is_directory=True)
    except OSError:
        pytest.skip("symlinks are unavailable")
    assert new_change_record("demo", "quick", str(repo)).startswith("invalid slug")
    assert list(outside.iterdir()) == []


def test_new_change_record_handles_symlink_loop_as_invalid(tmp_path):
    changes = tmp_path / ".nuclear" / "changes"
    changes.mkdir(parents=True)
    try:
        (changes / "loop").symlink_to(changes / "loop", target_is_directory=True)
    except OSError:
        pytest.skip("symlinks are unavailable")
    assert new_change_record("loop", "quick", str(tmp_path)).startswith("invalid slug")


def test_status_lists_packets(tmp_path):
    new_change_record("demo", "standard", str(tmp_path))

    assert "demo" in status(str(tmp_path))


def test_status_handles_empty_workspace(tmp_path):
    assert "No .nuclear/changes" in status(str(tmp_path))


def test_doctor_reports_workspace_problems(tmp_path):
    # A bare temp dir is neither a distribution repo nor an initialized workspace.
    assert doctor(str(tmp_path)).startswith("FAILED")


def test_build_server_registers_expected_tools():
    pytest.importorskip("mcp")
    import asyncio

    from nuclear_grade.mcp_server import build_server

    server = build_server()
    tools = asyncio.run(server.list_tools())
    names = {tool.name for tool in tools}
    assert {"validate_change_record", "doctor", "status", "new_change_record"} <= names


def test_validate_change_record_forwards_two_party(tmp_path):
    from tests.test_two_party import WORKED

    assert validate_change_record(str(WORKED), strict_custody=True).startswith("OK")
    strict = validate_change_record(str(WORKED), strict_custody=True, two_party=True)
    assert strict.startswith("FAILED")
    assert "C-001" in strict
