#!/usr/bin/env python3
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE.parent / "data" / "briefing-an-agent-amendment-validation"
TASKS = json.loads((DATA_DIR / "task.json").read_text())
SCHEMA = json.dumps({"type":"object","properties":{"meets_criteria":{"type":"string","enum":["YES","PARTIAL","NO"]},"quote":{"type":"string"}},"required":["meets_criteria","quote"]})
GRADER_MODEL = "claude-haiku-4-5"
# Bump whenever the grading prompt's instructional wording changes, so a
# wording-only edit invalidates the cache the same way a criteria or model
# change already does automatically (see grading_spec_hash).
PROMPT_VERSION = "v1"


def grading_spec_hash(task_key: str) -> str:
    """Fingerprint of everything besides the transcript that can change a
    verdict: the task's own pass_criteria text, the grader model, and the
    prompt template version. A cached row is only reused if this ALSO
    matches -- a criteria edit or grader-model change must force a re-grade
    even though the transcript itself hasn't changed."""
    criteria = TASKS[task_key]["pass_criteria"]
    return hashlib.sha256(f"{criteria}::{GRADER_MODEL}::{PROMPT_VERSION}".encode()).hexdigest()


def load_grade_cache(out_path: Path) -> dict:
    """Prior valid grades, keyed by (condition, trial) -- used so a partial
    rerun (one regenerated run file) doesn't send every other, unchanged
    transcript back through the live grader. Cache validity is decided by
    comparing the run file's own content hash (stored on the cached row)
    against its current hash, NOT by file mtimes: on a fresh checkout, git's
    write order gives run files and the graded-results file mtimes that
    reflect checkout order, not actual regeneration, so an mtime-based gate
    can miss the cache for most unchanged files. A cached row also carries a
    _criteria_sha256 fingerprint of the grading inputs (pass_criteria text,
    grader model, prompt version) that must still match the live inputs --
    a criteria edit or grader-model change invalidates a row even though
    the transcript itself hasn't changed."""
    if not out_path.exists():
        return {}
    try:
        prior_rows = json.loads(out_path.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    return {(r["condition"], r["trial"]): r
            for r in prior_rows if not r.get("error") and r.get("_source_sha256")}


def grade_one(path, cache: dict):
    raw = path.read_bytes()
    d = json.loads(raw)
    task_key = d["_task"]
    if d.get("type") == "error" or d.get("is_error"):
        return {"condition": d["_condition"], "trial": d["_trial"], "error": True}

    source_hash = hashlib.sha256(raw).hexdigest()
    spec_hash = grading_spec_hash(task_key)
    cached = cache.get((d["_condition"], d["_trial"]))
    if (cached is not None and cached.get("_source_sha256") == source_hash
            and cached.get("_criteria_sha256") == spec_hash):
        return cached

    criteria = TASKS[task_key]["pass_criteria"]
    prompt = (f"You are grading a response against ONE specific pass criterion. Do not reward general "
              f"competence or tone -- check ONLY whether this exact criterion is explicitly satisfied.\n\n"
              f"Pass criterion:\n{criteria}\n\nResponse to grade:\n---\n{d.get('result','')}\n---\n\n"
              f"Answer YES only if clearly and explicitly met, PARTIAL if hinted at but incomplete, NO if absent.")
    cmd = ["claude","-p",prompt,"--output-format","json","--model",GRADER_MODEL,
           "--safe-mode","--tools","","--no-session-persistence","--max-budget-usd","0.20","--json-schema",SCHEMA]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        record = json.loads(proc.stdout.strip())
        verdict = json.loads(record["result"])
    except Exception as e:
        return {"condition": d["_condition"], "trial": d["_trial"], "error": True,
                "grader_error": True, "grader_quote": str(e)[:200]}
    return {"condition": d["_condition"], "trial": d["_trial"], "meets_criteria": verdict["meets_criteria"],
            "quote": verdict["quote"], "_source_sha256": source_hash, "_criteria_sha256": spec_hash}

def main():
    paths = sorted((DATA_DIR/"runs").glob("*.json"))
    cache = load_grade_cache(DATA_DIR / "graded.json")
    rows = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(grade_one, p, cache): p for p in paths}
        for fut in as_completed(futs):
            rows.append(fut.result())
    (DATA_DIR/"graded.json").write_text(json.dumps(rows, indent=2))
    for cond in ["with_skill","without_skill"]:
        sub = [r for r in rows if r["condition"]==cond and not r.get("error")]
        yes = sum(1 for r in sub if r["meets_criteria"]=="YES")
        partial = sum(1 for r in sub if r["meets_criteria"]=="PARTIAL")
        print(f"{cond}: {yes}/{len(sub)} YES (+{partial} partial)")
    for r in sorted((r for r in rows if not r.get("error")), key=lambda r:(r["condition"],r["trial"])):
        print(r["condition"], r["trial"], r["meets_criteria"], "|", r["quote"][:150])

    failures = sum(1 for r in rows if r.get("error"))
    if failures:
        print(f"\n{failures}/{len(rows)} row(s) recorded a subject-run or grader error -- "
              f"see the excluded rows in graded.json", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
