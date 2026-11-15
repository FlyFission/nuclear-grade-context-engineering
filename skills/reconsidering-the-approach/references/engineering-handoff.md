# Architecture and spec-to-code handoff

This council does not itself approve changes. A winning alternative produces a **proposal** mapped onto Nuclear-grade's normal Question → Discover → Specify → Plan → Execute → Verify → Review → Decide → Baseline → Operate → Learn path.

## Draft ADR (for significant software choices)

- Title, status `PROPOSED`, accepted user outcome, decision owner and current lifecycle stage
- Accepted baseline, version/commit, decision drivers and non-goals
- Candidates considered and discarded, why each was rejected, and the strongest minority objection
- Selection rationale, observed evidence, unknowns, assumptions, cost/schedule uncertainty and sensitivity
- Invariants and non-negotiable guardrails (correctness, security, privacy, performance, boundary/authority)
- Data model/schema, interface and API contracts, integration boundaries and dependent modules
- Rollout/migration, data compatibility, rollback/compensation, irreversible side effects
- Verification strategy, test acceptance gates, owners and evidence paths
- Observable reversal/kill criteria and milestone
- Required decision right, human signoff, and change impact if `REOPEN` or `ESCALATE`

## Ordered implementation plan (not an approval)

For each increment identify actual file/module paths **when inspected**; otherwise label placeholders clearly. Provide input/output type/contracts, invariant, edge cases and expected failures; tests with executable commands where grounded; dependency and integration checkpoint; rollback or compensating action; evidence and acceptance owner. Start from the smallest end-to-end working slice rather than a large speculative rewrite. Do not replace approved tests or requirements to make the new design pass.

## Build permissions and proof

If the user explicitly requested *build* and the repo controls authorize implementation, proceed into existing Execute/Verify: inspect the working tree, protect user changes, write clean idiomatic code, run appropriate tests, inspect generated artifacts and diff, report changed paths, completed/failed checks, and provenance. No code from a debating council is production-ready by virtue of consensus. For regulated or safety-related work, qualified independent review and the designated human authority remain mandatory where applicable.

If the user asked *brainstorm* or *decide*, stop after a proposal, draft ADR, and feasible discriminating test. Do not write files, call external models, deploy, spend funds, or alter controlled baselines without permission.

## Lifecycle re-entry

- `CONTINUE`: return to previously active stage with the old approved scope unchanged.
- `REFINE`: limited changes to an editable draft; return to appropriate Specify/Plan phase if affected.
- `REOPEN`: accepted requirement/ADR needs owner's explicit approval; collect impact and proposal, do not silently change.
- `ESCALATE`: high-consequence missing evidence or unavailable authority; name exact decision and owner, hold affected work.

A council cannot raise itself into a human authority role or modify the review/ship gate.
