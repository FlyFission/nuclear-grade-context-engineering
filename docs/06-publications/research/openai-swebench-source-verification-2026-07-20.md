# OpenAI SWE-bench source verification

**Date checked:** 2026-07-20
**Purpose:** Resolve the RC1 red-team source check for manuscript citations `openai2024swebench` and `openai2026noswebench`.

## Access method

The live OpenAI pages returned a Cloudflare challenge to automated access. Their archived official-page snapshots were retrieved through the Internet Archive CDX index and Wayback payloads:

- `Introducing SWE-bench Verified`: OpenAI page snapshot `20240815183946`
- `Why SWE-bench Verified no longer measures frontier coding capabilities`: OpenAI page snapshot `20260406013110`

The source is therefore archived first-party page content, not a secondary summary. Live-page availability should still be rechecked manually at submission time.

## 2024 SWE-bench Verified claim

The archived OpenAI page states that:

- SWE-bench samples provide the agent the issue text and repository while tests are not shown to the agent;
- proposed edits are evaluated with `FAIL_TO_PASS` and `PASS_TO_PASS` tests;
- OpenAI used professional software developers to screen samples for appropriately scoped tests and sufficiently specified issue descriptions; and
- the resulting Verified subset contained 500 human-validated samples.

**Manuscript decision:** The sentence describing human-screened tasks and tests outside the solving agent is supported.

## 2026 retirement claim

The archived OpenAI page is titled *Why SWE-bench Verified no longer measures frontier coding capabilities* and states that SWE-bench Verified is increasingly contaminated. It reports:

- public benchmark/repository exposure makes contamination difficult to avoid;
- tests can be too narrow or too wide, creating false rejections or shortcut solutions;
- automated scoring is difficult to make robust;
- OpenAI had moved to reporting SWE-bench Pro and recommended that benchmark instead.

**Manuscript decision:** The sentence that OpenAI stopped using SWE-bench Verified for frontier evaluation because contamination and test defects weakened the evaluator is a fair bounded synthesis. It should not be generalized into a claim that all external execution is invalid.

## Residual limitation

Archived official-page text verifies the cited wording, but it does not independently reproduce OpenAI's contamination pipeline or test audit. The citation remains evidence of OpenAI's reported assessment, not third-party validation of that assessment.
