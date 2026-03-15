### What I Learned
- How HTTP security headers help protect websites from common web-based attacks.
- Learned that headers like Strict-Transport-Security, Content-Security-Policy, and X-Frame-Options add an additional layer of browser-side security.
- Understood how HTTP responses include metadata in the header section that can be inspected programmatically.
- Learned how to retrieve and analyze HTTP headers using Python and web requests.

### What I Built
- A Python-based HTTP Security Header Analyzer.
- The tool sends a request to a target website and retrieves the response headers.
- It checks whether important security headers are present.
- If a header exists, the script displays its value; if it is missing, the tool explains its purpose.
- The program also generates a summary showing how many recommended security headers are missing.

### What Failed
- Some websites blocked automated requests or redirected traffic, which sometimes prevented accurate header analysis.
- Certain headers may appear only on specific endpoints or responses, so scanning a single URL might not represent the entire site configuration.
- Network or connection issues could cause the request to fail.

### How I Fixed It
- Added exception handling to manage connection failures and prevent the script from crashing.
- Stored missing headers in a list to generate a clear summary at the end of the scan.
- Provided descriptions for each header so users can understand the security implications of missing protections.

### Security Insight
- Missing security headers can expose websites to vulnerabilities such as clickjacking, cross-site scripting (XSS), and content sniffing attacks.
- Security headers instruct browsers on how to safely handle content and restrict risky behaviors.
- Regular security header audits help developers strengthen web application defenses and align with modern security best practices.
