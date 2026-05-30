# U10 - Incident Regression Fix

## Scenario Facts

- A recent change broke CLI validation for set-up external workspaces (a regression: something that used to work now fails).
- The immediate fix is small.
- The team also needs to learn why the tests missed the external-workspace path.

## Simple Prompt Trial

Prompt:

```text
Fix the external workspace validator regression and add a test.
```

Expected simple output:

- Add or patch a test.
- Fix code.
- Report tests pass.

Simple path strengths:

- Good for immediate containment.
- Low overhead for a small regression.

Simple path gaps:

- May stop after the fix without recording the case the tests missed.
- May not update docs if the onboarding behavior changed.
- May not name the triggers for re-checking later.
- May not limit the agent's power if the fix is handed off.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `checking-what-a-change-affects`
- `rating-change-risk`
- `creating-change-records`
- `briefing-an-agent`
- `handing-off-work`
- `learning-from-experience`
- `proving-claims`

Workflows exercised:

- Questioning attitude
- Quick change
- Standard change
- Agent authority change
- Agent turnover
- OPEX learning

Nuclear-grade output:

- Mode: Quick for the code fix if it is local and reversible; Standard if docs or validator behavior changed.
- Questioning attitude: why did the earlier validation miss external workspaces?
- Context pack: the agent may edit the CLI, the validator tests, and docs tied directly to external-workspace behavior.
- Turnover: keep the fix state, the changed conditions, the proof run, the remaining docs impact, and the stop rules for the next reviewer.
- Proof claims: a set-up external workspace passes doctor; a blank template still fails; the distribution repo's doctor still checks the contracts.
- Impact screen: INSTALL and the CLI reference may need updates.
- OPEX (lessons from real operation): record why the earlier tests missed external workspaces, and add a trigger for a future test whenever the onboarding docs mention external-repo behavior.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 3 | 2 | 1 |
| Nuclear-grade | 4 | 4 | 4 | 4 | 3 |

Nuclear-grade helps by keeping the lesson, not by making the small code fix harder.

## Decision

Use Quick to contain the problem, and Standard when the fix changes public onboarding behavior.

## Boundary Note

This trial does not prove the validator covers every future onboarding path.
