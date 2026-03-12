### What I Learned
- How password hashes are used to store credentials securely instead of storing plain text passwords.
- Learned how the SHA-256 hashing algorithm works and how the same input always produces the same hash output.
- Understood how dictionary attacks attempt to crack passwords by hashing many common words and comparing them against stored hashes.
- Learned how to measure attack performance using execution time and track results during the cracking process.

### What I Built
- A Python-based dictionary attack simulation tool.
- The script reads password hashes from a file and compares them with hashes generated from a wordlist.
- Each word from the dictionary is hashed using SHA-256 and checked against the target hashes.
- If a match is found, the original password corresponding to the hash is revealed.
- The program also reports the number of cracked passwords and the total time taken for the attack.

### What Failed
- Weak or small wordlists reduced the chances of cracking passwords successfully.
- The attack was slower when large wordlists were used because each word needed to be hashed and compared with all target hashes.
- If the password hashes were generated with salting or stronger hashing methods, the attack would fail.

### How I Fixed It
- Added error handling to ensure the hash file and wordlist file exist before running the attack.
- Stored cracked hashes in a dictionary to prevent repeated reporting of the same cracked password.
- Measured the total execution time to better understand the performance of the attack.

### Security Insight
- Dictionary attacks demonstrate why weak or commonly used passwords are dangerous.
- Even strong hashing algorithms like SHA-256 cannot protect accounts if users choose predictable passwords.
- Security systems often defend against such attacks by using salting, slow hashing algorithms (like bcrypt), and strong password policies.
