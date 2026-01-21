### What I Learned
- How to create a basic firewall simulator in Python using lists and dictionaries.
- How to interact with the user using `input()` and handle simple control flow (`if/elif/else`).
- How to iterate through a list of rules to match specific conditions.

### What I Built
- A simple console-based firewall program that allows the user to:
  1. Add firewall rules (IP, port, and action).
  2. Check whether a network packet would be allowed or denied.
  3. View all current rules.
- Rules are stored in a Python list of dictionaries for easy lookup.

### What Failed
- The program does not validate user input (e.g., invalid IP addresses or ports).
- Port comparison is done as strings, which might cause unexpected behavior if numeric comparisons are needed.
- No persistence: rules disappear when the program exits.

### How I Fixed It
- Ensured all comparisons are done consistently as strings for now.
- Added clear prompts and messages for better user experience.
- Could improve later by adding input validation and saving rules to a file.

### Security Insight
- This program simulates a basic firewall but real firewalls require robust validation and logging.
- Improper rules could accidentally allow or block traffic, showing how critical careful rule management is.
- Highlights the importance of matching both IP and port when filtering traffic.
