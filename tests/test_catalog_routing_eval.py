import json
import sys
from pathlib import Path

import pytest

from nuclear_grade.routing_eval import (
    RoutingEvalError,
    load_observed,
    load_scenarios,
    score_routes,
)
from nuclear_grade.skill_catalog import load_catalog
from tools import ng_skill_catalog_route_score as score_cli

ROOT = Path(__file__).resolve().parents[1]


def test_repository_catalog_routing_scenarios_are_valid_and_model_routable():
    catalog = load_catalog(ROOT)
    scenarios = load_scenarios(ROOT / "evals" / "skill-routing-scenarios.jsonl", catalog)

    assert len(scenarios) >= 12
    assert len({scenario.id for scenario in scenarios}) == len(scenarios)
    assert all(scenario.required_skills for scenario in scenarios)


def test_exact_set_scorer_counts_misses_overtriggering_and_exact_routes(tmp_path):
    cases_path = tmp_path / "cases.jsonl"
    observed_path = tmp_path / "observed.jsonl"
    cases_path.write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "id": "a",
                        "prompt": "classify",
                        "required_skills": ["using-nuclear-grade", "rating-change-risk"],
                    }
                ),
                json.dumps(
                    {
                        "id": "b",
                        "prompt": "brief",
                        "required_skills": ["briefing-an-agent"],
                        "allowed_skills": ["briefing-an-agent", "using-nuclear-grade"],
                    }
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    observed_path.write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "id": "a",
                        "loaded_skills": ["using-nuclear-grade", "handing-off-work"],
                    }
                ),
                json.dumps(
                    {
                        "id": "b",
                        "loaded_skills": ["briefing-an-agent", "using-nuclear-grade"],
                    }
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    catalog = load_catalog(ROOT)
    scenarios = load_scenarios(cases_path, catalog)
    observed = load_observed(observed_path, scenarios, catalog)
    report = score_routes(scenarios, observed)

    assert report.true_positive == 2
    assert report.false_negative == 1
    assert report.false_positive == 1
    assert report.acceptable_cases == 1
    assert report.total_cases == 2
    assert report.precision == pytest.approx(2 / 3)
    assert report.recall == pytest.approx(2 / 3)
    assert report.failures == (
        "a: missing required skill(s): rating-change-risk",
        "a: unnecessary skill(s): handing-off-work",
    )


def test_observed_routes_fail_closed_on_unknown_missing_and_duplicate_rows(tmp_path):
    catalog = load_catalog(ROOT)
    cases_path = tmp_path / "cases.jsonl"
    cases_path.write_text(
        json.dumps(
            {
                "id": "a",
                "prompt": "classify",
                "required_skills": ["rating-change-risk"],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    scenarios = load_scenarios(cases_path, catalog)

    observed_path = tmp_path / "observed.jsonl"
    observed_path.write_text(
        "\n".join(
            [
                json.dumps({"id": "a", "loaded_skills": ["not-a-skill"]}),
                json.dumps({"id": "a", "loaded_skills": []}),
                json.dumps({"id": "extra", "loaded_skills": []}),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(RoutingEvalError) as exc:
        load_observed(observed_path, scenarios, catalog)

    message = str(exc.value)
    assert "unknown skill" in message
    assert "duplicate observed id" in message
    assert "no matching scenario" in message


def test_observed_routes_reject_empty_or_partial_runs(tmp_path):
    catalog = load_catalog(ROOT)
    cases_path = tmp_path / "cases.jsonl"
    cases_path.write_text(
        "\n".join(
            [
                json.dumps({"id": "a", "prompt": "a", "required_skills": ["rating-change-risk"]}),
                json.dumps({"id": "b", "prompt": "b", "required_skills": ["briefing-an-agent"]}),
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    scenarios = load_scenarios(cases_path, catalog)

    empty = tmp_path / "empty.jsonl"
    empty.write_text("\n", encoding="utf-8")
    with pytest.raises(RoutingEvalError, match="at least one observed route"):
        load_observed(empty, scenarios, catalog)

    partial = tmp_path / "partial.jsonl"
    partial.write_text(json.dumps({"id": "a", "loaded_skills": ["rating-change-risk"]}) + "\n", encoding="utf-8")
    with pytest.raises(RoutingEvalError, match="missing observed route.*b"):
        load_observed(partial, scenarios, catalog)


def test_cli_thresholds_can_intentionally_accept_nonperfect_observations(tmp_path, monkeypatch):
    cases = tmp_path / "cases.jsonl"
    observed = tmp_path / "observed.jsonl"
    cases.write_text(
        json.dumps(
            {
                "id": "a",
                "prompt": "classify",
                "required_skills": ["rating-change-risk"],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    observed.write_text(json.dumps({"id": "a", "loaded_skills": []}) + "\n", encoding="utf-8")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "ng_skill_catalog_route_score.py",
            "--repo",
            str(ROOT),
            "--cases",
            str(cases),
            "--observed",
            str(observed),
            "--min-recall",
            "0",
            "--min-acceptable-rate",
            "0",
        ],
    )

    assert score_cli.main() == 0


def test_scenario_manifest_rejects_zero_scenarios(tmp_path):
    catalog = load_catalog(ROOT)
    path = tmp_path / "cases.jsonl"
    path.write_text("\n", encoding="utf-8")

    with pytest.raises(RoutingEvalError, match="at least one routing scenario"):
        load_scenarios(path, catalog)


def test_score_routes_rejects_zero_scenarios():
    with pytest.raises(RoutingEvalError, match="at least one routing scenario"):
        score_routes((), {})


def test_scenario_rejects_non_model_routable_or_allowed_without_required(tmp_path):
    catalog = load_catalog(ROOT)
    path = tmp_path / "cases.jsonl"
    path.write_text(
        json.dumps(
            {
                "id": "bad",
                "prompt": "bad",
                "required_skills": ["rating-change-risk"],
                "allowed_skills": ["using-nuclear-grade"],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(RoutingEvalError, match="required_skills must be a subset"):
        load_scenarios(path, catalog)
