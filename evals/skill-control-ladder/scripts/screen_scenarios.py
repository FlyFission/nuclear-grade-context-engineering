#!/usr/bin/env python3
"""Pre-calibrate candidate scenarios against the live C1 control, then select.

This is the step the pilot never had. `STATISTICAL_ANALYSIS.md` found after the
fact that 17 of 27 v1 scenarios had a baseline success rate >= 50%, and the v1
ladder then showed 13 of them sitting at a hard ceiling where no difference
between arms could be detected at all. Authoring "harder" scenarios and assuming
they are harder would repeat that mistake with extra steps.

So difficulty is measured, not asserted. Every candidate is run against the C1
generic-prompting control at n=3 and graded blind. A candidate is eligible only
if C1 scores <= 0.5 -- the threshold the pilot's own plan proposed borrowing
from SkillsBench. Among eligible candidates the LOWEST-scoring one is selected,
because it leaves the most headroom for a skill to demonstrate a difference.

A skill with no eligible candidate is reported as unresolved and left OUT of the
selected pool. Selecting the best of three ineligible candidates would quietly
reintroduce the ceiling this whole exercise exists to remove.

Note the asymmetry this screening introduces, which `analyze_ladder.py`'s report
must state: scenarios are selected for being hard for C1 specifically. That is
the correct choice for measuring headroom, but it means the hard pool is not an
unbiased sample of difficulty -- C1's score on the selected pool is downward-
biased by selection, and the honest comparison is C4 against C1 *on scenarios
chosen without reference to C4*, which is what this produces.
"""

from __future__ import annotations

import hashlib
import json
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from ladder_common import (
    GENERIC_NUDGE,
    LADDER_DIR,
    MAX_WORKERS,
    TRIALS,
    blind_grade,
    response_text,
    run_subject,
)

OUT_DIR = LADDER_DIR / "data" / "hard-pool"
CANDIDATES_PATH = OUT_DIR / "candidates.json"
SCREEN_RUNS = OUT_DIR / "screening-runs"
SCREENING_PATH = OUT_DIR / "screening.json"
GRADE_CACHE_PATH = OUT_DIR / "screening-grade-cache.json"
SELECTED_PATH = OUT_DIR / "selected_tasks.json"
WORK_DIR = OUT_DIR / "work"

SCORE = {"YES": 1.0, "PARTIAL": 0.5, "NO": 0.0}
ELIGIBILITY_MAX_C1 = 0.5


def screen_one(skill: str, idx: int, cand: dict, trial: int) -> dict:
    scenario = cand["scenario_prompt"]
    spec = hashlib.sha256(f"{scenario}::{GENERIC_NUDGE}".encode()).hexdigest()
    out_path = SCREEN_RUNS / f"{skill}__cand{idx}__trial{trial}.json"

    if out_path.exists():
        rec = json.loads(out_path.read_text())
        if (rec.get("_spec") == spec and rec.get("type") != "error"
                and not rec.get("is_error")):
            return rec

    rec = run_subject(scenario, GENERIC_NUDGE, WORK_DIR / f"{skill}_{idx}_{trial}")
    rec["_spec"] = spec
    rec["_skill"], rec["_cand"], rec["_trial"] = skill, idx, trial
    out_path.write_text(json.dumps(rec, indent=2))
    return rec


