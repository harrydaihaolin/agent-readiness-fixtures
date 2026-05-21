# monorepo_pnpm

Synthetic fixture for `workspace_detect`'s Signal A (pnpm workspace).

Two packages under `packages/` plus a root `pnpm-workspace.yaml`. The
detector should classify this as `monorepo` with `confidence: high` and
`signals.fired` containing `"A:pnpm-workspace.yaml"`.

The scanner itself still scores this as one repo in v1 — per-package
breakdowns are an explicit non-goal of the workspace-detect spec.
