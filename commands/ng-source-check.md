# ng-source-check

## Purpose

Check where public ideas come from, and make sure you cite them safely, across docs, templates, skills, commands, and change records. This is a portable command prompt.

## Use when

- A public file cites source families, standards, agencies, or assurance ideas.
- You are adding new wording about the method.
- A source's status or a public URL may be out of date.
- A dependency, model, API, or vendor claim could be mistaken for your own local proof.

## Do not use when

- The change is private code with no public claim about the method.
- A source is proprietary and should stay out of this public repo.

## Inputs

- The public text you changed.
- `docs/00-standards-foundation/source-map.md`.
- `docs/01-field-guide/source-to-concept-crosswalk.md`.
- `docs/00-standards-foundation/compliance-boundaries.md`.

## Prompt text

```text
Run a Nuclear-grade source-lineage check (where the ideas come from).

Inputs:
- changed public text: <paste/link>
- cited source families: <list>
- source-map rows: <links>
- source or vendor claims used as evidence: <list>

Return:
- a status for each source: verified-public, supporting-context, public-url-needed, or excluded-direct
- the difference between an influence, a source's claim, local proof, a requirement, and an authority
- the wording changes needed so you make no claim of compliance or approval
- the source-map or crosswalk updates
- the validation and scan commands
```

## Files created or modified

- Public docs, templates, skills, commands, or packet files.
- `docs/00-standards-foundation/source-map.md` when a status changes.
- `docs/01-field-guide/source-to-concept-crosswalk.md` when a concept mapping changes.

## Expected outputs

- Wording that is safe about its sources.
- An updated source status, or a clear downgrade.
- The difference between your local proof and a source's claim, when that matters.
- A source-lineage note that stays inside the limits.

## Verification command

```bash
rg -n "URL to verify|before citation|Current retrieval gaps" docs/00-standards-foundation docs/01-field-guide
python tools/ng.py doctor .
```

## Failure modes

- Presenting unresolved sources as direct lineage.
- Turning an influence into a claim of compliance.
- Repeating long source essays in every file.

## Legal/assurance boundary note

Source lineage explains an influence and a concept mapping. It does not show you have satisfied those sources, and it does not create formal assurance.
