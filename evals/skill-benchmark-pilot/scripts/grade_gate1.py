#!/usr/bin/env python3
"""Blind-grade every run in runs_all/ against its skill's pre-registered pass_criteria."""
import hashlib
import json
import statistics as stats
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE.parent / "data" / "gate1-hard-case-pilot"
RUNS_DIR = DATA_DIR / "runs"
TASKS = json.loads((DATA_DIR / "gate1_tasks.json").read_text())
GRADER_MODEL = "claude-haiku-4-5-20251001"
MAX_WORKERS = 8
# Bump whenever the grading prompt's instructional wording changes, so a
# wording-only edit invalidates the cache the same way a criteria or model
# change already does automatically (see grading_spec_hash).
PROMPT_VERSION = "v1"


def grading_spec_hash(skill: str) -> str:
    """Fingerprint of everything besides the transcript that can change a
    verdict: the skill's own pass_criteria text, the grader model, and the
    prompt template version. A cached row is only reused if this ALSO
    matches -- a pass_criteria edit, corrected structural criterion, or
    grader model change must force a re-grade even though the transcript
    itself (and its _source_sha256) is unchanged."""
    criteria = TASKS[skill]["pass_criteria"]
    return hashlib.sha256(f"{criteria}::{GRADER_MODEL}::{PROMPT_VERSION}".encode()).hexdigest()

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "meets_criteria": {"type": "string", "enum": ["YES", "PARTIAL", "NO"]},
        "quote": {"type": "string"},
    },
    "required": ["meets_criteria", "quote"],
})


