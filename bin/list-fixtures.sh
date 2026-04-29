#!/usr/bin/env bash
# Print the fixture set as JSON. Mirrors `tools/list_fixtures.py` but is
# discoverable as an entry point under `bin/` for contributors and for
# the agent-readiness scanner.
#
# Usage: bin/list-fixtures.sh

set -euo pipefail

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 required" >&2
  exit 2
fi

python3 tools/list_fixtures.py
