### What I Learned
- How CORS (Cross-Origin Resource Sharing) controls which domains can access a web server’s resources.
- Learned that misconfigured CORS policies can allow unauthorized domains to read sensitive data.
- Understood the role of headers like Access-Control-Allow-Origin and Access-Control-Allow-Credentials.
- Learned how attackers can test different origins to identify weak CORS implementations.

### What I Built
- A Python-based CORS Misconfiguration Scanner.
- The tool sends HTTP requests to a target URL using different malicious or suspicious Origin headers.
- It analyzes the server’s response headers to determine how CORS is configured.
- The program identifies dangerous configurations, such as allowing all origins with credentials or reflecting arbitrary origins.
- It categorizes results into critical issues, warnings, and informational responses.

### What Failed
- Some servers block or ignore custom Origin headers, leading to incomplete results.
- The tool only tests a limited set of origins and may miss edge-case misconfigurations.
- It does not analyze preflight (OPTIONS) requests, which are important in real CORS behavior.

### How I Fixed It
- Added multiple test origins to simulate different attack scenarios.
- Implemented checks for both wildcard origins and reflected origins.
- Included exception handling to manage failed requests without stopping the scan.

### Security Insight
- Misconfigured CORS policies can expose sensitive APIs to malicious websites.
- Allowing credentials with a wildcard origin is a critical vulnerability.
- Proper CORS configuration should restrict trusted domains and avoid reflecting arbitrary origins.
