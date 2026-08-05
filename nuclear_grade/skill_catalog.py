"""Host-neutral lifecycle and invocation registry for Nuclear-grade skills.

``skill-catalog.json`` is the semantic owner. ``nuclear-grade.yaml`` retains its
flat ``skills`` and ``command_map`` blocks as compatibility projections, and tests
require those projections to remain exact.

The registry controls distribution metadata only. Invocation never grants file,
network, credential, approval, merge, deployment, or release authority.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

VALID_STATUSES = frozenset({"promoted", "beta", "deprecated", "retired"})
VALID_INVOCATIONS = frozenset({"model", "user", "both"})
VALID_ROLES = frozenset({"router", "orchestrator", "discipline", "reference"})
_REQUIRED_FIELDS = frozenset({"id", "path", "status", "invocation", "role", "command"})
_ALLOWED_FIELDS = _REQUIRED_FIELDS | {"replacement"}


class CatalogError(ValueError):
    """Raised when lifecycle metadata cannot safely drive distribution."""


@dataclass(frozen=True)
class SkillEntry:
    id: str
    path: str
    status: str
    invocation: str
    role: str
    command: str | None
    replacement: str | None = None


@dataclass(frozen=True)
class SkillCatalog:
    schema_version: int
    entries: tuple[SkillEntry, ...]
    profiles: tuple[tuple[str, tuple[str, ...]], ...] = ()

    @property
    def promoted(self) -> tuple[SkillEntry, ...]:
        return tuple(entry for entry in self.entries if entry.status == "promoted")

    @property
    def model_routable(self) -> tuple[SkillEntry, ...]:
        return tuple(
            entry
            for entry in self.promoted
            if entry.invocation in {"model", "both"} and entry.role != "reference"
        )

    @property
    def user_invocable(self) -> tuple[SkillEntry, ...]:
        return tuple(entry for entry in self.promoted if entry.invocation in {"user", "both"})

    @property
    def command_map(self) -> dict[str, str]:
        return {entry.id: entry.command for entry in self.promoted if entry.command is not None}

    def by_id(self) -> dict[str, SkillEntry]:
        return {entry.id: entry for entry in self.entries}

    def profile(self, name: str) -> tuple[SkillEntry, ...]:
        """Return a named promoted install profile; ``full`` is always computed."""

        if name == "full":
            return self.promoted
        configured = dict(self.profiles)
        if name not in configured:
            raise CatalogError(f"unknown skill profile: {name}")
        by_id = self.by_id()
        return tuple(by_id[skill_id] for skill_id in configured[name])


def _parse_entry(raw: object, index: int, errors: list[str]) -> SkillEntry | None:
    if not isinstance(raw, dict):
        errors.append(f"skills[{index}] must be an object")
        return None

    keys = set(raw)
    missing = sorted(_REQUIRED_FIELDS - keys)
    extra = sorted(keys - _ALLOWED_FIELDS)
    if missing:
        errors.append(f"skills[{index}] missing field(s): {', '.join(missing)}")
    if extra:
        errors.append(f"skills[{index}] has unsupported field(s): {', '.join(extra)}")

    skill_id = raw.get("id")
    path = raw.get("path")
    status = raw.get("status")
    invocation = raw.get("invocation")
    role = raw.get("role")
    command = raw.get("command")
    replacement = raw.get("replacement")

    if not isinstance(skill_id, str) or not skill_id:
        errors.append(f"skills[{index}] id must be a non-empty string")
        return None
    if not isinstance(path, str) or not path:
        errors.append(f"{skill_id}: path must be a non-empty string")
        path = ""
    if status not in VALID_STATUSES:
        errors.append(f"{skill_id}: invalid status {status!r}; expected {sorted(VALID_STATUSES)}")
    if invocation not in VALID_INVOCATIONS:
        errors.append(
            f"{skill_id}: invalid invocation {invocation!r}; expected {sorted(VALID_INVOCATIONS)}"
        )
    if role not in VALID_ROLES:
        errors.append(f"{skill_id}: invalid role {role!r}; expected {sorted(VALID_ROLES)}")
    if command is not None and (not isinstance(command, str) or not command.startswith("ng-")):
        errors.append(f"{skill_id}: command must be null or an ng-* string")
        command = None
    if replacement is not None and (not isinstance(replacement, str) or not replacement):
        errors.append(f"{skill_id}: replacement must be null or a non-empty skill id")
        replacement = None

    return SkillEntry(
        id=skill_id,
        path=path,
        status=status if isinstance(status, str) else "",
        invocation=invocation if isinstance(invocation, str) else "",
        role=role if isinstance(role, str) else "",
        command=command,
        replacement=replacement,
    )


def _validate_semantics(
    root: Path,
    entries: list[SkillEntry],
    profiles: dict[str, tuple[str, ...]],
    errors: list[str],
) -> None:
    ids: set[str] = set()
    paths: set[str] = set()
    commands: set[str] = set()

    for entry in entries:
        if entry.id in ids:
            errors.append(f"duplicate skill id: {entry.id}")
        ids.add(entry.id)
        if entry.path in paths:
            errors.append(f"duplicate skill path: {entry.path}")
        paths.add(entry.path)
        if entry.command is not None:
            if entry.command in commands:
                errors.append(f"duplicate command: {entry.command}")
            commands.add(entry.command)

        rel = Path(entry.path)
        if rel.is_absolute() or ".." in rel.parts:
            errors.append(f"{entry.id}: path must stay inside the repository: {entry.path}")
        expected_name = f"{entry.id}/SKILL.md"
        if not entry.path.endswith(expected_name):
            errors.append(f"{entry.id}: path must end with {expected_name!r}")

        exists = (root / rel).is_file()
        if entry.status != "retired" and not exists:
            errors.append(f"{entry.id}: missing skill file {entry.path}")

        in_promoted_tree = entry.path.startswith("skills/")
        if entry.status == "promoted" and not in_promoted_tree:
            errors.append(f"{entry.id}: promoted skill must live under skills/")
        if entry.status != "promoted" and in_promoted_tree:
            errors.append(
                f"{entry.id}: {entry.status} skill must not live under plugin-discoverable skills/"
            )

        if entry.command is not None and entry.invocation not in {"user", "both"}:
            errors.append(f"{entry.id}: a command requires invocation user or both")
        if entry.command is not None and entry.status != "promoted":
            errors.append(f"{entry.id}: only promoted skills may publish command cards")
        if entry.role == "router" and entry.invocation not in {"model", "both"}:
            errors.append(f"{entry.id}: a router must be model-routable")
        if entry.status == "deprecated" and not entry.replacement:
            errors.append(f"{entry.id}: deprecated skill requires a replacement")

    by_id = {entry.id: entry for entry in entries}
    for entry in entries:
        if not entry.replacement:
            continue
        replacement = by_id.get(entry.replacement)
        if replacement is None:
            errors.append(f"{entry.id}: replacement {entry.replacement!r} is not in the catalog")
        elif replacement.status != "promoted":
            errors.append(f"{entry.id}: replacement {entry.replacement!r} must be promoted")
        elif replacement.id == entry.id:
            errors.append(f"{entry.id}: replacement cannot point to itself")

    promoted_dirs = {
        path.parent.name for path in (root / "skills").glob("*/SKILL.md") if path.is_file()
    }
    registered_promoted = {entry.id for entry in entries if entry.status == "promoted"}
    unregistered = sorted(promoted_dirs - registered_promoted)
    missing_from_tree = sorted(registered_promoted - promoted_dirs)
    if unregistered:
        errors.append(f"unregistered promoted skill folder(s): {', '.join(unregistered)}")
    if missing_from_tree:
        errors.append(f"promoted catalog skill(s) missing from skills/: {', '.join(missing_from_tree)}")

    by_id = {entry.id: entry for entry in entries}
    for profile_name, profile_ids in profiles.items():
        if profile_name == "full":
            errors.append("profile name 'full' is reserved for all promoted skills")
        if len(profile_ids) != len(set(profile_ids)):
            errors.append(f"profile {profile_name!r} contains duplicate skill ids")
        for skill_id in profile_ids:
            entry = by_id.get(skill_id)
            if entry is None:
                errors.append(f"profile {profile_name!r} references unknown skill {skill_id!r}")
            elif entry.status != "promoted":
                errors.append(
                    f"profile {profile_name!r} references non-promoted skill {skill_id!r}"
                )


def _parse_profiles(raw: object, errors: list[str]) -> dict[str, tuple[str, ...]]:
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        errors.append("profiles must be an object of name -> skill-id list")
        return {}
    profiles: dict[str, tuple[str, ...]] = {}
    for name, value in raw.items():
        if not isinstance(name, str) or not name:
            errors.append("profile names must be non-empty strings")
            continue
        if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
            errors.append(f"profile {name!r} must be a list of non-empty skill ids")
            continue
        profiles[name] = tuple(value)
    return profiles


def load_catalog(root: Path) -> SkillCatalog:
    """Load and fail-closed validate ``skill-catalog.json`` under ``root``."""

    path = root / "skill-catalog.json"
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CatalogError(f"missing skill catalog: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CatalogError(f"invalid JSON in {path}: {exc}") from exc

    errors: list[str] = []
    if not isinstance(raw, dict):
        raise CatalogError("skill catalog root must be an object")
    if raw.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    raw_entries = raw.get("skills")
    if not isinstance(raw_entries, list):
        errors.append("skills must be a list")
        raw_entries = []

    entries = [entry for i, item in enumerate(raw_entries) if (entry := _parse_entry(item, i, errors))]
    profiles = _parse_profiles(raw.get("profiles"), errors)
    _validate_semantics(root, entries, profiles, errors)
    if errors:
        raise CatalogError("invalid skill catalog:\n- " + "\n- ".join(errors))
    return SkillCatalog(
        schema_version=1,
        entries=tuple(entries),
        profiles=tuple(profiles.items()),
    )


def load_yaml_projections(root: Path) -> tuple[list[str], dict[str, str]]:
    """Read legacy flat ``skills`` and ``command_map`` compatibility projections."""

    path = root / "nuclear-grade.yaml"
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    skills: list[str] = []
    commands: dict[str, str] = {}
    block: str | None = None

    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line[0].isspace():
            header = line.strip()
            block = header[:-1] if header.endswith(":") else None
            continue
        stripped = line.strip()
        if block == "skills" and stripped.startswith("- "):
            skills.append(stripped[2:].strip())
        elif block == "command_map" and ":" in stripped:
            key, _, value = stripped.partition(":")
            commands[key.strip()] = value.strip()
    return skills, commands
