### What I Learned
- How Linux stores process information inside the `/proc` filesystem.
- How to iterate through active process IDs programmatically.
- How to read process metadata such as the command name and executable path.
- How attackers can disguise malicious programs by using names of legitimate system processes.
- Why running executables from temporary directories can be a red flag.
- That deleted executables can still run in memory and remain active.

### What I Built
- A simple Linux process masquerading detector.
- A scanner that checks running processes against a list of common system process names.
- A detection mechanism that flags processes running from suspicious directories like `/tmp`, `/dev/shm`, and `/var/tmp`.
- A check to identify processes whose executables were deleted but are still running.
- A basic alert system that prints warnings when suspicious behavior is found.

### What Failed
- Some processes could not be accessed due to permission restrictions.
- Certain legitimate processes might trigger false positives.
- The detection logic is based only on name matching and location, which is not fully reliable.
- It does not perform deep behavioral or signature-based analysis.

### How I Fixed It
- Used exception handling to skip processes that cannot be accessed.
- Focused detection on specific high-risk directories to reduce noise.
- Clearly separated detection cases to make alerts easier to understand.
- Improved logical checks to prevent unnecessary crashes.

### Security Insight
- Process masquerading is a common technique used by attackers to avoid detection.
- Temporary directories are often abused to execute malicious payloads.
- A deleted executable does not mean the threat is gone — it may still be active in memory.
- Monitoring process execution paths is an important part of Linux system security.
