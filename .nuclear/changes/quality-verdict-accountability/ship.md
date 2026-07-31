# Quality / Verdict / Accountability — Ship

## Purpose

State the release decision, what backs it, and what stays open.

## Verdict

**ship-with-named-risk.**

The change is additive documentation. All deterministic checks pass: 238 tests green, ruff clean, `doctor` OK, token budget OK, command parity restored after regeneration, and no skill added or removed (29, matching `main`). The claims each trace to a public source, and every citation carries its boundary.

It is not a plain `ship` because two of the three new sources come from a single commercial vendor whose product category both findings favor, and because link liveness could not be verified from this environment. Those are named below rather than absorbed into a clean verdict.

## Named risks

| Risk | Why it is accepted | What would change the decision |
|---|---|---|
| Both statistical sources are vendor-authored or vendor-run, and neither is independently replicated | They are the best available public evidence on their questions, and the affiliation is disclosed at every citation point plus in a standing `source-map.md` note. The repo cites them as prevalence and cost evidence, never as efficacy proof for its own method | A replication contradicting either finding, or use of the figures to support a claim about Nuclear-grade's effectiveness |
| Link liveness unverified (`verification.md` V-14) | The environment's egress policy denies the hosts; the figures are corroborated across independent outlets | A reviewer finding any of the four URLs dead or the figures misquoted |
| The archetype source is a social-media post | Cited as `supporting-context` only, with a mirror recorded | The post being deleted, leaving no canonical reference |
| The archetype→mode-floor mapping is new and unvalidated | It is stated as this repo's authored extension, not as an external claim | First self-assessment cycle showing it changed no real grading decision — that would make it decorative, and decorative rigor should be cut |
| The `mcp` extra is now capped below 2.x, so the repo is pinned to a superseded major line | The cap restores a broken CI job today and narrows rather than widens what is accepted. The alternative — porting `mcp_server.py` to the 2.x API — is real code work outside this change's scope and needs its own packet | A 2.x port landing, or a security advisory against the 1.x line. Either should lift the bound rather than raise it silently |
| An unrelated repair rides in a doctrine PR | The owner was asked and chose this over a separate PR; the break is repo-wide and the fix is one constraint. Argued in `risk.md`, not silently absorbed | If a reviewer prefers the split, the `pyproject.toml` change lifts out cleanly as its own commit |

## Apply-clearance

This verdict is evidentiary acceptance only. Merge authority stays with a human reviewer via PR. The authoring agent drafted the doctrine, selected the evidence, and wrote the verification record; it does not clear its own work. See `docs/02-operating-system/quality-verdict-accountability.md` — this packet is the accountability term applied to itself.

## Rollback

Documentation only; every edit is additive and reverts with normal git history. The one generated artifact (`commands/ng-code-review.md`) is reproducible with `python tools/ng.py gen-commands .`.

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
