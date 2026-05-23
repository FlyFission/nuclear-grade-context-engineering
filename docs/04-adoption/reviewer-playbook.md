# Reviewer Playbook

**Purpose:** Review Nuclear-grade packets quickly without rereading the whole repo.

## Review sequence

1. Read `questioning-attitude.md` if present, then `risk.md`, and confirm the selected mode.
2. Read `basis.md`, `spec.md`, or `proof.md` for what must remain true.
3. Inspect `trace.md` for claim-to-evidence links.
4. Inspect `verification.md` for evidence status and gaps.
5. Inspect `ship.md` or `decision.md` for release decision, rollback, monitoring, residual risk, and baseline trigger.
6. Run or inspect validator output.

## What to challenge

- Claims broader than evidence.
- Unvalidated assumptions hidden behind confident prose.
- Quick mode hiding Standard triggers.
- Missing rollback or monitoring for release-facing work.
- AI authority broader than recorded.
- Public wording that implies compliance, certification, approval, safety, security, or formal verification.

## What not to demand

- Full source-family essays in every packet.
- Nuclear-mode artifacts when consequence does not activate them.
- Perfect prose before evidence is clear.

## Exit criteria

Approve the packet only when the decision is reviewable: what changed, why it matters, what proves it, what remains uncertain, and what happens if it fails.

## Source-lineage note

This playbook is an original review workflow influenced by public software assurance, configuration management, secure development, and release-readiness sources mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance.
