# ng-source-check

## Purpose

Check public source lineage and citation safety for docs, templates, skills, commands, and packets. This is a portable command prompt.

## Use when

- A public file cites source families, standards, agencies, or assurance concepts.
- New methodology language is added.
- A source status or public URL may be stale.

## Do not use when

- The change is private implementation code with no public methodology claim.
- A source is proprietary and should remain outside this public repo.

## Inputs

- Changed public text.
- `docs/00-standards-foundation/source-map.md`.
- `docs/01-field-guide/source-to-concept-crosswalk.md`.
- `docs/00-standards-foundation/compliance-boundaries.md`.

## Prompt text

```text
Run a Nuclear-grade source-lineage check.

Inputs:
- changed public text: <paste/link>
- cited source families: <list>
- source-map rows: <links>

Return:
- verified-public, supporting-context, public-url-needed, or excluded-direct status
- wording changes needed to avoid compliance or approval claims
- source-map or crosswalk updates
- validation and scan commands
```

## Files created or modified

- Public docs, templates, skills, commands, or packet files.
- `docs/00-standards-foundation/source-map.md` when status changes.
- `docs/01-field-guide/source-to-concept-crosswalk.md` when concept mapping changes.

## Expected outputs

- Source-safe wording.
- Updated source status or explicit downgrade.
- Boundary-safe source-lineage note.

## Verification command

```bash
rg -n "URL to verify|before citation|Current retrieval gaps" docs/00-standards-foundation docs/01-field-guide
python tools/ng.py doctor .
```

## Failure modes

- Presenting unresolved sources as direct lineage.
- Turning influence into compliance.
- Repeating long source essays in every artifact.

## Legal/assurance boundary note

Source lineage explains influence and concept mapping. It does not show satisfaction of those sources or create formal assurance.
