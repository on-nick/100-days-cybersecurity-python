### What I Learned
- How Base64 encoding is commonly used to hide or transport data within applications, logs, and scripts.
- Learned that attackers sometimes use Base64 to conceal malicious payloads, commands, or sensitive data inside files.
- Understood how pattern matching with regular expressions can detect long encoded strings that resemble Base64 data.
- Learned how decoding Base64 strings programmatically can reveal hidden content for security analysis.

### What I Built
- A Python-based Base64 payload detection tool for scanning directories.
- The program recursively scans files within a specified directory.
- It searches for long Base64-like strings using pattern matching.
- When a potential encoded string is found, the tool attempts to decode it.
- If the decoded content appears meaningful, the script displays both the encoded snippet and a preview of the decoded result.

### What Failed
- Some Base64-like strings were not actually valid encoded payloads, resulting in decoding attempts that produced meaningless text.
- Certain files contained large amounts of encoded data that slowed the scanning process.
- Binary files or unusual file encodings sometimes caused read errors.

### How I Fixed It
- Added a decoding function with error handling to safely attempt Base64 decoding.
- Introduced a minimum decoded content length check to filter out meaningless or extremely short results.
- Used exception handling while reading files to prevent the scanner from crashing when encountering unreadable data.

### Security Insight
- Base64 encoding is not encryption; it only converts data into a different representation.
- Attackers frequently use Base64 to hide malicious commands, web shells, or embedded payloads inside scripts and configuration files.
- Security scanners that automatically detect and decode Base64 strings can help analysts uncover hidden threats during code reviews or forensic investigations.
