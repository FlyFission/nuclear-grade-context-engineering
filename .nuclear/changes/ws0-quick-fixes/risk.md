# Quick Risk: WS0 quick fixes

## Selected mode

- **Mode:** Quick
- **Why this mode:** Documentation and citation corrections plus contributor instructions; no code, checker, dependency, release, or agent-authority change; every edit is a reversible text change with direct proof.

---

## Change

- Slug: ws0-quick-fixes
- PR / issue: draft PR from branch `claude/ws0-quick-fixes` (WS0 of the master plan)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-10-30
- Summary: Align the pre-PR checklist with CI, correct an outdated Claude Code source row, add the missing Gloaguen et al. source row that `targeted-agent-reading/basis.md` already cites, update that paper's citation to v3, tell starter-kit users how to load `AGENTS.md` when a `CLAUDE.md` exists, and replace a floor-level example in the Quick workflow.

## Scope

- Affected files/configs/docs: `CONTRIBUTING.md`; `docs/00-standards-foundation/source-map.md`; `docs/06-publications/research/related-work-matrix.md`; `docs/06-publications/arxiv/references.bib`; `docs/06-publications/nuclear-grade-context-engineering-white-paper.md` (erratum line only); `starter-kit/core/README.md`; `WORKFLOWS.md`.
- Controlled items touched: contributor instructions (`CONTRIBUTING.md`), public source wording (`source-map.md` rows), and publication citations.
- User-visible behavior changed? yes/no: no (documentation only)
- Dependency/model/API/prompt/tool permission changed? yes/no: no
- Release or rollback posture changed? yes/no: no

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A contributor runs one extra or missing local check, or a source row misstates a third party's documented behavior or a paper's finding. |
| Reversibility | Instant: revert the commit. |
| Detectability | High: the edits are seven short text changes, each quoted in `proof.md` against its source. |
| Exposure | Public docs read by contributors and adopters; no runtime surface. |
| Uncertainty | Low for checklist and citation edits; moderate for the Claude Code row, which describes vendor behavior that can change, so it is dated. |
| Why Quick is enough | The two source rows are claim-bearing wording without efficacy, assurance, or compliance language, and each is narrowed to what the cited source says. |

## Required proof

- Command/check/eval to run: `git diff --check`; `python -m pytest -q`; `python -m ruff check .`; `python tools/ng.py doctor .`; `python tools/ng.py validate .nuclear/changes/ws0-quick-fixes`; `python -m nuclear_grade.release`; `python tools/ng.py tokens .`; badge regenerated and unchanged afterwards.
- Expected result: all pass; the CONTRIBUTING commands match the steps in `.github/workflows/ci.yml`.
- Evidence link/location: `proof.md`.

## Critical-action self-check

- Exact target: the seven files listed in Scope; no file under `.nuclear/changes/` other than this packet; no closed record edited.
- Expected result: text edits only; every pinned public-docs test still passes.
- Stop condition: any test failure, or a source row that cannot be tied to a quoted source passage.

## Escalation check

None of the Standard triggers apply: no users, data, security, permissions, operations, or architecture change; no dependency, model, or API trust decision; nothing silent or hard to undo; the agent drafted text in a branch and the merge stays with the maintainer; the proof fits in one `proof.md`.

## Required links

- Packet: `.nuclear/changes/ws0-quick-fixes/`
- Related PR/issue: draft PR from `claude/ws0-quick-fixes`
- Proof record: [`proof.md`](proof.md)
- Relevant source-map/crosswalk if invoked: [`source-map.md`](../../../docs/00-standards-foundation/source-map.md)

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before the change and recorded in `proof.md`.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade record using the repository's own graded-rigor and claims discipline, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
