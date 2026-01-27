## Support multi-format ingestion (HTML/PDF) with example parsers

- Summary: Add libraries and parsers for HTML and PDF NRL reports; include example parsing rules.

- Acceptance criteria:
  - Uploads of `.html` and `.pdf` are parsed into normalized records.
  - Add dependencies and example input files for testing.
  - Document supported formats in `README.md`.

- Suggested files: `src/parser.py`, `requirements.txt`, `tests/fixtures/`.
