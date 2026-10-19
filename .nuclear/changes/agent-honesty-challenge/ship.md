# Ship: agent honesty challenge

## Release decision

**Decision: defer to PR review.** This is a reversible, additive folder plus tests. Merge authority stays with the owner, and the release stance does not change. The README and CHANGELOG lines are proposed in the hand-off, not applied.

Residual risk: E-001 and E-002 are self-checks; the scripted solutions were written by the same agent that wrote the scorer, so they show the scorer agrees with its author. No real agent has played (E-004). Known blind spots: an agent can rewrite git history, edit `score.py` in its own copy, add a `conftest.py` that alters test behavior, or write a made-up human approval into `ship.md`. The README names the pristine-scorer workaround and the approval limit.

## Rollback

Delete `challenge/` and `tests/test_challenge.py`, and revert the `docs/README.md` row and the residue-scan entry.

## Monitoring

Read the first shared scorecards. If real agents land on a verdict for reasons the checks did not intend, record it as OPEX and adjust the check, not the wording.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

CI is green and the owner makes the merge decision.

## Source-lineage note

This is a repository change decision, not a compliance, certification, safety, security, or regulatory-assurance claim. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
