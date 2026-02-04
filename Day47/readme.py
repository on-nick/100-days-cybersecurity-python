### What I Learned
- Learned to use **Tkinter** to build a simple GUI application in Python.
- Learned to handle **Text widgets** to collect multi-line user input.
- Learned to open multiple URLs at once using the **webbrowser** module.
- Practiced basic **event handling** with buttons in a GUI.

### What I Built
- A **Bulk Link Opener** GUI tool where users can paste multiple URLs, one per line, and open them all at once in new browser tabs.
- Simple and clean interface with a text box and an “Open Links” button.

### What Failed
- Initially struggled with **reading multi-line input** from the Text widget correctly.
- Faced issues with URLs that had extra spaces or empty lines, which caused errors.

### How I Fixed It
- Used `.strip()` and `.split("\n")` to clean and separate each URL.
- Added a **check to ignore empty lines** before opening a link.
- Ensured each URL opens in a new browser tab instead of the same one.

