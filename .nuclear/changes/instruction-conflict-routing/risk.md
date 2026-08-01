# Risk — instruction conflict routing

## Selected mode

- **Mode:** Standard
- **Why:** `AGENTS.md` controls agent behavior; even one new stop rule belongs on the repository's Standard path.

## Decision

Add one default-behavior rule requiring agents to expose conflicting instruction sources, use the host's documented precedence, and stop before an affected action when precedence cannot resolve the conflict.

The main risk is unnecessary blocking. The rule is limited to actual conflicts that affect an action; it adds no new precedence scheme, artifact, permission, role, or gate.

## Required links

- Changed item: [`AGENTS.md`](../../../AGENTS.md)
- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

The rule is host-neutral, actionable, and confined to unresolved instruction conflicts.

## Source-lineage note

This change responds to primary host behavior linked in [`basis.md`](basis.md) and uses the repository boundaries mapped in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). It makes no cross-host equivalence, efficacy, compliance, or safety claim.