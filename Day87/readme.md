### What I Learned
- How log files can be analyzed to detect unusual or potentially malicious user behavior.
- Learned how pattern extraction using regular expressions can isolate useful information such as usernames from logs.
- Understood how counting techniques can help identify anomalies like spikes in activity or repeated failed login attempts.
- Learned how basic statistical measures, such as averages, can be used to define what is “normal” behavior.

### What I Built
- A Python-based Log Anomaly Detection tool.
- The program reads a log file and extracts usernames based on a defined pattern.
- It tracks total activity per user and counts failed login attempts.
- The tool identifies users with unusually high activity compared to the average.
- It also flags users with excessive failed login attempts, indicating possible brute-force behavior.

### What Failed
- The detection relied on a simple average, which may not always accurately represent normal behavior in uneven datasets.
- Logs with inconsistent formats could break the pattern matching or miss important data.
- The tool could not distinguish between legitimate high activity and malicious behavior.

### How I Fixed It
- Used a Counter to efficiently track user activity and failed login attempts.
- Added conditional checks to identify anomalies based on relative thresholds.
- Included error handling to ensure the program exits gracefully if the log file cannot be accessed.

### Security Insight
- Log analysis is a powerful method for detecting suspicious activities such as brute-force attacks or compromised accounts.
- Unusual spikes in activity or repeated failed logins are common indicators of potential security threats.
- Automated log monitoring tools are essential in modern systems to quickly identify and respond to anomalies.
