# Quick Risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** Additive documentation only — one new operating-system page plus one
  index row. No code, validator logic, dependencies, permissions, or public assurance claims
  change. The page restates nothing and adds no gate; it indexes controls that already exist.

**Purpose:** Decide whether the runtime-enforcement crosswalk can safely stay in Quick mode
and name the proof required.

---

## Change

- Slug: runtime-enforcement-doctrine
- PR / issue: Runtime-enforcement crosswalk for AI-assisted engineering
- Owner: FlyFission
- Date: 2026-06-06
- Summary: Add `docs/02-operating-system/runtime-enforcement.md`, a short page that names the
  "controls should act, not merely advise" principle and maps contemporary enforceable
  AI-governance concepts onto the Nuclear-grade controls that already provide them, with a
  crosswalk table linking each to its owning file. Add one row to the `docs/README.md` "Use
  the repo" index so the page is reachable. No existing doctrine is duplicated: the
  enforcement maxims, the self-modification boundary, and the validator rungs already live in
  `MAXIMS.md`, `agent-authority-model.md`, and `validators.md`.

## Scope

- Affected files/configs/docs: `docs/02-operating-system/runtime-enforcement.md` (new),
  `docs/README.md` (one index row).
- User-visible behavior changed? no (documentation only).
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A crosswalk row points to the wrong file or reads poorly; reversible by edit. No runtime, evidence-gate, or trust-boundary effect. |
| Reversibility | Fully reversible; one new doc plus one additive index row. |
| Detectability | High; the test suite, `doctor`, `tokens`, and packet validation run green, and this page's link correctness is established by the explicit link-resolution check recorded in `proof.md`. The new page is not in the top-level public-doc test set, so its links and wording are checked by that proof step, not by `pytest`/`doctor`. |
| Exposure | Public docs, but additive and within the existing boundary wording. |
| Uncertainty | Low; no logic change; every linked control already exists and was path-checked. |
| Why Quick is enough | No new trust boundary, dependency, permission, gate, or release effect. |

## Required proof

- Command/check/eval to run: `python -m pytest -q`; `python tools/ng.py doctor .`;
  `python tools/ng.py tokens .`; `python tools/ng.py validate .nuclear/changes/runtime-enforcement-doctrine`.
- Expected result: full suite green; doctor OK; token budget OK; this packet validates; every
  internal link in the new page resolves.
- Evidence link/location: `proof.md`.

## Critical-action self-check

- Exact target: the new page and the single new row in `docs/README.md`.
- Expected result: the row is added without disturbing the `## Use the repo` and
  `## Reference foundation` headings the public-docs test asserts; every crosswalk link
  resolves to a real path.
- Stop condition: if any edit would remove an asserted heading or introduce a broken link or
  a compliance claim, stop and revert.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected — no;
- a trust decision about a dependency, model, or API changed — no;
- a failure could be silent, delayed, costly, or hard to undo — no;
- the AI had the power to write, run commands, use the network, or approve actions, beyond
  just drafting under review — no (the agent drafted documentation and ran read-only
  verification commands — tests, `doctor`, validators; it changed no product code, held no
  credentials, and the merge decision stays with a human via PR review, matching the
  accepted `prove-overlay` Quick packet, also an AI-prepared docs change);
- the proof will not fit in one small `proof.md` — false.

None apply. Quick stands. (If a follow-up adds validator code or a new gate, re-classify to
Standard.)

## Required links

- Packet: `.nuclear/changes/runtime-enforcement-doctrine/`
- Related PR/issue: Runtime-enforcement crosswalk for AI-assisted engineering
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade record inspired by public graded-rigor and software-assurance concepts
mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
