### What I Learned
- How the system `hosts` file works as a local DNS override before external DNS resolution.
- Why redirecting trusted domains like Google, Facebook, GitHub, Amazon, and Microsoft can indicate potential malicious tampering.
- The importance of checking whether `/etc/hosts` exists before reading it.
- How permission errors can occur when accessing protected system files.
- How to filter out comments and blank lines when parsing configuration files.
- How to split and analyze structured text line-by-line.

### What I Built
- A simple **Hosts File Poisoning Detector**.
- It scans `/etc/hosts` for suspicious entries.
- It checks whether trusted domains are redirected to non-local IP addresses.
- It prints a critical warning if possible DNS poisoning is detected.

### What Failed
- Initial attempts failed due to permission restrictions when reading `/etc/hosts`.
- Some lines in the hosts file caused parsing issues because they were empty or comments.
- IPv6 handling required making sure `::1` was included as a local address.

### How I Fixed It
- Added a file existence check before reading the hosts file.
- Wrapped the file reading logic in a `try/except` block to handle `PermissionError`.
- Ignored blank lines and comment lines starting with `#`.
- Defined a set of valid local IPs to reduce false positives.

### Security Insight
- The `hosts` file is a common target for malware because it can silently redirect traffic.
- Even simple scripts can help detect basic DNS poisoning attempts.
- Running periodic checks can improve system security awareness.
- Monitoring critical domains helps protect against phishing and man-in-the-middle attacks.
