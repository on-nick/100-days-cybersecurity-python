# LD_PRELOAD Injection Detector

## What I Learned
- How **LD_PRELOAD injection** works on Linux systems.
- How attackers can abuse `/etc/ld.so.preload` to force-load malicious shared libraries globally.
- How environment variables like `LD_PRELOAD` can override normal dynamic linking behavior.
- Why directories like `/tmp`, `/dev/shm`, and `/var/tmp` are commonly abused for storing malicious `.so` files.
- How to use Python’s `os` module to inspect system files and environment variables for security analysis.

## What I Built
- A lightweight Linux security detection script.
- A scanner that checks for:
  - Global preload injections via `/etc/ld.so.preload`
  - Active `LD_PRELOAD` environment variable usage
  - Suspicious `.so` files located in temporary directories
- A recursive filesystem scanner to detect shared libraries stored in risky paths.

## What Failed
- Full filesystem scanning (`/`) can be slow and resource-intensive.
- Permission errors may occur when scanning protected directories.
- The script may generate false positives if legitimate libraries exist in temporary paths.

## How I Fixed It
- Added error handling while reading files to prevent crashes.
- Used `errors="ignore"` when opening files to handle unreadable content safely.
- Structured alerts clearly to separate CRITICAL and ALERT findings.
- Considered limiting scan scope in production environments to improve performance.

## Security Insight
LD_PRELOAD injection is a powerful persistence and privilege escalation technique because it hijacks the dynamic linker before applications load their dependencies.  

Monitoring:
- `/etc/ld.so.preload`
- The `LD_PRELOAD` environment variable
- Suspicious `.so` files in temporary directories  

is critical for detecting stealthy Linux userland rootkits and shared library injection attacks.
