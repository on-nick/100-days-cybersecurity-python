### What I Learned
- How user input can be dangerous if not properly validated.
- Basic understanding of SQL injection attacks.
- Use of Python functions, loops, and if-else conditions.
- How input sanitization works using string operations.

### What I Built
- A simple Python program that:
  - Accepts user input.
  - Detects possible SQL injection using common keywords.
  - Sanitizes input by removing unsafe characters.
  - Displays warnings and cleaned output.

### What Failed
- Initially, the program did not detect SQL keywords written in uppercase.
- Removing full keywords caused some valid input to break.
- The detection logic was too strict at first.

### How I Fixed It
- Converted user input to lowercase before checking for SQL keywords.
- Limited sanitization to special characters instead of entire words.
- Tested multiple inputs to improve detection accuracy.

### Security Insight
- User input should never be trusted by default.
- Even simple applications are vulnerable to injection attacks.
- Basic input sanitization and validation are essential for secure applications.
