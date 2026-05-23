"""Repo-local wrapper for the Nuclear-grade CLI."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from nuclear_grade.cli import *  # noqa: F403
from nuclear_grade.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
