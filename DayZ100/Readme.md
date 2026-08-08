### What I Learned
- How a SIEM (Security Information and Event Management) system works by collecting, analyzing, and correlating logs in real time.
- Learned how detection rules can be defined using patterns and thresholds to identify suspicious activities.
- Understood how real-time log monitoring can help detect attacks as they happen instead of after damage is done.
- Gained experience in structuring security alerts in a readable JSON format for better analysis and reporting.

### What I Built
- A mini SIEM system implemented in Python as a final Day 100 project.
- The tool continuously monitors a log file in real time (like `tail -f` behavior).
- It applies multiple security detection rules such as failed logins, SQL injection attempts, XSS attempts, and sensitive file access.
- When suspicious activity crosses defined thresholds, the system generates structured alerts.
- Alerts include the event, triggered rules, and timestamp in JSON format for clarity.

### What Failed
- The detection logic relies on simple pattern matching, which can produce false positives.
- It does not correlate events across multiple sources or users, limiting deeper analysis.
- Large or high-speed log streams may affect performance due to continuous monitoring.

### How I Fixed It
- Used a rule-based system with thresholds to reduce noise from single occurrences.
- Implemented a real-time file follower to efficiently process new log entries.
- Structured alerts in JSON format to make them easier to read, store, or integrate with other systems.

### Security Insight
- SIEM systems are critical for detecting and responding to security incidents in real time.
- Even simple rule-based monitoring can quickly highlight common attack patterns.
- Advanced SIEM solutions expand on this by adding correlation, machine learning, and centralized logging for stronger defense.
