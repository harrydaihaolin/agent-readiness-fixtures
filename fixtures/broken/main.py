"""Broken fixture: deliberately missing README, AGENTS.md, Makefile, tests, .env.example, manifest."""

# Example-only secret pattern (NOT a real key) so secrets.basic_scan fires:
AWS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def go():
    return AWS_KEY[:4]


if __name__ == "__main__":
    print(go())
