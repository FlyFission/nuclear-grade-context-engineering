# Ship: challenge results harness

## Release decision

- **Agent recommendation:** defer to the maintainer.
- **Decision:** defer to the maintainer, a human, who decides after reviewing [`verification.md`](verification.md) and the CI run.
- **Residual risk:** all evidence is a self-check by the AI agent that wrote the change; E-003 (real agent CLIs) is deferred until the first scored round; nothing enforces the container rule.

## Rollback

Revert the commit. The harness is a new folder; the scorer change only adds an output flag.

## Monitoring

Before the first published round, run each agent once with `--trials 1` and compare the transcript to its CLI's current help. Watch dispute issues after publishing.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

The maintainer records the decision.

## Source-lineage note

Original Nuclear-grade record inspired by public configuration-management and operating-experience concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
