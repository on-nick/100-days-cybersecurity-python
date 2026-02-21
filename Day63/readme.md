# World-Writable File Auditor

## What I Learned
- How to recursively scan system directories using Python’s built-in file system utilities.
- How file permission bits work in Unix-like systems, especially the concept of **world-writable** permissions.
- How to safely handle permission errors and inaccessible files during large-scale directory scans.
- The importance of excluding virtual or sensitive system paths (like `/proc`, `/sys`, `/dev`) to avoid unnecessary errors or performance issues.

## What I Built
- A Python-based auditing script that scans critical system directories (`/etc`, `/usr`, `/var`, `/home`) for world-writable files and directories.
- A lightweight security auditing tool that:
  - Flags world-writable files as **ALERTS**
  - Flags world-writable directories as **WARNINGS**
  - Gracefully handles permission-related exceptions
- A structured scan workflow that avoids problematic system paths.

## What Failed
- Initial scans produced excessive permission errors when accessing protected system files.
- Performance issues occurred when scanning large directory trees without exclusions.
- The script originally attempted to scan virtual system directories, causing unnecessary noise and delays.

## How I Fixed It
- Added exclusion logic for `/proc`, `/sys`, and `/dev`.
- Implemented exception handling to silently skip inaccessible files.
- Structured the directory walk to continue scanning even when encountering restricted paths.
- Ensured the scan skips non-existent base directories.

## Security Insight
World-writable files and directories pose a significant security risk. Any local user can modify them, which can lead to:
- Privilege escalation
- Unauthorized configuration changes
- Malware persistence
- Data tampering

Regular auditing of file permissions is a critical component of system hardening and defensive security practices.
