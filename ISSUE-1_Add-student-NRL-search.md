## Add student NRL search and lookup

- Summary: Add endpoints and UI to search student NRL records by student email/ID and display detailed activity history.

- Acceptance criteria:
  - `GET /students/{email}` returns student profile and activity records.
  - Frontend: a search box on the UI to lookup by email and show results in a card.
  - Unit tests for the endpoint.

- Suggested files: `src/app.py`, `src/static/index.html`, `src/static/app.js`, add `src/searcher.py`.
