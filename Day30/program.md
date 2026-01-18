### What I Learned
- How basic audit logging works
- How checksums can detect data changes
- Why integrity checks are important

### What I Built
- A simple audit logging system
- A verification process to detect tampering

### What Failed
- The checksum approach is weak and insecure
- Log files can still be altered or deleted

### How I Fixed It
- Added checksum verification for each log entry
- Added file existence checks to prevent errors

### Security Insight
- Basic checksums are not sufficient for security
- Cryptographic hashes should be used in real systems
- Audit logs should be append-only and protected
