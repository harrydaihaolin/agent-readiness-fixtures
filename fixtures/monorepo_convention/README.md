# monorepo_convention

Synthetic fixture for `workspace_detect`'s Signal B (convention dir
plus child manifests).

No root workspace declaration — just `apps/webapp/package.json` and
`apps/worker/package.json`. The detector should classify this as
`monorepo` with `confidence: medium` and `signals.fired` containing a
`"B:apps/"` token.

Distinguishes from the `monorepo_pnpm` fixture (Signal A): same
ecosystem, same shape, but no `pnpm-workspace.yaml` or `package.json`
`workspaces` field, so the high-confidence path doesn't fire and we
fall through to Signal B.
