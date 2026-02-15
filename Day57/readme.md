### What I Learned
- How `systemd` manages services and where service unit files are commonly stored (`/etc/systemd/system`, `/lib/systemd/system`, and user-level directories).
- That persistence mechanisms on Linux often rely on legitimate service managers like systemd.
- How simple keyword-based detection can help flag potentially malicious service configurations.
- The importance of scanning both system-wide and user-level service directories.
- That basic file parsing and directory traversal can be effective for quick security audits.

### What I Built
- A lightweight Systemd Persistence Detector written in Python.
- A scanner that recursively checks systemd service directories.
- A keyword-based detection mechanism to flag suspicious command usage (temporary directories, remote download tools, reverse shell indicators, etc.).
- A simple alerting output that highlights potentially malicious service files and the matched keyword.

### What Failed
- Initially, the scanner did not account for user-level systemd paths.
- Some service files caused read errors due to encoding issues.
- The first version lacked error handling, which caused interruptions during scanning.
- Early testing showed false positives because some legitimate services use tools like `curl` or `wget`.

### How I Fixed It
- Added user-level systemd directory scanning using environment-aware path expansion.
- Implemented safe file reading with ignored encoding errors.
- Wrapped file operations in try/except blocks to prevent crashes.
- Improved keyword matching logic to reduce noise and stop after the first match per file.

### Security Insight
- Systemd is a common persistence vector because it provides automatic service execution at boot.
- Attackers often use temporary directories (`/tmp`, `/dev/shm`) to store payloads.
- Network utilities (`curl`, `wget`, `nc`) inside service files can indicate remote payload retrieval or command-and-control behavior.
- Simple behavioral indicators can quickly highlight anomalies, even without advanced threat detection tools.
- Regular auditing of service definitions is an effective defensive practice for Linux systems.
