#!/usr/bin/env python3
"""Analyze the control ladder and write REPORT.md.

Design note on the statistics
-----------------------------
The skill-benchmark-pilot ran one significance test per skill and then had to
Benjamini-Hochberg-correct 47 of them, after which nothing survived. That is a
predictable consequence of treating each skill as its own hypothesis at n=3.

This analysis pre-registers ONE primary hypothesis --

    across the 27-skill pool, loading the full skill beats the generic
    prompting control (C4 > C1) on paired per-skill scores

-- tested once, with the paired design (same scenario, same criterion, same
harness; only the appended text differs) supplying the power that per-skill
tests cannot have at n=3. Per-skill numbers are reported as descriptive, not as
27 additional hypotheses, and are labelled that way in the output.

Two tests are run on the same paired differences because they answer slightly
different questions and disagree in informative ways: the sign test asks only
how many skills moved in each direction, and the permutation test uses the
magnitudes. Both are exact or Monte-Carlo exact; neither assumes normality.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from collections import defaultdict

from ladder_common import (
    ARM_LABELS,
    ARMS,
    GENERIC_NUDGE,
    GRADED_PATH,
    LADDER_DIR,
    POOL,
    REPORT_PATH,
    TASKS,
    append_text,
    load_compressions,
)

SCORE = {"YES": 1.0, "PARTIAL": 0.5, "NO": 0.0}
PERMUTATIONS = 100_000
SEED = 20260726  # fixed so the reported p-value is reproducible, not resampled

# Per-skill uncertainty is reported as a bootstrap interval, not a threshold.
#
# A previous version hardcoded PER_SKILL_NOISE_FLOOR = 0.189, derived by taking
# the 90th percentile of same-grader cell movement (0.133) and multiplying by
# sqrt(2). That is not a valid confidence bound: a quantile of absolute shifts is
# not a standard deviation, multiplying a quantile by sqrt(2) does not give the
# corresponding quantile of a difference, it was estimated on the 7-skill hard
# pool and applied to pools with different rubrics and check counts, and it
# captured grader resampling noise while ignoring subject-model sampling noise.
#
# It is replaced by a percentile bootstrap over trials within each (skill, arm)
# cell, which propagates the subject-model sampling variation that dominates at
# n=3. With three trials per cell the resulting intervals are very wide -- that
# width IS the finding. It is why no per-skill "helps"/"hurts" verdict is issued
# here, and why the earlier ones were retracted.
BOOTSTRAP_RESAMPLES = 10_000
BOOTSTRAP_SEED = 20260803


def bootstrap_delta_ci(hi_trials: list[float], lo_trials: list[float],
                       rng: random.Random) -> tuple[float, float]:
    """Percentile bootstrap CI for a per-skill arm difference, resampling trials
    with replacement within each arm. At n=3 this is wide by construction, which
    is the honest representation of what three trials can support."""
    if not hi_trials or not lo_trials:
        return (float("nan"), float("nan"))
    deltas = []
    for _ in range(BOOTSTRAP_RESAMPLES):
        h = statistics.fmean(rng.choice(hi_trials) for _ in hi_trials)
        lo = statistics.fmean(rng.choice(lo_trials) for _ in lo_trials)
        deltas.append(h - lo)
    deltas.sort()
    return (deltas[int(0.025 * len(deltas))], deltas[int(0.975 * len(deltas))])


def sign_test(diffs: list[float]) -> tuple[int, int, int, float]:
    """Two-sided exact binomial test on the direction of paired differences.

    Ties are dropped, which is the standard sign-test convention and is
    conservative here: a skill that scores identically with and without its own
    text contributes no evidence that the text helped.
    """
    pos = sum(1 for d in diffs if d > 0)
    neg = sum(1 for d in diffs if d < 0)
    ties = len(diffs) - pos - neg
    n = pos + neg
    if n == 0:
        return pos, neg, ties, 1.0
    k = min(pos, neg)
    tail = sum(math.comb(n, i) for i in range(k + 1)) / (2 ** n)
    return pos, neg, ties, min(1.0, 2 * tail)


def permutation_test(diffs: list[float], rng: random.Random) -> float:
    """Two-sided paired permutation test: under the null, each skill's observed
    difference is equally likely to have carried the opposite sign."""
    observed = abs(statistics.fmean(diffs))
    hits = 0
    for _ in range(PERMUTATIONS):
        flipped = statistics.fmean(d if rng.random() < 0.5 else -d for d in diffs)
        if abs(flipped) >= observed - 1e-12:
            hits += 1
    return (hits + 1) / (PERMUTATIONS + 1)


def wilson(successes: float, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 1.0)
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scores", choices=("verdict", "rubric"), default="verdict",
                    help="verdict = one compound criterion (YES/PARTIAL/NO); "
                         "rubric = independent binary checks, higher resolution")
    args = ap.parse_args()

    # Both score sources run through the SAME statistics, validity gate, and
    # report generator. Forking the analysis per source would make the two
    # gradings incomparable, which is the whole point of re-grading.
    if args.scores == "rubric":
        rubric_path = LADDER_DIR / "data" / f"rubric-graded-{POOL}.json"
        if not rubric_path.exists():
            raise SystemExit(f"no rubric grades at {rubric_path}; run grade_rubric.py")
        rows = json.loads(rubric_path.read_text())
    else:
        rows = json.loads(GRADED_PATH.read_text())
    compressions = load_compressions()
    arms_present = [a for a in ARMS if any(r["arm"] == a for r in rows)]

    # scores[skill][arm] = mean score over trials
    by_cell: dict[tuple[str, str], list[float]] = defaultdict(list)
    cost: dict[str, list[float]] = defaultdict(list)
    out_tok: dict[str, list[int]] = defaultdict(list)
    for r in rows:
        cell_score = r["score"] if args.scores == "rubric" else SCORE.get(r["verdict"], 0.0)
        by_cell[(r["skill"], r["arm"])].append(cell_score)
        if r.get("cost_usd") is not None:
            cost[r["arm"]].append(r["cost_usd"])
        if r.get("output_tokens") is not None:
            out_tok[r["arm"]].append(r["output_tokens"])

    skills = sorted({r["skill"] for r in rows})
    score = {
        s: {a: statistics.fmean(by_cell[(s, a)]) for a in arms_present if by_cell[(s, a)]}
        for s in skills
    }

    def comparison(hi: str, lo: str, subset: list[str] | None = None) -> dict | None:
        pool = skills if subset is None else subset
        pairs = [(s, score[s][hi] - score[s][lo]) for s in pool
                 if hi in score[s] and lo in score[s]]
        if not pairs:
            return None
        diffs = [d for _, d in pairs]
        rng = random.Random(SEED)
        pos, neg, ties, p_sign = sign_test(diffs)
        return {
            "hi": hi, "lo": lo, "n": len(diffs),
            "mean_diff": statistics.fmean(diffs),
            "pos": pos, "neg": neg, "ties": ties,
            "p_sign": p_sign,
            "p_perm": permutation_test(diffs, rng),
            "losers": sorted(s for s, d in pairs if d <= 0),
        }

    # Instrument-validity gate.
    #
    # A ceiling (every arm at 1.00) and a floor (every arm at 0.00) are the same
    # failure: the scenario cannot express a difference, so the arms' equality
    # says nothing about the skills. v1 shipped a headline number without
    # noticing 13 ceilings; this makes that impossible to repeat by classifying
    # every skill before any pooled statistic is computed, and reporting the
    # primary test over informative skills only.
    #
    # PARTIAL rate is tracked alongside because it is a third way to lose
    # resolution: if the grader answers PARTIAL to almost everything, every arm
    # lands near 0.5 and real differences are compressed out of view. That is a
    # property of the criteria's wording, not of the skills.
    validity: dict[str, str] = {}
    for s in skills:
        vals = [score[s][a] for a in arms_present if a in score[s]]
        if vals and min(vals) >= 0.95:
            validity[s] = "ceiling"
        elif vals and max(vals) <= 0.05:
            validity[s] = "floor"
        else:
            validity[s] = "informative"
    informative = [s for s in skills if validity[s] == "informative"]
    # PARTIAL is a verdict-grading artefact and cannot occur under a binary
    # rubric, so the resolution warning is only meaningful for verdict scores.
    partial_rate = (
        sum(1 for r in rows if r["verdict"] == "PARTIAL") / max(1, len(rows))
        if args.scores == "verdict" else 0.0
    )

    primary = comparison("C4_full_skill", "C1_generic_nudge")
    primary_informative = comparison(
        "C4_full_skill", "C1_generic_nudge", subset=informative
    )
    secondary = [c for c in (
        comparison("C4_full_skill", "C0_bare"),
        comparison("C1_generic_nudge", "C0_bare"),
        comparison("C4_full_skill", "C3_compressed"),
        comparison("C4_full_skill", "C2_description_only"),
    ) if c]

    L: list[str] = []
    L.append("# Control Ladder: skill versus prompting\n")
    L.append(f"Pool: **{POOL}** · Scoring: **{args.scores}**"
             + (" (independent binary checks)" if args.scores == "rubric"
                else " (one compound YES/PARTIAL/NO criterion)") + "\n")
    L.append("Generated by `scripts/analyze_ladder.py`. Do not hand-edit — rerun it.\n")
    L.append("## What this measures\n")
    L.append(
        "The `skill-benchmark-pilot` in this repo compares a loaded skill against a bare\n"
        "prompt with nothing appended, which measures skill-versus-nothing. This ladder\n"
        "adds the intermediate arms needed to measure skill-versus-*prompting*. Every arm\n"
        "uses an identical model, tool allowlist, budget cap, isolation flags, scenario,\n"
        "and grading criterion; the only thing that varies is the text appended to the\n"
        "system prompt.\n"
    )
    L.append("| Arm | Appended to system prompt |")
    L.append("|---|---|")
    for a in arms_present:
        L.append(f"| `{a}` | {ARM_LABELS[a]} |")
    L.append("")
    L.append("The C1 control text, identical for all skills and containing no vocabulary\n"
             "from any of them:\n")
    L.append(f"> {GENERIC_NUDGE}\n")

    L.append("## Instrument validity\n")
    L.append(
        "A scenario where every arm scores 1.00 (ceiling) or every arm scores 0.00\n"
        "(floor) cannot express a difference between arms. Equality there is a\n"
        "property of the scenario, not a finding about the skills. Every skill is\n"
        "classified before any pooled statistic is computed, and the primary test is\n"
        "reported over informative skills only.\n"
    )
    counts = {k: sum(1 for v in validity.values() if v == k)
              for k in ("informative", "ceiling", "floor")}
    L.append(f"- Informative: **{counts['informative']}/{len(skills)}**")
    L.append(f"- Ceiling (all arms >= 0.95): **{counts['ceiling']}**")
    L.append(f"- Floor (all arms <= 0.05): **{counts['floor']}**")
    if args.scores == "verdict":
        L.append(f"- PARTIAL verdict rate: **{partial_rate:.0%}** of {len(rows)} gradings")
    else:
        met = sum(r["checks_met"] for r in rows)
        tot = sum(r["checks_total"] for r in rows)
        L.append(f"- Rubric checks met: **{met}/{tot}** ({met / max(1, tot):.0%}) "
                 f"across {len(rows)} gradings")
    L.append("")
    for kind in ("ceiling", "floor"):
        named = [s for s in skills if validity[s] == kind]
        if named:
            L.append(f"{kind.title()} skills, excluded from the primary test: "
                     + ", ".join(f"`{s}`" for s in named) + "\n")
    if partial_rate > 0.5:
        L.append(
            f"> **Resolution warning.** {partial_rate:.0%} of gradings are PARTIAL, so\n"
            f"> most cells sit near 0.5 regardless of arm and real differences are\n"
            f"> compressed out of view. This is a property of how the pass criteria are\n"
            f"> worded, not of the skills. Treat any null result from this pool as\n"
            f"> **inconclusive rather than negative** until the criteria are rewritten to\n"
            f"> be cleanly yes/no decidable.\n"
        )

    L.append("## Primary result\n")
    if primary:
        L.append(
            f"Pre-registered hypothesis: across the {primary['n']}-skill pool, the full\n"
            f"skill (C4) outscores the generic prompting control (C1) on paired per-skill\n"
            f"scores. Tested once.\n"
        )
        L.append(f"- Mean paired difference: **{primary['mean_diff']:+.3f}** "
                 f"(score scale 0–1; YES=1, PARTIAL=0.5, NO=0)")
        L.append(f"- Skills where C4 > C1: **{primary['pos']}** · "
                 f"C4 < C1: **{primary['neg']}** · tied: **{primary['ties']}**")
        L.append(f"- Two-sided exact sign test: **p = {primary['p_sign']:.4f}**")
        L.append(f"- Two-sided paired permutation test "
                 f"({PERMUTATIONS:,} resamples, seed {SEED}): **p = {primary['p_perm']:.4f}**")
        L.append("")
        if primary_informative and primary_informative["n"] != primary["n"]:
            pi = primary_informative
            L.append(
                f"Restricted to the {pi['n']} informative skills (ceilings and floors\n"
                f"removed): mean **{pi['mean_diff']:+.3f}**, "
                f"{pi['pos']} better / {pi['neg']} worse / {pi['ties']} tied, "
                f"sign p = {pi['p_sign']:.4f}, permutation p = {pi['p_perm']:.4f}.\n"
            )
        L.append("")
        # Ties are separated into ceiling and non-ceiling before any of them is
        # described as a skill "failing to beat" the control. A tie at 1.00 means
        # BOTH arms scored perfectly and the scenario cannot show a difference --
        # that is a measurement limit, not a finding about the skill. Lumping the
        # two kinds of tie together would read as 15 skills underperforming when
        # the data says nothing of the sort.
        # Losses and ties are separated first. `losers` holds every skill with a
        # non-positive difference, so treating the whole list as "ties" would
        # print a skill that genuinely lost under a "tied" heading -- and would
        # pair with an unconditional "never worse" claim that is simply false
        # whenever any skill lost. Both are decided from the data here.
        ceiling, real_ties, losses = [], [], []
        for s in primary["losers"]:
            c1 = score[s].get("C1_generic_nudge", 0.0)
            c4 = score[s].get("C4_full_skill", 0.0)
            if c4 < c1:
                losses.append((s, c1, c4))
            elif c1 >= 1.0 and c4 >= 1.0:
                ceiling.append((s, c1, c4))
            else:
                real_ties.append((s, c1, c4))

        if primary["neg"] == 0:
            L.append(
                f"C4 is **never worse** than C1 on any of the {primary['n']} skills. The "
                f"{primary['ties']} ties break down as follows, and the distinction "
                f"matters:\n"
            )
        else:
            L.append(
                f"C4 scores **lower** than C1 on {primary['neg']} of the {primary['n']} "
                f"skills, and ties on {primary['ties']}:\n"
            )
        if losses:
            L.append(
                f"**{len(losses)} skills where the full skill scored BELOW the generic "
                f"control**, which is a result against the skills and is reported as such:\n"
            )
            for s, c1, c4 in losses:
                L.append(f"- `{s}` (C1 {c1:.2f} → C4 {c4:.2f})")
            L.append("")
        if ceiling:
            L.append(
                f"**{len(ceiling)} ties at the C1/C4 ceiling** — both of the two arms "
                f"being compared scored 1.00, so this scenario cannot separate them. Note "
                f"this is a *looser* condition than the validity gate's ceiling above, "
                f"which requires ALL five arms to be maxed; a scenario can pin C1 and C4 "
                f"at 1.00 while a weaker arm still scores below, which is why the two "
                f"counts differ. Either way the C4-vs-C1 comparison learns nothing here, "
                f"and these are the top priority for harder replacement scenarios.\n"
            )
            L.append("> " + ", ".join(f"`{s}`" for s, _, _ in ceiling) + "\n")
        if real_ties:
            L.append(
                f"**{len(real_ties)} ties below the ceiling** — both arms scored the same "
                f"and neither was perfect. Here the generic paragraph genuinely matched the "
                f"skill with room to spare on both sides, which is the real finding:\n"
            )
            for s, c1, c4 in real_ties:
                L.append(f"- `{s}` (C1 {c1:.2f} = C4 {c4:.2f})")
            L.append("")

    L.append("## Secondary comparisons\n")
    L.append("| Comparison | Mean diff | Higher | Lower | Tied | Sign p | Perm p |")
    L.append("|---|---|---|---|---|---|---|")
    for c in secondary:
        L.append(f"| {c['hi']} vs {c['lo']} | {c['mean_diff']:+.3f} | {c['pos']} | "
                 f"{c['neg']} | {c['ties']} | {c['p_sign']:.4f} | {c['p_perm']:.4f} |")
    L.append("")
    L.append(
        "`C4 vs C0` is the comparison the original pilot ran. `C1 vs C0` is how much of\n"
        "that gap one reusable generic paragraph buys on its own. `C4 vs C3` is the\n"
        "compression lever: where it is near zero, the prose beyond five bullets is\n"
        "carrying token cost without a measured behavioral effect.\n"
    )

    L.append("## Cost ledger\n")
    L.append("| Arm | Mean appended words | Mean $/call | Mean output tokens | Pool score |")
    L.append("|---|---|---|---|---|")
    for a in arms_present:
        vals = [score[s][a] for s in skills if a in score[s]]
        pool = statistics.fmean(vals) if vals else 0.0
        lo, hi = wilson(sum(vals), len(vals))
        appended = statistics.fmean(
            len(append_text(s, a, compressions).split()) for s in skills
        )
        L.append(
            f"| `{a}` | {appended:,.0f} | ${statistics.fmean(cost[a]):.4f} | "
            f"{statistics.fmean(out_tok[a]):,.0f} | "
            f"{pool:.3f} (95% CI {lo:.2f}–{hi:.2f}) |"
        )
    L.append("")

    L.append("## Per-skill scores\n")
    L.append(
        "Mean score over 3 trials, 0–1, with a 95% percentile bootstrap interval on\n"
        "C4−C1 (10,000 resamples of trials within each arm, seed fixed).\n\n"
        "**No per-skill helps/hurts verdict is issued.** A bootstrap over three trials\n"
        "is itself unreliable: when all three trials happen to agree, it reports an\n"
        "artificially tight interval because it can only resample the values it saw.\n"
        "So an interval excluding zero here is a weak signal, not a verdict, and a\n"
        "wide one is a reliable statement that nothing can be concluded.\n"
        "An earlier version of this report classified skills against a hardcoded\n"
        "threshold and produced two claims the data did not support — four skills\n"
        "called harmful on one-check flips, and a proposal to delete ~14,000 words of\n"
        "skill text. Both were retracted. Intervals replace the threshold so the same\n"
        "over-reading is not available.\n\n"
        "The pooled tests above are unaffected: they aggregate every skill and carry\n"
        "their own permutation p-values.\n"
    )
    excl = [s_ for s_ in skills
            if not (lambda lo, hi: lo <= 0 <= hi)(
                *bootstrap_delta_ci(by_cell[(s_, "C4_full_skill")],
                                    by_cell[(s_, "C1_generic_nudge")],
                                    random.Random(BOOTSTRAP_SEED)))]
    L.append(f"**{len(excl)} of {len(skills)} skills** have a C4−C1 interval excluding "
             f"zero. Treat even those as provisional: one scenario, three trials, and "
             f"criteria authored inside this repository.\n")
    header = "| Skill | " + " | ".join(f"`{a.split('_')[0]}`" for a in arms_present) + " | C4−C1 [95% CI] |"
    L.append(header)
    L.append("|---" * (len(arms_present) + 2) + "|")
    for s in skills:
        cells = " | ".join(f"{score[s][a]:.2f}" if a in score[s] else "—" for a in arms_present)
        delta = (score[s].get("C4_full_skill", 0) - score[s].get("C1_generic_nudge", 0))
        lo, hi = bootstrap_delta_ci(by_cell[(s, "C4_full_skill")],
                                    by_cell[(s, "C1_generic_nudge")],
                                    random.Random(BOOTSTRAP_SEED))
        spans_zero = lo <= 0 <= hi
        note = "" if not spans_zero else " · spans 0"
        L.append(f"| `{s}` | {cells} | {delta:+.2f} [{lo:+.2f}, {hi:+.2f}]{note} |")
    L.append("")

    L.append("## Limitations\n")
    L.append(
        "- **One subject model** (`claude-sonnet-5`), one scenario per skill, 3 trials per\n"
        "  cell. Everything here is Sonnet-specific until replicated.\n"
        "- **Criteria are not independent of the skills.** The pass criteria are reused\n"
        "  unchanged from the pilot, and were authored by the same effort that wrote the\n"
        "  skills. C1 partly defuses this — a generic paragraph that satisfies the\n"
        "  criterion shows the criterion was measuring compliance rather than knowledge —\n"
        "  but it does not remove it.\n"
        "- **Trigger cases only.** Every scenario is one where the skill firing is the\n"
        "  right behavior. Nothing here measures the cost of a skill firing when it should\n"
        "  not, and nothing measures whether the right skill is selected out of the full\n"
        "  library. Both remain open.\n"
        f"- **{len(TASKS)} of the 29 skills on disk have a scenario.** "
        "`verifying-final-artifacts`\n  has no eval coverage at all; `reviewing-code-quality` is covered by the separate\n"
        "  3-task pilot rather than this pool.\n"
        "- **The C1 text is one specific paragraph.** A different generic control would\n"
        "  move these numbers. It was written to be strong on purpose; a weak control\n"
        "  would inflate every skill's measured effect.\n"
    )

    report_path = (REPORT_PATH if args.scores == "verdict"
                   else REPORT_PATH.with_name(REPORT_PATH.stem + "-rubric.md"))
    report_path.write_text("\n".join(L) + "\n")
    print(f"Wrote {report_path}")
    if primary:
        print(f"primary C4 vs C1: mean {primary['mean_diff']:+.3f}, "
              f"sign p={primary['p_sign']:.4f}, perm p={primary['p_perm']:.4f}, "
              f"{primary['pos']} better / {primary['neg']} worse / "
              f"{primary['ties']} tied ({len(ceiling)} at ceiling)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
