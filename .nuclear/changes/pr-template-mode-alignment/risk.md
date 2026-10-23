# PR template mode alignment — risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** This is a small, reversible correction to contributor guidance. It changes no runtime behavior, dependency, permission, public claim, or release stance.

## Change

- Slug: `pr-template-mode-alignment`
- Owner: FlyFission
- Date: 2026-08-03
- Summary: Let contributors select the documented administrative floor in the pull-request template and tie packet omission to that mode rather than to a file type.

## Scope and risk

- Affected item: `.github/PULL_REQUEST_TEMPLATE.md`
- Failure addressed: the template currently starts at Quick even though repository guidance permits an administrative floor, and it implies that being docs-only is enough to omit a packet.
- Main risk: contributors could overuse the floor. The revised wording requires them to name why it is the lightest honest mode; existing mode triggers remain unchanged.
- Reversibility: one normal revert.

## Required proof

- Inspect the focused diff.
- Run `python -m pytest tests/test_public_docs.py -q`, `python tools/ng.py doctor .`, and `git diff --check`.
- Record results in `proof.md` before commit.

## Exit criteria

- The template names all documented mode levels.
- Packet omission depends on the administrative-floor criteria, not on whether a change edits documentation.
- No new gate, artifact, or mode is introduced.

## Required links

- Changed item: [`.github/PULL_REQUEST_TEMPLATE.md`](../../../.github/PULL_REQUEST_TEMPLATE.md)
- Proof record: [`proof.md`](proof.md)

## Source-lineage note

This change reconciles the repository's own contributor surfaces. It invokes no outside standard and makes no efficacy, compliance, or safety claim; broader lineage conventions remain in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
