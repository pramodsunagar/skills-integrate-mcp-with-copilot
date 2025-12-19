Title: Add notifications (email/webhooks)

Description:
Notify participants and organizers about upcoming events, changes, cancellations, and reminders.

Acceptance criteria:
- Background task or scheduler to send reminder emails.
- Webhook support to integrate with external services.
- UI toggles for notification preferences.

Implementation notes:
- Integrate with an SMTP provider for emails; use Celery or FastAPI background tasks for scheduling.
- Consider SendGrid/Postmark for production usage.
