#!/usr/bin/env python3
"""Isolate whether creating-change-records' low scores (both rounds) are a
compound-criterion artifact -- like proving-claims turned out to be -- or a
real gap. Re-grade EXISTING round-1 and Gate-1 transcripts against a narrower
structural criterion: does it name the Standard-mode artifact set / use the
status-label vocabulary, separate from the full 5-part compound judgment."""
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1]
ROUND1_RUNS = DATA_DIR / "all-skills-pilot" / "runs"
GATE1_RUNS = DATA_DIR / "gate1-hard-case-pilot" / "runs"
OUT = Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True, parents=True)

CRITERIA = (
    "The response explicitly names at least 4 of these 6 Standard-mode change-record "
    "files by name (risk.md, basis.md, plan.md, trace.md, verification.md, ship.md) "
    "OR explicitly uses at least 2 of these specific status-label words for an evidence "
    "claim (pass, fail, gap, deferred, not applicable, planned). A well-reasoned answer "
    "that never uses this repo-specific vocabulary or file set fails this criterion, even "
    "if its judgment about risk/evidence is otherwise correct."
)

SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "meets_criteria": {"type": "string", "enum": ["YES", "PARTIAL", "NO"]},
        "quote": {"type": "string"},
    },
    "required": ["meets_criteria", "quote"],
})


GRADER_MODEL = "claude-haiku-4-5"
# Bump whenever the grading prompt's instructional wording changes, so a
# wording-only edit invalidates the cache the same way a criteria or model
# change already does automatically.
PROMPT_VERSION = "v1"
GRADING_SPEC_HASH = hashlib.sha256(f"{CRITERIA}::{GRADER_MODEL}::{PROMPT_VERSION}".encode()).hexdigest()


def load_grade_cache(out_path: Path) -> dict:
    """Prior valid grades, keyed by (round, condition, trial) -- used so a
    partial rerun (one regenerated run file) doesn't send every other,
    unchanged transcript back through the live grader. Cache validity is
    decided by comparing the run file's own content hash (stored on the
    cached row) against its current hash, NOT by file mtimes: on a fresh
    checkout, git's write order gives run files and the graded-results file
    mtimes that reflect checkout order, not actual regeneration, so an
    mtime-based gate can miss the cache for most unchanged files. A cached
    row also carries a _criteria_sha256 fingerprint of the grading inputs
    (CRITERIA text, grader model, prompt version) that must still match
    GRADING_SPEC_HASH -- a criterion edit or grader-model change invalidates
    a row even though the transcript itself hasn't changed."""
    if not out_path.exists():
        return {}
    try:
        prior_rows = json.loads(out_path.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    return {(r["round"], r["condition"], r["trial"]): r
            for r in prior_rows if not r.get("error") and r.get("_source_sha256")}


def grade_one(path, cache: dict, key):
    raw = path.read_bytes()
    d = json.loads(raw)
    if d.get("type") == "error" or d.get("is_error"):
        return {"error": True}

    text = d.get("result", "")
    # Hash only the substantive transcript text, not the whole file's raw
    # bytes -- hashing the full file means any unrelated metadata field added
    # to the run record later (e.g. the harness-settings fingerprint added in
    # round 33) invalidates every cached grade even though the graded content
    # never changed.
    source_hash = hashlib.sha256(text.encode()).hexdigest()
    cached = cache.get(key)
    if (cached is not None and cached.get("_source_sha256") == source_hash
            and cached.get("_criteria_sha256") == GRADING_SPEC_HASH):
        return cached
    prompt = (
        "You are grading a response against ONE specific vocabulary/structure criterion. "
        "Do not reward general correctness -- check ONLY this.\n\n"
        f"Criterion:\n{CRITERIA}\n\nResponse to grade:\n---\n{text}\n---\n\n"
        "Answer YES only if clearly met, PARTIAL if it names 1-3 files or 1 status word, "
        "NO if neither the files nor the status-label vocabulary appear at all."
    )
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--model", GRADER_MODEL,
           "--safe-mode", "--tools", "", "--no-session-persistence", "--max-budget-usd", "0.20",
           "--json-schema", SCHEMA]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        record = json.loads(proc.stdout.strip())
        verdict = json.loads(record["result"])
    except Exception as e:
        return {"error": True, "grader_error": True, "grader_quote": str(e)[:200]}
    return {"round": d.get("_round", "?"), "condition": d["_condition"], "trial": d["_trial"],
            "meets_criteria": verdict["meets_criteria"], "quote": verdict["quote"],
            "_source_sha256": source_hash, "_criteria_sha256": GRADING_SPEC_HASH}


