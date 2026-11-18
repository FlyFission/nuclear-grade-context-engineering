#!/usr/bin/env python3
"""Compare supplied prototype measurements; never execute candidates or verify their evidence.

Hard gate False = ineligible, None/missing = unknown. Missing metrics = unknown.
Scores are *relative to this candidate set*, not quality or assurance ratings.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def evaluate(payload: dict) -> dict:
    metrics = payload.get("metrics")
    candidates = payload.get("candidates")
    gates = payload.get("hard_gates", [])
    if not isinstance(metrics, dict) or not metrics:
        raise ValueError("metrics must be a nonempty mapping")
    if not isinstance(candidates, list) or len(candidates) < 2:
        raise ValueError("at least two candidates are required")
    if not isinstance(gates, list) or any(not isinstance(g, str) or not g for g in gates):
        raise ValueError("hard_gates must be nonempty names")
    if len(set(gates)) != len(gates):
        raise ValueError("duplicate hard gate")
    total_weight = 0.0
    for name, spec in metrics.items():
        if not isinstance(spec, dict) or spec.get("direction") not in ("min", "max"):
            raise ValueError(f"bad metric direction: {name}")
        weight = spec.get("weight")
        if isinstance(weight, bool) or not isinstance(weight, (int, float)) or not math.isfinite(weight) or weight < 0:
            raise ValueError(f"bad metric weight: {name}")
        total_weight += weight
    if total_weight <= 0:
        raise ValueError("positive total metric weight required")
    names = []
    observations = {m: [] for m in metrics}
    for c in candidates:
        if not isinstance(c, dict) or not isinstance(c.get("name"), str) or not c["name"]:
            raise ValueError("candidate must have a name")
        names.append(c["name"])
        status = c.get("gates", {})
        if not isinstance(status, dict) or set(status) != set(gates):
            raise ValueError(f"candidate {c['name']} must declare every gate")
        if any(v is not True and v is not False and v is not None for v in status.values()):
            raise ValueError(f"invalid gate status for {c['name']}")
        measured = c.get("results", {})
        if not isinstance(measured, dict) or set(measured) - set(metrics):
            raise ValueError(f"unknown metric for {c['name']}")
        for k, v in measured.items():
            if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
                raise ValueError(f"invalid measurement {k} for {c['name']}")
            observations[k].append(v)
    if len(set(names)) != len(names):
        raise ValueError("duplicate candidate name")
    rows = []
    for c in candidates:
        failed = [g for g in gates if c["gates"][g] is False]
        unknown_gates = [g for g in gates if c["gates"][g] is None]
        missing = [k for k in metrics if k not in c.get("results", {})]
        status = "INELIGIBLE" if failed else ("UNKNOWN" if unknown_gates or missing else "ELIGIBLE")
        score = None
        if status == "ELIGIBLE":
            score = 0.0
            for k, spec in metrics.items():
                lo, hi = min(observations[k]), max(observations[k])
                value = c["results"][k]
                scaled = 0.5 if hi == lo else (value - lo) / (hi - lo)
                if spec["direction"] == "min":
                    scaled = 1 - scaled
                score += spec["weight"] * scaled / total_weight
        rows.append({
            "name": c["name"], "status": status, "failed_gates": failed,
            "unknown_gates": unknown_gates, "missing_metrics": missing,
            "relative_score_100": round(score * 100, 3) if score is not None else None,
            "evidence": c.get("evidence", "NOT_PROVIDED"),
        })
    ranked = sorted((r for r in rows if r["status"] == "ELIGIBLE"),
                    key=lambda r: (-r["relative_score_100"], r["name"]))
    return {
        "ranking": [x["name"] for x in ranked],
        "provisional_winner": ranked[0]["name"] if ranked else None,
        "candidates": rows,
        "warning": "Provided measurements are unverified. Relative scores depend on this candidate set and chosen weights. Check uncertainty, sensitivity and recorded evidence before deciding. No prototypes were executed.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    try:
        report = evaluate(json.loads(args.input.read_text(encoding="utf-8")))
    except (ValueError, TypeError, KeyError, OSError) as exc:
        parser.error(str(exc))
    output = json.dumps(report, indent=2) + "\n"
    if args.out:
        args.out.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
