# Skill Consolidation: Report

**Result:** 1 of 7 proposed merges cleared every pre-registered bar. The catalog goes from 31 skills to 30, not to the 23 the audit hoped for. `choosing-what-to-control` and `recording-a-known-good-version` become `controlling-approved-versions`. The other six merges are not made, and the 13 skills they would have combined stay as they are.

**Protocol:** [`PROTOCOL.md`](PROTOCOL.md), committed before any result. Deviations are listed at the end.

## Decisions

| ID | Merge | A coverage | B routing | C fit | D size | Decision |
|---|---|---|---|---|---|---|
| M1 | `declaring-intent` → `double-checking-before-acting` | fail, rounds 1 and 2 | not run | not run | pass | not made |
| M2 | `tracking-deficiencies` + `reporting-shared-defects` → `learning-from-experience` | pass (round 2) | pass | **fail**: 1 miss of 27 | pass | not made |
| M3 | `checking-source-claims` → `checking-legal-and-safety-wording` (as `checking-public-claims`) | pass (round 2) | pass | **fail**: 1 forced of 4, on the target's own job | pass | not made |
| M4 | `choosing-what-to-control` → `recording-a-known-good-version` (as `controlling-approved-versions`) | pass (round 2) | pass | pass: 0 of 9 | pass | **made** |
| M5 | `closing-stale-packets` → `creating-change-records` (as `managing-change-records`) | pass (round 2) | **fail** | not run | pass | not made |
| M6 | `briefing-an-agent` → `handing-off-work` | fail, rounds 1 and 2 | not run | not run | pass | not made |
| M7 | `breaking-down-the-work` → `organizing-project-folders` (as `structuring-the-work`) | pass (round 2) | pass | **fail**: 1 miss + 1 forced of 13 | pass | not made |

## What each failure was

These are the concrete reasons. Each is the kind of loss the "hammer for a screw" test exists to catch.

- **M1, coverage.** The merged double-check either dropped the intent gate for actions that are hard to reverse, or applied it to every deploy, including throwaway previews. After revision it still left public claims out of the intent gate.
- **M6, coverage.** The merged brief either lost the reviewer's risk summary from the paste-able prompt, or made every mid-task subagent brief require a full turnover and a restatement round-trip.
- **M5, routing.** Its one relevant scenario was S-097, an abandoned Slack-integration branch with a switched-off flag in production. The current catalog routes it to `closing-stale-packets`. The merged skill leads with *creating* records, and the blind router missed it. That is one scenario, so the evidence is thin, but the risk it exposes is real: a cleanup trigger buried inside a creation skill.
- **M2, fit.** In S-048, the merged lesson path dropped "root cause, not the symptom", so a pool-size bump would be accepted as the fix for pool exhaustion.
- **M3, fit.** In S-032, a real SOC 2 Type I attestation claim on a homepage would run the source-lineage path and be reworded to "influence, never compliance". That is wrong for an attestation the company actually holds. This is the clearest hammer-for-a-screw case.
- **M7, fit.** In S-003, a module split with no breakdown on hand would be pushed into a full breakdown with dictionary rows. In S-100, the escalation for work no one understands ("pinned for a reason nobody remembers") was dropped.

## Evidence

| Step | What | Result |
|---|---|---|
| Corpus | 180 situations by an agent never shown the skills ([`scenarios.jsonl`](scenarios.jsonl)) | 12 work types × 10 stage gates, 45/92/43 low/medium/high. Work type and stage were assigned by rotation. |
| Ground truth | Two independent labelers with the full skill files ([`data/labels_a.jsonl`](data/labels_a.jsonl), [`data/labels_b.jsonl`](data/labels_b.jsonl)) | Exact set match on 143/180, micro Jaccard 0.826, same first skill on 163/180 |
| Adjudication | The 37 disagreements settled against the skill text ([`data/adjudicated.jsonl`](data/adjudicated.jsonl)) | 18 intersection, 5 labeler 2, 3 labeler 1, 3 union, 8 other |
| Coverage (A) | Capability map of all 15 originals against each draft ([`coverage-round1.md`](coverage-round1.md), [`coverage-round2.md`](coverage-round2.md)) | Round 1: 0/7 pass (19 losses, 8 over-applications). Round 2: 5/7 pass. |
| Routing (B) | Blind routers seeing names and descriptions only, on the 31-skill and 25-skill catalogs ([`data/route31.jsonl`](data/route31.jsonl), [`data/routenew.jsonl`](data/routenew.jsonl)) | Per-merge recall and false-positive rate in [`data/score.json`](data/score.json). Secondary set of 170 existing routing cases: 100.0% vs 99.4%; the one difference is a key artifact (see below). |
| Fit (C) | A judge read each merged draft against the original for every scenario that needed an original (53 rows, [`data/fit.jsonl`](data/fit.jsonl)) | Findings above |
| Size (D) | `ng tokens` counting | Every draft is within `skill_body_max` 3900 and `description_max` 200 |

