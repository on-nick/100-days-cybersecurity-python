### What I Learned
- How JSON Web Tokens (JWTs) are structured into header, payload, and signature components.
- Why insecure algorithms like `alg: none` are dangerous in authentication systems.
- How token replay attacks work and how time-based tracking can help detect them.
- The importance of validating token expiration (`exp`) in real time.

### What I Built
- A simple JWT abuse detection engine that analyzes tokens interactively.
- Logic to decode Base64URL-encoded JWT components safely.
- A replay-attack detection mechanism using a sliding time window.
- Alerts for insecure algorithms, expired tokens, and excessive reuse.

### What Failed
- Initial decoding attempts failed when Base64 padding was missing.
- Tokens without a `jti` field caused unreliable replay tracking.
- Early versions did not clean old timestamps, causing false positives.

### How I Fixed It
- Added dynamic Base64 padding handling to ensure reliable decoding.
- Used the full token as a fallback identifier when `jti` is absent.
- Implemented a rolling time window to discard outdated usage records.

### Security Insight
- JWTs should never rely on insecure algorithms like `none`.
- Token replay is a real-world threat, especially for stateless authentication.
- Even valid tokens become dangerous if reused excessively.
- Defensive monitoring adds an extra security layer beyond signature checks.
