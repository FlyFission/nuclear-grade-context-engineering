# Trace — claude-agents-bridge

## Trace summary

| ID | Claim | Basis | Task / code | Control | Evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|
| REQ-001 | Claude Code is routed to the existing agent brief without duplicated guidance. | `basis.md` | `plan.md` step 1 / `CLAUDE.md` | Import-only shim | `verification.md` E-001, E-002 | Human review before merge | pass |

## Evidence chain

```text
Claude Code does not natively use the repo's AGENTS.md
  → REQ-001: route without duplication
  → CLAUDE.md contains @AGENTS.md only
  → direct inspection + repository checks
  → human merge verdict
```

## Open trace gaps

| Gap | Disposition | Recheck trigger |
|---|---|---|
| No live Claude Code session is captured in CI. | accept; syntax is checked against Anthropic's primary documentation and the shim is directly inspectable | A field report that the import is not loaded |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- `CLAUDE.md`

## Exit criteria

- REQ-001 resolves from basis through code and evidence to the human verdict.
- The live gap is disclosed and not used as proof.

## Source-lineage note

The trace applies only to the Claude Code compatibility bridge documented at <https://code.claude.com/docs/en/memory> and carries no formal assurance claim.
