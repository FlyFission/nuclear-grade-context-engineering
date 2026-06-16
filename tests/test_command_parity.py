"""Safety net for the skills->commands single-sourcing (see gen_commands.py).

Two properties, together, make it safe to stop hand-maintaining command cards:

1. **Prompt preservation.** The one genuinely command-specific artifact -- the
   ready-to-paste prompt -- moved from each command's `## Prompt text` block into
   its skill's `## Prompt` section. `tests/fixtures/command_prompts.json` is the
   pre-teardown snapshot of those blocks, captured before any file was edited.
   We assert the prompt in the skill, and the prompt in the regenerated card, both
   equal that snapshot byte-for-byte. The snapshot is a controlled baseline of the
   prompts: a prompt may still change later, but only by deliberately updating the
   skill AND this fixture in the same diff -- which is the repo's own baseline
   discipline (Charter art. 10) applied to its load-bearing text.

2. **Exact projection.** Every card is regenerated from its skill with no drift,
   so a hand edit to a card cannot survive.
"""

import json
from pathlib import Path

from nuclear_grade import gen_commands

ROOT = Path(__file__).resolve().parents[1]
GOLDEN = json.loads(
    (ROOT / "tests" / "fixtures" / "command_prompts.json").read_text(encoding="utf-8")
)


def test_golden_covers_exactly_the_mapped_commands():
    mapping = gen_commands.load_command_map(ROOT)
    assert set(GOLDEN) == {f"{stem}.md" for stem in mapping.values()}


def test_command_map_is_a_bijection_with_command_files():
    mapping = gen_commands.load_command_map(ROOT)
    mapped_files = {f"{stem}.md" for stem in mapping.values()}
    on_disk = {path.name for path in (ROOT / "commands").glob("*.md")}
    assert mapped_files == on_disk
    assert len(set(mapping.values())) == len(mapping), "two skills map to one command"


def test_orphan_dispatcher_skill_has_no_command():
    mapping = gen_commands.load_command_map(ROOT)
    assert "using-nuclear-grade" not in mapping


def test_prompt_preserved_in_skill_byte_for_byte():
    mapping = gen_commands.load_command_map(ROOT)
    for skill_name, stem in mapping.items():
        skill_text = (ROOT / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")
        body = gen_commands.section_body(skill_text, "## Prompt")
        assert body is not None, f"{skill_name} has no ## Prompt section"
        assert body == GOLDEN[f"{stem}.md"], (
            f"{stem}: skill ## Prompt diverged from the pre-teardown snapshot; "
            f"if this prompt change is intentional, update tests/fixtures/command_prompts.json"
        )


def test_prompt_preserved_in_generated_card_byte_for_byte():
    for filename, content in gen_commands.generate(ROOT).items():
        assert gen_commands.prompt_from_command(content) == GOLDEN[filename], (
            f"{filename}: generated ## Prompt text diverged from the snapshot"
        )


def test_cards_are_an_exact_projection_of_their_skills():
    drift = gen_commands.check(ROOT)
    assert drift == [], (
        f"these cards are out of sync with their skills (run `ng gen-commands`): {drift}"
    )
