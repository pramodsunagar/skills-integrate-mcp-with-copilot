Title: Add persistent storage for activities and signups

Description:
Replace the in-memory `activities` dict with a persistent database to survive restarts and allow concurrent access. This will enable future features like analytics and backups.

Acceptance criteria:
- Add database integration (SQLite for MVP) and migrations.
- Model activities, participants, and signups with proper relations.
- Update endpoints to read/write to the DB instead of the in-memory dict.
- Tests demonstrating persistence across app restarts.

Implementation notes:
- Use SQLModel or SQLAlchemy + Alembic for migrations.
- Keep a simple repository layer in `src/db.py` to encapsulate DB operations.
