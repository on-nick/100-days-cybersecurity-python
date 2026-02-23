# Shadow Password Weak Hash Detector

### What I Learned
- Linux stores hashed user passwords in `/etc/shadow`.
- Different hash algorithms can be identified by their prefix (e.g., `$1$`, `$5$`, `$6$`).
- MD5 and certain Blowfish variants are considered weak compared to SHA-256 and SHA-512.
- Proper permission handling is required when accessing protected system files.
- Basic parsing of colon-separated fields allows extraction of usernames and password hashes.

### What I Built
- A Python script that reads `/etc/shadow`.
- Logic to detect weak hashing algorithms based on known prefixes.
- Alerts for weak hash usage.
- Warnings for unknown or custom hash formats.

### What Failed
- Initial attempts failed due to permission restrictions when accessing `/etc/shadow`.
- Some system accounts had special symbols (`*`, `!`, `!!`) instead of password hashes.
- Not all hash prefixes were initially categorized correctly.

### How I Fixed It
- Added exception handling for `PermissionError`.
- Skipped locked or disabled accounts with special password fields.
- Clearly separated weak and strong hash prefix lists for better detection logic.

### Security Insight
- Weak hashing algorithms increase the risk of successful password cracking.
- Regular audits of `/etc/shadow` can help identify insecure configurations.
- Using stronger hashing algorithms like SHA-512 improves password security.
- Security tools should include proper error handling to operate safely in restricted environments.
