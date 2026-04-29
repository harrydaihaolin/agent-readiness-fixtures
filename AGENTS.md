# Agent guide

Conventions for AI coding agents working in this repository.

## Canonical commands

- List fixtures: `python tools/list_fixtures.py`
- Self-scan:     `agent-readiness scan . --fail-below 95`

This repo is data only — fixtures + a tiny enumeration helper. There is
nothing to install, no tests beyond the self-scan.

## Adding a fixture

1. Create a new directory under `fixtures/<name>/`.
2. Add a stanza to `manifest.toml` with `name`, `path`, `expected_score_min/max`, `description`.
3. Bump `pack_version` minor (e.g., `1.0.0 → 1.1.0`); leave `fixture_set_version` alone unless you change the manifest layout.
4. Open a PR.

## Do-not-touch

- `manifest.toml` `fixture_set_version` integer — coordinated bump only;
  every consumer pins on this and a major change breaks them all.

## Style

- Each fixture stays small (~10 files). The point is to be readable in
  one sitting; large fixtures defeat the purpose.
- No real secrets, no real third-party tokens. The `broken/` fixture
  uses dummy patterns like `AKIAIOSFODNN7EXAMPLE`.
