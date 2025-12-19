Title: Add authentication and role-based access control

Description:
Introduce authentication for users and role-based permissions (organizer, student, admin) so sensitive actions are restricted.

Acceptance criteria:
- User model and login endpoints (JWT-based or session-based).
- Roles: `admin`, `organizer`, `student` with appropriate permissions.
- Protect endpoints like create/update/delete activities and attendance marking.

Implementation notes:
- Use `fastapi-users` or implement simple JWT-based auth.
- Store users and roles in the DB (see issue 02).
