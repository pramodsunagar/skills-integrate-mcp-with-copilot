Title: Mobile client integration and API improvements

Description:
Make API changes and documentation to enable mobile clients (Android/iOS) to integrate, plus improve performance for mobile usage.

Acceptance criteria:
- API returns compact payloads and supports pagination for lists.
- Add CORS and rate-limiting considerations.
- Document mobile API usage in `src/README.md`.

Implementation notes:
- Ensure endpoints return stable IDs and UTC timestamps.
- Add API versioning if breaking changes are needed.
