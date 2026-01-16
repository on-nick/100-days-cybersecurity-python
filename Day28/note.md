### What I Learned
- How to use Python’s `json` module to persist data between program runs.
- How to securely accept sensitive input using the `getpass` module.
- Basic file handling patterns (load, save, fallback defaults).
- Implementing simple authentication logic in a CLI application.
- Structuring a small program around reusable functions.

### What I Built
- A simple command-line secure notes vault.
- The app allows a user to set a PIN, authenticate, and store private notes.
- Notes are saved locally in a JSON file so they persist after the program exits.
- A menu-driven interface for adding and viewing notes.

### What Failed
- Initially, the program would crash if the data file didn’t exist.
- There was no separation between loading data and program logic.
- The PIN was not handled properly on first run.
- Error handling was too broad and unclear.

### How I Fixed It
- Added a fallback return value in `load_data()` to handle missing or invalid files.
- Created separate functions for loading and saving data.
- Checked if the PIN was `None` before prompting the user to set one.
- Simplified the program flow with clearer condition checks.

### Security Insight
- Using `getpass` prevents the PIN from being displayed on the screen.
- Storing a PIN in plain text JSON is **not secure** for real-world use.
- This project highlights why hashing (e.g., with `hashlib`) is important.
- Local file-based security is only as strong as the system permissions.
- This is a learning example, not production-grade security.
