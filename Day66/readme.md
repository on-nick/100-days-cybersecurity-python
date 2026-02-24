## What I Learned
- How attackers achieve persistence using shell startup files.
- How to scan multiple user home directories safely.
- How to detect suspicious command patterns inside configuration files.
- The importance of ignoring comments and blank lines during analysis.

## What I Built
- A lightweight Linux persistence detection script.
- A scanner that checks `.bashrc`, `.profile`, and `.bash_profile`.
- A simple pattern-based detection system for common reverse shell techniques.

## What Failed
- Initially scanned system directories unnecessarily.
- Didn’t handle file read errors gracefully.
- Flagged commented malicious examples before adding comment filtering.

## How I Fixed It
- Limited scanning to `/home` directories only.
- Added error handling using `try/except`.
- Ignored commented and empty lines before pattern matching.

## Security Insight
Shell startup files are a common persistence mechanism because they execute automatically when a user logs in. Even simple one-line reverse shells can survive reboots if placed in these files. Regular auditing of user startup scripts is a crucial defensive security practice.
