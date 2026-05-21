#!/usr/bin/env sh
# Promote each child dir containing MARKER_GIT_REPO into a real
# (empty) git repo, so the workspace-detect classifier sees this
# fixture as a multi-repo workspace.
#
# Git refuses to track files named `.git`, so we can't check the
# nested `.git/` directories into agent-readiness-fixtures directly.
# Hence this one-liner materialiser.
#
# Idempotent: re-running is a no-op once the .git directories exist.

set -eu

cd "$(dirname "$0")"

count=0
for marker in */MARKER_GIT_REPO; do
  [ -f "$marker" ] || continue
  dir="$(dirname "$marker")"
  if [ ! -d "$dir/.git" ]; then
    mkdir -p "$dir/.git"
    count=$((count + 1))
  fi
done
echo "materialised $count repos"
