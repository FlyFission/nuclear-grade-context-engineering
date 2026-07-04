# Skill Benchmark Pilot

**Purpose:** Test, objectively, whether loading a specific Nuclear-grade skill
changes a model's behavior versus a plain prompt with the same facts —
per-skill, with real cost/token data, blind grading, and every raw transcript
kept for independent inspection.

**Status:** An internally authored pilot benchmark. It is not an independent
benchmark, a certification, a safety claim, or a production-readiness claim.
See the self-audit in "How this holds up against industry practice" below
before treating any single result as settled.

**Relationship to the other comparison in this repo:**
[`docs/03-worked-examples/skill-workflow-comparison/`](../../docs/03-worked-examples/skill-workflow-comparison/)
is a qualitative, author-judged comparison of 12 realistic changes done with
and without the full Nuclear-grade workflow — it says up front that it is "not
a benchmark." This directory is the mechanized, per-skill complement: headless
runs, blind LLM grading against pre-registered criteria, real `$`/token/turn
data pulled from the API response, and every prompt, criterion, and raw
response checked into git.

## Start here

| If you want... | Read |
|---|---|
| The headline result across all 28 skills | The table below |
| The first pilot (round 1, all 28 skills, easy trigger-case scenarios) | [`REPORT.md`](REPORT.md) |
| The hard-case retest of the 14 skills that tied or lost in round 1 | [`GATE1_REPORT.md`](GATE1_REPORT.md) |
| A worked example of diagnose → fix → validate on one skill (`briefing-an-agent`) | [`AMENDMENT_VALIDATION.md`](AMENDMENT_VALIDATION.md) |
| Closeout of the two remaining open skills, and an overlap sweep across the rest | [`GATE2_AND_GATE3_FINDINGS.md`](GATE2_AND_GATE3_FINDINGS.md) |
| Every raw prompt, criterion, and model response | [`data/`](data/) (organized by pilot round) |
| The scripts that produced all of the above, and how to rerun or extend them | [`scripts/`](scripts/) |

## Final status, all 28 skills

27 of 28 skills have demonstrated evidence of changing model behavior versus a
plain prompt, at some point across the two test rounds and the two closeout
checks below. 1 (`creating-change-records`) is unresolved, not lost.

| Skill | Status | Strongest evidence |
|---|---|---|
| `reviewing-code-quality` | WINS | Round 1, 3-task design: 9/9 vs 6/9 |
| `breaking-down-the-work` | WINS (thin margin) | Round 1, n=3: 3/3 vs 2/3(+1p) |
| `briefing-an-agent` | WINS (amended) | Tied both rounds; diagnosed as scope overlap with `handing-off-work`, amended, revalidated on true niche: 5/5 vs 0/5 |
| `checking-legal-and-safety-wording` | WINS | Gate 1: 5/5 vs 4/5(+1p) |
| `checking-release-readiness` | WINS | Gate 1: 5/5 vs 4/5(+1p) |
| `checking-source-claims` | WINS (thin margin) | Round 1, n=3: 3/3 vs 2/3(+1p) |
| `checking-what-a-change-affects` | WINS | Gate 1: 5/5 vs 1/5(+4p) |
| `choosing-what-to-control` | WINS | Round 1, n=3: 3/3 vs 1/3(+2p) |
| `closing-stale-packets` | WINS | Round 1, n=3: 1/3(+2p) vs 0/3 |
| `creating-change-records` | **OPEN** | Round 1 marginal loss, Gate 1 tie; a follow-up structural recheck was partially supportive but the Gate 1 portion of that recheck used a flawed grading criterion and was discarded, not fixed |
| `deciding-who-decides` | WINS | Gate 1: 5/5 vs 2/5(+3p) |
| `declaring-intent` | WINS | Round 1, n=3: 2/3(+1p) vs 0/3(+2p) |
| `double-checking-before-acting` | WINS (thin margin) | Round 1, n=3: 3/3 vs 2/3(+1p) |
| `handing-off-work` | WINS | Gate 1: 5/5 vs 0/5(+1p) |
| `learning-from-experience` | WINS | Round 1, n=3: 3/3 vs 0/3(+2p) |
| `organizing-project-folders` | WINS | Gate 1: 5/5 vs 4/5(+1p) |
| `proving-claims` | WINS (closed via recheck) | Tied both rounds on decision correctness; closed by re-grading existing transcripts on artifact structure: 5/5 vs 0/5 |
| `questioning-attitude` | WINS (thin margin) | Round 1, n=3: 3/3 vs 2/3(+1p) |
| `rating-change-risk` | WINS | Gate 1: 4/5(+1p) vs 0/5(+1p) |
| `recording-a-known-good-version` | WINS | Round 1, n=3: 3/3 vs 0/3(+1p) |
| `recording-what-an-agent-did` | WINS | Gate 1: 4/5(+1p) vs 0/5(+5p) |
| `reporting-shared-defects` | WINS | Round 1, n=3: 3/3 vs 0/3(+3p) |
| `responding-to-incidents` | WINS | Gate 1: 5/5 vs 4/5(+1p) |
| `staying-on-mission` | WINS (thin margin) | Round 1, n=3: 3/3 vs 2/3(+1p) |
| `stress-testing-agent-changes` | WINS | Gate 1: 3/5(+2p) vs 0/5(+5p) |
| `tracking-deficiencies` | WINS | Round 1, n=3: 3/3 vs 0/3(+2p) |
| `using-nuclear-grade` | WINS | Round 1, n=3: 2/3 vs 0/3 |
| `vetting-outside-code-and-models` | WINS | Gate 1: 5/5 vs 4/5(+1p) |

