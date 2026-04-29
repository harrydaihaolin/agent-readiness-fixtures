"""Tiny CLI entry point so manifest.detected and entry_points.detected fire."""

from __future__ import annotations

import os
import sys


def main(argv: list[str] | None = None) -> int:
    greeting = os.environ.get("GREETING", "Hello")
    print(f"{greeting}, world.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
