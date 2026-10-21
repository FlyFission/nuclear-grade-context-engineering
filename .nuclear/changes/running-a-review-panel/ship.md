# Running a Review Panel — Ship

## Purpose

State the release decision, what backs it, and what stays open.

## Verdict

**defer — to a human, on two questions the authoring agent should not answer for itself.**

The evidentiary record is complete and the deterministic surface is clean. On the post-merge tree: 657 passed and 2 skipped, ruff clean, `doctor` OK, token budget OK, `git diff --check` clean, 30 skill folders matching all six stated counts, eval ratchet met, no dependency or runtime surface added, and this packet validating at Standard. The branch is no longer behind `main`.

It is not `ship` and not `ship-with-named-risk`, because two of the open items are not risks to accept — they are decisions:

1. **Should the repo add a 30th skill with no efficacy evidence?** An earlier packet in this repo answered no, and its decisive objection was the gap between the benchmarked and shipped catalogs. That objection was about a README claim that #86 has since scoped (`verification.md` V-12), which is why the question is live again rather than settled against. But the evidence did not improve — the gap went from one skill to two — and whether disclosure is sufficient where the earlier decision demanded measurement is a maintainer's call about the repo's own standard. An agent that wants the skill merged is the wrong party to decide it.
2. **Is a procedure different enough from a concept to earn a skill rather than a doctrine page?** The repo's precedent is explicit and runs the other way twice: `CORE.md` refused a skill for workflow architecture, "its home is the doctrine page, not a new `SKILL.md`," and the quality/verdict/accountability change landed as doctrine for the same reason. `basis.md` argues a procedure differs because an adopter executes it. That argument is in the record to be rejected, not asserted as settled.

Everything else below is a named risk in the ordinary sense, carried rather than hidden.

## Named risks

| Risk | Why it is accepted | What would change the decision |
|---|---|---|
| No efficacy evidence for this skill; the pilot measured 28 and the repo ships 30 | #86 scoped the pilot claim to the tested catalog, so no repo-level statement is now false. The gap is disclosed in the comparison table, the CHANGELOG, and here | A fresh benchmark run including this skill; or a maintainer judgment that unmeasured catalog entries are no longer acceptable, which blocks rather than adjusts |
| The procedure has never been run end to end | It is additive text that changes no runtime behavior, and the skill's own `## Verification` section says passing proves the panel was reported honestly, not that its findings are correct | First real use showing a step is unworkable, or showing the procedure changed no decision — which would make it decorative, and decorative rigor should be cut |
| The axis declaration is unenforced; a seat can name an axis it does not vary | The fold-down rule gives a reviewer something to check, and the skill states the limit rather than implying mechanical independence | A mechanical check becoming feasible, or field use showing the declaration is routinely gamed |
| Hosted CI — closed, after going red once | The first hosted run after the merge failed all three validate jobs on the evidence-badge staleness check that 0.6.0 added, which this branch's stale gate did not include. Regenerated, re-pushed, and now 7 of 7 green on head `572a3e5` (`verification.md` V-18, V-18a) | A later red check; that returns the change to the author |
| This packet was written after the change, not before | Recorded in `risk.md`; the requirement rows are reconstructions and are labeled as such | Nothing changes it retroactively. The control to fix is the next change, not this record |
| Cluster placement in `CORE.md` is a judgment call | Narrowed over review rounds two and three: the panel now has its own matrix route keyed to the verdict trigger, an overlay rather than a sixth cluster, and is still counted once inside Agent authority. Whether that is the right home remains a reviewer's call | A reviewer preferring a different home; a one-line move with a count re-check |
| The custody and coupling requirement, and the token ceiling that blocked it | **Resolved, with a controlled limit changed on the owner's decision.** The finding was real: a panel record could pass this skill's checklist while the change actor selected the packet, framed the context, and held retention and authority. The fix did not fit, the owner chose to reseed `skill_body_max` to 3900 and `command_max` to 1700, and both the fix and the reseed are applied. The basis sits beside the values in `nuclear-grade.yaml`, and both new ceilings still reject the bloated first draft `plan.md` refused a raise for (`verification.md` V-22, V-23) | A later skill consuming this margin the same way. The pattern to watch is a ceiling being raised per-file on demand, which is how a regression gate becomes a formality; the next raise should ask whether the skill is too long instead |
| The originating draft's runner and provider panel were dropped | The catalog is host-neutral; a vendor CLI list dates immediately, and a directory holding raw reviewer output raises retention and redaction questions this change does not answer | Wanting the orchestration shipped — in which case it belongs in `INTEGRATIONS.md` with its own packet, not in `skills/` |

