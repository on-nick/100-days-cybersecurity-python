### What I Learned
- How sensitive credentials such as API keys, private keys, and passwords can accidentally be exposed in source code.
- Learned how regular expressions can be used to detect patterns that resemble secrets or authentication tokens.
- Understood how automated scanning tools help security teams identify credential leaks before code is published or deployed.
- Learned how to traverse directories and inspect multiple files programmatically.

### What I Built
- A Python-based secret key leak scanner for local directories.
- The tool recursively scans files in a specified directory and searches for patterns that resemble sensitive credentials.
- It checks for common exposures such as AWS access keys, generic API keys, password assignments, private key headers, and JWT tokens.
- When a match is found, the scanner reports the type of secret, the file location, and a partial preview of the detected value.

### What Failed
- Some files contained text that matched the patterns but were not actually secrets, resulting in false positives.
- Binary files or unusual file encodings sometimes caused read errors during scanning.
- Very large directories increased scanning time due to the number of files being processed.

### How I Fixed It
- Added exception handling when reading files to prevent the program from crashing on unreadable files.
- Limited the displayed portion of detected secrets to avoid exposing the full credential in the output.
- Used recursive directory scanning to ensure all nested files were included in the analysis.

### Security Insight
- Hardcoded secrets are a major security risk, especially when code is shared publicly or stored in version control systems.
- Attackers often scan repositories automatically to find exposed credentials.
- Automated secret scanners can help detect leaks early, allowing developers to rotate compromised keys and remove sensitive information from the codebase.
