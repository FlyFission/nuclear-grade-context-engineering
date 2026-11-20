# Ship: lessons from Headroom

## Release decision

**Decision: defer to human review.** The change goes up as a draft pull request, and merge authority stays with the maintainer. No run is made or published.

Residual risk:

- E-001 to E-006 are self-checks by the AI agent that wrote the change; a second agent instance found the gaps, which is a challenge, not independent verification. CI on a clean runner is still to come.
- No real agent run has been made under schema version 2. The tests use synthetic runs, a temporary git repository and the fake agents in the existing test.
- An ignored file inside `challenge/` (a virtual environment, say) now marks every run from that checkout as unpinned. That is intended, because the copy carries it into the agent's folder, but a person running a round must start from a clean checkout.
- The ROADMAP items bind future work only. Nothing in the repo writes into instruction files today.

## Rollback

Revert the commit. No results exist yet, so nothing else holds state.

## Monitoring

On the first real round, check that each result has an `inputs_commit` and an empty `uncommitted_inputs` list, and that the table shows no "not comparable" note. If a note appears, read its reason before comparing that row with anything.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

A human reviews the diff, CI passes on a clean runner, and the maintainer makes the merge decision.

## Source-lineage note

This is a repository change decision. It makes no compliance, certification, safety, security, or regulatory-assurance claim. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
