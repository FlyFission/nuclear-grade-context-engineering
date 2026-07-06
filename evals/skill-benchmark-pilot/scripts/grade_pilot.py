#!/usr/bin/env python3
"""Blind-grade each run's review text against the pre-registered answer key.

Grading is done by a separate, cheap model (Haiku) that never sees which
condition (with_skill / without_skill) produced the text, forced into a
strict JSON schema so the verdict is mechanical, not a free-form judgment.
"""
import hashlib
import json
import re
import statistics as stats
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE.parent / "data" / "reviewing-code-quality-pilot"
RUNS_DIR = DATA_DIR / "runs"
ANSWER_KEYS = json.loads((DATA_DIR / "answer_keys.json").read_text())
GRADER_MODEL = "claude-haiku-4-5-20251001"
# Bump whenever the grading prompt's instructional wording changes, so a
# wording-only edit invalidates the cache the same way a criteria or model
# change already does automatically (see grading_spec_hash).
PROMPT_VERSION = "v1"


def grading_spec_hash(task: str) -> str:
    """Fingerprint of everything besides the transcript that can change a
    verdict: the task's own pass_criteria text, the grader model, and the
    prompt template version. A cached row is only reused if this ALSO
    matches -- an answer-key edit or grader-model change must force a
    re-grade even though the transcript itself hasn't changed."""
    criteria = ANSWER_KEYS[task]["pass_criteria"]
    return hashlib.sha256(f"{criteria}::{GRADER_MODEL}::{PROMPT_VERSION}".encode()).hexdigest()

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "meets_criteria": {"type": "string", "enum": ["YES", "PARTIAL", "NO"]},
        "quote": {"type": "string"},
    },
    "required": ["meets_criteria", "quote"],
})

VERDICT_RE = re.compile(r"\b(NOT VERIFIED|INCONCLUSIVE|VERIFIED)\b")


