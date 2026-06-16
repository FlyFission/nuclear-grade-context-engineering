"""Generate the portable command cards under ``commands/`` from their skills.

Single source of truth
-----------------------
A command card (``commands/ng-*.md``) used to be hand-authored prose that
restated its paired skill in different words -- 26 commands shadowing 26 skills,
two files to keep in sync for one idea. This module makes the skill the only
hand-maintained source: each card is *projected* from ``skills/<name>/SKILL.md``.

What is projected, and what moved
---------------------------------
The card pulls four sections straight from the skill -- ``When to Use`` ->
``Use when``, ``When Not to Use`` -> ``Do not use when``, ``Inputs``, and
``Verification`` -- plus the skill's frontmatter ``description`` as the lead.
The one genuinely command-specific artifact, the ready-to-paste prompt, now
lives in the skill as a ``## Prompt`` section (moved there verbatim, byte-for-byte
preserved -- see ``tests/test_command_parity.py``). Everything else a reader
might want (process, outputs, escalation, failure modes, source lineage) stays
in the skill; the card points at it rather than duplicating it.

The skill -> command link is semantic (``proving-claims`` -> ``ng-prove``), so it
cannot be computed from names; it is declared once in ``nuclear-grade.yaml`` under
``command_map:``. The link is NOT stored in skill frontmatter on purpose: skill
frontmatter follows the Anthropic skill-creator convention (a closed set of keys,
guarded by ``tests/test_skill_contracts.py``), and a custom key would break both
that contract and the convention.

Boundary
--------
This generator shapes documentation. It does not decide whether a command, skill,
or its evidence is correct, safe, secure, or compliant.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from nuclear_grade.tokens import split_frontmatter

# The skill sections a card projects, mapped to the card's own section headers.
# Order here is the order they appear in the generated card.
_SECTION_MAP = (
    ("## When to Use", "## Use when"),
    ("## When Not to Use", "## Do not use when"),
    ("## Inputs", "## Inputs"),
    ("## Prompt", "## Prompt text"),
    ("## Verification", "## Verification"),
)

# The card's required sections, in order -- the public contract `ng doctor` and
# `tests/test_command_contracts.py` enforce. Derived from _SECTION_MAP so the
# generator and the contract cannot drift apart.
REQUIRED_CARD_SECTIONS = tuple(card_header for _, card_header in _SECTION_MAP)


def section_body(text: str, header: str) -> str | None:
    """Return the verbatim body of the ``## header`` section, or ``None``.

    The body is every line after the header up to the next ``## `` heading,
    with surrounding blank lines trimmed but internal formatting preserved
    exactly (so a moved prompt round-trips byte-for-byte). Fenced code blocks
    are honored: a ``## `` line *inside* a fence is content, not a new section,
    so a prompt that happens to contain a Markdown-looking line is not truncated.
    """

    lines = text.split("\n")
    start: int | None = None
    for i, line in enumerate(lines):
        if line.strip() == header:
            start = i + 1
            break
    if start is None:
        return None

    body: list[str] = []
    in_fence = False
    for line in lines[start:]:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            body.append(line)
            continue
        if line.startswith("## ") and not in_fence:
            break
        body.append(line)
    return "\n".join(body).strip("\n")


def prompt_from_command(text: str) -> str | None:
    """Return a command card's ``## Prompt text`` body (verbatim), or ``None``.

    Used to snapshot the load-bearing artifact before the prompt is moved into
    its skill, and to assert the move preserved it byte-for-byte.
    """

    return section_body(text, "## Prompt text")


def load_command_map(repo: Path) -> dict[str, str]:
    """Read ``command_map:`` from ``nuclear-grade.yaml`` as ``{skill: ng-name}``.

    Parsed with a tiny stdlib reader (the repo carries no YAML dependency, by the
    same design constraint as ``tokens.load_budgets``): the flat ``key: value``
    pairs indented under a top-level ``command_map:`` key.
    """

    catalog = repo / "nuclear-grade.yaml"
    mapping: dict[str, str] = {}
    if not catalog.exists():
        return mapping
    text = catalog.read_text(encoding="utf-8").replace("\r\n", "\n")
    in_block = False
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line[0].isspace():
            in_block = line.strip() == "command_map:"
            continue
        if in_block and ":" in line:
            key, _, value = line.strip().partition(":")
            mapping[key.strip()] = value.strip()
    return mapping


@dataclass(frozen=True)
class CardSource:
    """The projected pieces of one skill needed to render its command card."""

    skill_name: str
    command_stem: str
    skill_rel: str  # repo-relative path, e.g. "skills/proving-claims/SKILL.md"
    description: str
    bodies: dict[str, str]  # card_header -> body text


def _parse_skill(repo: Path, skill_name: str, command_stem: str) -> CardSource:
    skill_path = repo / "skills" / skill_name / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    description, _ = split_frontmatter(text)
    bodies: dict[str, str] = {}
    missing: list[str] = []
    for skill_header, card_header in _SECTION_MAP:
        body = section_body(text, skill_header)
        if body is None:
            missing.append(skill_header)
        bodies[card_header] = body or ""
    if missing:
        raise ValueError(
            f"skills/{skill_name}/SKILL.md cannot back command {command_stem}: "
            f"missing section(s) {', '.join(missing)}"
        )
    return CardSource(
        skill_name=skill_name,
        command_stem=command_stem,
        skill_rel=f"skills/{skill_name}/SKILL.md",
        description=description,
        bodies=bodies,
    )


def render_card(source: CardSource) -> str:
    """Render one command card from its skill projection.

    The lead and the closing pointer both embed the skill path, so the
    boilerplate differs per card and never registers as repeated prose in the
    `ng tokens` redundancy gate.
    """

    return (
        f"# {source.command_stem}\n\n"
        f"Portable command prompt generated from `{source.skill_rel}`. "
        "Edit the skill, then run `python tools/ng.py gen-commands`; "
        "do not edit this file by hand.\n\n"
        f"> {source.description}\n\n"
        f"## Use when\n\n{source.bodies['## Use when']}\n\n"
        f"## Do not use when\n\n{source.bodies['## Do not use when']}\n\n"
        f"## Inputs\n\n{source.bodies['## Inputs']}\n\n"
        f"## Prompt text\n\n{source.bodies['## Prompt text']}\n\n"
        f"## Verification\n\n{source.bodies['## Verification']}\n\n"
        "## Full skill\n\n"
        "For the overview, process, outputs, escalation, common rationalizations, "
        f"red flags, and source lineage, see `{source.skill_rel}`. This command sets "
        "up evidence for engineering review; it does not create compliance, formal "
        "V&V, safety, security, certification, or regulatory adequacy "
        "(see `DISCLAIMER.md`).\n"
    )


def generate(repo: Path) -> dict[str, str]:
    """Return ``{command_filename: rendered_text}`` for every mapped skill."""

    mapping = load_command_map(repo)
    out: dict[str, str] = {}
    for skill_name, command_stem in sorted(mapping.items()):
        source = _parse_skill(repo, skill_name, command_stem)
        out[f"{command_stem}.md"] = render_card(source)
    return out


def check(repo: Path) -> list[str]:
    """Return command filenames whose on-disk content differs from generation.

    The drift signal for CI: empty means the cards are an exact projection of
    the skills; a non-empty list names every card that a regeneration would
    change (or that has no skill backing it).
    """

    commands_dir = repo / "commands"
    expected = generate(repo)
    drifted: list[str] = []
    for filename, content in expected.items():
        path = commands_dir / filename
        current = path.read_text(encoding="utf-8").replace("\r\n", "\n") if path.exists() else None
        if current != content:
            drifted.append(filename)
    # A command file with no backing skill in command_map is also drift.
    for path in sorted(commands_dir.glob("*.md")):
        if path.name not in expected:
            drifted.append(path.name)
    return sorted(set(drifted))


def write(repo: Path) -> list[str]:
    """Write every generated card to ``commands/``; return the filenames written."""

    commands_dir = repo / "commands"
    commands_dir.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    for filename, content in generate(repo).items():
        (commands_dir / filename).write_text(content, encoding="utf-8")
        written.append(filename)
    return sorted(written)
