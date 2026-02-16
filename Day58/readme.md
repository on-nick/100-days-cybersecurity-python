# Sudoers Misconfiguration Scanner

## What I Learned
- How Linux privilege escalation often happens through sudo misconfigurations.
- How to use Python’s `os` and `re` modules to scan system files.
- How to safely read protected configuration files while ignoring errors.
- How pattern matching can help detect insecure privilege rules automatically.

## What I Built
- A lightweight Python-based scanner that checks `/etc/sudoers` and `/etc/sudoers.d` for dangerous privilege rules.
- A regex-based detection system to identify risky configurations like `NOPASSWD: ALL` and unrestricted root access.
- A simple reporting mechanism that flags critical findings clearly in the terminal.

## What Failed
- Initially, the script stopped scanning if it encountered unreadable files.
- Some legitimate rules were flagged due to overly broad regex patterns.
- Error handling was too generic and silently ignored important debugging information.

## How I Fixed It
- Added safer file handling with error ignoring to prevent crashes.
- Refined regex patterns to better target truly dangerous configurations.
- Improved scanning logic to skip comments and blank lines properly.
- Ensured the scanner continues even if one file fails.

## Security Insight
Misconfigured sudo rules are one of the most common privilege escalation vectors in Linux systems.  
Rules like `NOPASSWD: ALL` or allowing shell access as root effectively remove all privilege boundaries.  
Automated scanning helps quickly identify these risks before they are exploited.
