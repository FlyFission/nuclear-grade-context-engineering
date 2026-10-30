#!/usr/bin/env python3
"""Backtest a consequence policy against merged history before the gate enforces it.

For each first-parent commit, classify the commit's own diff (parent -> commit) with the
policy and compare the required mode to (a) the modes declared by change records the
commit added and (b) an owner-labelled expected mode, when a labels file is given.

    python tools/ng_policy_backtest.py --policy .nuclear/consequence-policy.json --last 49
    python tools/ng_policy_backtest.py --policy <file> --labels labels.csv   # commit,expected_mode

Ground truth is the owner's labels, not "few failures": legacy records predate custody
and authority sections, so validity is not compared, only modes. Read-only.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nuclear_grade import consequence  # noqa: E402


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True).stdout


def declared_modes(repo: Path, commit: str, slugs: set[str], root: str) -> list[str]:
    modes = []
    for slug in sorted(slugs):
        result = subprocess.run(["git", "-C", str(repo), "show", f"{commit}:{root}/{slug}/risk.md"],
                                capture_output=True, text=True)
        match = consequence.MODE_DECLARATION_PATTERN.search(result.stdout) if result.returncode == 0 else None
        modes.append(match.group(1).lower() if match else "unspecified")
    return modes


def backtest(repo: Path, policy: consequence.Policy, commits: list[str], labels: dict[str, str]) -> list[dict]:
    rows = []
    for commit in commits:
        parents = _git(repo, "rev-list", "--parents", "-n", "1", commit).split()[1:]
        if not parents:
            continue
        _, _, results, new_slugs, _ = consequence.classify(repo, parents[0], commit, policy)
        required = consequence._max_mode(*(entry.required for entry in results.values()))
        fired = sorted({rule for entry in results.values() for rule in entry.rules})
        declared = declared_modes(repo, commit, new_slugs, policy.records_root)
        best = max((consequence.DECLARED_RANK.get(mode, "none") for mode in declared),
                   key=lambda mode: consequence.RANK[mode], default="none")
        label = next((labels[key] for key in labels if commit.startswith(key)), "")
        rows.append({
            "commit": commit[:7],
            "subject": _git(repo, "log", "-1", "--format=%s", commit).strip()[:60],
            "required": required,
            "rules": fired,
            "declared": declared,
            "declared_covers": consequence.RANK[best] >= consequence.RANK[
                "standard" if required == "standard+authority" else required],
            "label": label,
            "label_match": (label == required) if label else None,
        })
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--policy", type=Path, required=True, help="Policy JSON file to test.")
    parser.add_argument("--last", type=int, default=49, help="Number of first-parent commits from HEAD.")
    parser.add_argument("--labels", type=Path, default=None, help="CSV of commit,expected_mode (owner labels).")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    repo = args.repo.resolve()
    policy = consequence.load_policy(repo, consequence.WORKTREE, args.policy)
    commits = _git(repo, "rev-list", "--first-parent", f"-n{args.last}", "HEAD").split()
    labels: dict[str, str] = {}
    if args.labels is not None:
        with args.labels.open(encoding="utf-8") as handle:
            for row in csv.reader(handle):
                if len(row) >= 2 and row[1].strip() in consequence.RANK:
                    labels[row[0].strip()] = row[1].strip()
    rows = backtest(repo, policy, commits, labels)
    if args.json:
        print(json.dumps(rows, indent=2))
        return 0
    print("| Commit | Required | Rules | Declared | Declared covers | Label | Subject |")
    print("|---|---|---|---|---|---|---|")
    for row in rows:
        print(f"| {row['commit']} | {row['required']} | {', '.join(row['rules']) or '-'} | "
              f"{', '.join(row['declared']) or '-'} | {'yes' if row['declared_covers'] else 'no'} | "
              f"{row['label'] or '-'} | {row['subject']} |")
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["required"]] = counts.get(row["required"], 0) + 1
    print(f"\nrequired-mode counts: {counts}")
    labelled = [row for row in rows if row["label"]]
    if labelled:
        agree = sum(bool(row["label_match"]) for row in labelled)
        print(f"agreement with owner labels: {agree}/{len(labelled)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
