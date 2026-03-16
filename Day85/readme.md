### What I Learned
- How command history files can reveal risky or potentially dangerous terminal activity.
- Learned that certain shell commands, such as recursive deletion or piping downloads directly into a shell, are commonly associated with security risks.
- Understood how regular expressions can be used to detect patterns within command-line history.
- Learned how simple automation can help identify unsafe practices in system administration or development environments.

### What I Built
- A Python-based Terminal Command Risk Analyzer.
- The tool reads a bash history file and scans each command for patterns that may indicate dangerous behavior.
- It detects actions such as recursive file deletion, unsafe permission changes, downloading and executing scripts, or commands associated with reverse shells.
- When a suspicious command is detected, the program prints the warning type and the command responsible.

### What Failed
- Some legitimate administrative commands triggered warnings because they matched the defined patterns.
- The analyzer relied only on pattern matching, so it could not determine the context or intent behind the command.
- Commands written in slightly different formats sometimes bypassed the detection patterns.

### How I Fixed It
- Structured the detection logic using a dictionary of labeled patterns to clearly categorize each type of risky command.
- Added error handling to ensure the program exits gracefully if the history file cannot be read.
- Designed the analyzer to count and report the total number of suspicious commands for easier review.

### Security Insight
- Command history files can be valuable for security auditing and forensic investigations.
- Certain command patterns are often associated with malicious scripts, privilege abuse, or accidental destructive actions.
- Automated scanning of command history can help administrators identify risky practices and improve operational security awareness.
