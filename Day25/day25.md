### What I Learned
- How to read and analyze log files in Python.
- Using regular expressions (`re`) to extract IP addresses and HTTP status codes.
- Counting occurrences using dictionaries.
- Basic input handling for menu-driven scripts.

### What I Built
- A Python script that analyzes server access logs to detect suspicious IP addresses.
- The script tracks failed login attempts (HTTP 401 or 403) and alerts if an IP exceeds a threshold.
- Includes a function to create a sample log file for testing.

### What Failed
- Initially, I didn’t handle the case where the log file didn’t exist.
- Counting failed attempts across multiple status codes was tricky at first.

### How I Fixed It
- Added a check using `os.path.exists` to ensure the log file exists.
- Used `dict.get(ip, 0)` to increment the failed attempt counter safely.

### Security Insight
- Repeated failed login attempts can indicate brute-force attacks.
- Monitoring logs and alerting on multiple failed attempts is a simple but effective security measure.
