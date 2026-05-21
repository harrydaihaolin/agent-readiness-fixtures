.PHONY: install test lint run

install:
	pip install -e .

test:
	python -m unittest discover -s tests -v

lint:
	ruff check src tests

run:
	thin-pkg
