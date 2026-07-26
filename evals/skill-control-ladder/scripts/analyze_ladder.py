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

import json
import math
import random
import statistics
from collections import defaultdict

from ladder_common import ARM_LABELS, ARMS, GENERIC_NUDGE, GRADED_PATH, LADDER_DIR, TASKS

SCORE = {"YES": 1.0, "PARTIAL": 0.5, "NO": 0.0}
PERMUTATIONS = 100_000
SEED = 20260726  # fixed so the reported p-value is reproducible, not resampled


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
    rows = json.loads(GRADED_PATH.read_text())
    arms_present = [a for a in ARMS if any(r["arm"] == a for r in rows)]

    # scores[skill][arm] = mean score over trials
    by_cell: dict[tuple[str, str], list[float]] = defaultdict(list)
    cost: dict[str, list[float]] = defaultdict(list)
    out_tok: dict[str, list[int]] = defaultdict(list)
    in_tok: dict[str, list[int]] = defaultdict(list)
    for r in rows:
        by_cell[(r["skill"], r["arm"])].append(SCORE.get(r["verdict"], 0.0))
        if r.get("cost_usd") is not None:
            cost[r["arm"]].append(r["cost_usd"])
        if r.get("output_tokens") is not None:
            out_tok[r["arm"]].append(r["output_tokens"])
        if r.get("input_tokens") is not None:
            in_tok[r["arm"]].append(r["input_tokens"])

    skills = sorted({r["skill"] for r in rows})
    score = {
        s: {a: statistics.fmean(by_cell[(s, a)]) for a in arms_present if by_cell[(s, a)]}
        for s in skills
    }

    def comparison(hi: str, lo: str) -> dict | None:
        pairs = [(s, score[s][hi] - score[s][lo]) for s in skills
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

    primary = comparison("C4_full_skill", "C1_generic_nudge")
    secondary = [c for c in (
        comparison("C4_full_skill", "C0_bare"),
        comparison("C1_generic_nudge", "C0_bare"),
        comparison("C4_full_skill", "C3_compressed"),
        comparison("C4_full_skill", "C2_description_only"),
    ) if c]

    L: list[str] = []
    L.append("# Control Ladder: skill versus prompting\n")
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
        if primary["losers"]:
            L.append(
                f"**{len(primary['losers'])} of {primary['n']} skills did not beat a single "
                f"reusable generic paragraph** on their own scenario and their own criterion:\n"
            )
            for s in primary["losers"]:
                L.append(f"- `{s}` (C1 {score[s].get('C1_generic_nudge', 0):.2f} → "
                         f"C4 {score[s].get('C4_full_skill', 0):.2f})")
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
    L.append("| Arm | Mean $/call | Mean input tokens | Mean output tokens | Pool score |")
    L.append("|---|---|---|---|---|")
    for a in arms_present:
        vals = [score[s][a] for s in skills if a in score[s]]
        pool = statistics.fmean(vals) if vals else 0.0
        lo, hi = wilson(sum(vals), len(vals))
        L.append(
            f"| `{a}` | ${statistics.fmean(cost[a]):.4f} | "
            f"{statistics.fmean(in_tok[a]):,.0f} | {statistics.fmean(out_tok[a]):,.0f} | "
            f"{pool:.3f} (95% CI {lo:.2f}–{hi:.2f}) |"
        )
    L.append("")

    L.append("## Per-skill scores (descriptive, not 27 hypotheses)\n")
    L.append("Mean score over 3 trials, 0–1. These are **not** individually significance-\n"
             "tested: at n=3 per cell no per-skill test can survive correction, which is\n"
             "the lesson `STATISTICAL_ANALYSIS.md` already recorded. Read them as effect\n"
             "sizes for triage, not as verdicts.\n")
    header = "| Skill | " + " | ".join(f"`{a.split('_')[0]}`" for a in arms_present) + " | C4−C1 |"
    L.append(header)
    L.append("|---" * (len(arms_present) + 2) + "|")
    for s in skills:
        cells = " | ".join(f"{score[s][a]:.2f}" if a in score[s] else "—" for a in arms_present)
        delta = (score[s].get("C4_full_skill", 0) - score[s].get("C1_generic_nudge", 0))
        flag = " ⚠️" if delta <= 0 else ""
        L.append(f"| `{s}` | {cells} | {delta:+.2f}{flag} |")
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

    (LADDER_DIR / "REPORT.md").write_text("\n".join(L) + "\n")
    print(f"Wrote {LADDER_DIR / 'REPORT.md'}")
    if primary:
        print(f"primary C4 vs C1: mean {primary['mean_diff']:+.3f}, "
              f"sign p={primary['p_sign']:.4f}, perm p={primary['p_perm']:.4f}, "
              f"{len(primary['losers'])} non-winning skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
