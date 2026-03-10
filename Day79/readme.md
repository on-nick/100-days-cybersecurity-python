### What I Learned
- How typosquatting works and why attackers register domains that look very similar to popular websites.
- How string similarity algorithms can be used to detect suspicious domains.
- Learned to use Python's `difflib` library, especially the SequenceMatcher function, to compare two strings and calculate a similarity ratio.
- Understood how similarity thresholds can help identify domains that might be attempting to impersonate legitimate services.

### What I Built
- A simple Python-based typosquatting detection tool.
- The program takes a domain name as input and compares it with a list of popular domains.
- It calculates the similarity score between the entered domain and known trusted domains.
- If the similarity score crosses a defined threshold, the tool raises an alert indicating possible typosquatting.

### What Failed
- Initially, the tool could flag legitimate domains as suspicious if they shared many similar characters with popular domains.
- The detection accuracy depended heavily on the similarity threshold value.
- The tool only checked against a small predefined list of domains, which limited its real-world effectiveness.

### How I Fixed It
- Introduced a similarity threshold to reduce false positives.
- Added a condition to ensure that the exact same domain is not flagged as a threat.
- Adjusted the similarity score check to only trigger alerts when the match is significantly close but not identical.

### Security Insight
- Typosquatting is a common phishing technique where attackers register domains that differ by small spelling mistakes (e.g., goggle.com vs google.com).
- Automated similarity detection can help identify potentially malicious domains before users interact with them.
- Security tools often combine string similarity checks with DNS analysis, domain age checks, and threat intelligence feeds for stronger protection.
