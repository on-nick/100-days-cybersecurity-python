### What I Learned
- How OAuth authentication flows use parameters like access tokens and authorization codes for user authentication.
- Learned that exposing access tokens in URLs (especially in query parameters or fragments) can lead to serious security risks.
- Understood how URL parsing helps extract and analyze different components such as query strings and fragments.
- Learned about open redirect vulnerabilities and how they can be abused in OAuth flows.

### What I Built
- A Python-based OAuth Token Leakage Detector.
- The tool analyzes a given OAuth redirect URL for sensitive data exposure.
- It checks both the URL fragment and query parameters for access tokens.
- It identifies authorization codes and distinguishes them from more critical exposures.
- The program also scans for common redirect parameters that may indicate open redirect vulnerabilities.

### What Failed
- The tool relies on manually provided URLs and does not capture real-time OAuth traffic.
- It cannot verify whether a detected token is still valid or already expired.
- Some complex OAuth implementations may use different parameter names that are not covered.

### How I Fixed It
- Used URL parsing functions to accurately separate fragments and query parameters.
- Added checks for both access tokens and authorization codes to improve detection coverage.
- Included multiple common redirect parameter names to better identify potential open redirect issues.

### Security Insight
- Access tokens exposed in URLs can be leaked through browser history, logs, or referrer headers.
- Secure OAuth implementations should avoid placing sensitive tokens in URLs and prefer secure storage mechanisms.
- Open redirect vulnerabilities can be chained with OAuth flows to steal tokens or redirect users to malicious sites.
