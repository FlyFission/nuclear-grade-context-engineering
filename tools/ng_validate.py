"""Repo-local wrapper for the Nuclear-grade packet validator."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from nuclear_grade.ng_validate import (
    ValidationResult,
    check_internal_links,
    detect_packet_mode,
    main,
    validate_packet,
)

__all__ = [
    "ValidationResult",
    "check_internal_links",
    "detect_packet_mode",
    "main",
    "validate_packet",
]


if __name__ == "__main__":
    raise SystemExit(main())
