# Baseline

## Baseline identity

- Change: `matt-skill-lifecycle-and-flow`
- Pre-change approved source: `origin/main` at `3ade94ee994f727098a90ee7c5b69c157b107ddf`
- Candidate branch: `feat/matt-skill-lifecycle-and-flow`
- Candidate status: not approved; implementation and review pending

## Pre-change evidence

- Full pytest: pass.
- Ruff: pass.
- `ng doctor`: pass.
- `ng tokens`: pass.
- `ng eval`: 25/25 static signals.
- Command generation parity: pass.
- Codex manifest validation: pass.

## Candidate baseline rule

If the PR is merged, the merged commit becomes the new approved source baseline. The PR branch, local test run, and model-review outputs do not become approved baselines by themselves.

## Revalidation triggers

- skill status, invocation, role, command, or path changes;
- new beta/deprecated/retired content;
- plugin or installer behavior changes;
- routing scenario or scorer changes;
- token budget exceptions;
- compact-contract rollout beyond the pilot;
- workflow crosswalk or release-authority changes.

## Required links

- `risk.md`
- `verification.md`
- `ship.md`

## Exit criteria

- The pre-change and candidate identities remain distinct.
- A merge, if authorized, records the merged commit as the successor baseline.
- Every listed revalidation trigger reopens the relevant evidence.

## Source-lineage note

This record applies the public baseline disciplines mapped in `docs/00-standards-foundation/source-map.md`. It identifies software configuration state and does not create formal assurance or compliance.