"Thin margin" flags the 5 wins riding on a single trial's difference out of 3,
with one PARTIAL grade — real signal, weakest confidence on this list, never
retested at n=5. 14 of the 28 wins rest on round-1 evidence only (n=3, one
scenario) because they didn't need Gate 1's harder retest — that's fewer
trials than the skills that did.

## How this holds up against industry practice

Checked against Stanford HELM's transparency principles, the *Agentic
Benchmark Checklist* (Zhang et al., arXiv:2507.02825), and BetterBench's
46-item benchmark quality framework (arXiv:2411.12990), plus a direct look at
[BenchFlow AI's SkillsBench](https://github.com/benchflow-ai/skillsbench), a
comparable skill-evaluation benchmark with a genuinely stronger methodology in
places. Self-graded, not claimed as compliant:

| Practice | Status | Note |
|---|---|---|
| Raw prompts and completions published | **Yes** | Every scenario, criterion, and model response is in `data/`, matching HELM's top transparency practice. |
| Reproducible: scripts + exact commands checked in | **Yes** | `scripts/` reruns any pilot; exact `claude -p` flags are documented in each report. |
| Non-independence of task/criteria authorship disclosed | **Yes, prominently** | Same effort that built the skills built the tests, for every skill. Stated in the executive summary of `REPORT.md`, not buried in a footnote. |
| Bugs found during the run disclosed, not silently fixed | **Yes** | A tool-blocking harness bug (round 1) and a markdown-fence rendering bug (report generation) are both documented with before/after impact in `REPORT.md`. |
| Blind grading (grader doesn't know which condition it's scoring) | **Yes** | A separate model (Haiku) grades from the response text alone. |
| Statistical significance / confidence intervals | **No** | n=3–5 per cell, no formal CI or p-value computed per skill (one Fisher-exact estimate is mentioned qualitatively in `REPORT.md`, not applied systematically). This is the single biggest gap against current benchmark-reporting practice — see BetterBench's finding that most benchmarks skip this. |
| Task difficulty pre-calibrated against measured baseline performance | **No** | SkillsBench explicitly targets tasks where SOTA is measured below 50% *before* finalizing them. This pilot discovered its ceiling effects (11 of 13 round-1 ties were the baseline already at 100%) only after running round 1, and needed a full second round (Gate 1) to correct for it. Pre-measuring baseline performance before finalizing a scenario would have caught this up front. |
| Automated, non-LLM-graded verification (oracle + test execution) | **No, and not always applicable** | SkillsBench verifies with real oracle solutions and test scripts — stronger than LLM grading wherever the output is code-checkable. Most of these skills produce a judgment or a document, not code with a testable oracle, so LLM-based blind grading is close to the only practical option for them. Where a skill's output *is* code-checkable (`reviewing-code-quality`), an oracle-based redesign is a legitimate, unimplemented improvement. |
| Multi-model comparison | **No** | One subject model throughout (`claude-sonnet-5`), one grading model (`claude-haiku-4-5`). SkillsBench evaluates 6 frontier models by design. |
| Third-party / independent replication | **Not yet** | Invited, not performed. No outside reviewer who didn't help build the skills has re-run or re-scored this. |

**Read this table as the actual limitations section, not a compliance
checkmark list.** The "No" rows are the real, current gaps — not disclaimers
to skim past.

## What this is NOT

Not a certification, not a safety or security claim, not proof the skills
broadly improve model performance, not independently verified. It is evidence
that, on the specific scenarios tested, loading a specific skill changed a
specific model's behavior in a specific, checkable way — nothing broader
should be read into any single result without checking that result's own
report for its caveats.
