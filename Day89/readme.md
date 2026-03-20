### What I Learned
- How keystroke dynamics can be used as a behavioral biometric for user authentication.
- Learned that typing patterns, such as time intervals between keystrokes, are unique to individuals.
- Understood how timing data can be captured and compared to detect similarities or differences in behavior.
- Learned how basic statistical comparison methods can help evaluate authentication attempts.

### What I Built
- A Python-based Keystroke Dynamics Authentication system.
- The program captures typing timing data for a predefined text to create a baseline user profile.
- It then records a second typing attempt and compares it with the baseline.
- A difference score is calculated to determine how closely the two typing patterns match.
- Based on a threshold, the system decides whether authentication is successful or not.

### What Failed
- Timing accuracy depended on user input method, as using standard input introduced delays and inconsistencies.
- Small variations in typing speed could sometimes cause false authentication failures.
- The system used a fixed threshold, which may not be suitable for all users or environments.

### How I Fixed It
- Implemented a simple timing capture mechanism using time intervals between keystrokes.
- Used an average difference calculation to compare baseline and attempt patterns.
- Structured the process into two clear steps: profile creation and verification for better usability.

### Security Insight
- Keystroke dynamics provide an additional layer of authentication beyond passwords, making systems harder to compromise.
- Behavioral biometrics are difficult to replicate precisely, even if an attacker knows the password.
- Combining keystroke analysis with traditional authentication methods can significantly improve security.
