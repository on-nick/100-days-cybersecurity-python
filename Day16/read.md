### What I Learned
- How to use `PyPDF2.PdfMerger` to combine multiple PDF files into a single document.
- How to iterate through files in the current working directory using `os.listdir()` and `os.getcwd()`.
- How to filter files by extension (`.pdf`) before processing them.
- The importance of properly closing file handlers (`merger.close()`).

### What I Built
- A simple Python script that automatically merges all PDF files in the current directory into one file named `merged.pdf`.

### What Failed
- Initially, the merge order was inconsistent because `os.listdir()` does not guarantee sorted output.
- Non-PDF or corrupted PDF files could cause runtime errors if not handled.

### How I Fixed It
- Sorted the file list before merging to ensure a predictable merge order.
- Limited file selection strictly to files ending with `.pdf`.
- Ensured the merger object is properly closed after writing the output file.

### Security Insight
- Running the script in directories with untrusted PDFs may expose you to malformed or malicious files.
- Always validate input files and avoid running such scripts in sensitive or system-level directories.
- Keep third-party libraries like `PyPDF2` up to date to mitigate known vulnerabilities.
