.PHONY: install dev test lint

install:
	pip install -e .

dev:
	pip install -e ".[dev]"

test:
	python -m unittest discover -s tests -v

lint:
	ruff check src tests
