#!/usr/bin/env python3
"""Compute Fisher's exact test p-values (two-sided) and Wilson score confidence
intervals for every skill's with-vs-without comparison, across round 1, Gate 1,
and the reviewing-code-quality pilot -- then apply a Benjamini-Hochberg FDR
correction across all tests together, since running ~45 independent
significance tests at alpha=0.05 with no correction would produce roughly
1-2 spurious "significant" hits by chance alone even under a true null
everywhere (flagged by adversarial review before this was computed).

No scipy in this environment -- Fisher's exact test implemented directly via
the hypergeometric distribution using math.comb (pure stdlib, exact, not an
approximation).
"""
import json
import math
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ALL = DATA / "all-skills-pilot"
GATE1 = DATA / "gate1-hard-case-pilot"
RCQ = DATA / "reviewing-code-quality-pilot"
OUT = Path(__file__).resolve().parent


def fisher_exact_two_sided(a, b, c, d):
    """2x2 table: [[a,b],[c,d]] = [[with_yes, with_not_yes],[without_yes, without_not_yes]]."""
    R1, R2 = a + b, c + d
    C1 = a + c
    N = R1 + R2

    def prob(x):
        if x < 0 or x > R1 or (C1 - x) < 0 or (C1 - x) > R2:
            return 0.0
        return (math.comb(R1, x) * math.comb(R2, C1 - x)) / math.comb(N, C1)

    observed = prob(a)
    lo, hi = max(0, C1 - R2), min(R1, C1)
    total = 0.0
    for x in range(lo, hi + 1):
        p = prob(x)
        if p <= observed * (1 + 1e-9):
            total += p
    return min(1.0, total)


def wilson_interval(successes, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    phat = successes / n
    denom = 1 + z * z / n
    center = (phat + z * z / (2 * n)) / denom
    margin = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, center - margin), min(1.0, center + margin))


def benjamini_hochberg(pvalues, alpha=0.05):
    """Returns (adjusted_pvalues in original order, significant flags in original order)."""
    m = len(pvalues)
    indexed = sorted(range(m), key=lambda i: pvalues[i])
    adjusted = [0.0] * m
    prev = 1.0
    for rank, idx in enumerate(reversed(indexed), start=1):
        i = m - rank + 1
        raw = pvalues[idx] * m / i
        prev = min(prev, raw)
        adjusted[idx] = prev
    significant = [adjusted[i] <= alpha for i in range(m)]
    return adjusted, significant


tests = []  # list of dicts: skill, round, with_yes, with_n, without_yes, without_n

round1 = json.loads((ALL / "graded_results_all.json").read_text())
skills_r1 = sorted(set(r["skill"] for r in round1))
for skill in skills_r1:
    stat = {}
    for cond in ["with_skill", "without_skill"]:
        sub = [r for r in round1 if r["skill"] == skill and r["condition"] == cond and not r.get("error")]
        yes = sum(1 for r in sub if r["meets_criteria"] == "YES")
        stat[cond] = (yes, len(sub))
    tests.append({"skill": skill, "round": "round1",
                  "with_yes": stat["with_skill"][0], "with_n": stat["with_skill"][1],
                  "without_yes": stat["without_skill"][0], "without_n": stat["without_skill"][1]})

gate1 = json.loads((GATE1 / "graded_results_gate1.json").read_text())
skills_g1 = sorted(set(r["skill"] for r in gate1))
for skill in skills_g1:
    stat = {}
    for cond in ["with_skill", "without_skill"]:
        sub = [r for r in gate1 if r["skill"] == skill and r["condition"] == cond and not r.get("error")]
        yes = sum(1 for r in sub if r["meets_criteria"] == "YES")
        stat[cond] = (yes, len(sub))
    tests.append({"skill": skill, "round": "gate1",
                  "with_yes": stat["with_skill"][0], "with_n": stat["with_skill"][1],
                  "without_yes": stat["without_skill"][0], "without_n": stat["without_skill"][1]})

rcq = json.loads((RCQ / "graded_results.json").read_text())
task_names = sorted(set(r["task"] for r in rcq))
for task in task_names:
    stat = {}
    for cond in ["with_skill", "without_skill"]:
        sub = [r for r in rcq if r["task"] == task and r["condition"] == cond and not r.get("error")]
        yes = sum(1 for r in sub if r["meets_criteria"] == "YES")
        stat[cond] = (yes, len(sub))
    tests.append({"skill": f"reviewing-code-quality::{task}", "round": "rcq",
                  "with_yes": stat["with_skill"][0], "with_n": stat["with_skill"][1],
                  "without_yes": stat["without_skill"][0], "without_n": stat["without_skill"][1]})

for t in tests:
    a, b = t["with_yes"], t["with_n"] - t["with_yes"]
    c, d = t["without_yes"], t["without_n"] - t["without_yes"]
    t["p_value"] = fisher_exact_two_sided(a, b, c, d)
    t["with_ci"] = wilson_interval(t["with_yes"], t["with_n"])
    t["without_ci"] = wilson_interval(t["without_yes"], t["without_n"])

pvals = [t["p_value"] for t in tests]
adjusted, significant = benjamini_hochberg(pvals, alpha=0.05)
for t, adj, sig in zip(tests, adjusted, significant, strict=True):
    t["p_value_bh_adjusted"] = adj
    t["significant_at_bh_0.05"] = sig

n_sig = sum(significant)
print(f"Total tests: {len(tests)}")
print(f"Significant at BH-adjusted alpha=0.05: {n_sig} / {len(tests)}")
print()
for t in sorted(tests, key=lambda t: t["p_value"]):
    flag = "***" if t["significant_at_bh_0.05"] else ""
    print(f"{t['skill']:45s} [{t['round']:6s}] with={t['with_yes']}/{t['with_n']} "
          f"without={t['without_yes']}/{t['without_n']}  p={t['p_value']:.4f}  "
          f"bh_p={t['p_value_bh_adjusted']:.4f} {flag}")

(OUT / "statistical_summary.json").write_text(json.dumps(tests, indent=2))
