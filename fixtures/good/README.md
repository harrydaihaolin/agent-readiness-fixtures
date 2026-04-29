# good-fixture

Example healthy repo used by the agent-readiness fixture pack. Demonstrates
what an agent-ready Python project looks like at minimum size.

## Install

```bash
make dev
```

## Test

```bash
make test
```

## Lint

```bash
make lint
```

## Layout

- `src/good_fixture/` — package source
- `tests/` — unit tests
- `Makefile` — install/dev/test/lint targets
- `pyproject.toml` — manifest with `[project.scripts]` entry point
- `.env.example` — sample env vars
- `AGENTS.md` — agent guide
