---

## What I Learned
- How TLS/SSL handshakes work at a high level  
- How certificate metadata like expiration dates is structured  
- Why certificate lifecycle management is critical for security  
- The limitations of basic certificate inspection without deeper cryptographic parsing  

---

## What I Built
- A command-line tool concept for scanning HTTPS services  
- Logic to identify:
  - Certificates nearing expiration  
  - Potentially weak cryptographic configurations  
- A simple interactive workflow for testing multiple domains  

---

## What Failed
- Reliably extracting public key size information from standard certificate metadata  
- Handling all edge cases (invalid certificates, non-HTTPS services, network failures)  
- Detecting deeper TLS misconfigurations beyond surface-level checks  

---

## How I Fixed It
- Improved error handling to prevent crashes during failed scans  
- Used secure default TLS settings instead of manual configuration  
- Treated missing certificate fields as a limitation rather than a failure  

---

## Security Insight
HTTPS alone does not guarantee strong security. Certificates can be expired, misconfigured, or cryptographically weak. Regular certificate monitoring is essential to avoid service outages and reduce attack surface, especially in production environments.

---
