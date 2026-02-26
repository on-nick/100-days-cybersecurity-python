### What I Learned
- How systemd timers can be used as a persistence mechanism on Linux systems.
- That attackers may hide malicious execution inside scheduled timer units.
- How to recursively scan system and user directories for specific file types.
- How keyword-based detection can help quickly identify suspicious behavior patterns.
- The limitations of static string matching in security detection.

### What I Built
- A lightweight Systemd Timer Persistence Detector.
- It scans common timer locations:
  - `/etc/systemd/system`
  - `/lib/systemd/system`
  - `~/.config/systemd/user`
- It reads `.timer` files and searches for suspicious execution patterns such as:
  - Temporary directory usage (`/tmp/`, `/dev/shm/`)
  - Network tools (`curl`, `wget`, `nc`)
  - Inline execution (`bash -c`, `python -c`)
- It prints alerts when potentially malicious patterns are found.

### What Failed
- Pure keyword matching can generate false positives.
- It does not analyze linked `.service` files referenced by timers.
- It cannot detect obfuscated or encoded payloads.
- It does not validate whether flagged entries are actually malicious.

### How I Fixed It
- Improved keyword selection to focus on high-risk execution patterns.
- Added error handling to avoid crashes when reading protected files.
- Ensured the scan ignores non-existent directories.
- Structured output clearly to make alerts easier to review.

### Security Insight
- Systemd timers are a powerful and often overlooked persistence vector.
- Monitoring scheduled tasks is critical in incident response and threat hunting.
- Lightweight detection scripts can provide quick visibility, but should be combined with deeper analysis tools.
- Defense-in-depth requires monitoring both system-level and user-level persistence locations.
