# Reviewer Playbook

**Purpose:** Review Nuclear-grade packets quickly without rereading the whole repo.

## Review sequence

1. Read `questioning-attitude.md` if present, then `risk.md`, and confirm the selected mode.
2. Read `basis.md`, `spec.md`, or `proof.md` for what must remain true.
3. Inspect `trace.md` for claim-to-evidence links.
4. Inspect `verification.md` for evidence status and gaps.
5. Inspect `ship.md` or `decision.md` for release decision, rollback, monitoring, residual risk, and baseline trigger.
6. Inspect `turnover.md` or `self-check.md` when work transferred or critical actions occurred.
7. Run or inspect validator output.

## What to challenge

- Wrong or missing decision question.
- Instructions that are understandable only if read charitably, but still easy for a tired agent to misuse.
- Claims broader than evidence.
- Unvalidated assumptions hidden behind confident prose.
- Subjective confidence, source claims, or vendor language treated as local proof.
- Quick mode hiding Standard triggers.
- Fast candidate work treated as accepted configuration before audit gates.
- Premature baseline or release decision before evidence, rollback, monitoring, and residual risk are visible.
- Missing rollback or monitoring for release-facing work.
- AI authority broader than recorded.
- Public wording that implies compliance, certification, approval, safety, security, or formal verification.
- Missing turnover state when another agent, reviewer, verifier, releaser, support owner, or resumed thread continues work.
- A critical action with no target, expected result, stop condition, or after-action evidence.
- Vendor, model, API, or dependency claims treated as local proof.

## Verification challenge

Ask what kind of checking is being claimed:

| Claim | Reviewer challenge |
|---|---|
| self-check | Was the target and expected result named before action? |
| peer-check | Did another reviewer prevent a likely wrong action before it happened? |
| concurrent verification | Was the high-consequence action observed as it happened? |
| independent verification | Was final state checked separately from the performer claim? |
| peer review | Was the artifact reviewed for usability, scoped claims, and evidence fit? |

## What not to demand

- Full source-family essays in every packet.
- Nuclear-mode artifacts when consequence does not activate them.
- Perfect prose before evidence is clear.
- Slow procedure for reversible exploration when only acceptance needs stronger evidence.

## Exit criteria

Approve the packet only when the decision is reviewable: what changed, why it matters, what proves it, what remains uncertain, and what happens if it fails.

## Source-lineage note

This playbook is an original review workflow influenced by public software assurance, configuration management, secure development, and release-readiness sources mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance.
