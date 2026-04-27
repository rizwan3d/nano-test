---
name: python-testing
description: Use for testing Python code, adding or running Python unit tests, choosing pytest/unittest commands, debugging test failures, checking coverage, and validating Python scripts or packages.
---

Prefer the repository's existing Python test setup before introducing a new one.

1. Inspect test configuration first: `pyproject.toml`, `pytest.ini`, `tox.ini`, `noxfile.py`, `setup.cfg`, `requirements*.txt`, `Pipfile`, `poetry.lock`, and existing `tests/` files.
2. Use the configured runner when present. Prefer `python -m pytest` for pytest projects and `python -m unittest` for unittest projects.
3. Start with the smallest relevant test command, then broaden only when needed:
   - Single pytest file: `python -m pytest path/to/test_file.py`
   - Single pytest test: `python -m pytest path/to/test_file.py::test_name`
   - Unittest module: `python -m unittest module_name`
   - Unittest discovery: `python -m unittest discover`
4. If tests live inside a script, prefer importing through unittest or pytest rather than running the script directly, so demo or CLI code under `if __name__ == "__main__"` does not pollute test output.
5. When adding tests, follow the local layout and naming pattern. If no pattern exists, create focused pytest tests under `tests/` or focused unittest cases when the code already uses `unittest`.
6. Keep tests deterministic: avoid network, clock, filesystem, and environment dependencies unless the behavior being tested requires them; use temporary directories and monkeypatching/mocking where appropriate.
7. For failure investigation, read the assertion and traceback first, reproduce with the narrowest command, fix the behavior or test expectation, and rerun the failing test before running a broader suite.
8. Report the exact commands run and whether they passed, failed, or were skipped.
