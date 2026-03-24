### What I Learned
- How timing attacks exploit differences in response time to extract sensitive information.
- Learned that comparing secrets character-by-character with delays can leak information about correct prefixes.
- Understood how attackers can measure execution time to gradually reconstruct a secret value.
- Learned why constant-time comparison functions are important in secure systems.

### What I Built
- A Python-based Timing Attack Simulator.
- The program simulates a vulnerable password comparison function with artificial delays.
- It measures response times for different input guesses.
- By analyzing which guesses take longer, the tool infers correct characters one by one.
- The script gradually reconstructs the full secret password.

### What Failed
- Timing differences can be inconsistent due to system noise, making results less reliable.
- The attack assumes a predictable delay, which may not exist in real-world secure systems.
- Network latency (in real scenarios) can interfere with accurate timing measurements.

### How I Fixed It
- Implemented repeated timing measurements per character to improve accuracy.
- Sorted timing results to select the most likely correct character based on maximum delay.
- Structured the guessing process iteratively to build the password step by step.

### Security Insight
- Timing attacks reveal that even small implementation details can lead to serious vulnerabilities.
- Systems that compare secrets must use constant-time comparison methods to prevent leaks.
- Cryptographic libraries and secure authentication systems are designed to mitigate such side-channel attacks.
