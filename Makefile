.PHONY: install test lint clean

install:
	pip install -e .

test:
	pytest -v

lint:
	ruff check .
	ruff format --check .

fmt:
	ruff format .
	ruff check --fix .

clean:
	rm -rf __pycache__ .pytest_cache src/**/__pycache__ tests/__pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; true
