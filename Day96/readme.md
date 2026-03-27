### What I Learned
- How HTTP/2 handles multiple streams over a single connection and how this feature can be abused.
- Learned about the HTTP/2 Rapid Reset attack, where repeated request resets can overwhelm server resources.
- Understood how TLS connections are established before HTTP/2 communication begins.
- Gained insight into how concurrency (multi-threading) can amplify the impact of network-based attacks.

### What I Built
- A Python-based HTTP/2 Rapid Reset Attack Simulator.
- The tool establishes secure TLS connections to a target server.
- It sends repeated HTTP/2 preface frames to simulate rapid request behavior.
- Multiple threads are used to create parallel connections, increasing the intensity of the test.
- The program demonstrates how repeated rapid interactions can stress server resources.

### What Failed
- The simulation does not fully implement the HTTP/2 protocol, so it cannot replicate real rapid reset behavior accurately.
- Some servers may ignore or drop malformed or incomplete HTTP/2 frames.
- Network restrictions or protections may block repeated connection attempts.

### How I Fixed It
- Used threading to simulate concurrent request behavior and increase load.
- Wrapped sockets with SSL to ensure proper TLS communication with modern servers.
- Added exception handling to manage connection failures gracefully.

### Security Insight
- The HTTP/2 Rapid Reset attack can lead to denial-of-service (DoS) conditions by exhausting server resources.
- Even well-configured servers can be vulnerable if proper rate limiting and request handling controls are not in place.
- Mitigation strategies include request rate limiting, connection throttling, and applying patches provided by server vendors.
