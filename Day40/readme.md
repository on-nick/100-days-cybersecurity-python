### What I Learned
- How honeypots are used to observe and collect attacker behavior
- Why common usernames like `root` and `admin` are frequently targeted
- The importance of logging authentication attempts for security monitoring
- How even simple simulations can demonstrate real-world attack patterns

### What I Built
- A basic SSH honeypot **simulation**
- A logging mechanism that records:
  - Timestamp
  - Source IP
  - Username
  - Password attempts
- A fake authentication system designed to attract attackers

### What Failed
- The system is not a real SSH service
- Passwords are logged in plaintext
- No log rotation or protection against large log files
- No alerting or analysis of logged data

### How I Fixed It
- Clearly scoped the project as a **learning simulation**
- Ensured only fake users trigger logging
- Structured logs in a readable and consistent format
- Avoided exposing the system to real networks

### Security Insight
- Attackers rely heavily on predictable usernames
- Logging failed login attempts is critical for intrusion detection
- Honeypots should always be isolated from production systems
- Real-world honeypots must secure stored data and limit exposure
