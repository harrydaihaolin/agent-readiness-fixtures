# Contributing

We accept new fixtures that represent realistic repo patterns the
existing fixtures don't cover. Examples we'd take:

- A Rust monorepo with `cargo workspace`.
- A Go module with `cmd/` entry points.
- A repo using nested git submodules.
- A multi-language repo (Python + JS + shell scripts).

We'd reject:

- Production-sized clones of real OSS projects (use `agent-readiness-leaderboard` for that).
- Anything containing real credentials, even revoked ones.
- Fixtures that depend on running CI to be useful.

## PR checklist

- [ ] Fixture lives at `fixtures/<descriptive-name>/`.
- [ ] Added a stanza to `manifest.toml`.
- [ ] Bumped `pack_version` (semver).
- [ ] No real secrets (use the documented placeholder pattern, with `AKIA` separated from the suffix to keep secret-scanners happy in docs: `AKIA-IOSFODNN7-EXAMPLE` in prose; the *unbroken* literal lives only inside `fixtures/broken/`).
- [ ] Files under fixture are smaller than 50 KB each (this is a fixture pack, not a corpus).
