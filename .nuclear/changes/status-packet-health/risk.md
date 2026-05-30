# Quick Risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** Small, additive CLI output change with full test coverage; no new trust boundary, dependency, or release effect, and `status` was already read-only.

**Purpose:** Decide whether the `ng status` packet-health enhancement can stay in Quick mode and name the proof required.

---

## Change

- Slug: status-packet-health
- PR / issue: repo-review enhancements (Track C functionality)
- Owner: FlyFission
- Date: 2026-05-30
- Summary: `ng status` now tags each packet `ok`, `scaffold` (untouched draft still carrying the placeholder marker), or `invalid`, and prints a closing reminder when any packet needs attention -- surfacing abandoned half-filled drafts instead of leaving them silent.

## Scope

- Affected files/configs/docs: `nuclear_grade/cli.py` (handle_status + packet_health), `tests/test_ng_cli.py`, `docs/05-reference/cli-reference.md`.
- User-visible behavior changed? yes -- `status` output gains a health tag (existing `name: mode` prefix preserved).
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A packet is mislabeled in a read-only listing; reversible. |
| Reversibility | Fully reversible; one handler plus a helper. |
| Detectability | High; covered by three CLI tests and a live run. |
| Exposure | Local CLI output. |
| Uncertainty | Low; reuses the existing validator. |
| Why Quick is enough | Read-only command, no side effects, no trust boundary. |

## Required proof

- Command/check/eval to run: `python -m pytest -q`; `python tools/ng.py status .`.
- Expected result: 78 tests pass; every in-repo packet tagged `[ok]`.
- Evidence link/location: `proof.md`.

## Escalation check

Escalate to Standard if any are true:

- users, data, security, permissions, operations, or architecture care -- no;
- a dependency/model/API trust decision changed -- no;
- failure could be silent, delayed, costly, or hard to reverse -- no;
- AI had write/execute/network/approval authority beyond drafting -- no;
- proof cannot be captured in one small `proof.md` -- false.

None apply. Quick stands.

## Required links

- Packet: `.nuclear/changes/status-packet-health/`
- Related PR/issue: repo-review enhancements
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Mode is justified as Quick.
- Required proof is named before or during the change.
- No Standard/Nuclear activation trigger is hidden.

## Source-lineage note

Original Nuclear-grade record inspired by public configuration-management and operating-experience concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
