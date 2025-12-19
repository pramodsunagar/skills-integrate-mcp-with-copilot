Title: Frontend improvements and UX updates

Description:
Improve the static frontend served at `/static` to better display activities, handle signups, and support admin actions.

Acceptance criteria:
- Responsive UI for mobile and desktop.
- Activity detail pages with signup flow and attendee lists.
- Admin UI to create/edit/delete activities (hooks to API issue 01).

Implementation notes:
- Refactor `static/app.js` and `static/index.html` for modular components.
- Consider adding a build step (e.g., Vite) for advanced UI.
