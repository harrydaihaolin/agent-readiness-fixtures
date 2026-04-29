# Security policy

## Reporting

Email security reports to the maintainers via GitHub Security Advisories
on this repository.

## Scope

This repo contains only example fixture data. No code is executed by
default; consumers (agent-readiness, the rules pack, the engine) read
files. The only risk would be a malicious fixture file path triggering
a path traversal in a downstream evaluator — those bugs belong in the
downstream repo.

## Note on `broken/` fixture

The `broken/` fixture deliberately includes example-only secret patterns
(an AWS-shaped placeholder, written here as `AKIA-IOSFODNN7-EXAMPLE` so
secret-scanners don't trip on prose) so the `secrets.basic_scan` check
fires. These are documented placeholders, not real credentials. The
unbroken literal lives **only** inside `fixtures/broken/`.
