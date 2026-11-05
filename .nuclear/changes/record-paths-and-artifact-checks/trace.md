# Trace: record paths and artifact checks

| ID | Need | Control | Evidence | Status |
|---|---|---|---|---|
| REQ-001 | Confined record writes | shared CLI/MCP name/output validation | tests/test_ng_cli.py and tests/test_mcp_server.py | pass |
| REQ-002 | Bounded timeout cleanup | challenge-results/run.py helper | tests/test_challenge_results.py | pass |
| REQ-003 | Remove unverified copied abstracts | research metadata cleanup | tests/test_research_metadata.py | pass |
| REQ-004 | Cover public transcripts and diffs | expanded artifact review regression | public artifact tests | pass |
| REQ-005 | Honest release inventory and history limits | release-review and artifact review guidance | source inspection | pass |

## Required links

[risk.md](risk.md), [basis.md](basis.md), [plan.md](plan.md), [trace.md](trace.md), [verification.md](verification.md), [ship.md](ship.md).

## Exit criteria

The scoped regressions pass, remaining gaps are explicit, and maintainer review precedes merge.

## Source-lineage note

Original project remediation record using the public-source workflow mapped in [source-map.md](../../../docs/00-standards-foundation/source-map.md). No certification, legal opinion, or assurance claim.