def grade_review(skill: str, review_text: str) -> dict:
    criteria = TASKS[skill]["pass_criteria"]
    prompt = (
        "You are grading a response against ONE specific pass criterion. "
        "Do not reward general competence, tone, or thoroughness — check ONLY whether "
        "this exact criterion is explicitly satisfied.\n\n"
        f"Pass criterion:\n{criteria}\n\n"
        f"Response to grade:\n---\n{review_text}\n---\n\n"
        "Answer YES only if the criterion is clearly and explicitly met, "
        "PARTIAL if it is hinted at but not explicit or is materially incomplete, "
        "NO if it is absent."
    )
    cmd = [
        "claude", "-p", prompt,
        "--output-format", "json",
        "--model", GRADER_MODEL,
        "--safe-mode",
        "--tools", "",
        "--no-session-persistence",
        "--max-budget-usd", "0.20",
        "--json-schema", SCHEMA,
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        record = json.loads(proc.stdout.strip())
        return json.loads(record["result"])
    except Exception as e:
        return {"meets_criteria": "ERROR", "quote": str(e)[:200]}


def load_grade_cache(out_path: Path) -> dict:
    """Prior valid grades, keyed by (skill, condition, trial) -- used so a
    partial rerun (one regenerated run file) doesn't send every other,
    unchanged transcript back through the live grader. Cache validity is
    decided by comparing the run file's own content hash (stored on the
    cached row) against its current hash, NOT by file mtimes: on a fresh
    checkout, git's write order gives run files and the graded-results file
    mtimes that reflect checkout order, not actual regeneration, so an
    mtime-based gate can miss the cache for most unchanged files. A cached
    row also carries a _criteria_sha256 fingerprint of the grading inputs
    (pass_criteria text, grader model, prompt version) that must still match
    the live inputs -- a criteria edit or grader-model change invalidates a
    row even though the transcript itself hasn't changed."""
    if not out_path.exists():
        return {}
    try:
        prior_rows = json.loads(out_path.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    return {(r["skill"], r["condition"], r["trial"]): r
            for r in prior_rows if r.get("error") is False and r.get("_source_sha256")}


def grade_one(path: Path, cache: dict) -> dict:
    raw = path.read_bytes()
    d = json.loads(raw)
    skill = d.get("_skill")
    condition = d.get("_condition")
    trial = d.get("_trial")
    if d.get("type") == "error" or d.get("is_error"):
        return {"skill": skill, "condition": condition, "trial": trial, "error": True}

    result_text = d.get("result", "")
    # Hash only the substantive transcript text, not the whole file's raw
    # bytes -- hashing the full file means any unrelated metadata field added
    # to the run record later (e.g. the harness-settings fingerprint added in
    # round 33) invalidates every cached grade even though the graded content
    # never changed.
    source_hash = hashlib.sha256(result_text.encode()).hexdigest()
    spec_hash = grading_spec_hash(skill)
    cached = cache.get((skill, condition, trial))
    if (cached is not None and cached.get("_source_sha256") == source_hash
            and cached.get("_criteria_sha256") == spec_hash):
        meets_criteria = cached["meets_criteria"]
        grader_quote = cached["grader_quote"]
    else:
        grade = grade_review(skill, result_text)
        if grade.get("meets_criteria") == "ERROR":
            return {"skill": skill, "condition": condition, "trial": trial, "error": True,
                    "grader_error": True, "grader_quote": grade.get("quote")}
        meets_criteria = grade.get("meets_criteria")
        grader_quote = grade.get("quote")

    # Run-metadata fields are always rebuilt from the CURRENT run file, cache
    # hit or not -- a regenerated run with identical result text but corrected
    # cost/token/duration data (e.g. a retried transient failure) must not
    # silently keep serving the old run's now-stale metadata forever.
    usage = d.get("usage", {})
    return {
        "skill": skill, "condition": condition, "trial": trial, "error": False,
        "meets_criteria": meets_criteria,
        "grader_quote": grader_quote,
        "cost_usd": d.get("total_cost_usd"),
        "input_tokens": usage.get("input_tokens"),
        "output_tokens": usage.get("output_tokens"),
        "cache_read_tokens": usage.get("cache_read_input_tokens"),
        "cache_creation_tokens": usage.get("cache_creation_input_tokens"),
        "num_turns": d.get("num_turns"),
        "duration_ms": d.get("duration_ms"),
        "_source_sha256": source_hash,
        "_criteria_sha256": spec_hash,
    }


TRIALS = (1, 2, 3, 4, 5)


def check_complete():
    """Refuse to grade (and overwrite the checked-in graded-results file) on a
    partial batch -- e.g. a rerun interrupted after deleting one trial -- since
    downstream reports/statistics derive their denominators from whatever this
    writes, with no way to tell a genuinely complete batch from a truncated one.
    Also refuse if the directory holds files OUTSIDE the expected set (a stale
    experiment leftover, or a renamed/removed task's orphaned file) -- the
    grading loop below globs the whole directory, so an unexpected extra would
    otherwise silently ride along into graded_results_gate1.json/summary_gate1.json
    with no signal anything was wrong."""
    expected = {
        RUNS_DIR / f"{skill}__{condition}__trial{trial}.json"
        for skill in TASKS
        for condition in ("with_skill", "without_skill")
        for trial in TRIALS
    }
    actual = set(RUNS_DIR.glob("*.json"))
    missing = sorted(p.name for p in expected if not p.exists())
    extra = sorted(p.name for p in actual - expected)
    if missing:
        print(f"ERROR: {len(missing)} expected run file(s) missing from {RUNS_DIR} -- "
              f"refusing to grade a partial batch:", file=sys.stderr)
        for name in missing:
            print(f"  missing: {name}", file=sys.stderr)
    if extra:
        print(f"ERROR: {len(extra)} unexpected run file(s) in {RUNS_DIR} -- "
              f"refusing to grade with a stale/renamed task's file present:", file=sys.stderr)
        for name in extra:
            print(f"  extra: {name}", file=sys.stderr)
    if missing or extra:
        sys.exit(1)


def main():
    check_complete()
    paths = sorted(RUNS_DIR.glob("*.json"))
    cache = load_grade_cache(DATA_DIR / "graded_results_gate1.json")
    rows = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(grade_one, p, cache): p for p in paths}
        for i, fut in enumerate(as_completed(futures), 1):
            row = fut.result()
            rows.append(row)
            print(f"[{i}/{len(paths)}] {row['skill']:32s} {row['condition']:15s} t{row['trial']} -> {row.get('meets_criteria', 'ERR')}")

    failures = sum(1 for r in rows if r.get("error"))

    # Sort before writing -- ThreadPoolExecutor's as_completed() order is
    # scheduler-dependent, so a no-op cached rerun (every row served from
    # cache, nothing actually changed) would otherwise still reorder the
    # checked-in evidence file, burying any real grade/metadata diff in a
    # large order-only diff.
    rows.sort(key=lambda r: (r["skill"], r["condition"], r["trial"]))
    (DATA_DIR / "graded_results_gate1.json").write_text(json.dumps(rows, indent=2))

    print("\n\n=== SUMMARY (skill | with_skill catch | without_skill catch | cost delta) ===")
    skills = sorted(set(r["skill"] for r in rows))
    summary_rows = []
    for skill in skills:
        line = {"skill": skill}
        for condition in ["with_skill", "without_skill"]:
            sub = [r for r in rows if r["skill"] == skill and r["condition"] == condition and not r["error"]]
            if not sub:
                line[condition] = None
                continue
            yes = sum(1 for r in sub if r["meets_criteria"] == "YES")
            n = len(sub)
            costs = [r["cost_usd"] for r in sub if r["cost_usd"] is not None]
            out_tok = [r["output_tokens"] for r in sub if r["output_tokens"] is not None]
            line[condition] = {
                "catch": f"{yes}/{n}",
                "catch_rate": yes / n if n else None,
                "mean_cost": stats.mean(costs) if costs else None,
                "mean_output_tokens": stats.mean(out_tok) if out_tok else None,
            }
        summary_rows.append(line)
        w = line.get("with_skill") or {}
        wo = line.get("without_skill") or {}
        print(f"{skill:32s} with={w.get('catch','?'):6s} without={wo.get('catch','?'):6s} "
              f"cost ${w.get('mean_cost') or 0:.3f} vs ${wo.get('mean_cost') or 0:.3f}")

    (DATA_DIR / "summary_gate1.json").write_text(json.dumps(summary_rows, indent=2))

    if failures:
        print(f"\n{failures}/{len(rows)} row(s) recorded a subject-run or grader error -- "
              f"see the excluded rows in graded_results_gate1.json", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
