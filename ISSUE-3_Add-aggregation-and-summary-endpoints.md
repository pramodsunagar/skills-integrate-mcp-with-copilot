## Add aggregation and summary endpoints

- Summary: Provide server-side aggregation to compute totals, categories, and summary views for a student or activity.

- Acceptance criteria:
  - `GET /students/{email}/summary` returns totals and category breakdown.
  - `GET /activities/{name}/summary` returns aggregated stats.
  - Implement `src/aggregator.py`.

- Suggested files: `src/aggregator.py`, `src/app.py`.
