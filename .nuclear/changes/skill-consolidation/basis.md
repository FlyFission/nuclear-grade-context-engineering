# Skill Consolidation — Basis

## Problem

The catalog audit (`evals/skill-catalog-audit/2026-11-03.md`) found no skill named as used on unrelated work, measured gains that mostly matched a generic prompt, and overlapping triggers. It proposed 8 merges. The owner allowed consolidation only with high confidence that the smaller set still does everything the larger one did, without turning any skill into the wrong tool for a job. The owner also wants a simpler README and the skills presented visually: what they are and how they are invoked.

## Requirements

| ID | Requirement | Acceptance |
|---|---|---|
| REQ-001 | A merge is applied only if it passes all four pre-registered criteria: coverage, routing parity, fit, and size | `evals/skill-consolidation/PROTOCOL.md`, `REPORT.md` |
| REQ-002 | The applied merge leaves no dangling reference to the removed names in live docs, skills, code, tests, or eval cases | grep; full test suite; `ng doctor` |
| REQ-003 | Every figure that shows skills shows every catalog skill, and stays in step with the catalog | `tests/test_diagram_coverage.py` |
| REQ-004 | The README is shorter and keeps every boundary statement, the pinned strings tests require, and working links | public-doc tests; link check; rendered read-through |

## Design choices

- **Follow the protocol strictly.** Several failures were narrow (M2 lost four words), but relaxing a bar after seeing results is the failure this repo exists to prevent. A narrow miss earns a fresh pre-registered test, not a pass.
- **Show `controlling-approved-versions` twice on the map.** The skill works at two moments, scoping at the start and the baseline at acceptance, and the map says so rather than hiding one.
- **Generate figures from one list a test checks.** The map had silently fallen behind the catalog; a test now prevents that.
- **Keep dated records as written.** Trial records, benchmark plans, and the token audit keep the old names.

## Non-goals

- Re-testing the failed merges here.
- Changing any skill other than the two merged.

## Required links

- Risk: `risk.md`
- Plan: `plan.md`
- Trace: `trace.md`

## Exit criteria

- Every requirement has an acceptance method a reviewer can rerun.

## Source-lineage note

Original Nuclear-grade packet; method follows `docs/02-operating-system/verification-methods-and-depth.md`, with sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
