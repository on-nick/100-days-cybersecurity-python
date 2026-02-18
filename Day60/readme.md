# Hidden SetUID / SetGID Scanner Reflection

### What I Learned
- How privileged binaries use SetUID and SetGID permission bits.
- Why certain system binaries legitimately require elevated privileges.
- How attackers can abuse misconfigured or hidden privileged files for privilege escalation.
- How to traverse system directories safely and handle permission-related exceptions.
- The importance of comparing discovered binaries against a known safe baseline.

### What I Built
- A scanner that searches common system binary directories.
- Logic to detect files with SetUID or SetGID permission bits enabled.
- A filtering mechanism to ignore commonly known legitimate privileged binaries.
- An alert system to flag potentially suspicious privileged executables.

### What Failed
- Some directories or files could not be accessed due to permission restrictions.
- The scanner could generate false positives if legitimate binaries were not included in the known safe list.
- It does not verify file integrity or hashes, only permission flags.

### How I Fixed It
- Implemented exception handling to gracefully skip inaccessible files.
- Maintained a known list of legitimate privileged system binaries.
- Focused alerts only on binaries outside the expected safe list to reduce noise.

### Security Insight
- SetUID and SetGID binaries are common privilege escalation vectors.
- Even one misconfigured privileged binary can compromise an entire system.
- Regular auditing of privileged files is a critical defensive security practice.
- Security monitoring should combine permission checks with integrity validation for stronger protection.
