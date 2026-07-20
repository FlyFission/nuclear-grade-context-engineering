# Standard Risk

**Purpose:** Sort a real change by risk after questioning the assumptions, justify Standard mode, and name any extra records you turn on.

---

## Change identity

- Slug: skill-benchmark-and-amendments
- PR / issue: #62 (this packet), reconciled against #63 and an already-merged overlap fix on `main`
- Owner: FlyFission
- Date: 2026-07-06
- Current lifecycle phase: Verify
- Current work phase: accept
- Summary: Adds an objective with-skill-vs-without-skill benchmark for all 28 `skills/*/SKILL.md`
  files (headless `claude -p` A/B trials, blind LLM grading, real cost/token data, every raw
  transcript checked in), runs a harder second-round retest on the skills that showed no effect,
  computes formal statistical significance and a small honest multi-model check, and — as a direct
  result of what the testing found — amends two skill files (`briefing-an-agent`,
  `creating-change-records`) to fix a diagnosed scope-overlap and a diagnosed weak-model robustness
  gap, each amendment adversarially reviewed and validated before/after.
- Harvested from PR #63 (closed as superseded, its value folded in here): the Gate-1 deterministic
  benchmark tooling (`tools/ng_skill_audit.py`, `ng_skill_route_score.py`, `ng_skill_output_score.py`),
  the routing/output eval manifests (`evals/skill-routing-cases.jsonl`, `evals/skill-output-cases.jsonl`),
  the static-audit artifacts under `evals/skill-static-audit/2026-07-04/`, three reference docs under
  `docs/05-reference/`, and five `tests/test_skill_*`/`test_efficacy_signal_mutations.py` guards.
  A third skill amendment (`proving-claims`, scope-narrowed to trace construction) is also harvested;
  it is consistent with the same overlap-reduction direction but is **not** backed by the live A/B
  regression trials that back the other two amendments — its validation is deferred and stated as an
  open item (see REQ-006 in `trace.md`), so it must not be read as live-proven.

## Mission anchor

- Objective: answer, with real evidence instead of author judgment, whether loading each Nuclear-grade
  skill measurably changes model behavior versus a plain prompt — and act on anything the evidence
  shows is a real, fixable problem with a skill.
- Success criteria: every skill has a documented result (win/tie/loss/open) with raw evidence
  checked in; every self-identified methodological gap is either closed, honestly re-scoped, or
  explicitly logged as open; any content amendment made as a result is adversarially reviewed and
  validated, not applied on judgment alone.
- Non-goals / forbidden directions: this is not a certification, safety, security, or
  production-readiness claim; it does not claim independent/third-party replication; it does not
  claim cross-provider (non-Anthropic) model coverage; it does not silently consolidate or delete
  any skill based on this evidence alone.
- Drift check: re-anchor if a finding is used to justify a bigger content rewrite than the evidence
  supports; escalate if a skill amendment's validation contradicts its own justification (see the
  `creating-change-records` Haiku divergence, held as an open, reported gap rather than papered
  over).
- Traces to: originating request in this session's conversation; `evals/skill-benchmark-pilot/README.md`.

## Questioning-attitude summary

- Decision question: do the 28 skills, individually, change model behavior in a way worth their
  token/cost overhead — and where the evidence shows a real problem, is it fixable without
  regressing what already works?
- Evidence that would change the decision: a skill's amendment regressing its validated niche; a
  result failing to replicate across models in a way that invalidates rather than just qualifies
  the original finding; an adversarial critique finding the benchmark methodology itself unsound.
- Assumptions that changed the mode: this started as read-only evaluation (would have been Quick/no
  packet) and became Standard once it started changing shipped skill content that shapes agent
  behavior across the whole repo.
- Facts still needing validation: whether `creating-change-records`'s Haiku gap generalizes to other
  skills; whether the other 24 skills not multi-model-checked would show similar divergences;
  whether PR #63's `briefing-an-agent` version (still unmerged) should supersede this branch's.
