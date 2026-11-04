# Risk: Make the package page ready for PyPI

## Selected mode

- **Mode:** Standard
- **Why:** The change adds a build-time dependency (`hatch-fancy-pypi-readme`), which is a trust decision about a dependency, and edits both the CI and release workflows. CORE.md routes both to Standard.

## Decision

Get the package ready for its first PyPI upload without publishing anything:

1. Add author, keywords, classifiers, and project links to `pyproject.toml`, so the PyPI page says what the project is and links back to it.
2. Point the README's relative links and images at GitHub for the PyPI page only, using the `hatch-fancy-pypi-readme` metadata hook. PyPI shows the README without the repo around it, so the banner, the demo GIF, the diagrams, and about fifty links would break there. `README.md` itself is unchanged.
3. Run `twine check --strict` in CI and in the release build, so a page that would not render fails before any upload.
4. Spell out the PyPI setup steps in `docs/05-reference/releasing.md`.

Main failure modes and controls:

- **The new build dependency is compromised or breaks the build.** It runs only at build time and only rewrites the long description. Control: it is a small, widely used hatch plugin from a long-time PyPA contributor, pinned to `>=24.1`; the wheel's code files are unchanged (compared against the base build), and CI's wheel-smoke installs the built wheel.
- **A substitution mangles the README on PyPI.** Control: the built metadata was checked to hold no relative link or image source, and `twine check --strict` passes. The patterns skip absolute URLs, anchors, and `mailto:`.
- **The page claims more than the project does.** Control: classifiers name only the audience, Python versions, and topic. "Development Status :: 4 - Beta" matches a 0.x release with a changelog and release gates.
- **Something publishes early.** Control: no tag, no version bump, and the `pypi` job still needs `PUBLISH_TO_PYPI=true`, the `pypi` environment, and a trusted publisher, none of which this change sets.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

The built package passes `twine check --strict`, its long description has no relative link left, the wheel's files are unchanged, and nothing is published.

## Source-lineage note

Packaging metadata follows the public Python packaging guide at https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ and the plugin's docs at https://github.com/hynek/hatch-fancy-pypi-readme. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
