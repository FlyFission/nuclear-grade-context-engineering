# Nuclear-grade Skill Static Audit

This deterministic audit checks whether each `skills/*/SKILL.md` file is structurally ready for independent prompt-only vs skill-loaded A/B testing. It is a structural completeness gate, not proof of efficacy or measured lift. A 100 here can still tie or lose against prompt-only in live runs.

## Summary

- Skills audited: 28
- Average structural completeness score: 99.6/100
- Minimum structural completeness score: 96
- Maximum structural completeness score: 100
- Verdicts:
  - `ready-for-independent-live-ab`: 28

## Skill table

| Skill | Score | Verdict | Lines | Est. tokens | Eval prompts | Issues / warnings |
|---|---:|---|---:|---:|---:|---|
| `rating-change-risk` | 96 | `ready-for-independent-live-ab` | 110 | 2058 | 4+/2- | verification section has fewer than three checklist bullets |
| `breaking-down-the-work` | 97 | `ready-for-independent-live-ab` | 139 | 2727 | 4+/2- | high token cost estimate: 2727 tokens |
| `organizing-project-folders` | 97 | `ready-for-independent-live-ab` | 138 | 3033 | 3+/2- | high token cost estimate: 3033 tokens |
| `briefing-an-agent` | 100 | `ready-for-independent-live-ab` | 112 | 1774 | 4+/2- | — |
| `checking-legal-and-safety-wording` | 100 | `ready-for-independent-live-ab` | 98 | 1204 | 3+/2- | — |
| `checking-release-readiness` | 100 | `ready-for-independent-live-ab` | 112 | 1894 | 4+/2- | — |
| `checking-source-claims` | 100 | `ready-for-independent-live-ab` | 98 | 1161 | 3+/2- | — |
| `checking-what-a-change-affects` | 100 | `ready-for-independent-live-ab` | 91 | 1268 | 4+/2- | — |
| `choosing-what-to-control` | 100 | `ready-for-independent-live-ab` | 89 | 1226 | 3+/2- | — |
| `closing-stale-packets` | 100 | `ready-for-independent-live-ab` | 121 | 2245 | 4+/2- | — |
| `creating-change-records` | 100 | `ready-for-independent-live-ab` | 101 | 1366 | 3+/2- | — |
| `deciding-who-decides` | 100 | `ready-for-independent-live-ab` | 107 | 1668 | 3+/2- | — |
| `declaring-intent` | 100 | `ready-for-independent-live-ab` | 106 | 1578 | 3+/2- | — |
| `double-checking-before-acting` | 100 | `ready-for-independent-live-ab` | 106 | 1292 | 4+/2- | — |
| `handing-off-work` | 100 | `ready-for-independent-live-ab` | 102 | 1324 | 3+/2- | — |
| `learning-from-experience` | 100 | `ready-for-independent-live-ab` | 106 | 1838 | 4+/2- | — |
| `proving-claims` | 100 | `ready-for-independent-live-ab` | 107 | 1709 | 4+/2- | — |
| `questioning-attitude` | 100 | `ready-for-independent-live-ab` | 120 | 1950 | 5+/2- | — |
| `recording-a-known-good-version` | 100 | `ready-for-independent-live-ab` | 93 | 1228 | 3+/2- | — |
| `recording-what-an-agent-did` | 100 | `ready-for-independent-live-ab` | 123 | 1926 | 3+/2- | — |
| `reporting-shared-defects` | 100 | `ready-for-independent-live-ab` | 104 | 1690 | 3+/2- | — |
| `responding-to-incidents` | 100 | `ready-for-independent-live-ab` | 107 | 1548 | 3+/2- | — |
| `reviewing-code-quality` | 100 | `ready-for-independent-live-ab` | 114 | 1832 | 3+/2- | — |
| `staying-on-mission` | 100 | `ready-for-independent-live-ab` | 130 | 2436 | 4+/2- | — |
| `stress-testing-agent-changes` | 100 | `ready-for-independent-live-ab` | 123 | 2052 | 3+/2- | — |
| `tracking-deficiencies` | 100 | `ready-for-independent-live-ab` | 106 | 1517 | 3+/2- | — |
| `using-nuclear-grade` | 100 | `ready-for-independent-live-ab` | 108 | 2060 | 3+/2- | — |
| `vetting-outside-code-and-models` | 100 | `ready-for-independent-live-ab` | 102 | 1752 | 3+/2- | — |

## Recommended use

1. Treat `fix-before-live-ab` as a hard stop for live benchmark budget.
2. Treat `ready-for-independent-live-ab` only as eligibility for measurement; prioritize live A/B on PR-pilot ties/losses, overlap pairs, and thin-margin wins.
3. Keep this audit in CI as a cheap guard, but never cite the score as measured skill lift.
4. Pair this report with live route/output manifests and raw transcripts before claiming a skill improves over prompt-only.
