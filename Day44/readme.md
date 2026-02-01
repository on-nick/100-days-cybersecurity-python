---

## 🧠 What I Learned
- How privilege escalation attacks often begin with common Linux commands
- Basic real-time monitoring techniques using Python
- How to log security events for later analysis
- How to implement time-based detection logic

---

## 🛠️ What I Built
- A Python script that:
  - Continuously monitors executed commands
  - Logs commands with timestamps
  - Detects suspicious privilege-related commands
  - Triggers alerts when multiple events occur within 60 seconds

---

## ❌ What Failed
- The script cannot distinguish between legitimate administrative use and malicious intent
- It relies on keyword matching, which can cause false positives
- It only monitors manually entered commands, not actual system execution

---

## 🔧 How I Fixed It
- Added a rolling 60-second event window to reduce noise
- Limited alerts using an `ALERT_LIMIT` threshold
- Centralized logging into a single file for easier review

---

## 🔐 Security Insight
Privilege escalation attempts often involve repeated use of administrative commands in a short time frame. Monitoring command frequency and context—even with simple tools—can help identify suspicious behavior early.

---