def main() -> int:
    if not CANDIDATES_PATH.exists():
        print("No candidates; run author_scenarios.py first.", file=sys.stderr)
        return 2
    candidates = json.loads(CANDIDATES_PATH.read_text())
    SCREEN_RUNS.mkdir(parents=True, exist_ok=True)
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    jobs = [(s, i, c, t)
            for s, cands in sorted(candidates.items())
            for i, c in enumerate(cands)
            for t in range(1, TRIALS + 1)]

    print(f"Screening {len(jobs)} cells "
          f"({len(candidates)} skills x {len(next(iter(candidates.values())))} candidates "
          f"x {TRIALS} trials) against C1", file=sys.stderr)

    records: dict[tuple[str, int, int], dict] = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(screen_one, *j): j for j in jobs}
        done = 0
        for fut in as_completed(futures):
            s, i, _c, t = futures[fut]
            records[(s, i, t)] = fut.result()
            done += 1
            print(f"[{done}/{len(jobs)}] run {s}/cand{i}/t{t}", file=sys.stderr)

    errored = [k for k, r in records.items()
               if r.get("type") == "error" or r.get("is_error")]
    if errored:
        print(f"Refusing to select: {len(errored)} screening run(s) errored. "
              f"Re-run to retry them.", file=sys.stderr)
        for k in errored[:10]:
            print(f"  {k}", file=sys.stderr)
        return 1

    # Grading verdicts are cached on disk keyed by the response text and the
    # criterion. Without this, one transient grader failure forces a re-grade of
    # every other cell on the retry -- which is both wasteful and a source of
    # drift, since re-grading resamples verdicts that were already settled.
    cache: dict[str, str] = {}
    if GRADE_CACHE_PATH.exists():
        try:
            cache = json.loads(GRADE_CACHE_PATH.read_text())
        except (json.JSONDecodeError, OSError):
            cache = {}

    def cache_key(criteria: str, text: str) -> str:
        return hashlib.sha256(f"{criteria}::{text}".encode()).hexdigest()

    verdicts: dict[tuple[str, int, int], str] = {}
    grade_jobs = []
    for (s, i, t), r in records.items():
        criteria = candidates[s][i]["pass_criteria"]
        text = response_text(r)
        hit = cache.get(cache_key(criteria, text))
        if hit and hit != "ERROR":
            verdicts[(s, i, t)] = hit
        else:
            grade_jobs.append((s, i, t, criteria, text))

    print(f"grading: cached={len(verdicts)} to_grade={len(grade_jobs)}", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(blind_grade, j[3], j[4]): j for j in grade_jobs}
        done = 0
        for fut in as_completed(futures):
            s, i, t, crit, txt = futures[fut]
            verdict = fut.result().get("meets_criteria", "ERROR")
            verdicts[(s, i, t)] = verdict
            if verdict != "ERROR":
                cache[cache_key(crit, txt)] = verdict
            done += 1
            print(f"[{done}/{len(grade_jobs)}] grade {s}/cand{i}/t{t} -> "
                  f"{verdict}", file=sys.stderr)
    GRADE_CACHE_PATH.write_text(json.dumps(cache, indent=2) + "\n")

    if any(v == "ERROR" for v in verdicts.values()):
        n = sum(1 for v in verdicts.values() if v == "ERROR")
        print(f"Refusing to select: {n} grading call(s) errored. Re-run to retry.",
              file=sys.stderr)
        return 1

    screening, selected, unresolved = {}, {}, []
    for skill, cands in sorted(candidates.items()):
        rows = []
        for i, c in enumerate(cands):
            scores = [SCORE[verdicts[(skill, i, t)]] for t in range(1, TRIALS + 1)]
            rows.append({
                "candidate": i,
                "c1_score": statistics.fmean(scores),
                "verdicts": [verdicts[(skill, i, t)] for t in range(1, TRIALS + 1)],
                "planted_defect": c["planted_defect"],
                "eligible": statistics.fmean(scores) <= ELIGIBILITY_MAX_C1,
            })
        screening[skill] = rows

        eligible = [r for r in rows if r["eligible"]]
        if not eligible:
            unresolved.append(skill)
            continue
        best = min(eligible, key=lambda r: (r["c1_score"], r["candidate"]))
        chosen = cands[best["candidate"]]
        selected[skill] = {
            "scenario_prompt": chosen["scenario_prompt"],
            "pass_criteria": chosen["pass_criteria"],
            "_planted_defect": chosen["planted_defect"],
            "_candidate_index": best["candidate"],
            "_screened_c1_score": best["c1_score"],
        }

    SCREENING_PATH.write_text(json.dumps(screening, indent=2) + "\n")
    SELECTED_PATH.write_text(json.dumps(dict(sorted(selected.items())), indent=2) + "\n")

    print(f"\nSelected {len(selected)}/{len(candidates)} skills "
          f"(C1 <= {ELIGIBILITY_MAX_C1})", file=sys.stderr)
    for s, v in sorted(selected.items()):
        print(f"  {s}: cand{v['_candidate_index']} C1={v['_screened_c1_score']:.2f}",
              file=sys.stderr)
    if unresolved:
        print(f"\nUNRESOLVED -- no candidate hard enough, excluded from the pool: "
              f"{', '.join(unresolved)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