## Apply-clearance

This verdict is evidentiary acceptance only, and it is deliberately short of clearance. Merge authority stays with a human reviewer via PR; the PR remains a draft. The authoring agent wrote the skill, the doctrine cross-links, the eval cases, this packet, and ran every check cited in it — a single coupled reviewer, which is the precise condition the skill being added exists to refuse. Treating its own self-check as clearance would be the failure the change is about.

## Release decision

No release is proposed. Nothing here touches `pyproject.toml`, the version, the plugin manifests, or `CITATION.cff`, so the release identity check is unaffected and no tag is implied. The `CHANGELOG.md` entry sits under `[Unreleased]`, where the merge resolution deliberately placed it rather than backdating it into the shipped 0.6.0 section. The next release decision picks it up on its own schedule.

## Rollback

Additive text plus one generated artifact. Reverting the skill commit removes `skills/running-a-review-panel/`, the manifest entry, the catalog rows, the eval cases, and the test expectations together; `commands/ng-panel.md` is reproducible with `python tools/ng.py gen-commands .`, and `tests/fixtures/command_prompts.json` rebuilds from the same path.

Two parts need care rather than a blind revert:

| Part | Correct move | Not this |
|---|---|---|
| The skill-count statements in `CORE.md`, `INSTALL.md`, `cli-reference.md`, `skill-authoring-contract.md` | Revert them with the skill, in the same change, and re-run `ls -d skills/*/ \| wc -l` against each statement | Leaving a count of 30 with 29 folders on disk; the tests catch the manifest but prose counts are the softer surface |
| The `main` merge commit `a33f858` | Keep it. It is independent of the skill and carries the `CHANGELOG` conflict resolution; reverting it puts the branch two commits behind a release again | Reverting the merge to "undo the change," which re-opens the stale-base problem |

No baseline or controlled-item record outside this packet needs amending, because no controlled runtime item changed.

## Baseline trigger

Re-open this packet if: a benchmark run covering this skill completes, in either direction; the first real panel run finds a step unworkable or finds the procedure changed no decision; a mechanical axis check becomes feasible; or the orchestration dropped in `plan.md` is taken up, which would supersede the host-neutral scoping argued here.

## Monitoring

The change adds no runtime behavior, so there is nothing to watch in production. Two things are worth watching about the change itself, and neither is implemented by this PR — recording an intended path is more honest than claiming none is needed, but it is not the same as having one.

| What to watch | Why | How | Owner |
|---|---|---|---|
| Whether the procedure ever changes a panel decision | If it never does, it is decorative rigor and should be cut rather than maintained | The next `program-self-assessment.md` cycle, which already asks this question of new doctrine | Repo maintainer |
| Drift between the skill count on disk and the counts stated in prose | Tests pin the manifest and the rolled-up count; four prose statements are checked by reading | Add the prose counts to the count test if this recurs; today it is reviewer attention | Repo maintainer |
| Drift between the local gate and the hosted gate | The first push went red on a 0.6.0 check this branch's local gate did not include; the same class of drift recurs whenever the base adds a step | Treat the hosted job as the gate of record and re-read its steps after any base advance, rather than re-running a familiar four | Repo maintainer |

## Required links

- Risk: `risk.md`
- Basis: `basis.md`
- Plan: `plan.md`
- Trace: `trace.md`
- Verification: `verification.md`
- Skill: `../../../skills/running-a-review-panel/SKILL.md`
- Prior refusal being answered: `../quality-verdict-accountability/plan.md`

## Exit criteria

- The decision is one of ship / block / defer / ship-with-named-risk, stated out loud.
- Residual risk, rollback, baseline trigger, and monitoring are named.
- Apply-clearance is distinguished from the verdict.
- The questions reserved for a human are stated as questions, not absorbed into a verdict the agent issued to itself.

## Source-lineage note

Original Nuclear-grade packet inspired by public release-readiness, configuration-management, and independent-review concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
