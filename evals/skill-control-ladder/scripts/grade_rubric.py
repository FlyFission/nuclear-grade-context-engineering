#!/usr/bin/env python3
"""Re-grade existing transcripts against the binary rubric, at higher resolution.

Grades transcripts that already exist, so this buys resolution for the price of
grading alone -- no new subject-model calls.

Each transcript gets ONE grading call that returns a yes/no verdict per check,
rather than one call per check. That is deliberate: per-check calls would cost
5-6x more and, more importantly, would let the grader contradict itself across
checks it should be reasoning about together (a response either mentions
idempotency keys or it does not, and both the check that asks about it and the
one that asks why should see the same reading).

Blinding is unchanged: the grader sees the response text and the checks. It is
never told the arm, the skill, or that a comparison is running.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from ladder_common import (
    ARMS,
    GRADER_MODEL,
    LADDER_DIR,
    MAX_WORKERS,
    POOL,
    TASKS,
    TRIALS,
    response_text,
    run_path,
)

RUBRICS_PATH = LADDER_DIR / "data" / f"rubrics-{POOL}.json"
OUT_PATH = LADDER_DIR / "data" / f"rubric-graded-{POOL}.json"
PROMPT_VERSION = "r1"

PROMPT = (
    "You are grading one free-text response against a list of independent checks.\n\n"
    "For EACH check, answer whether the response explicitly satisfies it. Answer "
    "true ONLY if it is clearly and explicitly satisfied; answer false if it is "
    "absent, merely hinted at, or materially incomplete. Do not reward general "
    "competence, tone, structure, or length. Judge each check on its own.\n\n"
    "Checks:\n{checks}\n\n"
    "Response to grade:\n---\n{text}\n---"
)


def build_schema(ids: list[str]) -> str:
    return json.dumps({
        "type": "object",
        "properties": {
            "results": {
                "type": "array",
                "minItems": len(ids),
                "maxItems": len(ids),
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "enum": ids},
                        "met": {"type": "boolean"},
                        "quote": {"type": "string"},
                    },
                    "required": ["id", "met", "quote"],
                },
            }
        },
        "required": ["results"],
    })


def grade_one(checks: list[dict], text: str, model: str) -> dict[str, bool] | None:
    ids = [c["id"] for c in checks]
    listing = "\n".join(f"- {c['id']}: {c['check']}" for c in checks)
    cmd = [
        "claude", "-p", PROMPT.format(checks=listing, text=text),
        "--output-format", "json",
        "--model", model,
        "--safe-mode",
        "--tools", "",
        "--no-session-persistence",
        "--max-budget-usd", "0.20",
        "--json-schema", build_schema(ids),
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        rec = json.loads(proc.stdout.strip())
        if rec.get("is_error"):
            return None
        results = json.loads(rec["result"])["results"]
        got = {r["id"]: bool(r["met"]) for r in results}
        # A short return would silently deflate the score, so an incomplete
        # result is treated as a failed grading rather than a partial one.
        return got if set(got) == set(ids) else None
    except Exception:  # noqa: BLE001 -- None signals "retry this cell"
        return None


def rubric_hash(checks: list[dict], model: str) -> str:
    return hashlib.sha256(
        (json.dumps(checks, sort_keys=True) + f"::{model}::{PROMPT_VERSION}").encode()
    ).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=GRADER_MODEL,
                    help="grader model; vary it to measure cross-model agreement")
    ap.add_argument("--out", default=None, help="override output path")
    # Pools need not run every arm (the negative pool omits C2), and grading
    # must not demand transcripts a pool deliberately never produced.
    ap.add_argument("--arms", nargs="*", default=list(ARMS), choices=list(ARMS))
    args = ap.parse_args()

    if not RUBRICS_PATH.exists():
        print(f"No rubrics for pool {POOL!r}; run author_rubrics.py first.", file=sys.stderr)
        return 2
    rubrics = json.loads(RUBRICS_PATH.read_text())
    out_path = LADDER_DIR / "data" / args.out if args.out else OUT_PATH

    # Successful rows are also persisted to a sidecar so that a handful of
    # transient grader failures does not discard an otherwise complete batch.
    # Refusing to publish a partial authoritative file is correct -- downstream
    # statistics take their denominator from it -- but throwing away 396 good
    # gradings because 9 calls timed out is not, and on a 405-cell batch it makes
    # the retry loop nearly impossible to converge.
    partial_path = out_path.with_suffix(".partial.json")
    prior: dict[tuple[str, str, int], dict] = {}
    for src in (partial_path, out_path):
        if not src.exists():
            continue
        try:
            for r in json.loads(src.read_text()):
                prior[(r["skill"], r["arm"], r["trial"])] = r
        except (json.JSONDecodeError, OSError):
            continue

    rows, jobs, incomplete = [], [], []
    for skill in sorted(TASKS):
        if skill not in rubrics:
            incomplete.append(f"{skill}: no rubric")
            continue
        checks = rubrics[skill]["checks"]
        rh = rubric_hash(checks, args.model)
        for arm in args.arms:
            for trial in range(1, TRIALS + 1):
                p = run_path(skill, arm, trial)
                if not p.exists():
                    incomplete.append(f"{skill}/{arm}/t{trial}: missing run")
                    continue
                rec = json.loads(p.read_text())
                if rec.get("type") == "error" or rec.get("is_error"):
                    incomplete.append(f"{skill}/{arm}/t{trial}: run errored")
                    continue
                text = response_text(rec)
                sh = hashlib.sha256(text.encode()).hexdigest()
                hit = prior.get((skill, arm, trial))
                if hit and hit.get("_source_sha256") == sh and hit.get("_rubric_sha256") == rh:
                    rows.append(hit)
                else:
                    jobs.append((skill, arm, trial, checks, text, sh, rh, rec))

    if incomplete:
        print(f"Refusing to grade: {len(incomplete)} incomplete cell(s).", file=sys.stderr)
        for line in incomplete[:20]:
            print(f"  {line}", file=sys.stderr)
        return 2

    print(f"pool={POOL} model={args.model} cached={len(rows)} to_grade={len(jobs)}",
          file=sys.stderr)
    failed = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(grade_one, j[3], j[4], args.model): j for j in jobs}
        done = 0
        for fut in as_completed(futures):
            skill, arm, trial, checks, _text, sh, rh, rec = futures[fut]
            got = fut.result()
            done += 1
            if got is None:
                failed += 1
                print(f"[{done}/{len(jobs)}] {skill}/{arm}/t{trial} -> FAILED",
                      file=sys.stderr)
                continue
            core = [c["id"] for c in checks if c["weight"] == "core"]
            rows.append({
                "skill": skill, "arm": arm, "trial": trial,
                "checks_met": sum(1 for v in got.values() if v),
                "checks_total": len(checks),
                "score": sum(1 for v in got.values() if v) / len(checks),
                "core_met": sum(1 for i in core if got[i]),
                "core_total": len(core),
                "core_score": (sum(1 for i in core if got[i]) / len(core)) if core else None,
                "per_check": got,
                "cost_usd": rec.get("total_cost_usd"),
                "output_tokens": (rec.get("usage") or {}).get("output_tokens"),
                "_source_sha256": sh,
                "_rubric_sha256": rh,
            })
            print(f"[{done}/{len(jobs)}] {skill}/{arm}/t{trial} -> "
                  f"{rows[-1]['checks_met']}/{len(checks)}", file=sys.stderr)

    rows.sort(key=lambda r: (r["skill"], r["arm"], r["trial"]))
    if failed:
        partial_path.write_text(json.dumps(rows, indent=2) + "\n")
        print(f"{failed} grading call(s) failed; kept {len(rows)} good row(s) in "
              f"{partial_path.name} and did NOT write the authoritative file. "
              f"Re-run to grade only the {failed} missing cell(s).", file=sys.stderr)
        return 1

    out_path.write_text(json.dumps(rows, indent=2) + "\n")
    partial_path.unlink(missing_ok=True)
    print(f"Wrote {len(rows)} rows to {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
