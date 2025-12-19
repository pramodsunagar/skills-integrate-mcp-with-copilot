Title: Add event creation and management endpoints

Description:
Allow authenticated organizers to create, update, and delete activities via the API. Today the project serves a static in-memory `activities` dict and supports signup/unregister, but lacks endpoints for adding or editing activities.

Acceptance criteria:
- POST `/activities` creates a new activity with required fields (name, description, schedule, max_participants).
- PUT `/activities/{activity_name}` updates activity fields.
- DELETE `/activities/{activity_name}` removes an activity.
- Appropriate HTTP status codes and validation (400 for missing/invalid fields, 409 for name conflicts).

Implementation notes:
- Add FastAPI routes in `src/app.py` and validate inputs using Pydantic models.
- Require authentication/authorization for these endpoints (see issue 04 for auth plan).
- Store changes in persistent storage (see issue 02) or document if using in-memory only for now.
