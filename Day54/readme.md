### What I Learned
- How Linux process information is exposed through the `/proc` filesystem.
- How to identify running processes by iterating through numeric directories in `/proc`.
- How to read process metadata such as the command name (`/proc/[pid]/comm`) and executable path (`/proc/[pid]/exe`).
- How attackers may attempt process masquerading by naming malicious binaries after legitimate system processes.
- That deleted executables can continue running in memory, which can be a persistence or evasion technique.
- The importance of exception handling when accessing system-level process data.

### What I Built
- A lightweight Process Masquerading Detector for Linux.
- A script that scans all running processes on the system.
- A detection mechanism that:
  - Flags system process names running from suspicious directories like `/tmp`, `/dev/shm`, and `/var/tmp`.
  - Detects executables that have been deleted from disk but are still running.
- A simple alerting output that displays PID, process name, and executable path for suspicious findings.

### What Failed
- Some processes could not be inspected due to permission restrictions.
- Accessing certain `/proc/[pid]/exe` links caused errors when processes terminated during scanning.
- Not all suspicious behavior guarantees malicious activity (possible false positives).
- The broad exception handling initially hid useful debugging information.

### How I Fixed It
- Added exception handling to prevent the script from crashing when encountering permission errors or short-lived processes.
- Filtered `/proc` entries to include only numeric PIDs.
- Structured detection logic clearly into two cases: masquerading and deleted executables.
- Improved output formatting for readability and easier incident review.

### Security Insight
- Process masquerading is a common defense evasion technique used by malware to blend in with legitimate services.
- Monitoring execution paths is just as important as monitoring process names.
- Running binaries from world-writable directories is a strong behavioral indicator of compromise.
- Deleted-but-running executables are a red flag in incident response investigations.
- Simple behavioral checks can provide meaningful security visibility without complex tooling.
