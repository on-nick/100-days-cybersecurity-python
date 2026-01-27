### What I Learned
- How sensitive data gets accidentally exposed in source code, logs, and config files  
- Using Python regex to detect secrets like API keys, tokens, and passwords  
- Recursive directory scanning using `os.walk()`  
- Why masking sensitive values is important for ethical bug hunting  
- How static analysis tools help in real-world bug bounty recon  

### What I Built
- A **Sensitive Data Leakage Scanner** using Python  
- The tool scans directories recursively  
- Detects emails, API keys, tokens, passwords, JWTs, and private keys  
- Filters useful file types (`.env`, `.js`, `.log`, `.json`, etc.)  
- Displays file name, line number, and masked sensitive data

### What Failed
- Initial version only scanned one directory level
- No line numbers made findings weak for bug reports
- Too many false positives from binary files
- Printing full secrets was unsafe

### How I Fixed It
- Switched to recursive scanning using `os.walk()`
- Added line number tracking
- Limited scan to relevant file extensions
- Implemented masking to hide sensitive values

### Security Insight
- Hard-coded secrets are one of the most common real-world vulnerabilities
- Logs, backups, and `.env` files are high-value targets in bug hunting
- Even small leaks can lead to account takeover or data breaches
- Automated scanning significantly improves recon efficiency in bug bounty programs
