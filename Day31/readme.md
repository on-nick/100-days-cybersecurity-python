### What I Learned
- How to work with file operations using `os`, `shutil`, and `pathlib`
- How to create and manage backup directories safely
- How checksums can be used to verify file integrity
- How to build a menu-driven CLI program in Python
- Why validating data before restoration is important for security

### What I Built
- A simple file backup and restore system
- Automatic creation of a backup directory
- A checksum-based integrity verification mechanism
- Protection against restoring corrupted backup files

### What Failed
- The checksum method used is very basic and not cryptographically secure
- Large files may cause performance issues since the entire file is read into memory
- No exception handling for permission errors or interrupted operations

### How I Fixed It
- Added file existence checks before backup and restore
- Stored checksum values in a separate `.chk` file
- Blocked restoration when checksum verification fails

### Security Insight
- Integrity checks are critical when restoring backups
- Simple checksums can detect accidental corruption but are not secure against tampering
- Strong hashing algorithms like SHA-256 should be used for real-world backup systems
