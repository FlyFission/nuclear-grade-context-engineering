# Verification - Skill and Workflow Comparison

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim / requirement ID | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|
| C-001 | Automated public-doc coverage test | Every skill in `nuclear-grade.yaml` appears in `results-summary.md` and maps to multiple trials. | pass | `python -m pytest tests/test_public_docs.py -q` | not applicable |
| C-002 | Automated public-doc coverage test | Every workflow in `WORKFLOWS.md` appears in `results-summary.md` and maps to multiple trials. | pass | `python -m pytest tests/test_public_docs.py -q` | not applicable |
| C-003 | Public-doc review and test suite | Boundary language labels the comparison as qualitative and non-assurance. | pass | comparison README and public-doc tests | not applicable |
| C-004 | Reviewer read-through | Simple prompting is described as better for tiny local reversible work. | pass | comparison README | not applicable |
| C-005 | Automated public-doc depth test | At least 12 trial records exist and each has scenario, simple prompt, Nuclear-grade, scoring, decision, and boundary sections. | pass | `python -m pytest tests/test_public_docs.py -q` | not applicable |
| C-006 | Automated public-doc score test | Every U01-U12 use case has both simple-prompt and Nuclear-grade score rows. | pass | `python -m pytest tests/test_public_docs.py -q` | not applicable |

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- `source-map.md`

## Exit criteria

- Coverage tests pass.
- Packet validates.
- Boundary wording remains explicit.

## Source-lineage note

Original verification record mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
