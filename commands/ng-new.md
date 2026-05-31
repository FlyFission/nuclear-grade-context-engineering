# ng-new

## Purpose

Create the record files for a Quick or Standard Nuclear-grade change. This is a portable command prompt.

## Use when

- The mode is already chosen.
- You have finished a questioning-attitude screen. You do this whenever the stakes or the uncertainty are real.
- A new change needs lasting evidence saved in Git.
- You have started a handoff, a self-check, a lessons-from-operation record (OPEX), or a supplier-trust record.

## Do not use when

- The work is throwaway and no one needs to review it.
- A record already exists, unless you mean to update it.

## Inputs

- The change slug (its short, lowercase, hyphen-joined name).
- The chosen mode.
- The first cut of scope, the files it touches, the assumptions you questioned, and what the change must prove.

## Prompt text

```text
Create or update a Nuclear-grade change record.

Inputs:
- slug: <slug>
- mode: <quick|standard>
- scope: <summary>
- affected files/assets: <list>
- questioned assumptions: <list>
- what the change must prove: <command/review/evidence>
- safety-habit (HPI) records started: <turnover/self-check/opex/supplier-trust/none>

Use the repo templates. Keep the record short. Lean on links, and point at evidence. Include the required links, the conditions for being done, and a note on where the ideas come from. Do not imply formal assurance or compliance.
```

## Files created or modified

- `.nuclear/changes/<slug>/risk.md`
- `.nuclear/changes/<slug>/proof.md` for Quick mode
- `.nuclear/changes/<slug>/basis.md`
- `.nuclear/changes/<slug>/plan.md`
- `.nuclear/changes/<slug>/trace.md`
- `.nuclear/changes/<slug>/verification.md`
- `.nuclear/changes/<slug>/ship.md`
- `.nuclear/changes/<slug>/turnover.md` if started
- `.nuclear/changes/<slug>/self-check.md` if started
- `.nuclear/changes/<slug>/supplier-trust.md` if started

## Expected outputs

- The record files for the chosen mode.
- The starting state of the evidence, and the commands that prove it.

## Verification command

```bash
python tools/ng.py new <slug> --mode quick
python tools/ng.py new <slug> --mode standard
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Creating a Standard record for a change that is clearly Quick.
- Leaving out the note on where the ideas come from.
- Adding safety-habit (HPI) records by default, instead of by how much is at stake.
- Pasting long quotes from a source instead of linking to it.

## Legal/assurance boundary note

This record holds review evidence. It does not create a certified quality assurance program, formal verification and validation, certification, approval, or compliance.
