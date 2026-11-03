# Risk: Menu descriptions for the command cards

## Selected mode

- **Mode:** Standard
- **Why:** The change edits all 29 generated command cards, which are controlled prompts, and changes what Claude Code may do with them: the cards stop being something the model can call on its own. A change in AI power routes to Standard.

## Decision

Give each generated card Claude Code frontmatter:

- `description`: the first sentence of the paired skill's description. Today the cards have no frontmatter, so Claude Code falls back to the first line, and the `/` menu shows `# ng-prove` and the like. `claude plugin validate .` warns once per card.
- `disable-model-invocation: true`: the card runs when a person types it. The paired skill is already listed to the model with a fuller description, so listing the card as well would add a second entry for the same idea to every session's context.

To keep each card inside its token ceiling, the card drops the quoted copy of the full skill description (the first sentence is now in the frontmatter, and the rest repeats the card's own "Use when" and "Do not use when" sections), and the generation note and closing pointer are a little shorter.

Main failure modes and controls:

- **Someone relied on Claude calling `ng-*` on its own.** The paired skills still load on their own, so the behavior stays reachable through the skill. Control: the PR says so, and the change is one line in the generator to undo.
- **Frontmatter breaks other tools that read the cards as plain prompts.** The frontmatter is three short lines at the top of a Markdown file. Control: the rest of the card is unchanged in order and content, and the prompt text is still byte-for-byte (`tests/test_command_parity.py`).
- **A card grows past its ceiling later.** Control: every card is smaller than before; the largest went from 1,699 to 1,620 tokens, and the command total from 30,462 to 28,782.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Every card has the two fields, the token gate passes with room, the parity and contract tests pass, and `claude plugin validate .` stops warning about the cards.

## Source-lineage note

Claude Code's frontmatter fields are described in its public docs at https://code.claude.com/docs/en/slash-commands. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
