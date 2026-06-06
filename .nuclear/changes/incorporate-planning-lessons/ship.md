# Ship

## Release decision

- **Decision:** ship once CI is green.
- **Rationale:** Additive, non-breaking doctrine refinements that sharpen brownfield questioning and delegated-execution legibility. No new registered artifact and no contract change, so the manifest stays accurate at 0.5.0 with no version bump.
- **Pre-merge gates:**
  - `python -m pytest -q` green (117 passed)
  - `ruff check .` clean
  - `python tools/ng.py tokens .` OK
  - `python tools/ng.py doctor .` OK
  - `python tools/ng.py validate .nuclear/changes/incorporate-planning-lessons` OK

## Evidence status summary

| Area | Status | Reference |
|---|---|---|
| Verification | pass | `verification.md` |
| Trace | pass | `trace.md` |
| Token budget | pass | `python tools/ng.py tokens .` |
| Packet self-validation | pass | `python tools/ng.py validate .nuclear/changes/incorporate-planning-lessons` |

## Self-justification guard

This packet's validator only lints structure — it cannot judge whether the additions are good. Engineering merit was gated out-of-band: an adversarial review (recorded in `basis.md`), the human approval of the plan, and the full test suite the agent cannot rewrite to a pass. This avoids the "ship green by editing your own test" trap the agent-authority model warns about.

## Rollback / restore plan

- Revert the branch; all edits are markdown and templates. No data migration and no rollback-of-state needed.
- If a single addition reads poorly in practice, edit that one file; nothing else depends on it.

## Monitoring and post-release checks

- Watch the triggering behavior of the three refreshed eval prompts; refine an individual prompt if it over- or under-triggers.
- Watch whether the work-type lens gets confused with the rigor mode in adopter use; the orthogonality sentence, the lens doc, and the mode-side cross-links (`rating-change-risk`, `risk-tiers-and-modes.md`, docs index) are the guard.

## Maintainer follow-ups

- The CHANGELOG `[Unreleased]` entry for this refinement shipped with the change; no separate follow-up remains.
- Optional stretches recorded in `basis.md`: a scored planning-eval harness and a standalone brownfield worked example.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- Source map: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Release decision recorded; rollback named; monitoring named.

## Source-lineage note

Original Nuclear-grade ship record influenced by release-readiness practice mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
