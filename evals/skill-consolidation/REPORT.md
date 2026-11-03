# Skill Consolidation: Report

**Result:** none of the 7 proposed merges is made. The catalog stays at 31 skills.

One merge, `choosing-what-to-control` + `recording-a-known-good-version` → `controlling-approved-versions` (M4), passed every pre-registered bar and was applied at first. External reviews then asked for final-state evidence: routing on the actual 31- and 30-skill catalogs, repeated, plus a larger targeted fit test. Under the same bars, M4 failed both, so it was reverted. Two reviewers asked for that evidence; it took the last merge away, and that is the result.

**Protocol:** [`PROTOCOL.md`](PROTOCOL.md), committed before any result. Deviations are listed at the end.

## Decisions

| ID | Merge | A coverage | B routing | C fit | D size | Decision |
|---|---|---|---|---|---|---|
| M1 | `declaring-intent` → `double-checking-before-acting` | fail, rounds 1 and 2 | not run | not run | pass | not made |
| M2 | `tracking-deficiencies` + `reporting-shared-defects` → `learning-from-experience` | pass (round 2) | pass | **fail**: 1 miss of 27 | pass | not made |
| M3 | `checking-source-claims` → `checking-legal-and-safety-wording` (as `checking-public-claims`) | pass (round 2) | pass | **fail**: 1 forced of 4, on the target's own job | pass | not made |
| M4 | `choosing-what-to-control` → `recording-a-known-good-version` (as `controlling-approved-versions`) | pass (round 2) | pass on the 25-skill catalog; **fail** on the final 30-skill catalog (see below) | pass on 9 rows; **fail** on 40 targeted rows (1 miss) | pass | made, then **reverted** |
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

## Final-state evidence (requested by external reviews)

The external reviews (Codex, plus Grok and ChatGPT forwarded by the owner) noted that the routing comparison had used a 25-skill catalog, not the 30 that would ship, that no repeat run measured noise, and that M4's clean fit rested on 9 rows. Three follow-ups ran after M4 was applied:

1. **Paired routing on the actual catalogs.** Two runs each on the current 31 and the final 30, with catalog order shuffled per run ([`data/final/`](data/final/)).

   | Run | Precision | Recall | M4 recall | M4 false positives |
   |---|---|---|---|---|
   | 31a | 75.3 | 80.4 | 7/8 | 2/172 |
   | 31b | 76.6 | 76.6 | 7/8 | 1/172 |
   | 30a | 74.6 | 78.0 | 6/8 | 3/172 |
   | 30b | 73.7 | 74.2 | 6/8 | 5/172 |

   - Whole-catalog differences (recall −2.4 on average) are within run-to-run spread: two runs of the *same* catalog differ by 3.8 recall points and agree exactly on only 136/180 (31) and 128/180 (30) scenarios.
   - The M4-specific loss is consistent: S-067 ("23 hand-run SQL files, nobody knows which were applied to prod") routes to `choosing-what-to-control` in both 31 runs and is missed in both 30 runs.
   - The merged skill also fires on model-swap requests (S-053, S-089, S-101, S-173), which is debatable because a model ID is a controlled item.
   - Recall 75 vs 87.5 fails criterion B's 5-point tolerance. With n=8, any single scenario moves recall by 12.5 points.
2. **Targeted fit, 40 scenarios** ([`data/final/m4-scenarios.jsonl`](data/final/m4-scenarios.jsonl), [`data/final/m4-fit.jsonl`](data/final/m4-fit.jsonl)). These cover scope-only, accept-only, both, stale, premature, neither, and external cases. 39 fit; none forced unneeded work. In 1 the merged skill would miss needed work (M4-034): it dropped `recording-a-known-good-version`'s escalation for safety and outside-trust claims, so a vendor-moderation safety sign-off loses its explicit escalation. That fails criterion C (zero misses).
3. **A re-score by a different model family** was asked for and has not been done in this repo. It is still the largest gap, and it matters less now that no merge is made.

M4 had already used its one revision, so under the protocol it is not made. It was reverted and the two skills and their `/ng-what-to-control` and `/ng-baseline` cards are restored unchanged. The README, skill visuals, diagram tests, and this evaluation stay.

## What changed in the repo

No skill or command changed. Kept from this work:
- the evaluation (protocol, data, two coverage rounds, both draft rounds, final-state evidence, scorer, and a test that reruns the scorer against the committed scores);
- the skill catalog, invocation, and full-map figures, with tests that keep them in step with the catalog and with a fresh build.

## Limits

- **One model family.** Every agent here is the same model family as the author, briefed by the author's session: generator, both labelers, adjudicator, both routers, coverage auditor, and fit judge. This is a structured check, not independent verification. LLM errors are strongly correlated across models (Kim et al., ICML 2025).
- **Small samples per merge.** Relevant scenarios were 1 for M5, 4 for M3, 8–9 for M4, 11–13 for M7, and 23–27 for M2. A clean result on n items bounds the miss rate only near 3/n. M4's clean fit on 9 rows did not survive a 40-row test.
- **Frontmatter only.** Routing used frontmatter as the host shows it; truncation under catalog pressure was not simulated.
- **Strict pass/fail.** The bars are strict, and some failures are small wording losses (M2's especially). A merge that failed is not proof that no merge could work. It means this draft did not clear the bar this protocol set, so it was not made.

## Deviations from the protocol

1. **Name changes.** Several drafts took clearer names than their protocol targets (`checking-public-claims`, `controlling-approved-versions`, `managing-change-records`, `structuring-the-work`). Naming was not an acceptance criterion.
2. **Cleanup after round 2.** Low-severity leftovers from coverage round 2 were cleaned up in the surviving drafts after round 2 but before any routing or fit result existed. The routers and the fit judge saw the cleaned drafts.
3. **Corpus relaunch.** The first corpus generator was stopped by a worker restart before it wrote anything. A second generator ran the same blind brief and wrote in batches.
4. **Narrower routing catalog.** The 25-skill routing catalog leaves out M1 and M6, which had already failed criterion A, so routing tested only merges still eligible.

## Source-lineage note

Original evaluation following `PROTOCOL.md` and `docs/02-operating-system/verification-methods-and-depth.md`, with sources mapped in `docs/00-standards-foundation/source-map.md`. It shows how these drafts performed on these scenarios. It does not create formal verification, compliance, certification, or any safety, security, or regulatory guarantee.
