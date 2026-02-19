### What I Learned
- How SSH stores public keys inside the `~/.ssh/authorized_keys` file for each system user.
- That SSH keys can include additional options such as `command=`, `no-pty`, `from=`, `permitopen=`, and `environment=` which may restrict or automate behavior — and in some cases be abused.
- How to enumerate local system users using the `pwd` module and safely iterate through their home directories.
- The importance of ignoring commented or empty lines when parsing configuration files.
- Why defensive scanning scripts should handle file errors gracefully to avoid crashing mid-scan.

---

### What I Built
- A lightweight **SSH authorized_keys backdoor detector**.
- The script:
  - Iterates through all local users on a Unix/Linux system.
  - Checks each user’s `.ssh/authorized_keys` file (if it exists).
  - Scans for suspicious SSH key options that could indicate restricted or malicious access.
  - Flags malformed SSH key entries.
  - Prints alerts with the username, file path, and suspicious line preview.

---

### What Failed
- Initially, the script would crash when encountering unreadable files or permission issues.
- It did not handle empty or commented lines properly at first.
- Some legitimate SSH configurations were flagged as suspicious due to keyword-based detection being too broad.

---

### How I Fixed It
- Added error handling to prevent the script from stopping due to file access issues.
- Implemented line sanitization by stripping whitespace and skipping comments.
- Used keyword scanning carefully and limited output to a preview of the line for safer inspection.
- Added basic malformed entry detection to improve visibility into potential configuration problems.

---

### Security Insight
- SSH key-based access is powerful and often overlooked during audits.
- Malicious persistence can be hidden inside `authorized_keys` using options like forced commands.
- Regular auditing of SSH configurations across all users is critical for maintaining system integrity.
- Even simple keyword-based monitoring can provide early warning signs of compromise.
