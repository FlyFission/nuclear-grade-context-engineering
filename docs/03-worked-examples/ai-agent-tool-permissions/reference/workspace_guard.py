"""Reference implementation for C-001 in the AI agent tool-permissions example.

This small guard is intentionally educational: it demonstrates the evidence chain
for workspace-only file writes without claiming to be a full production sandbox.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


class WorkspaceViolation(ValueError):
    """Raised when a requested write would leave the approved workspace."""


class WorkspaceGuard:
    """Allow text writes only under a configured workspace root."""

    def __init__(self, workspace_root: str | Path):
        self.workspace_root = Path(workspace_root).resolve()
        self.workspace_root.mkdir(parents=True, exist_ok=True)
        self.audit_events: list[dict[str, Any]] = []

    def write_text(self, requested_path: str | Path, content: str) -> Path:
        """Write content when the resolved destination remains under workspace_root."""
        destination = self._resolve_destination(requested_path)
        if not self._is_within_workspace(destination):
            self._audit("write_denied", requested_path, destination, "outside_workspace")
            raise WorkspaceViolation(f"write denied outside workspace: {requested_path}")

        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
        self._audit("write_allowed", requested_path, destination, "within_workspace")
        return destination

    def _resolve_destination(self, requested_path: str | Path) -> Path:
        requested = Path(requested_path)
        if requested.is_absolute():
            return requested.resolve(strict=False)
        return (self.workspace_root / requested).resolve(strict=False)

    def _is_within_workspace(self, destination: Path) -> bool:
        try:
            destination.relative_to(self.workspace_root)
        except ValueError:
            return False
        return True

    def _audit(self, event: str, requested_path: str | Path, resolved_path: Path, reason: str) -> None:
        self.audit_events.append(
            {
                "event": event,
                "requested_path": str(requested_path),
                "resolved_path": str(resolved_path),
                "workspace_root": str(self.workspace_root),
                "reason": reason,
            }
        )
