# Command Authoring Contract

**Purpose:** Keep portable command prompts clear, easy to paste, and honest about how far they are wired in.

Command cards are **generated, not hand-authored**. Each `commands/<name>.md` is projected from its paired skill by `ng gen-commands` (see `nuclear_grade/gen_commands.py`), so the skill is the single source of truth and the card cannot drift from it.

## How to change a command

1. Edit the paired skill at `skills/<skill>/SKILL.md` — including its `## Prompt` section, which holds the exact prompt text.
2. Run `python tools/ng.py gen-commands` to regenerate the cards.
3. CI runs `python tools/ng.py gen-commands --check`; a card edited by hand fails it.

The skill→command pairing is declared in `nuclear-grade.yaml` under `command_map:`. It is semantic (`proving-claims` → `ng-prove`), so it cannot be inferred from names. A skill with no entry there — the `using-nuclear-grade` dispatcher — has no command.

## Generated structure

Every card lives at `commands/<name>.md` and contains, in order:

- a one-line note naming the source skill,
- the skill's `description` as a one-line summary,
- `## Use when` (from the skill's `## When to Use`),
- `## Do not use when` (from `## When Not to Use`),
- `## Inputs` (from `## Inputs`),
- `## Prompt text` (from the skill's `## Prompt`, byte-for-byte),
- `## Verification` (from the skill's `## Verification`),
- `## Full skill` — a pointer back to the skill for the overview, process, outputs, escalation, failure modes, and source lineage, with the assurance-boundary note.

## Writing rules

- In Public v0, call them portable command prompts (never "slash commands").
- Keep the prompt text in the skill's `## Prompt` section; it is preserved exactly in the card.
- Everything a reader needs beyond the prompt lives in the skill the card points to, so the card stays thin.

## Tests

`tests/test_command_contracts.py` checks the public section contract. `tests/test_command_parity.py` checks that each prompt was preserved byte-for-byte when it moved into its skill, and that every card is an exact projection of its skill (no hand edits).

## Source-lineage note

This contract is an original writing standard for Nuclear-grade command prompts. It does not create formal assurance or compliance.
