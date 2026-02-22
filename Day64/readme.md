# Password Reuse Risk Analyzer

### What I Learned
- How SHA-256 hashing protects passwords by converting them into fixed-length hash values  
- Why storing plaintext passwords is insecure  
- How password reuse can be detected by comparing hashed values  
- How dictionaries can efficiently map hashes to multiple users  
- The security risks associated with credential reuse  

### What I Built
- A simple CLI-based Password Reuse Risk Analyzer  
- A system that securely hashes passwords before storage  
- A detection feature that identifies when multiple users share the same password  
- A reusable structure for basic security auditing  

### What Failed
- Initially overwrote hash entries instead of grouping users properly  
- Forgot to account for multiple users having identical hashed passwords  
- The reuse detection logic did not trigger correctly in early versions  

### How I Fixed It
- Grouped users by their hashed passwords using proper dictionary handling  
- Implemented a loop to check for hashes linked to multiple users  
- Added a flag system to clearly report when no reuse is detected  

### Security Insight
Even when passwords are hashed, reuse can still be identified if two hashes match. Password reuse is a serious security risk because if one account is compromised, attackers can potentially access all other accounts using the same password.
