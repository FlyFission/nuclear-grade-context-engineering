# Quick Risk Record

## Selected mode

- **Mode:** Quick
- **Why this mode:** Adds one additive test guard and de-identifies existing residue; reversible, detectable, no runtime/dependency/release change.

**Purpose:** Decide whether a small change can safely stay in Quick mode, and name the proof it needs.

**Activation threshold:** Use for low-stakes changes you can undo and check easily, with no new line of user trust, no dependency trust decision, no effect on security or privacy, no change in release stance, and no change in AI power.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, move up to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden reasons to escalate, not to run a full design review.

---

## Change

- Slug: harden-residue-scan
- PR / issue: (this PR)
- Owner: FlyFission
- Date: 2026-08-01
- Summary: Widen the internal-residue scan so it covers the trees readers and agents actually consume — `.nuclear/`, `docs/`, `evals/`, `skills/`, `commands/`, `templates/`, `starter-kit/`, `tools/` — not just the ~13 top-level `PUBLIC_DOCS`, and add generic home-directory and macOS-user absolute-path patterns alongside the existing codename and mount-path checks. Scrub the pre-existing residue this newly catches (an internal codename in eight change packets/publication files and two Windows/WSL mount machine paths) so the guard starts green.

## Scope

- Affected files/configs/docs: `tests/test_public_docs.py` (new `test_repo_trees_contain_no_internal_residue`); residue scrubbed from `.nuclear/changes/{agents-skill-loading-rule,quickstart-mode-ambiguity,sharpen-scope-boundaries,targeted-agent-reading,white-paper-draft}` and `docs/06-publications/reviews/v0.3-rc1-red-team-decision-log.md`.
- User-visible behavior changed? no — a test/CI guard plus documentation de-identification; no runtime, skill, template, or command behavior changes.
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A false positive could block a future PR on a legitimate path string; mitigated by scoping to codenames and machine home/mount paths that have no legitimate use in these trees (verified zero on the current tree). |
| Reversibility | One-line: revert the commit to remove the test and restore prior wording. |
| Detectability | High: the guard itself is the detector; failures name file and token. |
| Exposure | Low: test + docs de-identification; no user data, credentials, or release surface. |
| Uncertainty | Low: the residue set and scanned trees are enumerated and verified clean before the guard is added. |
| Why Quick is enough | Additive guard + reversible docs edits; removes no capability. |

## Required proof

- Command/check/eval to run: `python -m pytest tests/test_public_docs.py -q` (incl. a teeth check: an injected residue string fails the new test), `python -m pytest -q`, `python -m ruff check .`, `python tools/ng.py doctor .`, `python tools/ng.py tokens .`, and `python tools/ng.py validate` on each scrubbed packet.
- Expected result: all pass; residue rescan across the scanned trees returns zero.
- Evidence link/location: `proof.md`.

## Critical-action self-check

Use only if the Quick change could hit the wrong target.

- Exact target: the residue scan in `tests/test_public_docs.py` and the enumerated residue occurrences.
- Expected result: only the codename/machine-path residue is removed; no result data or prose meaning changes.
- Stop condition: a scrub alters a score, a command, or a claim rather than an identifier/path.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected; — no
- a trust decision about a dependency, model, or API changed; — no
- a failure could be silent, delayed, costly, or hard to undo; — no (one-line revert)
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting; — no
- the proof will not fit in one small `proof.md`. — no

## Required links

- Packet: `.nuclear/changes/harden-residue-scan/`
- Related PR/issue: this PR
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: n/a.

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on matching rigor to stakes, keeping the approved version under control (CM), software assurance, and secure development, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
