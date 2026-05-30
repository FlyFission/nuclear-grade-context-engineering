# Skill Trigger Evaluation Verification

## Verification context

- Slug: skill-trigger-evaluation
- Related basis: `basis.md`
- Owner: FlyFission
- Date: 2026-05-25
- Verification scope: Skill descriptions, skill-evaluation prompt bank, reference index, contract tests, and this packet.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim / requirement ID | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|
| REQ-001 | Pytest skill contract | Descriptions start with `Use when`, have 90 to 180 chars, and avoid prohibited words | pass | `python -m pytest -q` | none |
| REQ-002 | Pytest eval coverage | Each expected skill has three positive and two negative prompts | pass | `python -m pytest -q` | none |
| REQ-003 | Git diff review | No per-skill resources added without demonstrated need | pass | local git diff | future benchmark still useful |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Unit/contract tests | `python -m pytest -q` | local Windows PowerShell | pass | terminal output |
| Repo doctor | `python tools/ng.py doctor .` | local Windows PowerShell | pass | terminal output |
| Packet validation | `python tools/ng.py validate .nuclear/changes/skill-trigger-evaluation` | local Windows PowerShell | pass | terminal output |
| Manual review | Compare changed files against skill-creator guidance | local review | pass | git diff |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Over-broad descriptions | Enforce max length and inspect context nouns | pass | pytest and diff |
| Under-specified descriptions | Enforce minimum length and realistic trigger contexts | pass | pytest and diff |
| Missing eval prompts | Coverage test for every expected skill | pass | pytest |
| Formal assurance implication | Existing public docs and packet validator language checks | pass | pytest and validator |

## AI-assisted work checks

- AI scope: Assisted adversarial review, patch drafting, and verification.
- Model/tool used: Codex with local shell, apply_patch, and web review of public skill-creator guidance.
- Permissions/actions allowed: Local repo edits and validation commands.
- Independent checks performed: Automated tests and packet validator.
- Hallucination/slop screening: Source-bound comparison to local and public skill-creator guidance.
- Human approval gates exercised: User requested adversarial review and updates.

## Security / dependency / supply-chain checks

- Dependency review: not applicable; no dependency changes.
- SBOM/provenance/build evidence: not applicable.
- Vulnerability/security review: no executable runtime surface added.
- Revalidation trigger: Future skill packaging, marketplace publishing, or major skill behavior rewrite.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes: local terminal output
- Implementation diff / PR: repo diff for this change

## Exit criteria

- Each important claim has pass, fail, gap, deferred, or not applicable status.
- Evidence is linked rather than pasted in full.
- Gaps are explicit and reflected in `ship.md`.
- Reviewer can tell whether the evidence supports the release decision.

## Source-lineage note

Original Nuclear-grade verification inspired by public sources on software verification and validation (V&V), test documentation, secure development, software assurance, AI risk, and application-security checks, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
