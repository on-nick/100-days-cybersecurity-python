### What I Learned
- How to create a basic session management system using Python dictionaries.
- Using `uuid.uuid4()` to generate unique session IDs.
- Implementing a simple action-based session timeout (limited number of actions per session).
- Handling user input for login, logout, and actions.

### What I Built
- A command-line session management tool that:
  - Allows users to log in and get a unique session ID.
  - Tracks the number of actions each user performs.
  - Expires a session after a set number of actions (`TIMEOUT = 3`).
  - Supports logging out and exiting the program.

### What Failed
- The program doesn’t handle simultaneous users in real applications (it’s single-threaded and CLI-based).
- Session timeout is action-based, not time-based, which may not be secure in a real-world scenario.
- No authentication for users; anyone can log in as any username.
- The session ID is typed manually for actions and logout, which is error-prone.

### How I Fixed It
- Implemented action counting and automatic session deletion when exceeding the allowed `TIMEOUT`.
- Added checks for invalid session IDs to prevent errors.

### Security Insight
- Using UUIDs for session IDs is better than predictable IDs, but they should be kept secret.
- Real-world session management should include:
  - Password authentication.
  - Expiry based on time, not just actions.
  - Secure storage of session IDs.
  - Protection against session hijacking (e.g., HTTPS, secure cookies).
- Manual input of session IDs is unsafe; in a real application, session tokens are stored and sent automatically.
