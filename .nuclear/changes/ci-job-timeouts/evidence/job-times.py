"""Per-job wall time, queue wait and cap margins for the CI timeout proposal.

Reads job-times.input.csv (one row per job per run: created_at, started_at and completed_at
of the GitHub job). Prints, per workflow and job, the run time (completed minus started), the
longest wait before the job started (started minus created), and cap divided by worst run time.
The caps below are the proposal under review: policy choices, not measurements.
Usage: python3 job-times.py job-times.input.csv > job-times.txt
"""
import csv
import statistics
import sys
from datetime import datetime

CAPS_MINUTES = {
    ("ci", "validate"): 20, ("ci", "wheel-smoke"): 15, ("ci", "mcp-smoke"): 15, ("ci", "ci-gate"): 5,
    ("release", "build"): 15, ("release", "mcp-smoke"): 15, ("release", "wheel-smoke"): 15,
    ("release", "github-release"): 10, ("release", "pypi"): 10,
}
FMT = "%Y-%m-%dT%H:%M:%SZ"


def secs(a, b):
    return int((datetime.strptime(b, FMT) - datetime.strptime(a, FMT)).total_seconds())


def main(path):
    runs, waits, per = set(), {}, {}
    with open(path, newline="") as handle:
        for row in csv.DictReader(handle):
            key = (row["workflow"], row["job"])
            runs.add((row["workflow"], row["run_id"]))
            per.setdefault(key, []).append(secs(row["started_at"], row["completed_at"]))
            waits.setdefault(key, []).append(secs(row["created_at"], row["started_at"]))
    missing = set(CAPS_MINUTES) - set(per)
    if missing:
        sys.exit(f"jobs with a proposed cap but no data: {sorted(missing)}")
    total = sum(len(v) for v in per.values())
    print(f"Nuclear-grade CI and release, {len(runs)} runs, {total} job timings")
    print("run time = started_at to completed_at of the job; wait = created_at to started_at\n")
    print(f"{'workflow':8} {'job':15} {'n':>3} {'min s':>6} {'median s':>9} {'max s':>6} {'max wait s':>11} {'cap min':>8} {'cap / max':>10}")
    for key in sorted(per, key=lambda k: (k[0], -max(per[k]))):
        v = per[key]
        cap = CAPS_MINUTES[key]
        print(f"{key[0]:8} {key[1]:15} {len(v):>3} {min(v):>6} {int(statistics.median(v)):>9} {max(v):>6} "
              f"{max(waits[key]):>11} {cap:>8} {cap * 60 / max(v):>9.1f}x")
    others = [w for k, ws in waits.items() if k != ("release", "pypi") for w in ws]
    print(f"\nMedian wait for every job except release pypi: {int(statistics.median(others))} s; "
          f"largest: {max(others)} s. Release pypi wait: {waits[('release', 'pypi')][0]} s.")


if __name__ == "__main__":
    main(sys.argv[1])
