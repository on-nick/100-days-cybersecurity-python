### What I Learned
- How DNS rebinding attacks exploit the way browsers trust the same domain across different IP resolutions.
- Learned that an attacker can first point a domain to an external IP and later “rebind” it to an internal IP (e.g., localhost).
- Understood how this technique can allow access to internal services that are normally not exposed to the internet.
- Learned how simple HTTP servers can simulate internal services for testing security scenarios.

### What I Built
- A Python-based simulation of a DNS rebinding attack.
- The program starts a local HTTP server to represent an internal service.
- It simulates DNS behavior by showing how a domain initially resolves to an external IP and then switches to an internal IP.
- Demonstrates how a browser could unknowingly access internal resources through the same trusted domain.

### What Failed
- The simulation does not perform real DNS rebinding; it only mimics the behavior conceptually.
- No actual browser interaction is involved, so the full real-world impact is not demonstrated.
- The internal server is simplistic and does not represent complex real services.

### How I Fixed It
- Used threading to run the internal server concurrently with the simulation logic.
- Structured the simulation with delays to clearly show the transition from external to internal IP.
- Simplified the demonstration to focus on the core concept without requiring real DNS manipulation.

### Security Insight
- DNS rebinding can bypass same-origin policy protections and expose internal network services to attackers.
- Applications that rely solely on IP-based trust (e.g., localhost access) are especially vulnerable.
- Mitigation strategies include validating Host headers, using authentication for internal services, and implementing DNS pinning protections.
