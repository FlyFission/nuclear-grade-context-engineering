# Running a Review Panel — Risk

## Change identity

- Slug: running-a-review-panel
- PR / issue: #97 — add the `running-a-review-panel` skill and wire the panel doctrine to a procedure
- Owner: FlyFission
- Date: 2026-10-20
- Current lifecycle phase: Verify / Review / Decide
- Summary: The repo asserted that high-consequence verdicts should use a panel and that a panel sharing one brief is "one view voiced three times," but supplied no method for building one. This change adds the procedure as a 30th skill: each seat declares the diversity axis it varies, one evidence packet is frozen at a pinned revision, the first pass runs independently, panel health (dropped, timed-out, truncated, invalid seats) is recorded beside the result, and no finding becomes actionable until it is verified against live source in the host session.

## Record-order deviation

**This packet was written after the change, not before it.** The branch was developed from a design discussion; the PR body recorded the missing packet as a known gap and said the right fix was "a packet before merge, not after." This is that packet, and the deviation is stated here rather than disguised by the file dates.

What that costs: the requirement rows in `basis.md` and the sequence in `plan.md` are reconstructions of decisions already taken, not constraints that shaped them. They are accurate as a record and weak as a control — a packet's gating value comes from being written while the outcome is still open, and this one was not. Treat the requirement rows as claims a reviewer should check against the diff, not as evidence the diff was built to meet them.

## Questioning-attitude summary

- Decision question: Does adding a 30th skill clear the objection that an earlier packet in this repo used to refuse exactly this, and is the panel procedure load-bearing rather than a restatement of the doctrine it came from?
- Assumptions that set the mode: `CORE.md`, `SKILLS.md`, `COMMANDS.md`, `INSTALL.md`, `nuclear-grade.yaml`, the generated command cards, and both eval manifests are controlled items; a skill in the catalog is a surface agents load and cite, and the skill makes a claim about independence, which is the class of wording this repo guards most closely.
- Facts still needing validation: that the procedure changes a real panel decision in practice, and that the axis-declaration step is not satisfiable by a seat naming an axis it does not actually vary.
- Stop or hold conditions: hold if the contract tests, token budget, `doctor`, or packet validation fail; if the skill count on disk disagrees with any stated count; or if the efficacy gap below is absorbed into a clean verdict instead of being carried as a named risk.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `skills/running-a-review-panel/SKILL.md` | skill (new) | The procedure itself; the 30th catalog entry | repo |
| `nuclear-grade.yaml` | manifest | Catalog membership and the `command_map` entry that generates the card | repo |
| `commands/ng-panel.md` | generated card | Projection of the skill; drifts if regenerated inconsistently | repo |
| `tests/fixtures/command_prompts.json` | golden fixture | Byte-for-byte snapshot of every `## Prompt` block | repo |
| `CORE.md`, `SKILLS.md`, `COMMANDS.md`, `INSTALL.md` | public headline docs | Carry the catalog counts and the cluster placement | repo |
| `docs/05-reference/cli-reference.md`, `docs/05-reference/skill-authoring-contract.md` | reference docs | State the skill count in prose | repo |
| `docs/02-operating-system/evaluation-integrity.md`, `independence-architecture.md` | doctrine | Cross-link from the assertion to the procedure | repo |
| `evals/skill-routing-cases.jsonl`, `evals/skill-output-cases.jsonl`, `docs/05-reference/skill-evaluation.md` | eval manifests + prompt bank | Coverage ratchet for a new skill | repo |
| `docs/03-worked-examples/skill-workflow-comparison/results-summary.md` | worked-example evidence | Records the skill as post-trial, with trial records pending | repo |
| `tests/test_skill_contracts.py`, `tests/test_command_contracts.py`, `tests/test_ng_cli.py` | contract tests | Encode the expected skill and command sets and the rolled-up count | repo |
| `CHANGELOG.md` | public record | The `[Unreleased]` entry; see the merge note below | repo |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Adds a catalog surface other agents route to and cite; no production system, credential, or permission changes |
| Reversibility | high | One skill folder, one generated card, and documentation; reverts with normal git history plus `gen-commands` |
| Detectability | medium | A wrong count or a stale generated card is caught by tests; a procedure that reads well and changes no decision is not caught by anything here |
| Exposure | high | Public repo; adopters install the catalog and quote `CORE.md` |
| Uncertainty | high | The procedure has no field use behind it and no efficacy measurement; see the gap below |
| Dependency trust | low | No dependency, vendor CLI, runner script, or new runtime directory; no new external source registered |
| AI authority | medium | Drafted by an AI agent, which also wrote this record and ran its own verification; merge decision stays with a human |

