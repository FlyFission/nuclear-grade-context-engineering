#!/usr/bin/env python3
"""Validate or score catalog-level skill-routing observations.

Examples:
  python tools/ng_skill_catalog_route_score.py
  python tools/ng_skill_catalog_route_score.py --observed path/to/observed.jsonl

Observed JSONL rows use:
  {"id": "catalog-001", "loaded_skills": ["using-nuclear-grade", "rating-change-risk"]}

Without ``--observed`` the command validates lifecycle and scenario contracts only.
That structural pass is not evidence that a live model or host routed correctly.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nuclear_grade.routing_eval import load_observed, load_scenarios, score_routes
from nuclear_grade.skill_catalog import load_catalog


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument(
        "--cases",
        type=Path,
        default=Path("evals/skill-routing-scenarios.jsonl"),
    )
    parser.add_argument("--observed", type=Path)
    parser.add_argument("--min-precision", type=float, default=1.0)
    parser.add_argument("--min-recall", type=float, default=1.0)
    parser.add_argument("--min-exact-rate", type=float, default=1.0)
    args = parser.parse_args()

    repo = args.repo.resolve()
    cases_path = args.cases if args.cases.is_absolute() else repo / args.cases
    catalog = load_catalog(repo)
    scenarios = load_scenarios(cases_path, catalog)
    print(
        f"Validated {len(scenarios)} catalog-routing scenario(s) against "
        f"{len(catalog.model_routable)} promoted model-routable skill(s)."
    )

    if args.observed is None:
        print("No observed routes supplied; live routing behavior was not scored.")
        return 0

    observed_path = args.observed if args.observed.is_absolute() else repo / args.observed
    observed = load_observed(observed_path, scenarios, catalog)
    report = score_routes(scenarios, observed)
    for failure in report.failures:
        print(f"- {failure}")
    print(
        "Catalog routing: "
        f"precision={report.precision:.3f} "
        f"recall={report.recall:.3f} "
        f"exact={report.exact_cases}/{report.total_cases} ({report.exact_rate:.3f}) "
        f"false_positive={report.false_positive} false_negative={report.false_negative}"
    )

    threshold_failures = []
    if report.precision < args.min_precision:
        threshold_failures.append(
            f"precision {report.precision:.3f} is below {args.min_precision:.3f}"
        )
    if report.recall < args.min_recall:
        threshold_failures.append(f"recall {report.recall:.3f} is below {args.min_recall:.3f}")
    if report.exact_rate < args.min_exact_rate:
        threshold_failures.append(
            f"exact rate {report.exact_rate:.3f} is below {args.min_exact_rate:.3f}"
        )
    for failure in threshold_failures:
        print(f"- {failure}")
    return 0 if not report.failures and not threshold_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
