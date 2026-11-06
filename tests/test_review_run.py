"""Admission tests exercise actual CLI decisions, not narrative keyword matching."""
import hashlib
import json

import pytest

from tests.test_ng_cli import run_ng
from tests.test_ng_validate import minimal_quick_packet


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture
def run(tmp_path):
    tmp_path = minimal_quick_packet(tmp_path)
    authorization = {
        "schema_version": 1, "scope": "calibration", "approved_by": "budget-owner", "approved_at": "2026-11-01T00:00:00Z",
        "required_usable_cases": 2, "attempt_ceiling": 3, "transport_reserve": 1,
        "reservation_per_attempt": 100, "reservation_ceiling": 300,
        "runtime_sha256": "a" * 64, "stop_on": ["calibration_failed", "unknown"],
    }
    digest = write_json(tmp_path / "review-authorization.v1.json", authorization)
    record = {"schema_version": 1, "authorization_sha256": digest, "attempts": [],
              "next_attempt": {"id": "A1", "case_id": "A1", "runtime_sha256": "a" * 64}}
    return tmp_path, authorization, record


def check(run, before=True):
    path, _, record = run
    write_json(path / "review-run.v1.json", record)
    return run_ng("validate", str(path), *( ["--before-review"] if before else []))


def attempt(identity, outcome="usable"):
    return {"id": identity, "case_id": identity, "runtime_sha256": "a" * 64, "outcome": outcome,
            "started_at": "2026-11-02T00:00:00Z", "reserved_units": 100,
            "coverage_credit": outcome == "usable", "opinion": "support" if outcome == "usable" else None}


def test_valid_first_call_and_old_packet_compatibility(run):
    assert check(run).returncode == 0
    (run[0] / "review-run.v1.json").unlink()
    assert run_ng("validate", str(run[0])).returncode == 0
    assert run_ng("validate", str(run[0]), "--before-review").returncode == 1


@pytest.mark.parametrize("mutation, expected", [
    (lambda r: r.update(authorization_sha256="0" * 64), "authorization digest"),
    (lambda r: r.update(attempts=[attempt("A1")]), "duplicate"),
    (lambda r: r.update(attempts=[attempt("old", "calibration_failed")]), "stop condition"),
    (lambda r: r.update(attempts=[attempt("old", "unknown")]), "stop condition"),
    (lambda r: r.update(attempts=[attempt("old", "transport_failed") | {"coverage_credit": True}]), "no review support"),
    (lambda r: r.update(attempts=[attempt("old") | {"reserved_units": 0}]), "full reservation"),
    (lambda r: r.update(attempts=[attempt("old") | {"started_at": "2026-10-01T00:00:00Z"}]), "predates authorization"),
    (lambda r: r.update(next_attempt={"id": "A1", "case_id": "A1", "runtime_sha256": "b" * 64}), "runtime"),
    (lambda r: r.update(next_attempt={"id": "A1", "case_id": "A1", "runtime_sha256": "a" * 64, "recovery_of": "absent"}), "transport failure"),
    (lambda r: r.update(attempts=[attempt("x"), attempt("y")]), "ordinary attempt ceiling"),
    (lambda r: r.update(attempts=[attempt("x"), attempt("y"), attempt("z")]), "attempt ceiling"),
])
def test_pre_dispatch_rejects_invalid_or_stopped_run(run, mutation, expected):
    mutation(run[2])
    result = check(run)
    assert result.returncode == 1
    assert expected in result.stdout


def test_transport_recovery_needs_pinned_repair_evidence(run):
    path, _, record = run
    record["attempts"] = [attempt("old", "transport_failed")]
    record["next_attempt"].update(recovery_of="old", case_id="old")
    assert "repair evidence" in check(run).stdout
    digest = write_json(path / "repair.json", {"regression": "passed"})
    record["next_attempt"]["repair_evidence"] = {"path": "repair.json", "sha256": digest}
    assert check(run).returncode == 0
    (path / "repair.json").write_text("changed")
    assert "repair evidence" in check(run).stdout


def test_reserve_exhaustion_blocks_second_recovery(run):
    path, _, record = run
    digest = write_json(path / "repair.json", {"regression": "passed"})
    repair = {"path": "repair.json", "sha256": digest}
    record["attempts"] = [attempt("old", "transport_failed"),
                          attempt("replacement", "transport_failed") | {"case_id": "old", "recovery_of": "old", "repair_evidence": repair}]
    record["next_attempt"].update(recovery_of="replacement", case_id="old", repair_evidence=repair)
    assert "transport reserve" in check(run).stdout


def test_overspent_history_rejected_without_dispatch_flag(run):
    run[2]["attempts"] = [attempt(str(i)) for i in range(4)]
    assert check(run, before=False).returncode == 1


@pytest.mark.parametrize("value", [None, [], {"schema_version": 2}, {"schema_version": True}])
def test_malformed_artifact_fails_closed(run, value):
    write_json(run[0] / "review-run.v1.json", value)
    assert run_ng("validate", str(run[0]), "--before-review").returncode == 1


