Title: Add tests and CI workflow

Description:
Add automated tests and CI to ensure stability for future changes.

Acceptance criteria:
- Unit tests for `src/app.py` endpoints and DB layer.
- GitHub Actions workflow to run tests on push and PR.
- Linting and formatting checks (flake8/black) in CI.

Implementation notes:
- Use pytest and a test database (SQLite in-memory) for fast runs.
