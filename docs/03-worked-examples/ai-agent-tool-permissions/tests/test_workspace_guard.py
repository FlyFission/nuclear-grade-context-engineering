
import pytest
from reference.workspace_guard import WorkspaceGuard, WorkspaceViolation


def test_allowed_relative_write_stays_inside_workspace(tmp_path):
    guard = WorkspaceGuard(tmp_path / "workspace")

    written = guard.write_text("changes/add-agent-tool-permissions/notes.txt", "evidence")

    assert written == (tmp_path / "workspace" / "changes" / "add-agent-tool-permissions" / "notes.txt").resolve()
    assert written.read_text(encoding="utf-8") == "evidence"


def test_parent_traversal_write_is_denied_and_logged(tmp_path):
    guard = WorkspaceGuard(tmp_path / "workspace")

    with pytest.raises(WorkspaceViolation):
        guard.write_text("../outside.txt", "escape")

    assert not (tmp_path / "outside.txt").exists()
    assert guard.audit_events[-1]["event"] == "write_denied"
    assert guard.audit_events[-1]["reason"] == "outside_workspace"


def test_absolute_path_write_is_denied(tmp_path):
    guard = WorkspaceGuard(tmp_path / "workspace")
    outside = tmp_path / "outside.txt"

    with pytest.raises(WorkspaceViolation):
        guard.write_text(outside, "escape")

    assert not outside.exists()
    assert guard.audit_events[-1]["event"] == "write_denied"


def test_symlink_escape_is_denied(tmp_path):
    workspace = tmp_path / "workspace"
    outside = tmp_path / "outside"
    outside.mkdir()
    workspace.mkdir()
    (workspace / "link").symlink_to(outside, target_is_directory=True)
    guard = WorkspaceGuard(workspace)

    with pytest.raises(WorkspaceViolation):
        guard.write_text("link/escaped.txt", "escape")

    assert not (outside / "escaped.txt").exists()
    assert guard.audit_events[-1]["event"] == "write_denied"
