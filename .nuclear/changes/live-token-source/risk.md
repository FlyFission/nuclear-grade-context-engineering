# Live token source — risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** This is a small, reversible correction to public guidance with no runtime, dependency, permission, or release effect.

## Change

- Slug: `live-token-source`
- PR / issue: PR from `docs/daily-1pct-20260728-live-token-source`
- Owner: FlyFission
- Date: 2026-07-28
- Summary: Replace stale undated token totals in `CORE.md` with the command that produces live totals and a link to explicitly dated snapshots.

## Scope

- Affected files/configs/docs: `CORE.md` and this Quick packet
- User-visible behavior changed? no; documentation accuracy only
- Dependency/model/API/prompt/tool permission changed? no
- Release or rollback posture changed? no

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A reader follows the existing command and sees the live figures; no executable behavior changes. |
| Reversibility | One normal revert. |
| Detectability | `ng tokens`, public-doc tests, and diff review expose the result. |
| Exposure | One paragraph in adoption guidance. |
| Uncertainty | Low: the live command reports 61,650 body tokens while the paragraph says about 35k. |
| Why Quick is enough | The change removes a stale number rather than changing token policy or tooling. |

## Required proof

- Command/check/eval to run: `python tools/ng.py tokens .`, `python -m pytest tests/test_public_docs.py -q`, `git diff --check`
- Expected result: token command passes and reports live totals; public-doc tests and whitespace check pass.
- Evidence link/location: `proof.md`

## Critical-action self-check

- Exact target: only the undated measurement paragraph in `CORE.md`
- Expected result: live command becomes the source for mutable totals; dated audit snapshots remain historical.
- Stop condition: any test failure or change outside the paragraph and packet.

## Escalation check

No Standard trigger is present: no users, data, security, permissions, dependencies, operations, architecture, release stance, or hard-to-reverse action changes.

## Required links

- Packet: `.nuclear/changes/live-token-source/`
- Related PR/issue: PR from `docs/daily-1pct-20260728-live-token-source`
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: not invoked

## Exit criteria

- The live counter is the only undated source cited for current totals.
- The historical audit is described as dated snapshots.
- Targeted checks pass.

## Source-lineage note

This record uses the repository's own deterministic token counter and checked-in audit as primary evidence. No outside-standard or compliance claim is made; broader lineage conventions are mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md).
