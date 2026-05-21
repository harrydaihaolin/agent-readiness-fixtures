# agent-readiness-fixtures

**Shared test repos for the agent-readiness ecosystem.**

Tiny example repos used by every consumer's CI to validate that
behavior stays consistent across the version boundary:

- [`agent-readiness`](https://github.com/harrydaihaolin/agent-readiness) — the public scanner runs each fixture and snapshots its score.
- [`agent-readiness-rules`](https://github.com/harrydaihaolin/agent-readiness-rules) — the rules pack's CI runs the reference evaluator against each fixture.
- The closed insights engine — runs the same fixtures and asserts parity on the 5 OSS match types.

Without a shared fixture set, each consumer would build its own and
divergence would only surface in production.

## Fixture catalog

| Fixture | What it represents | Expected score band |
|---|---|---|
| `fixtures/good/` | Healthy repo: AGENTS.md, Makefile, tests, CI, .env.example, lockfile | 90–100 |
| `fixtures/noisy/` | Passes basics but trips noise checks (large generated files, ambiguous names) | 60–80 |
| `fixtures/broken/` | Multiple gaps: no README, no test command, hardcoded secret pattern | 20–40 |
| `fixtures/monorepo/` | Turbo-style monorepo for monorepo-tooling detection | 70–90 |
| `fixtures/python_thin_gitignore/` | Regression guard for the v2.4.4 `gitignore_coverage` language-aware threshold fix. Primary contract: `safety.gitignore.covers_junk` must NOT fire (score 100). | 70–90 |
| `fixtures/monorepo_pnpm/` | Workspace detection — Signal A (high). `pnpm-workspace.yaml` + two packages. | _not scored_ |
| `fixtures/monorepo_bazel/` | Workspace detection — Signal A (high), build-system branch. Bazel `WORKSPACE` + two `BUILD` files. | _not scored_ |
| `fixtures/monorepo_convention/` | Workspace detection — Signal B (medium). `apps/webapp/package.json` + `apps/worker/package.json`, no root declaration. | _not scored_ |
| `fixtures/multi_repo_workspace/` | Workspace detection — step 2 (parent dir with N child `.git/`). Three sibling repos + AGENTS.md drift warning. Requires `materialize.sh` before use. | _not scored_ |

`manifest.toml` lists the fixtures with metadata so tools can enumerate
them deterministically.

### Workspace-detection fixtures

The last four fixtures above feed `agent-readiness`'s `workspace_detect`
module (and the MCP server's `detect_workspace` / `scan_workspace`
tools). They are **not scored** by the rules engine — the scanner
either treats them as one repo (the three `monorepo_*` cases, by
design) or refuses to score them at all (the `multi_repo_workspace`
case, which exits non-zero with a `multi_repo_workspace` structured
error). See each fixture's `README.md` for the expected classifier
output and `multi_repo_workspace/AGENTS.md` for the materialise step
(git refuses to track nested `.git/` directories, so the markers ship
as sentinel files).

## Versioning

`fixture_set_version` in `manifest.toml`. Bump:

- minor on adding a new fixture or adding files to an existing one
- major on renaming/removing a fixture or changing the manifest layout

Consumers pin a range like `fixture_set>=1,<2`.

## Usage from a consumer's CI

```yaml
- uses: actions/checkout@v4
  with:
    repository: harrydaihaolin/agent-readiness-fixtures
    ref: v1.0.0
    path: fixtures
- run: agent-readiness scan fixtures/fixtures/good --json
```

Or as a git submodule when you want a reproducible local dev setup:

```bash
git submodule add https://github.com/harrydaihaolin/agent-readiness-fixtures fixtures
```

## License

MIT — fixtures are example code, free to copy or adapt.
