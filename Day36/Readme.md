### What I Learned
- How to aggregate logs from multiple sources (auth, web, firewall) for threat detection.
- Using `defaultdict` to dynamically store threat metrics per IP.
- Assigning weighted scores to different types of suspicious activity.
- Basic SIEM-style risk reporting based on cumulative threat scores.

### What I Built
- A Python script that processes authentication, web, and firewall logs.
- A threat database (`threat_db`) that tracks per-IP metrics: authentication failures, web access failures, firewall blocks, and a cumulative risk score.
- A simple scoring system:
  - Auth fail = +2 points
  - Web fail (401/403) = +1 point
  - Firewall block = +3 points
- A high-risk alert report for IPs with a score ≥ 6.

### What Failed
- Initially, miscounted threat scores when multiple logs existed for the same IP.
- Log parsing could fail if the log format changes (e.g., extra whitespace or unexpected fields).

### How I Fixed It
- Ensured each log type is split and processed consistently.
- Used `defaultdict` to automatically initialize threat metrics for new IPs.
- Carefully mapped log actions/status codes to score increments.

### Security Insight
- Even a single IP repeatedly failing authentication or triggering blocks across multiple systems can indicate malicious behavior.
- Correlating logs from multiple sources gives a more accurate threat picture than analyzing a single log type in isolation.
- Scoring thresholds allow prioritization of alerts, helping SOC teams focus on high-risk events first.
