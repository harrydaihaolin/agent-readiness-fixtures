# Agent guide — thin-pkg

This Python fixture exists to pin a specific scanner behaviour: the
language-aware `gitignore_coverage` matcher must tolerate one
missing language group (here: `coverage`) without firing
`safety.gitignore.covers_junk`. See README for context.

- Install: `pip install -e .`
- Test:    `python -m unittest discover -s tests -v`
- Run:     `thin-pkg`

## CI and the feedback loop

After updating this fixture, run the rules-pack reference-eval CI
(`agent-readiness-rules` repo). When it goes red, read the diff in
`tests/expected/` against the new `.gitignore`, fix the root cause,
and iterate until green.
