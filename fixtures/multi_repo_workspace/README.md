# multi_repo_workspace

Synthetic fixture exercising step 2 of `workspace_detect`:

- A parent directory containing three sibling repos (each with a
  `.git/` after materialise).
- A root `AGENTS.md` enriches each detected repo with a `display_name`
  + `description`.
- AGENTS.md lists a fourth repo (`./delta-not-checked-out`) that is
  deliberately missing on disk to exercise the `missing_from_disk`
  drift warning.

See [`AGENTS.md`](./AGENTS.md) for the materialiser recipe.

Expected classification (post-materialise):

```json
{
  "version": "detect_v1",
  "classification": "multi_repo_workspace",
  "confidence": "high",
  "signals": { "fired": ["step2:child_git>=2"] },
  "repos": [
    { "name": "alpha-svc",  "display_name": "Alpha HTTP service.",       "description": "Python" },
    { "name": "beta-lib",   "display_name": "Beta shared library.",      "description": "Rust" },
    { "name": "gamma-cli",  "display_name": "Gamma command-line client.", "description": "Go" }
  ],
  "drift_warnings": [
    { "kind": "missing_from_disk", "agents_md_path": "./delta-not-checked-out" }
  ]
}
```
