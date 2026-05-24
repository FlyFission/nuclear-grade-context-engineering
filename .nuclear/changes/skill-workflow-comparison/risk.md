# Risk - Skill and Workflow Comparison

## Selected mode

- **Mode:** Standard
- **Reason:** This adds a public-facing evaluation artifact about repo effectiveness. It changes adoption claims and therefore needs source/legal boundary review, evidence status, and release decision.

## Scope

- Added artifact: `docs/03-worked-examples/skill-workflow-comparison/README.md`
- Updated artifact: `EXAMPLES.md`
- Affected public claim: usefulness of skills and workflows compared with simple prompting
- Controlled item families: public docs, workflow claims, skill coverage, example catalog

## Risk screen

| Question | Answer |
|---|---|
| Consequence if wrong | Readers may over-trust a qualitative comparison as benchmark evidence. |
| Reversibility | Revert documentation and example-catalog update. |
| Exposure | Public README-linked docs may influence adoption expectations. |
| Uncertainty | Medium; scoring is qualitative and must be clearly labeled. |
| Required proof | Verify every published skill and workflow appears in coverage, and boundary wording avoids benchmark or assurance overclaiming. |

## Escalation triggers

- Claims become empirical benchmark claims.
- The comparison implies safety, security, compliance, certification, or production suitability.
- A published skill or workflow is missing from the coverage matrix.
- The artifact presents simple prompting as universally inferior.

## Required links

- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `docs/03-worked-examples/skill-workflow-comparison/README.md`
- `source-map.md`

## Exit criteria

- Evaluation scope is clearly qualitative.
- Each published skill and workflow is covered.
- Simple prompting remains represented as the better option for tiny local work.
- Boundary note prevents assurance or benchmark overclaiming.

## Source-lineage note

Original workflow evaluation mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
