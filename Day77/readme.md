### What I Learned

* I learned how a **password spraying attack** works by testing a small set of common passwords across multiple user accounts instead of repeatedly attacking a single account.
* I understood how password hashes (using SHA-256) can be compared instead of storing or checking plain-text passwords.
* I learned how weak or commonly used passwords make systems vulnerable even when hashing is used.
* I also learned how simple automation can quickly reveal insecure password practices.

### What I Built

* I built a **basic password spraying simulator** in Python.
* The program contains a simulated user database where passwords are stored as SHA-256 hashes.
* A list of commonly used passwords is tested against all users.
* When a hash matches, the script flags the account as compromised and reports the weak password.

### What Failed

* At first, I expected hashing alone to prevent password compromise.
* However, the simulation showed that hashing does not protect accounts if users choose weak passwords that attackers commonly try.
* This demonstrated that password security depends not only on encryption but also on password strength and policy.

### How I Fixed It

* I analyzed which users were compromised during the simulation.
* The fix would be enforcing **strong password policies**, such as longer passwords and avoiding common password lists.
* Additional defenses like **account lockout mechanisms, multi-factor authentication, and login monitoring** can reduce the effectiveness of password spraying attacks.

### Security Insight

Password spraying attacks succeed because many users reuse weak or predictable passwords. Even when systems store passwords securely using hashing, attackers can still gain access by guessing common passwords. Strong password policies, rate limiting, and multi-factor authentication are critical defenses against this type of attack.
