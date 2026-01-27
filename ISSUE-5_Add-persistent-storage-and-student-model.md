## Add persistent storage and richer student model (SQLite)

- Summary: Replace in-memory storage with SQLite; expand student model to include name, grade, and history.

- Acceptance criteria:
  - Add a `sqlite` DB file and migration or init script.
  - Update endpoints to read/write DB (activities, students, signups).
  - Data persists across restarts; include basic migration script.

- Suggested files: `src/db.py`, update `src/app.py`, add migration `scripts/init_db.py`.
