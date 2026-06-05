# Verification

## Claim-to-evidence

| Claim | Evidence | Status |
|---|---|---|
| Edits keep every skill's 11-section contract | `python -m pytest -q tests/test_skill_contracts.py` | pass |
| Skill bodies stay under the token budget | `python tools/ng.py tokens .` (OK: token budget) | pass |
| No overclaiming language introduced | `tests/test_public_docs.py` green | pass |
| Eval blocks keep >=3 trigger / >=2 near-miss | `test_skill_evaluation_prompts_cover_every_skill` | pass |
| Templates still validate with new fields | synthetic fixtures untouched; full suite green | pass |
| Full suite and lint clean | `python -m pytest` (117 passed); `ruff check .` | pass |
| This packet validates | `python tools/ng.py validate .nuclear/changes/incorporate-planning-lessons` | pass |
| No new always-on cost | no new skill/template/command; manifest unchanged | pass |
| Work-type/mode confusion guarded by cross-links | mode-side docs and `rating-change-risk` point to `work-type-lens.md` | pass |

## Light efficacy note (baseline vs skill)

Per the `docs/05-reference/skill-evaluation.md` method, a qualitative baseline-vs-skill check on the prompt "add a field to the user record in the billing service": a baseline plan lists the code edit. With the revised `questioning-attitude`, the agent first classifies the work as brownfield and surfaces the schema-migration, backward-compatibility, and rollback-of-state questions, then screens the runtime blast radius. The behavior delta is the migration and rollback questions a generic plan omits. Status: pass (qualitative; no automated score — a scored harness is a declined/deferred stretch).

## Gaps

- No automated planning-behavior score. Status: deferred — recorded as an optional stretch, not a blocker.

## Required links

- `plan.md`
- `ship.md`
- Source map: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Each claim maps to evidence with a status.
- Open gaps are labeled and dispositioned.

## Source-lineage note

Original Nuclear-grade verification record influenced by software-assurance and skill-evaluation practice mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
