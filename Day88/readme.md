### What I Learned
- How browsers store cookies in local SQLite databases and how they can be analyzed programmatically.
- Learned the importance of cookie security flags such as **Secure** and **HttpOnly** in protecting user sessions.
- Understood that cookies without proper flags can be vulnerable to attacks like session hijacking and cross-site scripting (XSS).
- Gained experience working with SQLite databases using Python.

### What I Built
- A Python-based Browser Cookie Security Analyzer.
- The tool reads a browser’s cookie database and extracts relevant fields such as domain, cookie name, and security flags.
- It checks whether cookies have the **Secure** and **HttpOnly** attributes enabled.
- The program flags cookies missing these protections and provides a summary of potentially insecure cookies.

### What Failed
- The script depends on a specific cookie database schema, so it may not work with all browsers or versions.
- Some cookies are intentionally set without certain flags, leading to false positives.
- Encrypted cookie values or restricted database access may limit analysis in some environments.

### How I Fixed It
- Added file existence checks to ensure the database path is valid before processing.
- Implemented error handling for database connection and query execution.
- Structured the analysis to clearly separate checks for Secure and HttpOnly flags for better readability.

### Security Insight
- Cookies without the **Secure** flag can be transmitted over unencrypted connections, making them vulnerable to interception.
- Cookies without the **HttpOnly** flag can be accessed via JavaScript, increasing the risk of theft through XSS attacks.
- Regular auditing of browser cookies helps identify weak configurations and improve overall session security.
