"""Part-count inventory for a Nuclear-grade repository.

What this measures
------------------
The number of *parts* the repo carries -- the surfaces a maintainer must keep in
sync and a reader must navigate:

- **skills** (``skills/*/SKILL.md``) and **commands** (``commands/*.md``), the
  two parallel surfaces that today describe the same workflows twice;
- **templates** and the **modes** they span;
- **root docs** (``*.md``) and the **docs/** reference tree;
- **change records** under ``.nuclear/`` (the repo dogfooding itself);
- **starter kits** and **agent-role docs**.

It also derives the **authored skill/command surface** -- the count of
hand-maintained objects standing behind the workflow ideas -- and the
**commands-per-skill** ratio, because that ratio is the clearest single signal of
duplicated maintenance effort (a parallel command tree shows up as ~1.0).

What this does NOT measure
--------------------------
Whether a part is correct, necessary, or worth keeping. A high count is not proof
of waste and a low one is not proof of value; this reports the part count so a
human can weigh it against what each part actually does. It counts parts, not
quality.

Design constraints
------------------
Stdlib-only and deterministic: the same tree yields the same counts on CI and on
every machine, with no dependency on git or on the ``nuclear-grade.yaml`` manifest
-- counts come straight from the filesystem. That makes a "before vs after"
comparison reproducible, and lets the numbers back a regression gate later.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# Known template modes, in declaration order. Only used to *label* and *order* the
# per-mode reporting; the file and mode counts below are derived from the tree, so
# adding or removing a mode never needs an edit here.
TEMPLATE_MODES = ("quick", "standard", "cm", "golden-path")


def _count(paths) -> int:
    """Length of an iterable of paths, without materializing a list."""

    return sum(1 for _ in paths)


@dataclass(frozen=True)
class Inventory:
    """A measured part-count for one repository."""

    skills: int
    commands: int
    template_files: int
    template_modes: int
    root_docs: int
    docs_tree: int
    change_record_files: int
    change_record_packets: int
    starter_kits: int
    agent_roles: int
    markdown_total: int

    @property
    def authored_surface(self) -> int:
        """Hand-maintained skill + command objects (the parallel surface)."""

        return self.skills + self.commands

    @property
    def commands_per_skill(self) -> float:
        """~1.0 means a command mirrors every skill -- the duplication signal."""

        return self.commands / self.skills if self.skills else 0.0

    @property
    def prose_files(self) -> int:
        """Self-contained prose a reader or agent navigates."""

        return self.skills + self.commands + self.template_files + self.root_docs + self.docs_tree


def build_inventory(root: Path) -> Inventory:
    """Count every part under ``root`` from the filesystem (no git, no manifest)."""

    skills = _count((root / "skills").glob("*/SKILL.md"))
    commands = _count((root / "commands").glob("*.md"))

    template_files = _count((root / "templates").rglob("*.md"))
    templates_dir = root / "templates"
    template_modes = (
        sum(1 for child in templates_dir.iterdir() if child.is_dir() and any(child.rglob("*.md")))
        if templates_dir.is_dir()
        else 0
    )

    root_docs = _count(root.glob("*.md"))
    docs_tree = _count((root / "docs").rglob("*.md"))

    changes_dir = root / ".nuclear" / "changes"
    change_record_packets = sum(1 for child in changes_dir.iterdir() if child.is_dir()) if changes_dir.is_dir() else 0
    change_record_files = _count((root / ".nuclear").rglob("*.md"))

    starter_dir = root / "starter-kit"
    starter_kits = sum(1 for child in starter_dir.iterdir() if child.is_dir()) if starter_dir.is_dir() else 0

    agents_dir = root / "agents"
    agent_roles = _count(agents_dir.glob("*.md")) if agents_dir.is_dir() else 0

    markdown_total = _count(root.rglob("*.md"))

    return Inventory(
        skills=skills,
        commands=commands,
        template_files=template_files,
        template_modes=template_modes,
        root_docs=root_docs,
        docs_tree=docs_tree,
        change_record_files=change_record_files,
        change_record_packets=change_record_packets,
        starter_kits=starter_kits,
        agent_roles=agent_roles,
        markdown_total=markdown_total,
    )
