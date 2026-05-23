# Enterprise Rollout

**Purpose:** Adopt Nuclear-grade without turning every change into a process exercise.

## Pilot path

1. Pick one team and one change type with real consequence.
2. Start with Standard packets for that change type.
3. Add the validator to PR checks.
4. Require ship-readiness review only for release-facing changes.
5. Capture friction and remove fields that do not help decisions.

## Team policy starter

- Quick packets are allowed for local, reversible, easy-to-prove work.
- Standard packets are required for user, data, dependency, permission, AI-authority, operational, or release consequence.
- Stronger modes require human review and project-specific controls.
- AI-assisted changes must record agent scope, evidence, and independent checks when material.

## PR adoption

Add PR checklist items:

- Packet path or reason not needed.
- Mode selected.
- Proof command.
- Residual risk or none.
- Boundary wording checked for public docs.

## CI adoption

Run:

```bash
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/<slug>
```

Project teams can add custom checks after the Quick and Standard path is stable.

## Exit criteria

Adoption is working when reviewers can make faster, more consistent decisions from packet evidence rather than chat history or persuasion.

## Source-lineage note

This rollout guide is an original adoption pattern influenced by public lifecycle, configuration, secure development, and software assurance sources mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance.
