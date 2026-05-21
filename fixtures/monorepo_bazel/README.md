# monorepo_bazel

Synthetic fixture for `workspace_detect`'s Signal A (Bazel
build-system branch).

Root `WORKSPACE` + two `BUILD` files under `srv/` and `client/`. The
detector should classify this as `monorepo` with `confidence: high` and
`signals.fired` containing `"A:WORKSPACE"`.