## The objection this change has to clear

An earlier packet in this repo, `.nuclear/changes/quality-verdict-accountability/plan.md`, refused to add a skill under "Deliberately not done," and its decisive objection was not cost:

> `README.md` still claims "28 of 28 skills show a measured behavior change versus a plain prompt," and the repo now ships 29 skills after #81 added `verifying-final-artifacts`. Adding another unbenchmarked skill would widen a gap between the shipped count and the benchmarked count that the efficacy claim depends on.

This change does the thing that packet refused, so the objection has to be answered rather than skipped.

**What actually changed is the claim, not the evidence.** Commit `b7f0ab6` (#86, "docs: scope skill pilot claims to tested catalog") rewrote the README so the pilot is reported as a measurement of "28 skills that were in the catalog when the July 2026 pilot ran," closing with "Treat it as a historical snapshot, not evidence for skills added later." Verified by reading the current `README.md` and by `git log -S` on that sentence. The unqualified "28 of 28" headline the prior packet objected to no longer exists, so a 30th skill no longer puts a repo-level efficacy claim out of true.

**What did not change: this skill has no efficacy evidence.** The benchmarked set is still 28 and the shipped set is now 30, so the numeric gap went from one to two. #86 makes that gap *disclosed* rather than *contradictory*; it does not make it smaller. Carried as the first named risk in `ship.md`, and recorded in the comparison table using the repo's existing post-trial convention ("formal trial records pending") rather than by inventing a trial result.

## Merge-base note

The branch's CI last ran on 2026-08-05 against base `3ade94e`. By 2026-10-20 `main` had taken the 0.6.0 release (#110) and the editorial-diagrams change (#114), so the four green checks on the PR were evidence about a base that no longer exists, and the PR's reported `mergeable_state: clean` predated the divergence. `main` was merged into the branch as commit `a33f858`: one conflict in `CHANGELOG.md`, resolved by keeping main's 0.6.0 section as released and moving this change's entry to `[Unreleased]`. The full gate was re-run on the merge result; see `verification.md` V-1 to V-6.

## Selected mode

- **Mode:** Standard
- Why this mode: the change adds a catalog surface agents load and cite, edits public headline docs and their counts, and makes a claim about reviewer independence. The activation question "will someone rely on the claim?" answers yes — an adopter can run a panel because this file told them how.
- Why lighter mode is not enough: a Quick record would not hold the claim-to-evidence trace this change needs, and the specific thing a reviewer has to check — whether the prior packet's objection is answered or merely stepped around — is an argument, not a test result. It needs `basis.md` and `trace.md` to be legible.
- Why heavier mode is not yet required: no production system, credential, permission, safety, or regulatory control changes; no new gate is authored; no dependency or supplier is added. The one irreversible-in-effect property, a public catalog entry adopters may quote, is covered by Standard.

## Immediate proof obligations

- Minimum evidence before build: the prior packet's objection located and quoted from the record, and the status of the README claim it rests on independently verified rather than taken from the PR description.
- Minimum evidence before merge/release: pytest, ruff, `ng doctor`, `ng tokens`, and packet validation pass on the merge result, not on the pre-merge tree; the skill count on disk matches every stated count; the generated card and the golden fixture agree with the skill.
- Independent review needed? yes. The authoring agent wrote the skill, the doctrine cross-links, this record, and ran every check in it. That is the actor–evidence coupling this repo asks others to disclose, and the skill being added is itself about not trusting a single coupled reviewer. A human owns the merge call.

## Required links

- Packet: `.nuclear/changes/running-a-review-panel/`
- Basis: `basis.md`
- Plan: `plan.md`
- Trace: `trace.md`
- Verification: `verification.md`
- Ship: `ship.md`
- Skill: `../../../skills/running-a-review-panel/SKILL.md`
- Doctrine it implements: `../../../docs/02-operating-system/evaluation-integrity.md`, `../../../docs/02-operating-system/independence-architecture.md`
- Prior refusal being answered: `../quality-verdict-accountability/plan.md`

## Exit criteria

- The mode is justified against both a lighter and a heavier option.
- The affected controlled items are explicit.
- The prior on-record refusal is quoted and answered, not omitted.
- The record-order deviation and the stale merge base are stated.

## Source-lineage note

Original Nuclear-grade packet inspired by public ideas on graded rigor, independent verification, configuration management, and diversity in redundant review mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
