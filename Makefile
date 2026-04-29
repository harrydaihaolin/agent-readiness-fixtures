.PHONY: list test validate help

# `list` prints the fixture inventory as JSON. Consumers (CI matrices,
# downstream eval scripts) call this rather than parsing the manifest
# themselves.
list:
	python tools/list_fixtures.py

# `test` is the canonical sanity check for this repo: every fixture dir
# named in manifest.toml must exist and be non-empty. Cheap and fast.
test:
	python tools/list_fixtures.py | python -c "import json,sys,os; data=json.load(sys.stdin); fail=0; \
[print(f'  ok   fixtures/{f[\"name\"]}') if os.path.isdir(f'fixtures/{f[\"name\"]}') and os.listdir(f'fixtures/{f[\"name\"]}') else (print(f'  FAIL fixtures/{f[\"name\"]} missing or empty'), exit(1)) for f in data['fixtures']]"

validate: test

help:
	@echo "Targets:"
	@echo "  list      - print fixture manifest as JSON"
	@echo "  test      - assert every fixture dir exists and is non-empty"
	@echo "  validate  - alias for test"
