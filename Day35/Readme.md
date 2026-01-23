### What I Learned
- How to read and process multiple log files in a directory using Python.
- How to use regular expressions (`re`) to extract IP addresses and HTTP status codes from log lines.
- How to use `defaultdict` to count occurrences of events efficiently.
- Basic logic for detecting suspicious activity (multiple failed login attempts).

### What I Built
- A Python script that can create sample logs for testing.
- A log analyzer that scans all logs in a folder and alerts when an IP has too many failed login attempts.

### What Failed
- Initially, I didn’t handle the case where the log folder might not exist.
- My first regex for status codes was too loose and could match unintended numbers.

### How I Fixed It
- Used `os.makedirs(LOG_FOLDER, exist_ok=True)` to ensure the log folder exists before writing logs.
- Improved regex to specifically match `401` or `403` surrounded by spaces.

### Security Insight
- Multiple failed login attempts from the same IP could indicate a brute-force attack.
- Logging and monitoring failed access attempts is critical for early detection of suspicious behavior.
- Simple scripts like this can help automate monitoring and alerting for potential security threats.