def test_nine_attempts_eight_usable_cannot_finish_sixteen_case_gate(run):
    path, auth, record = run
    auth.update(required_usable_cases=16, attempt_ceiling=16, transport_reserve=0, reservation_ceiling=1600)
    record["authorization_sha256"] = write_json(path / "review-authorization.v1.json", auth)
    record["attempts"] = [attempt(str(i)) for i in range(8)] + [attempt("failed", "transport_failed")]
    result = check(run)
    assert result.returncode == 1
    assert "required usable cases infeasible" in result.stdout


def test_complete_run_without_dispatch_and_receipt_marks_admission(run):
    run[2]["attempts"] = [attempt("x"), attempt("y")]
    assert check(run, before=False).returncode == 0
    run[2]["attempts"] = []
    assert check(run).returncode == 0
    result = run_ng("validate", str(run[0]), "--before-review", "--json")
    assert result.returncode == 0
    assert json.loads(result.stdout)["before_review"] is True


@pytest.mark.parametrize("changes, expected", [
    ({"attempt_ceiling": True}, "integer"),
    ({"transport_reserve": -1}, "integer"),
    ({"reservation_ceiling": 99}, "full reservations"),
    ({"required_usable_cases": 4}, "ordinary attempt ceiling"),
    ({"stop_on": []}, "stop_on"),
    ({"approved_by": ""}, "budget owner"),
    ({"unrecognized": 1}, "unknown record fields"),
])
def test_malformed_authorization_rejected_even_with_matching_digest(run, changes, expected):
    path, auth, record = run
    auth.update(changes)
    record["authorization_sha256"] = write_json(path / "review-authorization.v1.json", auth)
    assert expected in check(run).stdout


def test_duplicate_case_cannot_inflate_usable_coverage(run):
    run[2]["attempts"] = [attempt("old") | {"case_id": "A1"}]
    assert "duplicate case" in check(run).stdout


def test_usable_non_support_opinion_allows_changed_state_review(run):
    path, auth, record = run
    auth["scope"] = "review"
    record["authorization_sha256"] = write_json(path / "review-authorization.v1.json", auth)
    record["attempts"] = [attempt("original-state") | {"opinion": "non_support"}]
    record["next_attempt"]["case_id"] = "changed-exact-state"
    assert check(run).returncode == 0


def test_calibration_stop_cannot_mislabel_ordinary_review_findings(run):
    path, auth, record = run
    auth["scope"] = "review"
    record["authorization_sha256"] = write_json(path / "review-authorization.v1.json", auth)
    record["attempts"] = [attempt("old", "calibration_failed")]
    assert "ordinary findings are usable opinions" in check(run).stdout


def parallel_budget(run, *, required=4, ceiling=4):
    path, auth, record = run
    auth.update(required_usable_cases=required, attempt_ceiling=ceiling, transport_reserve=0,
                reservation_ceiling=ceiling * 100)
    record["authorization_sha256"] = write_json(path / "review-authorization.v1.json", auth)
    return record


def test_four_reserved_in_flight_attempts_block_fifth_under_four_cap(run):
    record = parallel_budget(run)
    record["attempts"] = [attempt(str(i), "in_flight") for i in range(4)]
    assert check(run, before=False).returncode == 0
    result = check(run)
    assert result.returncode == 1
    assert "total attempt ceiling" in result.stdout


def test_pending_potential_keeps_feasible_target_admissible(run):
    record = parallel_budget(run)
    record["attempts"] = [attempt(str(i), "in_flight") for i in range(3)]
    assert check(run).returncode == 0


def test_pending_cannot_claim_usable_credit_or_opinion(run):
    record = parallel_budget(run)
    record["attempts"] = [attempt("pending", "in_flight") | {"coverage_credit": True}]
    assert "no review support or coverage credit" in check(run).stdout
    record["attempts"][0].update(coverage_credit=False, opinion="non_support")
    assert "only usable reviews have" in check(run).stdout


def test_pending_retains_full_reservation(run):
    record = parallel_budget(run)
    record["attempts"] = [attempt("pending", "in_flight") | {"reserved_units": 0}]
    assert "full reservation" in check(run).stdout


def test_pending_settles_same_id_without_consuming_extra_slot(run):
    record = parallel_budget(run)
    record["attempts"] = [attempt(str(i), "in_flight") for i in range(3)]
    assert check(run).returncode == 0
    record["attempts"][0] = attempt("0") | {"opinion": "non_support"}
    assert check(run).returncode == 0
    record["attempts"].append(attempt("0"))
    assert "duplicate attempt id" in check(run).stdout


def test_unknown_blocks_new_dispatch_even_with_later_pending_or_settled_peers(run):
    record = parallel_budget(run, required=2)
    record["attempts"] = [attempt("failed", "unknown"), attempt("peer", "in_flight"), attempt("settled")]
    assert check(run, before=False).returncode == 0
    assert "stop condition" in check(run).stdout


def test_in_flight_cannot_be_retried_using_transport_reserve(run):
    run[2]["attempts"] = [attempt("pending", "in_flight")]
    run[2]["next_attempt"].update(recovery_of="pending", case_id="pending")
    assert "earlier transport failure" in check(run).stdout
