# Risk — ADR governance lessons and landscape benchmark

## Selected mode

- **Mode:** Standard
- **Why:** The change touches CI (`.github/`), widens a dependency range (`mcp<2` to `mcp<3`), and adds validator output that other tooling may consume. Each is a trust-boundary tripwire that lifts the work above Quick.

## Decision

Adopt the release-governance patterns from uber/ADR that fit this repository's evidence-custody center, and port the deferred MCP 2.x change, without changing validation semantics, exit codes, or the release stance.

Main failure modes and controls:

- **A red build reads as green.** A skipped job satisfies a required check. Control: the `CI gate` job runs with `if: always()` and fails unless every upstream job succeeded.
- **The MCP range admits an untested major.** Control: `mcp-smoke` runs against both `mcp>=1.0,<2` and `mcp>=2,<3`, and the bound stops at `<3`.
- **A receipt is mistaken for proof.** Control: the receipt carries a boundary string saying it is not a signature and not an adequacy claim, and the docs repeat it.
- **A passing packet with open gaps reads as gap-free.** Control: the receipt counts declared statuses and reports `open_evidence_items`.

The release stance does not change. No version bump or tag is made here.

## Required links

- Basis and benchmark: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

CI, dependency, and validator-output changes are each controlled by a named check, and the full local suite passes.

## Source-lineage note

The pattern lineage is uber/ADR, recorded in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md) Tier 6. No security, compliance, or efficacy claim is made.