- Stop or hold conditions: stop amending a skill after one adversarially-reviewed attempt if
  validation shows the root cause is a model-capability boundary, not a fixable wording gap (applied
  to `creating-change-records`).

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `skills/briefing-an-agent/SKILL.md` | Skill (AI behavior) | Content amended: narrowed scope to remove overlap with `handing-off-work`; changes what the skill instructs a model to do | `skills/briefing-an-agent/SKILL.md` |
| `skills/creating-change-records/SKILL.md` | Skill (AI behavior) | Content amended: added an explicit instruction to name required packet files by name; changes model output structure | `skills/creating-change-records/SKILL.md` |
| `commands/ng-context-pack.md`, `commands/ng-new.md` | Generated command cards | Mechanical projection of the two amended skills; must stay in sync or `test_command_parity.py` fails | `commands/` |
| `tests/fixtures/command_prompts.json` | Golden snapshot fixture | Pins the `## Prompt` text of every skill byte-for-byte; deliberately updated twice this change (once per amended skill), per the repo's own baseline-discipline practice | `tests/fixtures/command_prompts.json` |
| `evals/skill-benchmark-pilot/` (new directory) | Evaluation tooling and evidence | The benchmark itself: harness scripts, every raw scenario/criterion/response, generated reports | `evals/skill-benchmark-pilot/` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | Medium | Two skill files that shape agent behavior across the whole repo changed content; a wrong amendment could make a skill worse, not better. |
| Reversibility | High | Fully reversible via git; no runtime, data, or production system touched. |
| Detectability | High | Full test suite, ruff, doctor, gen-commands parity, and this packet's own validator all catch structural drift immediately. |
| Exposure | Medium | Public repo; the benchmark's claims and the skill amendments are both things downstream adopters could read and rely on. |
| Uncertainty | Medium | Benchmark methodology has known, disclosed statistical limits (n=3-5, no significance after correction); one amendment (`creating-change-records`) was validated and found insufficient, which is itself uncertainty worth carrying forward, not resolved. |
| Dependency trust | Low | No new external dependency; `claude` CLI headless mode is the only new tool surface, already present in the environment. |
| AI authority | Medium | The benchmark runs an AI agent with `--dangerously`-adjacent flags are NOT used; runs are sandboxed (`--safe-mode`, restricted tool list, isolated empty directories, budget caps). The amendments change what future AI agents will be instructed to do via the skill files. |
| Controllability (human gate can catch/reverse in time?) | High | Every change is a PR under human review; nothing here is auto-applied to a running system. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | — |
| Known procedure where following the steps matters | yes | packet path (this record); the repo's own draft→critique→apply→validate discipline was followed for both skill amendments |
| New or uncertain work where the assumptions may be wrong | yes | questioning attitude applied throughout (adversarial critique of the amendment plan itself; a critique of each skill amendment before trusting it) |
| Work that was interrupted, resumed, or handed off | no | single continuous session |
| A high-stakes critical action | no | reversible, PR-gated, no production system |

## Selected mode

- Mode: Standard
- Why this mode: user-visible/agent-visible behavior changed (two skill files that shape how
  future AI agents act), and the benchmark itself makes a public, falsifiable claim about which
  skills add measured value — both cross the administrative floor and the Quick bar.
- Why lighter mode is not enough: a Quick record's `risk.md`+`proof.md` can't carry the
  claim-to-evidence trace this work actually needs (statistical methodology, multi-model
  divergence, adversarial review findings, cross-PR reconciliation) — reviewers need to see the
  full chain, not just a pass/fail.
- Why heavier mode is not yet required: no production system, no credentials, no irreversible
  action; fully reversible via PR review and git.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Folded into this record's own sections rather than a separate file; no long drifting session requiring re-anchoring. | — |
| `basis.md` | yes | See `basis.md`. | FlyFission |
| `verification.md` | yes | See `verification.md`. | FlyFission |
| `ship.md` | yes | See `ship.md`. | FlyFission |
| `turnover.md` | no | Single continuous session, no handoff. | — |
| `self-check.md` | no | Critical-action self-checks were done inline via adversarial-review subagents per amendment, documented in `AMENDMENT_VALIDATION.md` and `MULTI_MODEL_CHECK.md` rather than a separate self-check file. | — |
| `supplier-trust.md` | no | No new dependency, model, or supplier introduced. | — |
| Nuclear subset record | no | Not applicable at this stakes level. | — |

## Immediate evidence obligations

- Minimum evidence before build: none — this was evaluation-first, amendment-second; no code was
  written before the benchmark evidence existed.
- Minimum evidence before merge/release: full test suite, ruff, doctor, and `gen-commands --check`
  green; both skill amendments adversarially reviewed and validated (before/after regression checks)
  before being kept.
- Independent review needed? Not yet performed — see `verification.md`'s evidence-independence
  section and `evals/skill-benchmark-pilot/README.md`'s self-audit ("Third-party / independent
  replication: Not yet"). A human PR reviewer is the closest independent check this work has had.

## Required links

- Packet: `.nuclear/changes/skill-benchmark-and-amendments/`
- `basis.md`
- `verification.md`
- `ship.md`
- Benchmark evidence root: `evals/skill-benchmark-pilot/` (`README.md`, `REPORT.md`,
  `GATE1_REPORT.md`, `AMENDMENT_VALIDATION.md`, `GATE2_AND_GATE3_FINDINGS.md`,
  `STATISTICAL_ANALYSIS.md`, `MULTI_MODEL_CHECK.md`, `PLAN_STATUS.md`)

## Exit criteria

- The mode is justified.
- The artifacts you turned on are named.
- Important risks, assumptions, and evidence due are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on graded quality, keeping the approved version under control (CM), software lifecycle, software assurance, secure development, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
