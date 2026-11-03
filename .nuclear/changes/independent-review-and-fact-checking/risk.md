# Independent Review and Fact Checking — Risk

## Change identity

- Slug: independent-review-and-fact-checking
- PR / issue: draft PR from branch `claude/independent-review-fact-check`
- Owner: FlyFission
- Date: 2026-11-03
- Current lifecycle phase: Verify / Review / Decide
- Summary: The owner asked how good the repo is at independent review and fact checking, then asked for three things: wire the parked two-party check into the validator, add a fact-check skill, and give the repo the nuclear vocabulary for review that goes deeper than a standard design check. The owner also asked whether every skill is used and adds value. This change does the first three. It answers the fourth with an evidence-backed audit and a consolidation **proposal**, and leaves the merges for the owner to decide.

## Questioning-attitude summary

- Decision question: Does `--two-party` make a `pass` without a second party fail, without breaking any packet that validates today? Do the new doc and skill say only what their sources support?
- Assumptions that set the mode: the validator, skill catalog, generated command cards, templates, source map, and public headline docs are controlled items. A checker change alters what "OK" means for adopters.
- Facts still needing validation: the exact wording of 10 CFR 50 Appendix B Criterion III and of DOE-HDBK-1028-2009 Vol. 2. These were fetched and compared during build (see `verification.md`) and re-checked by the reviewer.
- Stop or hold conditions: hold if default-mode validation changes for any existing packet, if any quotation fails the second-source comparison, if the skill count on disk disagrees with a stated count, or if the consolidation audit is presented as a decision rather than a proposal.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `nuclear_grade/two_party.py`, `nuclear_grade/ng_validate.py` | checker | Defines what `ng validate --two-party` accepts | repo |
| `nuclear_grade/cli.py`, `nuclear_grade/mcp_server.py`, `nuclear_grade/receipt.py` | CLI / MCP / receipt surface | New flag, new MCP argument, new additive receipt key `strict.two_party` | repo |
| `templates/standard/verification.md` | template | Adds the four verification-depth types and points to `--two-party` | repo |
| `docs/02-operating-system/verification-methods-and-depth.md` | doctrine (new) | Defines check vs. design review vs. alternate method vs. qualification test | repo |
| `skills/checking-facts/SKILL.md`, `commands/ng-fact-check.md` | skill and generated card (new) | Skill 31 | repo |
| `skills/checking-source-claims/SKILL.md`, `skills/proving-claims/SKILL.md` and their cards | skills | New pointers to `checking-facts` in When Not to Use | repo |
| `nuclear-grade.yaml`, `CORE.md`, `SKILLS.md`, `COMMANDS.md`, `INSTALL.md`, `docs/05-reference/*`, `tools/build_diagrams.py`, `docs/assets/diagrams/skill-map.svg` | catalog and headline docs | Skill count and placement | repo |
| `docs/00-standards-foundation/source-map.md`, `docs/01-field-guide/source-to-concept-crosswalk.md` | source lineage | New concept-lineage uses of two sources already marked verified-public | repo |
| `evals/skill-routing-cases.jsonl`, `evals/skill-output-cases.jsonl`, `docs/05-reference/skill-evaluation.md`, `docs/03-worked-examples/skill-workflow-comparison/results-summary.md` | eval manifests | Coverage ratchet for the new skill | repo |
| `evals/skill-catalog-audit/2026-11-03.md` | audit report (new) | Evidence behind the consolidation proposal | repo |
| `tests/test_two_party.py`, `tests/test_receipt.py`, `tests/test_skill_contracts.py`, `tests/test_command_contracts.py`, `tests/test_ng_cli.py`, `tests/fixtures/command_prompts.json` | tests | Encode the new behavior and catalog | repo |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Changes a checker, but only behind a new opt-in flag. Default mode changes only for packets that declare a `## Claim authorship` table, and none does today. |
| Reversibility | high | Normal git revert plus `ng gen-commands`. |
| Detectability | medium | Tests catch regressions in the code paths. A two-party rule that is subtly wrong (passes a packet it should fail) is only caught by review or by the adversarial tests. |
| Exposure | high | Public repo; adopters run `ng validate` in CI and install the skill catalog. |
| Uncertainty | medium | The quotations were checked against two copies. The new skill has no efficacy measurement. |
| Dependency trust | low | No new dependency. |
| AI authority | medium | An AI agent drafted, tested, and recorded this. The review was another agent instance of the same model family, briefed by the same session. A human owns the merge. |

## Selected mode

- **Mode:** Standard
- Why this mode: a checker's semantics changed, a skill was added, and public doctrine now quotes regulatory text. Someone will rely on all three.
- Why lighter mode is not enough: the two-party rule's edge cases, and whether the quotes are exact, are claims a reviewer must be able to trace one by one.
- Why heavier mode is not yet required: the new rule is opt-in and default validation is unchanged; no production system, credential, permission, or release action is involved; and no skill is removed, so the consolidation stays a proposal.

## Immediate proof obligations

- Before build: the primary-source text of both cited sources, fetched and compared across two copies.
- Before merge: pytest, ruff, `ng doctor`, `ng tokens`, and the CONTRIBUTING strict-custody validation pass; default-mode validation of every existing packet is unchanged against `main`; every stated skill count is 31.
- Independent review needed? Yes. An agent review ran (see `verification.md`), and it is classified as a self-check because it shares the model family and orchestrator. The human owner is the pending second party. By design, `ng validate --two-party` on this packet fails until the owner fills in the verifier.

## Required links

- Basis: `basis.md`
- Plan: `plan.md`
- Trace: `trace.md`
- Verification: `verification.md`
- Ship: `ship.md`
- Doctrine: `../../../docs/02-operating-system/verification-methods-and-depth.md`
- Skill: `../../../skills/checking-facts/SKILL.md`
- Audit: `../../../evals/skill-catalog-audit/2026-11-03.md`

## Exit criteria

- The mode is justified against a lighter and a heavier option.
- Controlled items are explicit.
- The consolidation is recorded as a proposal with an owner decision pending.

## Source-lineage note

Original Nuclear-grade packet inspired by public ideas on graded rigor, design verification by alternate methods, independent verification, and configuration management mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
