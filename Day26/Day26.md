### What I Learned
- How to parse URLs using `urllib.parse.urlparse`
- How to apply basic heuristic-based scoring to detect suspicious URLs
- How regular expressions can help identify IP-based URLs
- How small indicators (HTTPS, length, keywords) combine to assess phishing risk

### What I Built
- A simple command-line phishing URL scanner
- A risk scoring system based on multiple red flags
- An interactive menu that allows repeated URL checks

### What Failed
- The scanner can flag legitimate URLs as suspicious (false positives)
- It cannot detect sophisticated phishing sites that avoid common keywords
- No real-time validation against known phishing databases

### How I Fixed It
- Balanced detection by using multiple signals instead of a single rule
- Used a scoring threshold (low/medium/high) instead of a binary result
- Structured the code so new checks and keywords can be added easily

### Security Insight
- Phishing detection works best when multiple weak signals are combined
- HTTPS alone does not guarantee safety
- Simple static analysis can help users think critically before clicking links
- Automated tools should assist human judgment, not replace it
