## Implement search logging and basic analytics

- Summary: Log search queries and user actions for analytics; add an admin endpoint to view basic stats.

- Acceptance criteria:
  - Log searches to a local table/file with timestamp, query, source IP.
  - `GET /admin/search-stats` returns counts and top queries (protected or local-only).
  - Add `src/search_logger.py` and wire logging into search endpoints.

- Suggested files: `src/search_logger.py`, `src/app.py`.
