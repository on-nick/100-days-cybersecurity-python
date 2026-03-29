### What I Learned
- How subdomain takeovers occur when DNS records point to external services that are no longer properly configured.
- Learned that attackers can claim these abandoned services and gain control over the subdomain.
- Understood how DNS resolution and HTTP response analysis can help detect such vulnerabilities.
- Learned how service-specific fingerprints can indicate misconfigured or unclaimed resources.

### What I Built
- A Python-based Subdomain Takeover Checker.
- The tool generates common subdomains for a target domain and attempts to resolve them.
- For valid subdomains, it sends HTTP requests and analyzes the response content.
- It checks for known fingerprints from services like GitHub Pages, Heroku, AWS, and Azure.
- If a match is found, the tool alerts a potential subdomain takeover vulnerability.

### What Failed
- The tool only checks a limited list of common subdomains and may miss others.
- Some services may change their error messages, causing fingerprint detection to fail.
- Network timeouts or unreachable hosts can lead to incomplete scanning results.

### How I Fixed It
- Added exception handling for DNS resolution and HTTP requests to ensure smooth execution.
- Used a dictionary of service fingerprints to simplify detection logic.
- Implemented timeouts to prevent the scanner from hanging on unresponsive subdomains.

### Security Insight
- Subdomain takeovers can allow attackers to host malicious content under a trusted domain.
- This can lead to phishing, cookie theft, or reputational damage.
- Regular monitoring and proper decommissioning of external services are essential to prevent such vulnerabilities.
