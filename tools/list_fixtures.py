#!/usr/bin/env python3
"""Print fixture metadata as JSON. Used by consumers' CI to enumerate fixtures.

Reads `manifest.toml` and emits one JSON object per fixture, suitable for
piping into `jq` or for use as a GitHub Actions matrix.
"""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    manifest = tomllib.loads((ROOT / "manifest.toml").read_text())
    fixtures = manifest.get("fixtures", [])
    out = {
        "fixture_set_version": manifest["fixture_set_version"],
        "pack_version": manifest["pack_version"],
        "fixtures": fixtures,
    }
    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
