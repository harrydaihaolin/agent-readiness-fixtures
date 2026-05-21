# Multi-repo workspace (fixture)

A parent directory containing three sibling repos plus a root
`AGENTS.md` that lists a fourth — the fourth doesn't exist on disk
to exercise the drift-warning code path.

## Repos

| Repo | One-line | Lang/stack |
|---|---|---|
| [`alpha-svc`](./alpha-svc) | Alpha HTTP service. | Python |
| [`beta-lib`](./beta-lib) | Beta shared library. | Rust |
| [`gamma-cli`](./gamma-cli) | Gamma command-line client. | Go |
| [`delta-not-checked-out`](./delta-not-checked-out) | Deliberately missing from disk. | TypeScript |

## How to use

The three repos ship as plain directories with a `MARKER_GIT_REPO`
sentinel inside each one. Promote them to real (empty) git repos
before running workspace-detect tests:

```sh
./materialize.sh
```

After materialise the detector sees three `.git/` entries at depth 1
and classifies this directory as `multi_repo_workspace` (confidence:
high), with one `missing_from_disk` drift warning pointing at
`./delta-not-checked-out` (listed above but not present).

Re-running `materialize.sh` is a no-op once the `.git/` directories
exist.

## Why a materialise step?

Git refuses to track files named `.git` (a fundamental safety
invariant), so we can't check the nested `.git/` directories into
`agent-readiness-fixtures` directly. The materialiser converts the
sentinels into real git directories at test time.
