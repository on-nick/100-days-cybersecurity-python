## 📌 Description

Cron jobs are often abused by attackers to maintain persistence on compromised systems.  
This script checks standard cron directories and files for keywords commonly associated with malicious activity.

---

##  What I Learned
- How Linux cron jobs are structured and stored
- Common persistence techniques used by attackers
- How to safely read system files using Python
- Pattern matching for basic threat detection

---

##  What I Built
- A Python-based cron job scanner
- Keyword-based detection for suspicious commands
- Support for scanning both cron files and directories

---

##  What Failed
- Initial scans produced too many false positives
- Some cron files could not be read due to permission restrictions
- Keyword matching alone missed obfuscated commands

---

##  How I Fixed It
- Limited keyword list to commonly abused tools
- Used `errors="ignore"` to prevent crashes
- Wrapped file access in try/except blocks for stability

---

##  Security Insight
Attackers frequently use cron jobs to:
- Download payloads (`curl`, `wget`)
- Open backdoors (`nc`)
- Execute scripts (`bash`, `sh`, `python`)

Regular auditing of cron jobs is a simple but effective defensive practice.

---
