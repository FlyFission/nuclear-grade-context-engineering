# Ship: initial tool runner

## Release decision

- **Agent recommendation:** defer to the release owner.
- **Decision:** ship, recorded by the release owner (a human) after reviewing [`verification.md`](verification.md).
- **Residual risk:** the tests are a self-check by the agent that wrote the code; E-002 is deferred.

## Rollback

Revert the commit. The config is a single file.

## Monitoring

Review denied-tool messages in the agent's logs after release.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

The release owner records the decision.

## Source-lineage note

Record shape from Nuclear-grade, https://github.com/FlyFission/nuclear-grade-context-engineering. No compliance claim is made.
