### What I Learned
- How to use Python’s `hashlib` library to securely hash passwords.
- Implementing a simple command-line interface (CLI) for user interaction.
- Basics of storing and validating user credentials in memory.
- Using loops and conditional statements to manage program flow.

### What I Built
- A command-line user registration and login system.
- Passwords are hashed using SHA-256 before storage.
- Login validation checks hashed passwords for authentication.

### What Failed
- Initially, plain-text passwords were stored, which is insecure.
- Login verification sometimes failed if hashing wasn’t applied consistently.
- Users are only stored in memory, so data is lost when the program exits.

### How I Fixed It
- Implemented `hash_password` function to hash all passwords before storage.
- Ensured password input is hashed both during registration and login.
- Added `time.sleep(2)` delay on failed login to improve user experience.

### Security Insight
- Storing plain-text passwords is a major security risk; always hash passwords.
- SHA-256 provides basic hashing but lacks salting; adding a unique salt per user would improve security.
- In-memory storage is temporary; for real applications, use secure databases.
