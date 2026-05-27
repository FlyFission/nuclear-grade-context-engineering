# ng-new

## Purpose

Create the packet files for a Quick or Standard Nuclear-grade change. This is a portable command prompt.

## Use when

- A mode decision exists.
- A questioning-attitude screen is complete when uncertainty or consequence is material.
- A new change needs durable evidence in Git.
- A turnover, self-check, OPEX, or supplier-trust record has been activated.

## Do not use when

- The work is disposable and has no review need.
- A packet already exists unless you are intentionally updating it.

## Inputs

- Change slug.
- Selected mode.
- Initial scope, affected files, questioned assumptions, and evidence obligation.

## Prompt text

```text
Create or update a Nuclear-grade packet.

Inputs:
- slug: <slug>
- mode: <quick|standard>
- scope: <summary>
- affected files/assets: <list>
- questioned assumptions: <list>
- evidence obligation: <command/review/evidence>
- activated HPI records: <turnover/self-check/opex/supplier-trust/none>

Use the repo templates. Keep the packet short, link-heavy, and evidence-oriented. Include required links, exit criteria, and source-lineage notes. Do not imply formal assurance or compliance.
```

## Files created or modified

- `.nuclear/changes/<slug>/risk.md`
- `.nuclear/changes/<slug>/proof.md` for Quick mode
- `.nuclear/changes/<slug>/basis.md`
- `.nuclear/changes/<slug>/plan.md`
- `.nuclear/changes/<slug>/trace.md`
- `.nuclear/changes/<slug>/verification.md`
- `.nuclear/changes/<slug>/ship.md`
- `.nuclear/changes/<slug>/turnover.md` if activated
- `.nuclear/changes/<slug>/self-check.md` if activated
- `.nuclear/changes/<slug>/supplier-trust.md` if activated

## Expected outputs

- Packet files for the selected mode.
- Initial evidence status and proof commands.

## Verification command

```bash
python tools/ng.py new <slug> --mode quick
python tools/ng.py new <slug> --mode standard
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Creating a Standard packet for a clearly Quick change.
- Omitting source-lineage notes.
- Adding HPI records by default instead of by consequence.
- Copying long source excerpts instead of linking.

## Legal/assurance boundary note

Packet creation records review evidence. It does not create a regulated quality program, formal V&V, certification, approval, or compliance.
