Title: Performance and scalability improvements

Description:
Plan for scaling the app beyond a single-process in-memory server.

Acceptance criteria:
- Identify bottlenecks and add caching layers where appropriate.
- Ensure database connection pooling and safe concurrent writes.
- Load testing report for baseline traffic (e.g., 1000 concurrent users).

Implementation notes:
- Consider adding Redis for caching and background job queues.
