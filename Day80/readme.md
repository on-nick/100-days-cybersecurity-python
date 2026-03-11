### What I Learned
- How API rate limiting works and why it is used to protect servers from abuse, spam, or denial-of-service attempts.
- Learned how to automate repeated HTTP requests using Python.
- Understood how HTTP status codes indicate server behavior, especially **200 (success)** and **429 (Too Many Requests)**.
- Learned to introduce controlled delays between requests to simulate different traffic patterns.
- Understood how to track results using counters to evaluate server responses.

### What I Built
- A Python-based API rate limit testing script.
- The tool sends multiple HTTP GET requests to a specified API endpoint.
- It records and categorizes responses based on status codes.
- The script reports how many requests were successful, rate-limited, or returned other errors.
- It provides a final summary indicating whether rate limiting appears to be implemented.

### What Failed
- Some APIs returned different error codes instead of **429**, making it harder to clearly identify rate limiting.
- Network instability or temporary connection failures sometimes produced request errors.
- Testing results could vary depending on the delay between requests and server-side protections.

### How I Fixed It
- Added exception handling to catch network or request-related errors.
- Implemented counters to classify responses into successful, rate-limited, and error categories.
- Introduced a configurable delay between requests to simulate more realistic traffic behavior and avoid overwhelming the target server.

### Security Insight
- Rate limiting is a critical defense mechanism against brute-force attacks, scraping, and automated abuse.
- APIs that do not implement rate limiting can be vulnerable to resource exhaustion or abuse by automated scripts.
- Observing status codes and response patterns helps security testers evaluate whether proper protections are in place.
