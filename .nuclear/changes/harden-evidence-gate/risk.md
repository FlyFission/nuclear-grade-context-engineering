# Risk

## Selected mode

- **Mode:** Standard
- **Change:** Add a placeholder marker that templates ship with and the validator rejects, broaden doctor's required public files, and move an internal SWOT audit out of the public docs tree.
- **Why Standard:** The change touches the validator, the doctor health check, the public templates, and the public docs surface. A regression would let an untouched scaffold validate green and weaken the evidence gate that the project promises in its public docs.

## Risk summary

| Area | Status | Note |
|---|---|---|
| Validator semantics | pass | New marker check appends a clear message; public signatures `validate_packet` and `detect_packet_mode` are preserved. |
| Doctor checks | pass | Three additional public files are required and all exist; CLI test scaffold already writes them. |
| Template surface | pass | Marker injected exactly once near the top of every template in `templates/quick`, `templates/standard`, `templates/cm`, `templates/golden-path`. |
| Public docs tree | pass | `report-swot-gap-remediation.md` removed from version control and tracked only under gitignored `.research/`. |
| Maintainer-decision items | gap | `docs/00-standards-foundation/flyfission-ops-knowledge-graph-usage.md` keeps FlyFission-specific framing and needs a vendor-neutral rename decision. |

## Required links

- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Untouched scaffold packets fail validation because of the marker.
- All existing packets continue to validate.
- Doctor and tests stay green.
- The SWOT audit is no longer reachable from the public docs tree.

## Source-lineage note

This packet describes an original validator and configuration-management hygiene change grounded in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
