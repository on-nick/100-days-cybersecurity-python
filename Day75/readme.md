### What I Learned
- Many malicious programs attempt to hide themselves using **hidden files or directories** that start with a dot (`.`) in Unix-based systems.
- Common temporary locations such as `/tmp`, `/var/tmp`, and `/dev/shm` are frequently abused by malware because they are writable and often ignored by users.
- Python's `os` module makes it easy to **traverse directories recursively** and inspect files across different system paths.
- Even simple detection scripts can reveal suspicious artifacts when they systematically scan for hidden items.

### What I Built
- A **Hidden File and Directory Detector** that scans common temporary and user directories.
- The tool recursively walks through system paths and identifies files or directories that begin with a dot and have names longer than two characters.
- Any discovered hidden items are collected and displayed after the scan completes, allowing quick inspection of potentially suspicious artifacts.

### What Failed
- During early testing, the script attempted to scan directories that **did not exist on some systems**, which caused interruptions in the scanning process.
- Some system folders contained many legitimate hidden files, making the results **noisy and harder to analyze**.

### How I Fixed It
- Added a check to verify whether a directory exists before scanning it.
- Improved the scanning logic so the program continues smoothly even when certain paths are missing.
- Organized the results so that hidden files are only printed **after the scan completes**, making the output clearer.

### Security Insight
Hidden files are not automatically malicious, but attackers often rely on them for **stealth persistence**. By periodically scanning common temporary directories and user locations, defenders can quickly spot unusual artifacts that may indicate malware, unauthorized scripts, or persistence mechanisms.