Whole catalog on the 180 scenarios: precision 70.7 → 72.8 and recall 81.9 → 78.7 (31 → 25 skills). The recall dip is not attributable to the merges. The misses that moved are mostly on skills whose descriptions are identical in both catalogs: `checking-facts` went from 0 misses to 4, and `staying-on-mission` from 4 to 2. That is run-to-run variance between two router instances, which this protocol did not measure with a repeat run.

Secondary-set note: R-126 ("I am actively filling this packet right now and about to validate it") was keyed "do not trigger `closing-stale-packets`". The 25-skill router picked the merged `managing-change-records`, which covers creating and validating a record, so the pick is correct and the key was written for the narrower skill.

## What changed in the repo (M4 only)

- `skills/controlling-approved-versions/` replaces `skills/choosing-what-to-control/` and `skills/recording-a-known-good-version/`. The skill now has two explicit phases: scoping what is controlled, and recording the baseline at acceptance.
- `/ng-control` replaces `/ng-what-to-control` and `/ng-baseline`.
- The routing and output cases for both originals were relabeled to the merged skill, with their prompts kept.
- Catalog wiring, counts, the comparison table, the prompt bank, and the diagrams were updated. Dated historical records (trial records, benchmark plans, the token audit) keep the old names.

## Limits

- **One model family.** Every agent here is the same model family as the author, briefed by the author's session: generator, both labelers, adjudicator, both routers, coverage auditor, and fit judge. This is a structured check, not independent verification. LLM errors are strongly correlated across models (Kim et al., ICML 2025).
- **Small samples per merge.** Relevant scenarios were 1 for M5, 4 for M3, 8–9 for M4, 11–13 for M7, and 23–27 for M2. A clean result on n items bounds the miss rate only near 3/n, so M4's clean fit on 9 rows bounds its miss rate below about 30%.
- **Frontmatter only.** Routing used frontmatter as the host shows it; truncation under catalog pressure was not simulated.
- **Strict pass/fail.** The bars are strict, and some failures are small wording losses (M2's especially). A merge that failed is not proof that no merge could work. It means this draft did not clear the bar this protocol set, so it was not made.

## Deviations from the protocol

1. **Name changes.** Several drafts took clearer names than their protocol targets (`checking-public-claims`, `controlling-approved-versions`, `managing-change-records`, `structuring-the-work`). Naming was not an acceptance criterion.
2. **Cleanup after round 2.** Low-severity leftovers from coverage round 2 were cleaned up in the surviving drafts after round 2 but before any routing or fit result existed. The routers and the fit judge saw the cleaned drafts.
3. **Corpus relaunch.** The first corpus generator was stopped by a worker restart before it wrote anything. A second generator ran the same blind brief and wrote in batches.
4. **Narrower routing catalog.** The 25-skill routing catalog leaves out M1 and M6, which had already failed criterion A, so routing tested only merges still eligible.

## Source-lineage note

Original evaluation following `PROTOCOL.md` and `docs/02-operating-system/verification-methods-and-depth.md`, with sources mapped in `docs/00-standards-foundation/source-map.md`. It shows how these drafts performed on these scenarios. It does not create formal verification, compliance, certification, or any safety, security, or regulatory guarantee.
