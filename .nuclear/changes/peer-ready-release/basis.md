# Basis

## Mission

Make Nuclear-grade Public v0 understandable and usable as a workflow product before public release.

## Protected outcomes

- New users understand what the repo is in the first minute.
- Enterprises can see install, adoption, governance, support, and boundary posture.
- Agents can use skills and portable command prompts without guessing.
- The CLI gives deterministic local help without extra dependencies.
- Public text avoids formal assurance or compliance claims.

## Unacceptable outcomes

- Skills become vague prose.
- Command cards imply unsupported harness integration.
- README remains standards-first.
- CLI overwrites user files silently.
- Legal boundary language is hidden in only one file.

## Derived claims

| ID | Claim | Evidence planned |
|---|---|---|
| E-001 | Repo has action-first WBS. | Top-level docs and docs map. |
| E-002 | Skills and commands are contract-tested. | Contract tests. |
| E-003 | CLI supports init, new, validate, doctor, list, and status. | CLI tests and doctor run. |
| E-004 | Boundary wording is propagated. | Public docs test and scans. |

## Required links

- `risk.md`
- `trace.md`
- `verification.md`
- `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Every derived claim has pass evidence or named gap.
- No unresolved boundary issue blocks public release.

## Source-lineage note

This basis is part of an original public-source-inspired workflow and references `docs/00-standards-foundation/source-map.md`. It does not claim satisfaction of external standards.
