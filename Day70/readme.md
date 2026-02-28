### What I Learned
- How environment variables like `PATH` influence command execution order in operating systems.
- Why writable directories inside `PATH` can create serious security risks.
- The difference between world-writable permissions and user-writable permissions.
- How permission bits work conceptually and why checking them matters for system security.
- The importance of defensive programming when scanning system-level configurations.

### What I Built
- A lightweight PATH hijacking vulnerability scanner.
- A script that iterates through each directory listed in the system `PATH`.
- A permission-check mechanism that identifies:
  - World-writable directories (critical risk)
  - Directories writable by the current user (warning level)
- A simple reporting structure to clearly classify risk severity.

### What Failed
- Initially, duplicate directories in `PATH` caused redundant checks.
- Some invalid or non-existent directories caused errors during scanning.
- Early versions did not clearly separate critical risks from warnings.

### How I Fixed It
- Added a mechanism to track and skip duplicate directories.
- Implemented checks to confirm a directory exists before scanning it.
- Wrapped permission checks in error handling to prevent crashes.
- Improved output formatting to clearly distinguish critical issues from warnings.

### Security Insight
- PATH hijacking is possible when an attacker can place a malicious executable in a writable directory that appears earlier in `PATH`.
- World-writable directories inside `PATH` represent a high-severity vulnerability.
- Even user-writable directories can become dangerous in shared or misconfigured systems.
- Regular auditing of environment variables is an essential part of system hardening.
