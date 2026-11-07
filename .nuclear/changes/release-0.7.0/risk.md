# Risk: Prepare release 0.7.0

## Selected mode

- **Mode:** Standard
- **Why:** The change sets the release identity that the tag, the GitHub release, and a PyPI upload will carry. A wrong version there cannot be fixed by moving the tag, only by a new version.

## Decision

Bump every version declaration from 0.6.0 to 0.7.0 and date the changelog section, so the maintainer can tag `v0.7.0` on the merge commit.

Main failure modes and controls:

- **One declaration is missed and the tag fails or ships mixed versions.** Control: `python -m nuclear_grade.release --tag v0.7.0` checks every manifest, the citation, and the changelog, and CI runs it on this PR. The release workflow runs it again against the tag.
- **The changelog date does not match the tag day.** Control: the date is 2026-11-03. If the tag goes out on another day, change the date in `CHANGELOG.md` and `CITATION.cff` together before tagging; the identity check fails if only one changes.
- **The 0.7.0 section claims something that did not merge.** Control: the section holds only the entries that were already under `[Unreleased]` on `main` after #115 to #121 and #127 merged. No entry was added or reworded.
- **Something publishes early.** Control: this change makes no tag. The PyPI job also needs `PUBLISH_TO_PYPI=true`, the `pypi` environment, and a trusted publisher.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

The release identity check passes with `--tag v0.7.0`, the built wheel reports 0.7.0, and nothing is tagged.

## Source-lineage note

See [`releasing.md`](../../../docs/05-reference/releasing.md) and [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
