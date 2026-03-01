### What I Learned
- How Linux exposes active network connections through `/proc/net/tcp` and `/proc/net/udp`.
- How TCP states work, especially the `LISTEN` state (`0A`) in the `/proc` filesystem.
- How to convert hexadecimal IP addresses and ports into readable formats.
- The difference between common service ports and high-risk ports.
- Basic service exposure analysis for local system security auditing.

### What I Built
- A lightweight Service Exposure Scanner for Linux systems.
- A script that reads active TCP and UDP connections directly from the `/proc` filesystem`.
- A filter that ignores common ports (22, 80, 443) to reduce noise.
- A detection mechanism that flags potentially high-risk ports (21, 23, 25, 3389, 5900).
- A simple alert system for exposed services that may require security review.

### What Failed
- Initially misinterpreted TCP connection states and displayed non-listening connections.
- Hexadecimal IP addresses were printed incorrectly before reversing byte order.
- UDP handling did not differentiate between bound and active sockets.

### How I Fixed It
- Added a condition to only display TCP sockets in the `LISTEN` state.
- Reversed the byte order when converting hexadecimal IP addresses.
- Improved parsing logic to correctly extract local address and port information.
- Implemented port filtering logic to reduce false positives.

### Security Insight
- Not all open ports are dangerous, but unnecessary exposed services increase attack surface.
- High-risk ports should be monitored carefully, especially if exposed to external networks.
- Regular system audits can help identify unintended service exposure.
- Even simple scripts can provide valuable visibility into system security posture.
