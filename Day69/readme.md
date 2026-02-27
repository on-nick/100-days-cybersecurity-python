# Kernel Module Integrity Checker

## Overview
This project is a simple integrity verification tool for Linux kernel modules.  
It compares currently loaded kernel modules (from `/proc/modules`) with module files stored on disk (`/lib/modules`) and generates SHA256 hashes for verification purposes.

The goal is to detect:
- Loaded modules that do not exist on disk
- Potential inconsistencies between runtime state and filesystem state
- Early signs of tampering or stealth kernel-level persistence

---

## What I Learned
- How Linux exposes runtime kernel module information through `/proc/modules`
- How kernel modules are stored and structured inside `/lib/modules`
- Recursive filesystem scanning using `os.walk`
- Generating SHA256 hashes for integrity verification
- The importance of validating runtime artifacts against static disk artifacts
- How rootkits may hide modules from disk or from `/proc`

---

## What I Built
- A Python-based kernel module integrity checker
- Automatic enumeration of currently loaded modules
- Recursive search of module files on disk
- SHA256 hashing of discovered `.ko` files
- Alert generation for modules loaded in memory but missing on disk

---

## What Failed
- Initial attempts did not account for permission restrictions
- Some modules may exist in compressed formats (`.ko.xz`) and were not detected
- Kernel version mismatches between `/proc/modules` and `/lib/modules` can produce false alerts
- Performance can degrade due to full recursive scans of `/lib/modules`

---

## How I Fixed It
- Added exception handling for file access failures
- Improved search logic to better match module names
- Broke loops early once a module match is found to reduce overhead
- Added clear alert messages for missing modules
- Improved output formatting for readability

---

## Security Insight
Runtime vs disk validation is a powerful defensive technique.

If a kernel module is:
- Loaded in memory
- But not present on disk

It may indicate:
- Rootkit activity
- Manual module injection
- Kernel persistence techniques
- Tampering with module files

Integrity monitoring at the kernel level is critical because once kernel space is compromised, traditional userland detection tools can no longer be fully trusted.

---