def grade_review(task: str, review_text: str) -> dict:
    criteria = ANSWER_KEYS[task]["pass_criteria"]
    prompt = (
        "You are grading a code review against ONE specific pass criterion. "
        "Do not reward general competence or thoroughness — check ONLY whether "
        "this exact criterion is explicitly satisfied.\n\n"
        f"Pass criterion:\n{criteria}\n\n"
        f"Code review to grade:\n---\n{review_text}\n---\n\n"
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
        verdict = json.loads(record["result"])
        return verdict
    except Exception as e:
        return {"meets_criteria": "ERROR", "quote": str(e)[:300]}


def load_grade_cache(out_path: Path) -> dict:
    """Prior valid grades, keyed by (task, condition, trial) -- used so a
    partial rerun (one regenerated run file) doesn't send every other,
    unchanged transcript back through the live grader. Cache validity is
    decided by comparing the run file's own content hash (stored on the
    cached row) against its current hash, NOT by file mtimes: on a fresh
    checkout, git's write order gives run files and the graded-results file
    mtimes that reflect checkout order, not actual regeneration, so an
    mtime-based gate can miss the cache for most unchanged files. A cached
    row also carries a _criteria_sha256 fingerprint of the grading inputs
    (pass_criteria text, grader model, prompt version) that must still match
    the live inputs -- an answer-key edit or grader-model change invalidates
    a row even though the transcript itself hasn't changed."""
    if not out_path.exists():
        return {}
    try:
        prior_rows = json.loads(out_path.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    return {(r["task"], r["condition"], r["trial"]): r
            for r in prior_rows if r.get("error") is False and r.get("_source_sha256")}


TRIALS = (1, 2, 3)


def check_complete():
    """Refuse to grade (and overwrite the checked-in graded-results file) on a
    partial batch -- e.g. a rerun interrupted after deleting one trial -- since
    downstream reports/statistics derive their denominators from whatever this
    writes, with no way to tell a genuinely complete batch from a truncated one.
    Also refuse if the directory holds files OUTSIDE the expected set (a stale
    experiment leftover, or a renamed/removed task's orphaned file) -- the
    grading loop below globs the whole directory, so an unexpected extra would
    otherwise silently ride along into graded_results.json with no signal
    anything was wrong."""
    expected = {
        RUNS_DIR / f"{task}__{condition}__trial{trial}.json"
        for task in ANSWER_KEYS
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
    cache = load_grade_cache(DATA_DIR / "graded_results.json")
    rows = []
    for path in sorted(RUNS_DIR.glob("*.json")):
        raw = path.read_bytes()
        d = json.loads(raw)
        task = d.get("_task")
        condition = d.get("_condition")
        trial = d.get("_trial")
        if d.get("type") == "error" or d.get("is_error"):
            rows.append({"task": task, "condition": condition, "trial": trial, "error": True})
            continue

        source_hash = hashlib.sha256(raw).hexdigest()
        spec_hash = grading_spec_hash(task)
        cached = cache.get((task, condition, trial))
        if (cached is not None and cached.get("_source_sha256") == source_hash
                and cached.get("_criteria_sha256") == spec_hash):
            rows.append(cached)
            continue

        result_text = d.get("result", "")
        usage = d.get("usage", {})
        grade = grade_review(task, result_text)
        if grade.get("meets_criteria") == "ERROR":
            rows.append({"task": task, "condition": condition, "trial": trial, "error": True,
                         "grader_error": True, "grader_quote": grade.get("quote")})
            continue
        verdict_format_present = bool(VERDICT_RE.search(result_text))

        rows.append({
            "task": task,
            "condition": condition,
            "trial": trial,
            "error": False,
            "meets_criteria": grade.get("meets_criteria"),
            "grader_quote": grade.get("quote"),
            "verdict_format_present": verdict_format_present,
            "cost_usd": d.get("total_cost_usd"),
            "input_tokens": usage.get("input_tokens"),
            "output_tokens": usage.get("output_tokens"),
            "cache_read_tokens": usage.get("cache_read_input_tokens"),
            "cache_creation_tokens": usage.get("cache_creation_input_tokens"),
            "num_turns": d.get("num_turns"),
            "duration_ms": d.get("duration_ms"),
            "_source_sha256": source_hash,
            "_criteria_sha256": spec_hash,
        })
        print(f"{task:28s} {condition:15s} trial{trial}  meets_criteria={grade.get('meets_criteria')}  cost=${d.get('total_cost_usd'):.4f}")

    failures = sum(1 for r in rows if r.get("error"))

    (DATA_DIR / "graded_results.json").write_text(json.dumps(rows, indent=2))

    print("\n\n=== SUMMARY ===")
    tasks = sorted(set(r["task"] for r in rows))
    for task in tasks:
        print(f"\n--- {task} ---")
        for condition in ["with_skill", "without_skill"]:
            sub = [r for r in rows if r["task"] == task and r["condition"] == condition and not r["error"]]
            if not sub:
                print(f"  {condition}: no successful runs")
                continue
            catch = sum(1 for r in sub if r["meets_criteria"] == "YES")
            partial = sum(1 for r in sub if r["meets_criteria"] == "PARTIAL")
            n = len(sub)
            verdict_fmt = sum(1 for r in sub if r["verdict_format_present"])
            costs = [r["cost_usd"] for r in sub if r["cost_usd"] is not None]
            out_tok = [r["output_tokens"] for r in sub if r["output_tokens"] is not None]
            in_tok = [(r["input_tokens"] or 0) + (r["cache_creation_tokens"] or 0) + (r["cache_read_tokens"] or 0) for r in sub]
            turns = [r["num_turns"] for r in sub if r["num_turns"] is not None]
            dur = [r["duration_ms"] for r in sub if r["duration_ms"] is not None]
            print(f"  {condition}: caught {catch}/{n} (+{partial} partial), verdict-format {verdict_fmt}/{n}")
            print(f"    cost: mean=${stats.mean(costs):.4f} (n={n})  | output_tok: mean={stats.mean(out_tok):.0f} | input+cache_tok: mean={stats.mean(in_tok):.0f} | turns: mean={stats.mean(turns):.1f} | duration_ms: mean={stats.mean(dur):.0f}")

    if failures:
        print(f"\n{failures}/{len(rows)} row(s) recorded a subject-run or grader error -- "
              f"see the excluded rows in graded_results.json", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
