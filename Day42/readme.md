### What I Learned
- How Shannon entropy can be used to detect suspicious file behavior, such as encryption.
- How ransomware often increases file entropy due to encryption or compression.
- How to monitor a directory continuously using Python.
- The importance of thresholds and counters to reduce false positives in security tools.

### What I Built
- A **basic ransomware detection engine** that:
  - Monitors a folder in real time
  - Reads the first 2048 bytes of each file
  - Calculates entropy to detect potential encryption
  - Raises alerts when multiple high-entropy files are detected
- The system simulates how real endpoint detection tools flag suspicious activity.

### What Failed
- The script initially crashed due to a **syntax error** (`break|` instead of `break`).
- The alert counter kept increasing even when the same file was scanned repeatedly.
- Some normal files (like compressed files) triggered false positives due to high entropy.

### How I Fixed It
- Removed the invalid character after `break` to fix the syntax error.
- Verified file handling with `try/except` to prevent crashes.
- Added an alert threshold (`SUSPICIOUS_COUNT`) so a single high-entropy file wouldn’t immediately trigger a critical warning.
- Limited reads to 2048 bytes to improve performance.

### Security Insight
- **High entropy ≠ ransomware**, but it is a strong indicator when combined with behavior patterns.
- Real-world ransomware detection relies on **multiple signals**, not just entropy.
- This project shows why behavioral analysis is more effective than signature-based detection alone.
- Even simple defensive scripts can provide meaningful early warnings in cybersecurity.
