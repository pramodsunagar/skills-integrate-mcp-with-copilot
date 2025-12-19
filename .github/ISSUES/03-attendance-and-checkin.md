Title: Implement attendance tracking and check-in

Description:
Provide a way for organizers to track attendance for an activity and allow participants to check in.

Acceptance criteria:
- Endpoint to mark attendance for a participant by email or id.
- Optionally generate attendance reports (CSV) per activity.
- Frontend hooks to display attendee lists and check-in status.

Implementation notes:
- Store attendance records in the DB (see issue 02).
- Consider implementing QR-code based check-in for events.
