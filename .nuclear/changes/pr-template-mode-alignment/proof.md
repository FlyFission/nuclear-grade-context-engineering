# PR template mode alignment — proof

## Claim

The pull-request template now permits the repository's documented administrative floor and no longer treats “docs-only” as the condition for omitting a packet.

## Method

- Environment: disposable clone of `origin/main`, Python 3.12.
- Inspect the focused diff and compare the template wording with the mode guidance in `README.md` and `AGENTS.md`.
- Run `python -m pytest tests/test_public_docs.py -q`, `python tools/ng.py doctor .`, and `git diff --check`.
- Evidence is reproducible from checked-in files; the AI-assisted author selected and summarized it, while CI and reviewer reruns provide separate execution paths.

## Result

- Evidence status: pass
- Actual result: 15 targeted public-doc tests and the full pytest suite passed; Ruff passed; repository doctor returned `OK`; packet validation and `git diff --check` passed.

## Reviewer note

Confirm that the wording closes the mismatch without making the administrative floor easier to misuse or adding a new review ritual.

## Required links

- Changed item: [`.github/PULL_REQUEST_TEMPLATE.md`](../../../.github/PULL_REQUEST_TEMPLATE.md)
- Risk record: [`risk.md`](risk.md)

## Exit criteria

- The diff is limited to the template and its Quick packet.
- All listed checks pass.
- A reviewer can revert the change in one commit.

## Source-lineage note

The proof compares checked-in repository guidance and uses checked-in tests and tooling. It does not create a safety, security, compliance, or assurance claim; broader lineage conventions remain in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
