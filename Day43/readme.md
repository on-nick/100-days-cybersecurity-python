### What I Learned -
- How DNS tunneling works by encoding data inside subdomains
- Shannon entropy and how it helps detect randomness in strings
- How attackers abuse DNS because it is often allowed through firewalls
- Tracking behavior per source IP to reduce false positives

### What I Built -
- A Python-based DNS tunneling detector
- Calculates entropy of DNS subdomains
- Flags high-entropy queries as suspicious
- Detects repeated suspicious queries from the same IP

### What Failed -
- Single high-entropy queries caused false alerts
- Legitimate services sometimes generate random-looking subdomains

### How I Fixed It -
- Added per-IP tracking using `defaultdict`
- Used average entropy over multiple queries instead of single checks
- Introdued a query limit threshold before raising critical alerts

### Security Insight -
- DNS tunneling is commonly used for data exfiltration and C2 communication
- High entropy alone is not enough; behavioral analysis is required
- Monitoring frequency + entropy significantly improves detection accuracy
