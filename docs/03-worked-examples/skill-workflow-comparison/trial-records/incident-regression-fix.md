# U10 - Incident Regression Fix

## Scenario Facts

- A recent change broke CLI validation for initialized external workspaces.
- The immediate fix is small.
- The team also needs to learn why tests missed the external-workspace path.

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

- May stop after the fix without recording the missed scenario.
- May not update docs if onboarding behavior changed.
- May not identify future revalidation triggers.
- May not bound agent authority if the fix is delegated.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `screening-change-impact`
- `classifying-change-risk`
- `creating-change-packets`
- `packing-agent-context`
- `proving-claims`

Workflows exercised:

- Questioning attitude
- Quick change
- Standard change
- Agent authority change

Nuclear-grade output:

- Mode: Quick for the code fix if local and reversible; Standard if docs/validator semantics changed.
- Questioning attitude: why did previous validation miss external workspaces?
- Context pack: agent may edit CLI, validator tests, and docs directly tied to external workspace behavior.
- Proof claims: initialized external workspace passes doctor; blank template still fails; distribution repo doctor still checks contracts.
- Impact screen: INSTALL and CLI reference may need updates.
- Learn trigger: add future test whenever onboarding docs mention external repo behavior.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 3 | 2 | 1 |
| Nuclear-grade | 4 | 4 | 4 | 4 | 3 |

Nuclear-grade adds value by preserving the learning path, not by making the small code fix harder.

## Decision

Use Quick for containment and Standard when the fix changes public onboarding behavior.

## Boundary Note

This trial does not prove the validator covers every future onboarding path.