ROUND1_TRIALS = (1, 2, 3)
GATE1_TRIALS = (1, 2, 3, 4, 5)


def check_complete():
    """Refuse to grade (and overwrite the checked-in graded-results file) on a
    partial batch -- e.g. a rerun interrupted after deleting one trial -- since
    downstream reports/statistics derive their denominators from whatever this
    writes, with no way to tell a genuinely complete batch from a truncated one.
    Also refuse if the same creating-change-records__*.json globs this
    script's own main() uses (one per runs directory) turn up files OUTSIDE
    the expected set (a stray extra trial) -- both ROUND1_RUNS and GATE1_RUNS
    hold every skill's files, so "actual" is scoped to the identical glob
    pattern main() grades in each directory, not the whole directory."""
    expected = {
        ROUND1_RUNS / f"creating-change-records__{condition}__trial{trial}.json"
        for condition in ("with_skill", "without_skill")
        for trial in ROUND1_TRIALS
    } | {
        GATE1_RUNS / f"creating-change-records__{condition}__trial{trial}.json"
        for condition in ("with_skill", "without_skill")
        for trial in GATE1_TRIALS
    }
    actual = (set(ROUND1_RUNS.glob("creating-change-records__*.json"))
              | set(GATE1_RUNS.glob("creating-change-records__*.json")))
    missing = sorted(str(p) for p in expected if not p.exists())
    extra = sorted(str(p) for p in actual - expected)
    if missing:
        print(f"ERROR: {len(missing)} expected run file(s) missing -- "
              f"refusing to grade a partial batch:", file=sys.stderr)
        for name in missing:
            print(f"  missing: {name}", file=sys.stderr)
    if extra:
        print(f"ERROR: {len(extra)} unexpected creating-change-records run file(s) -- "
              f"refusing to grade with an extra trial present:", file=sys.stderr)
        for name in extra:
            print(f"  extra: {name}", file=sys.stderr)
    if missing or extra:
        sys.exit(1)


def main():
    check_complete()
    round1_paths = [(p, "round1") for p in sorted(ROUND1_RUNS.glob("creating-change-records__*.json"))]
    gate1_paths = [(p, "gate1") for p in sorted(GATE1_RUNS.glob("creating-change-records__*.json"))]
    all_paths = round1_paths + gate1_paths

    cache = load_grade_cache(OUT / "ccr_structure_graded.json")
    rows = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {}
        for p, rnd in all_paths:
            d = json.loads(p.read_text())
            key = (rnd, d["_condition"], d["_trial"])
            futs[ex.submit(grade_one, p, cache, key)] = (p, rnd, d["_condition"], d["_trial"])
        for fut in as_completed(futs):
            p, rnd, cond, trial = futs[fut]
            v = fut.result()
            if v.get("error"):
                rows.append({"round": rnd, "condition": cond, "trial": trial, "error": True})
                continue
            rows.append({"round": rnd, "condition": cond, "trial": trial,
                         "meets_criteria": v["meets_criteria"], "quote": v["quote"],
                         "_source_sha256": v["_source_sha256"],
                         "_criteria_sha256": v["_criteria_sha256"]})

    (OUT / "ccr_structure_graded.json").write_text(json.dumps(rows, indent=2))
    for rnd in ["round1", "gate1"]:
        for cond in ["with_skill", "without_skill"]:
            sub = [r for r in rows if r["round"] == rnd and r["condition"] == cond and not r.get("error")]
            yes = sum(1 for r in sub if r["meets_criteria"] == "YES")
            partial = sum(1 for r in sub if r["meets_criteria"] == "PARTIAL")
            print(f"{rnd} {cond}: {yes}/{len(sub)} YES (+{partial} partial)")

    failures = sum(1 for r in rows if r.get("error"))
    if failures:
        print(f"\n{failures}/{len(rows)} row(s) recorded a subject-run or grader error -- "
              f"see the excluded rows in ccr_structure_graded.json", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
