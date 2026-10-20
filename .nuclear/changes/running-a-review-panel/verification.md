# Running a Review Panel — Verification

## Purpose

Record what was checked, how, and what the check did and did not establish.

## Evidence ledger

| ID | Claim | Check | Result | Status |
|---|---|---|---|---|
| V-1 | Full test suite passes on the tree being accepted, which is the post-merge tree, not the tree CI saw in August | `python -m pytest` on merge commit `a33f858` | 657 passed, 2 skipped | pass |
| V-2 | Lint | `python -m ruff check .` | All checks passed | pass |
| V-3 | Repo health and internal link resolution | `python tools/ng.py doctor .` | `OK: Nuclear-grade doctor` | pass |
| V-4 | Token budget not inflated to admit the new skill | `python tools/ng.py tokens .` | `OK: token budget` | pass |
| V-5 | No whitespace or conflict residue from the merge | `git diff --check`, plus a grep for conflict markers across all tracked Markdown | clean; no markers found | pass |
| V-6 | The branch is no longer behind `main` | `git rev-list --left-right --count origin/main...HEAD` after merging `a33f858` | 0 behind | pass |
| V-7 | Skill count on disk matches every stated count | `ls -d skills/*/ \| wc -l` compared against `CORE.md` (two places), `INSTALL.md`, `cli-reference.md`, `skill-authoring-contract.md` | 30 on disk; 30 = 7 Core + 22 ancillary + 1 router in `CORE.md`; all four other statements read 30 | pass |
| V-8 | `main` added no competing skill that would collide with the count | `git ls-tree -d --name-only origin/main skills/` | 29 on `main`, 30 after this change | pass |
| V-9 | Catalog, command, and prompt-bank wiring is complete | Contract, parity, catalog, and prompt-bank tests inside V-1 | included in the 657 | pass |
| V-10 | Eval coverage meets the ratchet for a new skill | Parsed `evals/skill-routing-cases.jsonl` and counted `evals/skill-output-cases.jsonl` | 6 routing cases, 4 trigger and 2 not-trigger; 1 output case | pass |
| V-11 | The skill adds no dependency, runner, runtime directory, or external source | `git diff --name-only 3ade94e e1a61d6` reviewed in full; `git diff` on `source-map.md` for that commit | 20 files, all skill/doc/test/manifest; `source-map.md` diff empty | pass |
| V-12 | The prior refusal to add a skill rested on a README claim that has since been scoped | Read the current `README.md` pilot paragraph; `git log -S "historical snapshot, not evidence for skills added later" -- README.md` | Claim now reads "28 skills that were in the catalog when the July 2026 pilot ran" and closes "not evidence for skills added later"; landed in `b7f0ab6` (#86) | pass |
| V-13 | This skill has a measured behavior change versus a plain prompt | Not attempted | **No measurement exists.** Benchmarked set is 28; shipped set is 30 | gap |
| V-14 | The procedure has been executed end to end at least once | Not attempted | **The skill has never been used to convene an actual panel.** It is reviewed text, not exercised process | gap |
| V-15 | The axis declaration is enforced rather than requested | Read Process step 3 and `## Verification` | Enforced by instruction only; nothing mechanical prevents a seat from naming an axis it does not vary | gap |
| V-16 | `reviewing-code-quality` is unchanged | `git diff 3ade94e e1a61d6 -- skills/reviewing-code-quality/` | empty diff | pass |
| V-17 | This packet satisfies Standard mode | `python tools/ng.py validate .nuclear/changes/running-a-review-panel` | `OK` | pass |
| V-18 | GitHub CI passes on the tree being accepted | Pushed; hosted run `39445687566` on head `572a3e5` | 7 of 7 jobs green: validate 3.11 / 3.12 / 3.13, wheel-smoke, both mcp-smoke matrix legs, CI gate | pass |
| V-18a | The first hosted run after the merge | Run `39444990072` on head `53911e3` | **Failed all three validate jobs** on the evidence-badge staleness check — see the note below | superseded |
| V-19 | An independent reviewer reads the shipped text for internal contradiction | `chatgpt-codex-connector` review on head `e0b3fe2` (PR #97), two P2 findings | Both upheld on reading the source: the matrix listed the panel unconditionally in a cluster whose trigger fires on nearly every agent change, contradicting the same page's gating sentence; and the gate exclusion suppressed the panel in the Nuclear / Tier 0 flows the skill names as its primary use. Both reworded | pass |
| V-20 | Second review round on the fixed text | `chatgpt-codex-connector` review on head `e3e7af4`, one P1 and one P2 | Both upheld. P1: the Nuclear / Tier 0 path required only a diversity axis, below the three-axis plus rung-4-CI-and-human floor in `independence-architecture.md` lines 64-69 — verified against that file, not taken from the finding. P2: the V-19 fix left the panel's only matrix route nested under the Agent-authority precondition, which is false for a human-led release or security review. Both fixed | pass |

## Notes on the gaps

**V-13 is the gap this change is most likely to be judged on.** The July 2026 pilot measured 28 skills. The repo now ships 30. #86 (V-12) changed the *claim* so the pilot is reported as a historical snapshot of the catalog as it then stood, which is why a 30th skill no longer puts a repo-level statement out of true. It did not produce evidence for this skill, and nothing here should be read as if it did. The comparison table records the skill with "formal trial records pending," which is the convention this repo already uses for post-trial additions, and `ship.md` carries it as the first named risk.

**V-14 is distinct from V-13 and arguably worse.** V-13 is about a missing measurement; V-14 is about a procedure that has never been run. Every claim about this skill — that the axis declaration is load-bearing, that panel health catches a silent degradation, that step 8 stops an unverified finding from becoming an edit — is a claim about what would happen, derived by reading. A reviewer should treat the eight steps as a design to critique, not as a method with field behavior behind it. The skill's own `## Verification` section makes the matching admission about its outputs: passing proves the panel was built and reported honestly, not that its findings are correct.

**V-15 names a limit of the design, not a defect in the diff.** A seat can satisfy the declaration by asserting an axis. The skill's answer is the fold-down rule — a seat that cannot state what it varies is folded into the seat it duplicates before counting — but that rule is executed by whoever runs the panel, who may be the same agent that composed the seats. This is the self-authorship problem the repo names in `actor-evidence-independence.md`, reappearing one level up inside the remedy. Recorded rather than papered over.

**The token ceiling is now binding, and that is worth saying out loud.** The P1 fix had to be single-sourced to `independence-architecture.md` rather than restated, because restating the three axes and the backstops did not fit: the generated card sits at exactly 1600 against `command_max` 1600 and the body at 3597 against 3600. Two sentences of genuine duplication were cut to fund even the reference (an Overview line already restated in Common Rationalizations, and mechanism examples already listed in Process step 3). Single-sourcing is the better practice here anyway — a requirement restated in a skill drifts from the doctrine that owns it. But the honest reading is that this skill has consumed the budget headroom for its own file, so the gate can no longer absorb a correctness fix without a cut somewhere. Whether that calls for a higher ceiling or a shorter skill is a maintainer's call, named here rather than settled by the authoring agent — `plan.md` already refused to raise a ceiling once, and refusing it again while quietly shaving prose to fit is the same move with better manners.

**V-19: the first seat this packet did not fill itself.** Every other row in this ledger was generated, selected, and read by the authoring agent — the coupled-reviewer condition `ship.md` names as the reason its verdict is `defer`. The Codex review is one genuinely separate seat on a different model family, and it found two contradictions internal to the text that the author had read several times. That is a small but real data point for the skill's own claim: a seat varying one axis catches what the same reader re-reading does not. It does not close the `defer`, which turns on questions of judgment a review bot does not answer.

**V-18a: the local gate was not the hosted gate, and the first push proved it.** The four commands this packet had been treating as "the gate" (pytest, ruff, `doctor`, `tokens`) are the gate as it stood in August. The 0.6.0 release added steps this branch had never seen: a release-identity check, a committed evidence badge that CI regenerates and fails if stale, and a 3.13 matrix leg. The new change record moved the badge (54 to 55 records, 24 to 28 open items), so all three validate jobs failed on a file this packet's own addition had invalidated.

Fixed by regenerating `.nuclear/badge.json` and committing it, then re-running every step the hosted job runs rather than the four that were familiar. The lesson is small and exactly on this repo's theme: a gate inherited from a stale base is not the gate, and "my checks pass" measured a set of checks that no longer existed. It is recorded here rather than silently amended because V-18 was held at `planned` on the argument that stale green checks must not be reported as current — and then the first honest run went red, which is the argument working.

**A side finding from the same fix.** While regenerating the badge, the open-item count read 29 where this ledger has 28. The counter reads statuses from both prose and table cells, and the word "Deferred" in V-18's result cell was counted alongside that row's `planned` status, double-counting one item. The cell was reworded. The badge is a public evidence surface, so a number inflated by a stray word is a misstatement even when it errs toward looking worse.

**Why V-18 was held at `planned` until it could be `pass`.** The four green checks visible on the PR completed on 2026-08-05 against base `3ade94e`. `main` has since taken #110 and #114. Reporting those checks as current evidence would be the exact substitution this repo warns about: a green badge from a run that did not test the tree being accepted. The local gate was re-run on the merge result instead, and the hosted run is owed before merge.

## What this verification does not establish

- That the procedure improves a panel outcome. Nothing here measures it, and nothing here has run it (V-13, V-14).
- That the eight steps are the right decomposition. The tests confirm the skill is well-formed, wired, and within budget — not that its content is correct. That judgment is the reviewer's.
- That declaring an axis makes seats independent. The skill says so itself; independence extends only as far as the axes actually varied, and the declaration is unenforced (V-15).
- That the catalog is the right home. Doctrine pages were the precedent for the two previous concept additions; this change argues a procedure differs from a concept, and that argument is in `basis.md` for a reviewer to reject.

## Evidence custody and coupling

The agent that wrote the skill also wrote the doctrine cross-links, this record, and ran every check in it. See `../../../docs/02-operating-system/actor-evidence-independence.md`. The irony is noted and not resolved: the change adds a procedure for not trusting a single coupled reviewer, and its own evidence has exactly one.

### Custody record

| Evidence ID | Claim ID | Decisive? | Artifact / raw result | Change actor | Generated by | Selected by | Transformed / summarized by | Executed / captured by | Retained by | Presented by | Verified / witnessed by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | REQ-008 | yes | `pytest`, `ruff`, `doctor`, `tokens`, `diff --check` output (V-1 to V-5) | AI agent | repo test suite and checkers | whole suite, no selection | not summarized beyond counts, pass, and fail | AI agent | git | AI agent | nobody yet; reproducible verbatim by any reviewer |
| E-002 | REQ-008, REQ-009 | yes | Count and diff inspections (V-7, V-8, V-11, V-16) | AI agent | git | AI agent | AI agent | AI agent | packet | AI agent | nobody yet; commands stated so they are re-runnable |
| E-003 | REQ-007 | yes | README claim status and its origin commit (V-12) | AI agent | repo history and `README.md` | AI agent | AI agent | AI agent | packet | AI agent | nobody yet; `git log -S` re-derives it |
| E-004 | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-010 | yes | Readings of the skill text against each claim | AI agent | AI agent | AI agent | AI agent | AI agent | packet | AI agent | nobody; not independently witnessed |
| E-005 | REQ-007 | yes | Absence of any efficacy or execution evidence (V-13, V-14, V-15) | AI agent | not applicable; nothing was produced | AI agent | AI agent | not executed | packet | AI agent | nobody; the absence is the finding |

### Coupling profile

Every row classifies as **self-check**. The deterministic rows feel independent because the tooling is standard and reproducible, but the change actor still chose what to run, ran it, and presented it — and this repo's rule is that a role label is not independence. Reproducibility belongs in the disposition, not in the classification.

| Evidence ID | Actor | Context | Mechanism | Authority | Resource | Classification | Admissibility / residual-risk disposition |
|---|---|---|---|---|---|---|---|
| E-001 | coupled; the agent ran the suite and reported it | partially separated; the suite and checkers predate this change and the agent did not author them | partially separated; standard tooling the agent cannot silently alter | partially separated; a human owns merge | separated; no budget pressure shaped the outcome | self-check | admitted; reproducible verbatim, residual risk carried to `ship.md` |
| E-002 | coupled; the agent chose and ran the inspections | coupled; authored and executed in one session | partially separated; plain git commands, stated in full | partially separated; a human owns merge | separated; no budget pressure shaped the outcome | self-check | admitted; commands stated so a reviewer can re-run them, residual risk carried to `ship.md` |
| E-003 | coupled; the agent chose which history to query | partially separated; the README text and the commit predate this change | partially separated; `git log -S` over existing history | partially separated; a human owns merge | separated; no budget pressure shaped the outcome | self-check | admitted; the admissibility argument rests on this row, so a reviewer should re-derive it, residual risk carried to `ship.md` |
| E-004 | coupled; the agent read text it wrote | coupled; same session | coupled; unaided reading, no external check | partially separated; a human owns merge | coupled; the agent set its own depth | self-check | admitted only as a claim to re-derive; the reviewer must read the skill, residual risk carried to `ship.md` |
| E-005 | coupled; the agent reports the absence of its own evidence | coupled; same session | coupled; no mechanism, because nothing was run | partially separated; a human owns merge | coupled; the agent chose not to run a trial | self-check | admitted as a disclosed gap, not as evidence; carried to `ship.md` as the first named risk |

- **Evidence pattern used:** actor-selected artifacts and actor narrative throughout. No row reaches independent reproduction, because nobody but the change actor has run anything.
- **Verdict owner:** human reviewer via PR.
- **Apply-clearance owner:** human reviewer via PR; the authoring agent holds neither.
- **Minimum profile required by the consequence:** an additive public catalog surface with an independence claim — deterministic checks reproducible, the admissibility argument independently re-derivable, and the efficacy gap disclosed at every surface that could be read as measured. Met for E-001 to E-003 and E-005; E-004 is reader-dependent by nature.
- **Any unmet separation carried into `ship.md`:** yes — no efficacy measurement, no end-to-end execution, and an unenforced axis declaration. The hosted CI run is no longer owed (V-18), but it was owed when this row was first written, and it went red.

## Commands, evals, and reviews

```bash
python -m pytest                                            # 657 passed, 2 skipped
python -m ruff check .                                      # All checks passed
python tools/ng.py doctor .                                 # OK: Nuclear-grade doctor
python tools/ng.py tokens .                                 # OK: token budget
git diff --check                                            # clean
ls -d skills/*/ | wc -l                                     # 30
git rev-list --left-right --count origin/main...HEAD        # 0 behind after the merge
git diff --name-only 3ade94e e1a61d6                        # 20 files, skill/doc/test/manifest only
git log -S "historical snapshot, not evidence for skills added later" -- README.md
python tools/ng.py validate .nuclear/changes/running-a-review-panel
```

## Negative / failure-mode checks

- A stated skill count disagreeing with the folder count: checked across six statements, 0 mismatches.
- Conflict markers surviving the merge: grepped across tracked Markdown, 0 found.
- A comparison-table row implying this skill was measured: read, phrased as pending; 0 found.
- An edit to `reviewing-code-quality` sneaking the overlay into a clean contract: diff empty.
- The token ceiling raised to admit the new file: `nuclear-grade.yaml` budgets unchanged; the skill was cut instead.
- A new external source cited without registration: the skill's five sources were already in `source-map.md`, and that file is untouched by the skill commit.
- The packet claiming strict-authority or strict-custody validation it did not run: neither is claimed; V-17 records the default run only.

## AI-assisted work checks

- Scope: the agent drafted the skill, the doctrine cross-links, the eval cases, the CHANGELOG entry, this packet, and resolved the `main` merge. It ran read-only verification commands plus the local gate.
- Authority: no credentials held, no production code changed, no CI workflow, hook, or gate authored or edited.
- Approval: merge decision stays with a human via PR review; the PR remains a draft.
- Custody and coupling: recorded above; coupled on authorship, selection, and presentation for every row.

## Security / dependency / supply-chain checks

| Item | What the check establishes | Status |
|---|---|---|
| Dependencies | None added, removed, or re-bounded. `pyproject.toml` is untouched by this change | pass |
| New runtime surface | None. No runner script, no provider configuration, no new top-level or runtime directory; the originating draft's `.council/`-style directory was deliberately dropped | pass |
| External network use | None. The skill is text; nothing it adds fetches anything at runtime or in CI | pass |
| Credential or permission surface | Untouched. The skill grants no tool access and its prompt directs no write action | pass |
| New external sources | None registered; all five cited sources were already in `source-map.md` | pass |
| Untrusted-input handling in the procedure | The skill treats packet contents and reviewer output as material to verify before acting, and forbids promoting an unverified finding to a recommendation. This is an instruction, not an enforced boundary | pass with the V-15 limit |

## Required links

- Risk: `risk.md`
- Basis: `basis.md`
- Plan: `plan.md`
- Trace: `trace.md`
- Ship: `ship.md`
- Skill: `../../../skills/running-a-review-panel/SKILL.md`
- Coupling doctrine: `../../../docs/02-operating-system/actor-evidence-independence.md`

## Exit criteria

- Every claim has a status.
- The gaps are described rather than smoothed over, and the two that matter most are separated.
- The limits of the verification are stated.
- Stale hosted CI is recorded as owed, not reported as current.

## Source-lineage note

Original Nuclear-grade packet inspired by public verification, evidence-status, evidence-custody, and independent-review concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
