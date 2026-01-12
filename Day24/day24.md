### What I Learned
- Learned how to use Python’s `hashlib` to compute SHA-256 hashes of files.  
- Understood the concept of file integrity verification using cryptographic hashing.  
- Learned to use `os.path.exists()` to safely check for the existence of a file before processing.  

### What I Built
- A Python script that computes and saves the SHA-256 hash of a file.  
- The script waits for user input to check the file again after potential modifications.  
- It then compares the original hash with the new hash to verify file integrity.  

### What Failed
- Initially, the script could crash if the file didn’t exist.  
- Reading very large files entirely into memory might be inefficient.  

### How I Fixed It
- Added a check with `os.path.exists()` to gracefully handle missing files.  
- Could be improved further by reading the file in chunks instead of all at once (not implemented yet).  

### Security Insight
- Using SHA-256 ensures a strong cryptographic hash to detect accidental or malicious file modifications.  
- This approach can serve as a simple form of tamper detection, but SHA-256 alone does not prevent intentional hash collisions if an attacker is sophisticated.  
- For higher security, this method could be combined with digital signatures or storing hashes in a secure location.  
