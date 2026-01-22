### What I Learned
- Hashing is a **one-way function** and cannot be reversed directly.
- Different hash algorithms can be identified by their **output length**.
- Hash “cracking” works only by **guessing inputs** and comparing hashes.
- Python’s `hashlib` library supports many secure hash algorithms.
- Clean structure and simple variables make security tools easier to understand and audit.

### What I Built
- A Python-based **hash detection and cracking tool**.
- The tool automatically detects common hash types such as:
  - MD5
  - SHA1
  - SHA224
  - SHA256
  - SHA384
  - SHA512
- It attempts to recover plaintext using a **dictionary (wordlist) attack**.
- The design is simple but extendable for learning purposes.

### What Failed
- Attempting to “convert” a hash directly back into plaintext.
- Expecting the tool to crack hashes **without the correct word in the wordlist**.
- Assuming all hashes of the same length are always the same algorithm.
- Trying to crack strong passwords with very small wordlists.

### How I Fixed It
- Switched from the idea of reversing hashes to **verifying guesses**.
- Used hash length as a **best-effort detection method**.
- Improved clarity by separating:
  - hash detection
  - hash generation
  - cracking logic
- Focused on **educational use cases** like CTFs and learning cryptography basics.

### Security Insight
- Hashing is not encryption — **lost plaintext cannot be recovered**.
- Strong passwords + salts make dictionary attacks ineffective.
- Never use MD5 or SHA1 for real password storage.
- Security tools should only be used on **systems you own or have permission to test**.
- Understanding how attacks work helps developers **build stronger defenses**.
