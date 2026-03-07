### What I Learned

* How file integrity monitoring works using cryptographic hashing.
* The role of **SHA-256 hashing** in detecting file modifications.
* How to walk through directories recursively using `os.walk()`.
* How to store and load baseline data using JSON files.
* The concept of creating a **baseline snapshot** of files and later comparing it to detect changes.
* Basic security monitoring concepts used in intrusion detection and host integrity tools.

### What I Built

* A simple **File Integrity Monitoring (FIM) tool** in Python.
* The program scans a directory, calculates SHA-256 hashes for each file, and stores them in a baseline JSON file.
* Later, it rescans the directory and compares the current file hashes with the saved baseline.
* The tool reports:

  * Deleted files
  * Modified files
  * Newly added files
* This mimics a simplified version of what security tools like Tripwire do.

### What Failed

* Initial runs produced errors when files could not be read (permission issues or locked files).
* Some files changed between scans due to normal system processes, creating unexpected alerts.
* Large directories made the scan slower than expected.

### How I Fixed It

* Added exception handling so unreadable files are safely skipped instead of crashing the program.
* Improved the hashing function to read files in chunks to avoid memory issues.
* Used JSON to reliably store and reload the baseline hash data.
* Structured the program with clear functions for creating the baseline and checking integrity.

### Security Insight

* File integrity monitoring is a **core defensive security technique** used to detect unauthorized changes.
* Attackers often modify system files, scripts, or configuration files after gaining access.
* By comparing hashes against a trusted baseline, defenders can quickly detect tampering.
* Even a simple tool like this demonstrates the principle behind professional security monitoring systems used in real environments.
