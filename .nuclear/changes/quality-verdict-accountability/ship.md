# Quality / Verdict / Accountability — Ship

## Purpose

State the release decision, what backs it, and what stays open.

## Verdict

**ship-with-named-risk.**

The change is additive documentation. All deterministic checks pass on the current tree: 317 collected with 0 failures, ruff clean, `doctor` OK, token budget OK, command parity restored after regeneration, and no skill added or removed (29, matching `main`). The claims each trace to a public source, and every citation carries its boundary.

It is not a plain `ship` because two of the three new sources come from a single commercial vendor whose product category both findings favor, and because link liveness could not be verified from this environment. Those are named below rather than absorbed into a clean verdict.

## Named risks

| Risk | Why it is accepted | What would change the decision |
|---|---|---|
| Both statistical sources are vendor-authored or vendor-run, and neither is independently replicated | They are the best available public evidence on their questions, and the affiliation is disclosed at every citation point plus in a standing `source-map.md` note. The repo cites them as prevalence and cost evidence, never as efficacy proof for its own method | A replication contradicting either finding, or use of the figures to support a claim about Nuclear-grade's effectiveness |
| Link liveness unverified (`verification.md` V-14) | The environment's egress policy denies the hosts; the figures are corroborated across independent outlets. Both source rows are therefore held at `public-url-needed` rather than `verified-public`, since that status means *link checked* and it was not | A reviewer with unrestricted egress confirming the URLs — which promotes both rows — or finding any of them dead |
| The archetype source is a social-media post | Cited as `supporting-context` only, with a mirror recorded | The post being deleted, leaving no canonical reference |
| The archetype→mode-floor mapping is new and unvalidated | It is stated as this repo's authored extension, not as an external claim | First self-assessment cycle showing it changed no real grading decision — that would make it decorative, and decorative rigor should be cut |
| The `mcp` extra is now capped below 2.x, so the repo is pinned to a superseded major line | The cap restores a broken CI job today and narrows rather than widens what is accepted. The alternative — porting `mcp_server.py` to the 2.x API — is real code work outside this change's scope and needs its own packet | A 2.x port landing, or a security advisory against the 1.x line. Either should lift the bound rather than raise it silently |
| Advisories against `mcp` 1.x were not checked | The pin was made to repair CI, not as a supplier trust decision, and `mcp` was already an accepted optional dependency. But holding a superseded major line without checking its advisory status is a real gap, not a formality — see the dependency table in `verification.md` | Any advisory against 1.x; that turns the bound from a repair into a liability and forces the 2.x port |
| An unrelated repair rides in a doctrine PR | The owner was asked and chose this over a separate PR; the break is repo-wide and the fix is one constraint. Argued in `risk.md`, not silently absorbed | If a reviewer prefers the split, the `pyproject.toml` change lifts out cleanly as its own commit |

## Apply-clearance

This verdict is evidentiary acceptance only. Merge authority stays with a human reviewer via PR. The authoring agent drafted the doctrine, selected the evidence, and wrote the verification record; it does not clear its own work. See `docs/02-operating-system/quality-verdict-accountability.md` — this packet is the accountability term applied to itself.

## Rollback

**Documentation and packet edits.** Additive; they revert with normal git history. The one generated artifact (`commands/ng-code-review.md`) is reproducible with `python tools/ng.py gen-commands .`.

**The `pyproject.toml` constraint is not documentation and needs its own handling.** Reverting it to `mcp>=1.0` restores the resolution that breaks `mcp-smoke`, so a plain revert re-opens the fault this change closed. Two supported paths, depending on why the bound is being removed:

| Reason the bound must go | Correct move | Not this |
|---|---|---|
| A 2.x port of `nuclear_grade/mcp_server.py` lands | Lift the ceiling to `mcp>=2` (or a range the ported code supports) **in the same change as the port**, so the constraint and the code that depends on it move together | Removing the bound ahead of the port |
| An advisory lands against the 1.x line | Treat as an incident, not a rollback: the port becomes urgent, and the extra should be marked unavailable rather than left resolving to a vulnerable line | Widening the range and hoping resolution avoids 1.x |
| The reviewer prefers this repair as its own PR | Revert only the `pyproject.toml` hunk from this branch; nothing else in this change depends on it | Reverting the whole change |

The constraint is a controlled item under `docs/02-operating-system/controlled-items.md`, so whichever path is taken updates the baseline rather than being handled as an untracked edit.

## Baseline trigger

Re-open this packet if: either statistical finding is replicated or contradicted; the archetype source becomes unreachable; or a `program-self-assessment.md` cycle finds the archetype lens has not changed a grading decision in practice.

## Monitoring

None applicable — no runtime behavior changes.

## Required links

- Risk: `risk.md`
- Basis: `basis.md`
- Plan: `plan.md`
- Trace: `trace.md`
- Verification: `verification.md`

## Exit criteria

- The decision is one of ship / block / defer / ship-with-named-risk, stated out loud.
- The residual risk, rollback, and baseline trigger are named.
- Apply-clearance is distinguished from the verdict.

## Source-lineage note

Original Nuclear-grade packet inspired by public release-readiness and configuration-management concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
