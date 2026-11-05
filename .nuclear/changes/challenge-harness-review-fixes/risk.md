# Risk: Fix five gaps a code review found in the challenge harness

## Selected mode

- **Mode:** Standard
- **Why:** The harness decides what the repo will say in public about named coding agents. A run that is lost, mis-scored, or missing its environment could mislabel a real tool.

## Decision

An automated code review of the merged harness raised ten findings. Each was traced against the code. Nine are fixed here (item 8 covers two):

1. Run IDs were unique only to the second, so two runs could overwrite each other. They now carry a random part, and a run refuses to replace an earlier file.
2. A timeout killed only the agent's CLI. A child process could keep editing the folder while it was staged and scored. The agent now runs in its own process group, which is stopped on timeout (POSIX; elsewhere only the CLI is stopped, and the harness already asks for a container).
3. The diff was taken against `HEAD`, which an agent moves when it commits. It is now taken against the root commit, the same baseline the scorer uses.
4. Runs did not record the OS or container image that METHOD.md's Pinning section asks for. They do now; the image comes from `NG_CONTAINER_IMAGE`.
5. The scorer reports a failed record before failing tests, so a run with failing tests could count as "record does not validate", a good outcome on the plain track. That outcome now needs passing tests.
6. Rulings were checked only for `run_id` and `outcome`. All five fields METHOD.md lists are now required.
7. `pypi-package-page/risk.md` called `>=24.1` a pin. It is a minimum version, and the record now says so.
8. The command-card record said 29 cards; after the merge with `main` there are 30. A new test checks each card against its skill directly, not through the generator.

One was traced and left as it is: README directory links on PyPI use `/blob/main/`, which GitHub answers with a redirect to `/tree/main/`, so they work.

Main failure modes and controls:

- **The process-group change breaks normal runs.** Control: all earlier harness tests still pass, and a new test shows a timed-out agent's child is stopped.
- **A stricter ruling check rejects a real ruling.** No rulings exist yet. The fields are the ones METHOD.md already lists.
- **A rule changes after results are seen.** No round has been published. METHOD.md logs the change with the date and reason.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Each new test fails on the old code and passes on the new, and every gate passes.

## Source-lineage note

See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
