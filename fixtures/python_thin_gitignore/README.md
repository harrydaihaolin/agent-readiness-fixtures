# thin-pkg

Tiny Python project used as a regression-guard fixture for the
`agent-readiness` scanner. Its `.gitignore` is intentionally **thin**:
it covers the three universal groups (`dotenv`, `ide_junk`, `logs`)
and three of the four Python language-specific groups, but
**deliberately omits the `coverage` group**.

## Why this fixture exists

In `agent-readiness 2.4.3`, the `safety.gitignore.covers_junk` rule's
`language_aware` mode silently switched from "7-of-13 groups required"
(the v1.5.0 default) to "every filtered group required". A Python
repo with a `.gitignore` exactly like this one (six of seven required
groups present) flipped from passing to firing. The
[2026-05-21 calibration cycle](https://github.com/harrydaihaolin/agent-readiness-research/pull/34)
measured this as a +4.1 pp regression on the full v3 cohort and
[agent-readiness #80](https://github.com/harrydaihaolin/agent-readiness/pull/80)
shipped the v2.4.4 fix.

This fixture pins the corrected behaviour: when the engine scans
`thin_pkg`, **`safety.gitignore.covers_junk` must NOT fire**. Any
future change to the language-aware threshold semantics that silently
flips this fixture is a regression to revert.

## Run

```bash
pip install -e .
thin-pkg
python -m unittest discover -s tests -v
```

## Score expectation

See `manifest.toml`: this fixture targets `expected_score_min = 80`.
The point is the safety pillar; the rest of the repo is a minimal
healthy Python project.
