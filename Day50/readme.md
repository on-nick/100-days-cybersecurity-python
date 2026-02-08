### What I Learned
- Clipboard contents can be monitored by polling at fixed time intervals
- Hashing clipboard data allows change detection without storing previous values
- Sensitive information is frequently exposed through normal clipboard usage
- Simple keyword checks can act as an early warning for security risks

### What I Built
- A clipboard monitoring tool that detects when clipboard data changes
- A basic alert system that flags potentially sensitive copied content
- A lightweight security-awareness utility for everyday development workflows

### What Failed
- The detection relies only on keyword matching, which can cause false positives
- It cannot identify sensitive data that does not contain obvious keywords
- Clipboard polling is not event-driven and may miss very short-lived changes

### How I Fixed It
- Used hashing to avoid repeatedly processing identical clipboard content
- Normalized clipboard text to lowercase to improve keyword detection accuracy
- Added a configurable check interval to balance performance and responsiveness

### Security Insight
- The clipboard is an often-overlooked attack surface
- Secrets copied even briefly can be exposed to malicious background processes
- Developers should treat clipboard data as sensitive and minimize its use for secrets
