### What I Learned
- How to use `defaultdict(list)` to group request timestamps by IP address
- How basic rate limiting logic works by counting requests per client
- How to simulate API traffic without needing a real server
- The importance of monitoring usage patterns to detect abuse

### What I Built
- A simple API abuse detection script in Python
- A request logger that tracks request times per IP
- A basic analyzer that flags IPs exceeding a fixed request limit
- A small simulation to test normal vs abusive behavior

### What Failed
- The script does not actually use the `WINDOW` value to enforce time-based limits
- Requests are only counted, not filtered by time range
- Once an IP exceeds the limit, it stays flagged forever
- No real-time blocking or prevention is implemented

### How I Fixed It
- Verified that logging and counting requests worked correctly
- Ensured the rate limit logic correctly identifies excessive requests
- Used a simulated request list to validate expected behavior
- Left time-window enforcement as a known limitation for future improvement

### Security Insight
- Rate limiting is a critical first defense against API abuse and DoS attacks
- Counting requests alone is not enough—time windows matter
- Even simple monitoring can quickly reveal suspicious patterns
- Proper rate limiting should combine request counts, time windows, and enforcement actions
