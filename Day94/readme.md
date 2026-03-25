### What I Learned
- How WebSocket connections are established through an HTTP handshake and then upgraded to a persistent connection.
- Learned that the Origin header plays an important role in validating the source of WebSocket requests.
- Understood that improper validation of Origin can allow unauthorized cross-site WebSocket connections.
- Gained insight into low-level socket programming and crafting raw HTTP requests.

### What I Built
- A Python-based WebSocket Security Tester.
- The tool manually crafts a WebSocket handshake request with a malicious Origin header.
- It sends the request directly to the target server using a TCP socket.
- The program analyzes the server’s response to determine whether the connection upgrade is accepted.
- It identifies potential security issues if the server accepts connections from untrusted origins.

### What Failed
- Some servers require secure connections (WSS), which cannot be tested using a simple socket approach.
- The tool does not fully implement the WebSocket protocol beyond the handshake phase.
- Certain servers may respond differently based on additional headers or authentication requirements.

### How I Fixed It
- Constructed a proper WebSocket handshake request including required headers.
- Checked for key indicators like “101 Switching Protocols” and “Sec-WebSocket-Accept” in the response.
- Added exception handling to manage connection failures gracefully.

### Security Insight
- Accepting WebSocket connections without validating the Origin header can expose applications to cross-site attacks.
- Attackers can exploit this to interact with WebSocket endpoints from malicious websites.
- Proper Origin validation and authentication mechanisms are essential for securing WebSocket communications.
