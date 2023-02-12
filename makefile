PYTHON=python3

run:
	$(PYTHON) main.py

run-tests:
	$(PYTHON) -m pytest -v

clean:
	rm -rf __pycache__/
	rm -f .coverage
	rm -f .pytest_cache/

.PHONY: run run-tests clean
