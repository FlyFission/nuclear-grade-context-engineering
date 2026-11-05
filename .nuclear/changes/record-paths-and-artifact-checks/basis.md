# Basis: record paths and artifact checks

## Need and design

The user's public-release review identified concrete code and publication defects. Use existing stdlib and repository patterns. Reject invalid record names and resolved output escapes before any write, using one validator for CLI/MCP. Bound agent termination and output collection instead of assuming parent death closes descendant pipes. Remove third-party abstract/summary text, preserving citations and repo-authored analysis. Expand regression scanning to raw publication destinations; distinguish fixtures and public author attribution from accidental residue.

## Alternatives

Prefer removing copied abstracts to an unverified blanket reuse claim. Prefer explicit validation to normalizing attacker-controlled names. Prefer bounded output collection to waiting indefinitely for descendants. Keep history cleanup as a coordinated maintainer operation rather than silently force-pushing old branches. These are implementer choices under the user's instruction to fix the audit findings.

## Requirements

| ID | Requirement | Proof |
|---|---|---|
| REQ-001 | CLI and MCP refuse escaping/non-name slugs and output symlinks outside the permitted packet | CLI/MCP regression tests |
| REQ-002 | Agent timeout returns after bounded cleanup even if a descendant retains pipes | harness subprocess regression |
| REQ-003 | Research metadata retains citations without copied abstract/summary fields | metadata regression |
| REQ-004 | Public-artifact regression checks include challenge-results, diffs, YAML and mailbox review | artifact review fixtures and repository scan |
| REQ-005 | Release inventory discloses current corpus, provenance, historical exposure, and review limits | source review and cleanup runbook |

## Interfaces and limitations

No dependencies added; Python 3.11+ remains supported. Ordinary record names and successful CLI behavior stay compatible; nested path names are deliberately rejected. Filesystem checks are not race-proof sandboxing against a concurrently malicious process. The harness runs trusted local tools inside a disposable environment; timeout cleanup is not containment. Publicly intentional author attribution is not treated as accidental disclosure.

## Required links

[risk.md](risk.md), [basis.md](basis.md), [plan.md](plan.md), [trace.md](trace.md), [verification.md](verification.md), [ship.md](ship.md).

## Exit criteria

The scoped regressions pass, remaining gaps are explicit, and maintainer review precedes merge.

## Source-lineage note

Original project remediation record using the public-source workflow mapped in [source-map.md](../../../docs/00-standards-foundation/source-map.md). No certification, legal opinion, or assurance claim.
