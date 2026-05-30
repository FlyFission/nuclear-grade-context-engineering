# Enterprise Rollout

**Purpose:** Adopt Nuclear-grade without turning every change into a paperwork drill.

Adoption should keep two speeds. Teams move fast while they try out reversible ideas. They slow down at the acceptance gates: claims, controlled items, public wording, the version everyone agreed is correct, releases, and agent authority.

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
- Teams should not add Standard records to reversible Quick work just to look careful. The control should change a decision.

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

Project teams can add their own checks once the Quick and Standard path is stable.

## Exit criteria

Adoption is working when reviewers decide faster and more consistently from packet evidence, not from chat history or a sales pitch.

## Source-lineage note

This rollout guide is an original adoption pattern. Public sources on lifecycle, configuration, secure development, and software assurance shaped it. Those sources are mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance.
