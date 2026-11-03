#!/usr/bin/env python3
"""Score the skill-consolidation evaluation against PROTOCOL.md.

Inputs (all JSONL, one object per line, keyed by scenario ``id``):

- ``scenarios.jsonl``        {"id", "work_type", "stage", "risk", "prompt"}
- ``truth.jsonl``            {"id", "skills": [...31-catalog names...]}  adjudicated
- ``labels_a.jsonl``, ``labels_b.jsonl``  the two independent labelings (same shape)
- ``route31.jsonl``, ``route23.jsonl``    blind router picks (same shape)
- ``fit.jsonl``              {"id", "merge", "origin", "misses_needed_work": bool,
                              "forces_unneeded_work": bool, "section", "note"}

``map-31-to-23.json`` maps each 31-catalog name to its 23-catalog name.

Criterion B (routing parity) and C (fit) are computed here. A (coverage) and D
(context) come from the coverage audit and ``ng tokens``. Stdlib only.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

MERGES = {
    "M1": ("double-checking-before-acting", ["double-checking-before-acting", "declaring-intent"]),
    "M2": ("learning-from-experience", ["learning-from-experience", "tracking-deficiencies", "reporting-shared-defects"]),
    "M3": ("checking-public-claims", ["checking-legal-and-safety-wording", "checking-source-claims"]),
    "M4": ("controlling-approved-versions", ["recording-a-known-good-version", "choosing-what-to-control"]),
    "M5": ("managing-change-records", ["creating-change-records", "closing-stale-packets"]),
    "M6": ("briefing-and-handing-off", ["handing-off-work", "briefing-an-agent"]),
    "M7": ("structuring-the-work", ["organizing-project-folders", "breaking-down-the-work"]),
}
# The surviving original whose old jobs must not get heavier (criterion C).
TARGETS = {
    "M1": "double-checking-before-acting",
    "M2": "learning-from-experience",
    "M3": "checking-legal-and-safety-wording",
    "M4": "recording-a-known-good-version",
    "M5": "creating-change-records",
    "M6": "handing-off-work",
    "M7": "organizing-project-folders",
}


def load(path: Path) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            out[row["id"]] = list(row.get("skills", []))
    return out


def rows(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]


def agreement(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict:
    ids = sorted(set(a) & set(b))
    exact = sum(set(a[i]) == set(b[i]) for i in ids)
    pos = [(set(a[i]), set(b[i])) for i in ids]
    inter = sum(len(x & y) for x, y in pos)
    union = sum(len(x | y) for x, y in pos)
    return {"n": len(ids), "exact_set_match": exact, "jaccard_micro": round(inter / union, 3) if union else 1.0}


def pct(num: int, den: int) -> float:
    return round(100 * num / den, 1) if den else float("nan")


def score_routing(truth, r31, r23, mapping) -> dict:
    out = {}
    for mid, (new, olds) in MERGES.items():
        rel = [i for i in truth if set(truth[i]) & set(olds)]
        other = [i for i in truth if i not in rel]
        hit31 = sum(bool(set(r31.get(i, [])) & set(truth[i]) & set(olds)) for i in rel)
        hit23 = sum(new in r23.get(i, []) for i in rel)
        fp31 = sum(bool(set(r31.get(i, [])) & set(olds)) for i in other)
        fp23 = sum(new in r23.get(i, []) for i in other)
        recall31, recall23 = pct(hit31, len(rel)), pct(hit23, len(rel))
        fpr31, fpr23 = pct(fp31, len(other)), pct(fp23, len(other))
        out[mid] = {
            "merged": new,
            "relevant_n": len(rel),
            "recall_31": recall31,
            "recall_23": recall23,
            "fp_rate_31": fpr31,
            "fp_rate_23": fpr23,
            "B_pass": (recall23 >= recall31 - 5) and (fpr23 <= fpr31 + 5),
        }
    # Whole-catalog micro precision/recall, with truth mapped into each catalog.
    for name, routed, conv in (("31", r31, lambda s: s), ("23", r23, lambda s: mapping.get(s, s))):
        tp = fp = fn = 0
        for i, t in truth.items():
            want = {conv(s) for s in t}
            got = set(routed.get(i, []))
            tp += len(want & got)
            fp += len(got - want)
            fn += len(want - got)
        out[f"catalog_{name}"] = {
            "precision": pct(tp, tp + fp),
            "recall": pct(tp, tp + fn),
            "none_correct": sum(1 for i, t in truth.items() if not t and not routed.get(i)),
            "none_truth": sum(1 for t in truth.values() if not t),
        }
    return out


def score_fit(fit_rows: list[dict]) -> dict:
    out = {}
    for mid in MERGES:
        rs = [r for r in fit_rows if r.get("merge") == mid]
        misses = [r["id"] for r in rs if r.get("misses_needed_work")]
        forced = [r["id"] for r in rs if r.get("forces_unneeded_work")]
        forced_target = [
            r["id"] for r in rs if r.get("forces_unneeded_work") and r.get("origin") == TARGETS[mid]
        ]
        n = len(rs)
        out[mid] = {
            "n": n,
            "misses": misses,
            "forced": forced,
            "forced_on_target_jobs": forced_target,
            "forced_rate": pct(len(forced), n),
            "C_pass": n > 0 and not misses and pct(len(forced), n) <= 10 and not forced_target,
        }
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("data", type=Path, help="folder holding the JSONL inputs and map-31-to-23.json")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)
    d = args.data
    truth = load(d / "truth.jsonl")
    mapping = json.loads((d / "map-31-to-23.json").read_text(encoding="utf-8"))
    result = {
        "labeler_agreement": agreement(load(d / "labels_a.jsonl"), load(d / "labels_b.jsonl")),
        "routing": score_routing(truth, load(d / "route31.jsonl"), load(d / "route23.jsonl"), mapping),
    }
    if (d / "fit.jsonl").exists():
        result["fit"] = score_fit(rows(d / "fit.jsonl"))
    text = json.dumps(result, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
