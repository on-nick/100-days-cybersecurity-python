### What I Learned
- How to use Python’s `os` module to recursively walk through directory trees.
- How to check file permissions using `os.stat()` and `stat.S_IWOTH`.
- The security risks associated with world-writable files and directories.
- The importance of excluding virtual/system directories like `/proc`, `/sys`, and `/dev` during scans.

### What I Built
- A simple Linux security auditing script.
- A recursive scanner that identifies world-writable files and directories.
- A lightweight command-line auditing tool for basic permission misconfiguration detection.

### What Failed
- Initial scans included special system directories, causing errors and performance issues.
- Some permission errors occurred when accessing restricted files.
- The script initially did not handle exceptions cleanly.

### How I Fixed It
- Added an exclusion list for system directories.
- Wrapped `os.stat()` calls in `try/except` blocks to prevent crashes.
- Added existence checks before scanning base paths.

### Security Insight
World-writable files and directories can be exploited for privilege escalation, malicious file replacement, or unauthorized modifications. Regular auditing of file permissions is a critical step in maintaining system security and reducing attack surfaces.
