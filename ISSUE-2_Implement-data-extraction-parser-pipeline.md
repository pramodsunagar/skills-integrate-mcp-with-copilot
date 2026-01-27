## Implement data extraction & parser pipeline

- Summary: Add modules and an upload endpoint to ingest raw NRL data (HTML/text/PDF) and parse into normalized records.

- Acceptance criteria:
  - `POST /ingest` accepts file uploads and returns parsed records.
  - Add `src/extractor.py` and `src/parser.py` to perform parsing.
  - Basic error handling and tests for common formats.

- Suggested files: `src/extractor.py`, `src/parser.py`, `src/app.py`.
