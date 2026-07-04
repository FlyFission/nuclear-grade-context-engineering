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
| Formal significance testing and a free pre-calibration audit — read this before trusting any single "WINS" | [`STATISTICAL_ANALYSIS.md`](STATISTICAL_ANALYSIS.md) |
| A small, honestly-scoped check of whether results hold on a different model | [`MULTI_MODEL_CHECK.md`](MULTI_MODEL_CHECK.md) |
| The amendment plan for this project's own self-audit gaps, adversarially reviewed before execution, plus a real cross-PR conflict it surfaced | [`PLAN_STATUS.md`](PLAN_STATUS.md) |
| Every raw prompt, criterion, and model response | [`data/`](data/) (organized by pilot round) |
| The scripts that produced all of the above, and how to rerun or extend them | [`scripts/`](scripts/) |

## Final status, all 28 skills

28 of 28 skills have demonstrated evidence of changing model behavior versus a
plain prompt on `claude-sonnet-5`, at some point across the two test rounds
and the closeout checks below. **Read this as directional pilot evidence, not
statistical proof** — see [`STATISTICAL_ANALYSIS.md`](STATISTICAL_ANALYSIS.md):
zero of the 44 significance tests run across this project survive correction
for multiple comparisons. A small honest multi-model check
([`MULTI_MODEL_CHECK.md`](MULTI_MODEL_CHECK.md)) found 3 of 4 sampled results
replicate on a different model and 1 does not — treat every "WINS" as
Sonnet-specific until shown otherwise, not as a claim about the skill in
general.

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
| `creating-change-records` | WINS on Sonnet; unresolved on Haiku | Round 1 marginal loss, Gate 1 tie on a criterion that conflated this skill's job with `rating-change-risk`'s and `proving-claims`'; re-graded on a criterion scoped to this skill's actual packet-shell job (per PR #63's independent boundary clarification): 4/5 vs 0/5. **Does not replicate on Haiku** (0/3 vs 0/3). A targeted amendment was drafted, adversarially critiqued, and applied to fix this — validated afterward and found insufficient: Sonnet held at 3/3, Haiku stayed at 0/3. Root cause is a model-capability boundary (Haiku reasons in a general safety-refusal register on this scenario, bypassing the skill's process entirely), not a fixable wording gap. Amendment kept anyway (harmless, small improvement, no regression); gap reported as attempted-and-open, not fixed. See `MULTI_MODEL_CHECK.md`. |
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
| Statistical significance / confidence intervals | **Computed — and it's bad news** | Fisher's exact test + Wilson CIs run for all 44 tests, then Benjamini-Hochberg corrected for running that many tests at once. **Zero survive correction at α=0.05**, including the strongest raw result in the project. See [`STATISTICAL_ANALYSIS.md`](STATISTICAL_ANALYSIS.md). This doesn't mean the effects are fake — it means the statistical layer of evidence is weak on top of, not instead of, the direct-transcript-inspection layer used throughout. |
| Task difficulty pre-calibrated against measured baseline performance | **No, but the retroactive cost of that is now known** | 17 of 27 round-1 scenarios (63%) had a baseline success rate ≥50% — computed for free from existing data, see `STATISTICAL_ANALYSIS.md`. Confirms the gap was real and larger than the "thin margin" cohort alone suggested. Going forward, this project's scripts should baseline-test at n=3 before finalizing any new scenario. |
| Automated, non-LLM-graded verification (oracle + test execution) | **No, and not always applicable** | SkillsBench verifies with real oracle solutions and test scripts — stronger than LLM grading wherever the output is code-checkable. Most of these skills produce a judgment or a document, not code with a testable oracle, so LLM-based blind grading is close to the only practical option for them. An adversarial review of the plan to fix this found the "reuse existing transcripts for free" premise was wrong — they're prose recommendations, not diffs — so this remains correctly scoped as future work, not attempted here. See `PLAN_STATUS.md`. |
| Multi-model comparison | **Started, small** | 4 of 28 skills checked on `claude-haiku-4-5` as a second subject model ($0.32 total). 3 replicated, 1 (`creating-change-records`) did not — see [`MULTI_MODEL_CHECK.md`](MULTI_MODEL_CHECK.md). Still one subject model for the other 24 skills, still no non-Anthropic model (no credentials in this environment), still no `claude-opus-4-8` check (deferred on cost, not abandoned). |
| Third-party / independent replication | **Not yet** | Invited, not performed. No outside reviewer who didn't help build the skills has re-run or re-scored this. A parallel, independently-authored effort (PR #63) reached the same diagnosis for `briefing-an-agent` without seeing this work — a genuine independent cross-check on that one finding — but that's a coincidence of timing, not a replication process, and doesn't change this row's answer. |

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
