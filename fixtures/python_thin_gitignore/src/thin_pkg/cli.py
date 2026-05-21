import os


def main() -> int:
    greeting = os.environ.get("THIN_PKG_GREETING", "hi")
    print(greeting)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
