#!/usr/bin/env python3
"""Score the skill-consolidation evaluation against PROTOCOL.md.

Inputs (all JSONL, one object per line, keyed by scenario ``id``):

- ``scenarios.jsonl``        {"id", "work_type", "stage", "risk", "prompt"}
- ``truth.jsonl``            {"id", "skills": [...31-catalog names...]}  adjudicated
- ``labels_a.jsonl``, ``labels_b.jsonl``  the two independent labelings (same shape)
- ``route31.jsonl``, ``routenew.jsonl``    blind router picks (same shape)
- ``fit.jsonl``              {"id", "merge", "origin", "misses_needed_work": bool,
                              "forces_unneeded_work": bool, "section", "note"}

``map-31-to-new.json`` maps each 31-catalog name to its name in the candidate catalog.

Criterion B (routing parity) and C (fit) are computed here. A (coverage) and D
(context) come from the coverage audit and ``ng tokens``. Stdlib only.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

# M1 (declaring-intent -> double-checking-before-acting) and M6 (briefing-an-agent
# -> handing-off-work) failed criterion A (coverage) after their one allowed
# revision, so per PROTOCOL.md they are not made and are not scored here.
MERGES = {
    "M2": ("learning-from-experience", ["learning-from-experience", "tracking-deficiencies", "reporting-shared-defects"]),
    "M3": ("checking-public-claims", ["checking-legal-and-safety-wording", "checking-source-claims"]),
    "M4": ("controlling-approved-versions", ["recording-a-known-good-version", "choosing-what-to-control"]),
    "M5": ("managing-change-records", ["creating-change-records", "closing-stale-packets"]),
    "M7": ("structuring-the-work", ["organizing-project-folders", "breaking-down-the-work"]),
}
# The surviving original whose old jobs must not get heavier (criterion C).
TARGETS = {
    "M2": "learning-from-experience",
    "M3": "checking-legal-and-safety-wording",
    "M4": "recording-a-known-good-version",
    "M5": "creating-change-records",
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


def pct(num: int, den: int) -> float | None:
    """A percentage, or None (JSON null) when there is nothing to divide by."""
    return round(100 * num / den, 1) if den else None


def score_routing(truth, r31, rnew, mapping) -> dict:
    out = {}
    for mid, (new, olds) in MERGES.items():
        rel = [i for i in truth if set(truth[i]) & set(olds)]
        other = [i for i in truth if i not in rel]
        hit31 = sum(bool(set(r31.get(i, [])) & set(truth[i]) & set(olds)) for i in rel)
        hitnew = sum(new in rnew.get(i, []) for i in rel)
        fp31 = sum(bool(set(r31.get(i, [])) & set(olds)) for i in other)
        fpnew = sum(new in rnew.get(i, []) for i in other)
        recall31, recallnew = pct(hit31, len(rel)), pct(hitnew, len(rel))
        fpr31, fprnew = pct(fp31, len(other)), pct(fpnew, len(other))
        out[mid] = {
            "merged": new,
            "relevant_n": len(rel),
            "recall_31": recall31,
            "recall_new": recallnew,
            "fp_rate_31": fpr31,
            "fp_rate_new": fprnew,
            "B_pass": None
            if None in (recall31, recallnew, fpr31, fprnew)
            else (recallnew >= recall31 - 5) and (fprnew <= fpr31 + 5),
        }
    # Whole-catalog micro precision/recall, with truth mapped into each catalog.
    for name, routed, conv in (("31", r31, lambda s: s), ("new", rnew, lambda s: mapping.get(s, s))):
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
    """Criterion C, counted per scenario as PROTOCOL.md states it.

    A scenario that needed two originals of one merge has one row per origin; it
    is one scenario. It misses (or forces) work if any of its rows does, and it
    forces work on a target job if a forcing row's origin is the target skill.
    """
    out = {}
    for mid in MERGES:
        rs = [r for r in fit_rows if r.get("merge") == mid]
        ids = sorted({r["id"] for r in rs})
        misses = sorted({r["id"] for r in rs if r.get("misses_needed_work")})
        forced = sorted({r["id"] for r in rs if r.get("forces_unneeded_work")})
        forced_target = sorted(
            {r["id"] for r in rs if r.get("forces_unneeded_work") and r.get("origin") == TARGETS[mid]}
        )
        n = len(ids)
        rate = pct(len(forced), n)
        out[mid] = {
            "n": n,
            "rows": len(rs),
            "misses": misses,
            "forced": forced,
            "forced_on_target_jobs": forced_target,
            "forced_rate": rate,
            "C_pass": n > 0 and not misses and rate <= 10 and not forced_target,
        }
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("data", type=Path, help="folder holding the JSONL inputs and map-31-to-new.json")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)
    d = args.data
    truth = load(d / "truth.jsonl")
    # The mapping is a fixed artifact of the evaluation, kept beside this script;
    # a copy in the data folder wins if present.
    map_path = d / "map-31-to-new.json"
    if not map_path.exists():
        map_path = Path(__file__).resolve().parent / "map-31-to-new.json"
    mapping = json.loads(map_path.read_text(encoding="utf-8"))
    result = {
        "labeler_agreement": agreement(load(d / "labels_a.jsonl"), load(d / "labels_b.jsonl")),
        "routing": score_routing(truth, load(d / "route31.jsonl"), load(d / "routenew.jsonl"), mapping),
    }
    if (d / "fit.jsonl").exists():
        result["fit"] = score_fit(rows(d / "fit.jsonl"))
    text = json.dumps(result, indent=2, allow_nan=False)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
