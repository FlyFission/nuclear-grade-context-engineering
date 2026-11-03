# Skill Consolidation — Risk

## Change identity

- Slug: skill-consolidation
- PR / issue: draft PR from `claude/skill-consolidation`, stacked on `claude/independent-review-fact-check` (#124)
- Owner: FlyFission
- Date: 2026-11-03
- Current lifecycle phase: Verify / Review / Decide
- Summary: The owner allowed consolidating the skill catalog "if we're high confident", as long as the smaller set still covers what the larger did and no merged skill becomes "a hammer to drive a screw". The owner also asked for a simpler README and excellent visuals. Seven merges were tested under a pre-registered protocol. One passed and was applied, then failed the final-state evidence the external reviews asked for, and was reverted. The catalog stays at 31 skills. The README is rewritten and the skill visuals are rebuilt.

## Questioning-attitude summary

- Decision question: Does each applied merge keep every capability, route as well as the originals, and avoid forcing the wrong work on any job its parts used to do?
- Assumptions that set the mode: skills, command cards, the catalog manifest, the README, and diagrams are controlled items, and adopters type `/ng-*` names.
- Facts still needing validation: whether merges that failed narrowly (M2) would pass after a further revision. That needs a new, separately pre-registered test.
- Stop or hold conditions: hold if any applied merge fails a criterion, if a count disagrees with the catalog, if a figure omits a skill, or if a README boundary statement is lost.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `skills/`, `commands/` | skills and cards | Unchanged in the end: the one merge was reverted | repo |
| `nuclear-grade.yaml`, tests, `tests/fixtures/command_prompts.json` | manifest and contracts | Catalog membership and the parity snapshot | repo |
| `README.md` | public landing page | Rewritten for brevity; boundary wording must survive | repo |
| `tools/build_diagrams.py`, `docs/assets/diagrams/skill-*.svg`, `docs/diagrams.md`, `SKILLS.md` | diagrams | Visual catalog, invocation flow, full skill map | repo |
| `CORE.md`, `COMMANDS.md`, `INSTALL.md`, `WORKFLOWS.md`, reference docs, evals cases, prompt bank | catalog docs | Counts and names | repo |
| `evals/skill-consolidation/` | evaluation | Protocol, data, report | repo |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Adopters lose two slash-command names; the README is the first thing every visitor reads |
| Reversibility | high | `git revert` plus `ng gen-commands` and `python tools/build_diagrams.py` |
| Detectability | medium | Contract, parity, and diagram-coverage tests catch catalog drift; a lost nuance in a merged skill would not be caught by any test |
| Exposure | high | Public repo and plugin |
| Uncertainty | medium | Every check was done by agents of one model family; samples per merge are small |
| Dependency trust | low | No dependency change |
| AI authority | medium | An AI agent designed, ran, and recorded the evaluation; a human owns the merge |

## Selected mode

- **Mode:** Standard
- Why this mode: it removes and renames skills adopters use, rewrites the public landing page, and rests on an evaluation someone will rely on.
- Why lighter mode is not enough: each merge decision has to trace to pre-registered evidence.
- Why heavier mode is not yet required: no production system, credential, permission, or release action; one reversible merge.

## Immediate proof obligations

- Before build: the protocol committed before any result; both coverage rounds kept.
- Before merge: full pre-PR gate green; diagram-coverage test green; every count is 30; README boundary statements present.
- Independent review needed? Yes. All evaluation agents share the author's model family and orchestrator. The owner is the pending second party.

## Required links

- Protocol: `../../../evals/skill-consolidation/PROTOCOL.md`
- Report: `../../../evals/skill-consolidation/REPORT.md`
- Basis: `basis.md`
- Verification: `verification.md`
- Ship: `ship.md`

## Exit criteria

- Mode justified; controlled items explicit; stop conditions named.

## Source-lineage note

Original Nuclear-grade packet inspired by public configuration-management and verification practice mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
