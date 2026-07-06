#!/usr/bin/env python3
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE.parent / "data" / "creating-change-records-amendment-validation"

CRITERIA = (
    "Under a corrected scope where this skill owns only the change-record packet "
    "shell (required files and how they link), NOT the mode-choice decision "
    "(Quick vs Standard) and NOT the evidence-adequacy judgment (whether tests are "
    "sufficient) -- the response passes if it explicitly names at least 4 of these "
    "6 Standard-mode files as the required packet structure: risk.md, basis.md, "
    "plan.md, trace.md, verification.md, ship.md. It does NOT need to also argue "
    "why Standard mode applies, or independently judge whether the linter tests "
    "are sufficient evidence -- only naming the correct file/link structure is "
    "being checked here."
)

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "meets_criteria": {"type": "string", "enum": ["YES", "PARTIAL", "NO"]},
        "quote": {"type": "string"},
    },
    "required": ["meets_criteria", "quote"],
})

GRADER_MODEL = "claude-sonnet-5"
# Bump whenever the grading prompt's instructional wording changes, so a
# wording-only edit invalidates the cache the same way a criteria or model
# change already does automatically (see grading_spec_hash).
PROMPT_VERSION = "v1"
GRADING_SPEC_HASH = hashlib.sha256(f"{CRITERIA}::{GRADER_MODEL}::{PROMPT_VERSION}".encode()).hexdigest()


def load_grade_cache(out_path: Path) -> dict:
    """Prior valid grades, keyed by (model, trial) -- used so a partial rerun
    (one regenerated run file) doesn't send every other, unchanged transcript
    back through the live grader. Cache validity is decided by comparing the
    run file's own content hash (stored on the cached row) against its
    current hash, NOT by file mtimes: on a fresh checkout, git's write order
    gives run files and the graded-results file mtimes that reflect checkout
    order, not actual regeneration, so an mtime-based gate can miss the cache
    for most unchanged files. A cached row also carries a _criteria_sha256
    fingerprint of the grading inputs (CRITERIA text, grader model, prompt
    version) that must still match GRADING_SPEC_HASH -- a criterion edit or
    grader-model change invalidates a row even though the transcript itself
    hasn't changed."""
    if not out_path.exists():
        return {}
    try:
        prior_rows = json.loads(out_path.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    return {(r["model"], r["trial"]): r
            for r in prior_rows if not r.get("error") and r.get("_source_sha256")}


def grade_one(path, cache: dict):
    raw = path.read_bytes()
    d = json.loads(raw)
    if d.get("type") == "error" or d.get("is_error"):
        return {"model": d["_model"], "trial": d["_trial"], "error": True}

    source_hash = hashlib.sha256(raw).hexdigest()
    cached = cache.get((d["_model"], d["_trial"]))
    if (cached is not None and cached.get("_source_sha256") == source_hash
            and cached.get("_criteria_sha256") == GRADING_SPEC_HASH):
        return cached

    text = d.get("result", "")
    prompt = (
        "You are grading a response against ONE specific structural criterion. "
        "Do not reward general correctness -- check ONLY whether the required file "
        "names appear as the named packet structure.\n\n"
        f"Criterion:\n{CRITERIA}\n\nResponse to grade:\n---\n{text}\n---\n\n"
        "Answer YES if 4+ of the 6 files are explicitly named, PARTIAL if 1-3 are "
        "named, NO if none of the 6 specific filenames appear."
    )
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--model", GRADER_MODEL,
           "--safe-mode", "--tools", "", "--no-session-persistence", "--max-budget-usd", "0.20",
           "--json-schema", SCHEMA]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        record = json.loads(proc.stdout.strip())
        verdict = json.loads(record["result"])
    except Exception as e:
        return {"model": d["_model"], "trial": d["_trial"], "error": True,
                "grader_error": True, "grader_quote": str(e)[:200]}
    return {"model": d["_model"], "trial": d["_trial"],
            "meets_criteria": verdict["meets_criteria"], "quote": verdict["quote"],
            "_source_sha256": source_hash, "_criteria_sha256": GRADING_SPEC_HASH}


MODELS = ("claude-sonnet-5", "claude-haiku-4-5")
TRIALS = (1, 2, 3)


def check_complete():
    """Refuse to grade (and overwrite the checked-in graded-results file) on a
    partial batch -- e.g. a rerun interrupted after deleting one trial -- since
    downstream reports/statistics derive their denominators from whatever this
    writes, with no way to tell a genuinely complete batch from a truncated one.
    Also refuse if the directory holds files OUTSIDE the expected set (a stale
    experiment leftover, or a renamed/removed model's orphaned file) -- the
    grading loop below globs the whole directory, so an unexpected extra would
    otherwise silently ride along into validation_graded.json with no signal
    anything was wrong."""
    runs_dir = DATA_DIR / "runs"
    expected = {
        runs_dir / f"{model}__with_skill__trial{trial}.json"
        for model in MODELS
        for trial in TRIALS
    }
    actual = set(runs_dir.glob("*.json"))
    missing = sorted(p.name for p in expected if not p.exists())
    extra = sorted(p.name for p in actual - expected)
    if missing:
        print(f"ERROR: {len(missing)} expected run file(s) missing from {runs_dir} -- "
              f"refusing to grade a partial batch:", file=sys.stderr)
        for name in missing:
            print(f"  missing: {name}", file=sys.stderr)
    if extra:
        print(f"ERROR: {len(extra)} unexpected run file(s) in {runs_dir} -- "
              f"refusing to grade with a stale/renamed model's file present:", file=sys.stderr)
        for name in extra:
            print(f"  extra: {name}", file=sys.stderr)
    if missing or extra:
        sys.exit(1)


def main():
    check_complete()
    paths = sorted((DATA_DIR / "runs").glob("*.json"))
    cache = load_grade_cache(DATA_DIR / "validation_graded.json")
    rows = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(grade_one, p, cache): p for p in paths}
        for fut in as_completed(futs):
            rows.append(fut.result())
    (DATA_DIR / "validation_graded.json").write_text(json.dumps(rows, indent=2))
    for model in ["claude-sonnet-5", "claude-haiku-4-5"]:
        sub = [r for r in rows if r["model"] == model and not r.get("error")]
        yes = sum(1 for r in sub if r["meets_criteria"] == "YES")
        partial = sum(1 for r in sub if r["meets_criteria"] == "PARTIAL")
        print(f"{model}: {yes}/{len(sub)} YES (+{partial}p)")
    for r in sorted((r for r in rows if not r.get("error")), key=lambda r: (r["model"], r["trial"])):
        print(r["model"], r["trial"], r["meets_criteria"], "|", r["quote"][:150])

    failures = sum(1 for r in rows if r.get("error"))
    if failures:
        print(f"\n{failures}/{len(rows)} row(s) recorded a subject-run or grader error -- "
              f"see the excluded rows in validation_graded.json", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
