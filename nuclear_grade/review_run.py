"""Opt-in declared review budget checks; no provider calls or approval authentication."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path


class InvalidRun(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise InvalidRun(message)


def fields(value: object, required: set[str], optional: set[str] | None = None) -> dict:
    require(isinstance(value, dict), "record must be an object")
    require(required <= value.keys() <= required | (optional or set()), "missing or unknown record fields")
    return value


def positive(value: object, label: str, *, zero: bool = False) -> int:
    require(type(value) is int and value >= (0 if zero else 1), f"{label} must be an integer")
    return value


def timestamp(value: object) -> datetime:
    require(isinstance(value, str) and value.endswith("Z"), "timestamps must be UTC ISO strings ending Z")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def pin(packet: Path, value: object, label: str) -> Path:
    item = fields(value, {"path", "sha256"})
    require(isinstance(item["path"], str), f"{label} path must be a string")
    path = (packet / item["path"]).resolve()
    require(path.is_relative_to(packet.resolve()) and path.is_file(), f"{label} must be a file inside packet")
    require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"{label} digest mismatch")
    return path


def check_review_run(packet: Path, *, before_review: bool = False) -> list[str]:
    """Validate present v1 history; admission additionally checks proposed next attempt."""
    run_file = packet / "review-run.v1.json"
    if not run_file.exists():
        return ["before-review requires review-run.v1.json"] if before_review else []
    try:
        run = fields(json.loads(run_file.read_text()),
                     {"schema_version", "authorization_sha256", "attempts", "next_attempt"})
        require(type(run["schema_version"]) is int and run["schema_version"] == 1, "unsupported schema_version")
        auth_file = packet / "review-authorization.v1.json"
        require(auth_file.is_file(), "missing review-authorization.v1.json")
        require(hashlib.sha256(auth_file.read_bytes()).hexdigest() == run["authorization_sha256"],
                "authorization digest mismatch")
        auth = fields(json.loads(auth_file.read_text()), {
            "schema_version", "scope", "approved_by", "approved_at", "required_usable_cases", "attempt_ceiling",
            "transport_reserve", "reservation_per_attempt", "reservation_ceiling", "runtime_sha256", "stop_on",
        })
        require(type(auth["schema_version"]) is int and auth["schema_version"] == 1, "unsupported authorization version")
        require(auth["scope"] in {"review", "calibration"}, "scope must be review or calibration")
        require(isinstance(auth["approved_by"], str) and bool(auth["approved_by"].strip()), "missing budget owner")
        approved = timestamp(auth["approved_at"])
        ceiling = positive(auth["attempt_ceiling"], "attempt ceiling")
        reserve = positive(auth["transport_reserve"], "transport reserve", zero=True)
        required = positive(auth["required_usable_cases"], "required usable cases")
        reservation = positive(auth["reservation_per_attempt"], "reservation per attempt")
        require(required <= ceiling - reserve, "required usable cases exceed ordinary attempt ceiling")
        require(positive(auth["reservation_ceiling"], "reservation ceiling") >= ceiling * reservation,
                "reservation ceiling cannot fund full reservations")
        require(isinstance(auth["runtime_sha256"], str) and re.fullmatch(r"[0-9a-f]{64}", auth["runtime_sha256"]) is not None,
                "runtime must be a SHA256 digest")
        require(auth["stop_on"] == ["calibration_failed", "unknown"], "stop_on must preserve calibration_failed and unknown")
        require(isinstance(run["attempts"], list), "attempts must be a list")
        prior: dict[str, dict] = {}
        ordinary = recovered = usable = pending = 0
        stopped = False
        for attempt in run["attempts"] + ([run["next_attempt"]] if before_review else []):
            proposed = before_review and attempt is run["next_attempt"]
            item = fields(attempt, {"id", "case_id", "runtime_sha256"} if proposed else {
                "id", "case_id", "runtime_sha256", "outcome", "started_at", "reserved_units", "coverage_credit", "opinion",
            }, {"recovery_of", "repair_evidence"})
            require(isinstance(item["id"], str) and bool(item["id"].strip()), "attempt id must be nonempty")
            require(item["id"] not in prior, "duplicate attempt id")
            require(isinstance(item["case_id"], str) and bool(item["case_id"].strip()), "case_id must be nonempty")
            require(item["runtime_sha256"] == auth["runtime_sha256"], "attempt runtime differs from authorization")
            if proposed:
                require(not stopped, "stop condition blocks further dispatch; preserve history for budget-owner disposition")
            if "recovery_of" in item:
                original = prior.get(item["recovery_of"]) if isinstance(item["recovery_of"], str) else None
                require(original is not None and original["outcome"] == "transport_failed",
                        "recovery must reference an earlier transport failure")
                require(item["case_id"] == original["case_id"], "transport recovery must preserve case_id")
                require(not any(a.get("recovery_of") == item["recovery_of"] for a in prior.values()),
                        "transport failure already has a replacement")
                require("repair_evidence" in item, "transport recovery requires pinned repair evidence")
                pin(packet, item["repair_evidence"], "repair evidence")
                recovered += 1
            else:
                require("repair_evidence" not in item, "repair evidence requires recovery_of")
                require(not any(a["case_id"] == item["case_id"] for a in prior.values()),
                        "duplicate case requires transport recovery")
                ordinary += 1
            require(len(prior) + 1 <= ceiling, "total attempt ceiling exceeded")
            require(ordinary <= ceiling - reserve, "ordinary attempt ceiling exceeded")
            require(recovered <= reserve, "transport reserve exhausted")
            if not proposed:
                require(timestamp(item["started_at"]) >= approved, "attempt predates authorization")
                require(type(item["reserved_units"]) is int and item["reserved_units"] == reservation,
                        "every attempt retains its full reservation")
                require(item["outcome"] in {"usable", "in_flight", "transport_failed", "calibration_failed", "unknown"}, "invalid outcome")
                require(item["opinion"] in {"support", "non_support"} if item["outcome"] == "usable"
                        else item["opinion"] is None, "only usable reviews have support/non_support opinions")
                require(item["outcome"] != "calibration_failed" or auth["scope"] == "calibration",
                        "calibration_failed requires calibration scope; ordinary findings are usable opinions")
                require(type(item["coverage_credit"]) is bool and item["coverage_credit"] == (item["outcome"] == "usable"),
                        "failed or unknown attempts supply no review support or coverage credit")
                usable += item["outcome"] == "usable"
                pending += item["outcome"] == "in_flight"
                # Already-launched peers may settle later; none may clear a recorded stop.
                stopped = stopped or item["outcome"] in auth["stop_on"]
                prior[item["id"]] = item
        if before_review:
            require(required - usable <= pending + ceiling - len(run["attempts"]),
                    "required usable cases infeasible within remaining attempt ceiling")
        return []
    except (InvalidRun, ValueError, TypeError, KeyError, OSError) as error:
        return [f"review-run.v1.json: {error}"]
