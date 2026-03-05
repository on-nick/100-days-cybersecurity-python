### What I Learned

* How Linux stores active TCP connection information inside `/proc/net/tcp`.
* How socket **inodes** link network connections to running processes.
* How to navigate the `/proc` filesystem to inspect process file descriptors.
* How basic threat-hunting can be done using Python by correlating ports with process IDs.
* Why ports above 1024 are commonly used by user processes and may sometimes indicate unusual services.

### What I Built

* A small **Python security utility** that scans active TCP connections on a Linux system.
* The script maps socket **inodes to listening ports**, then searches through `/proc/[PID]/fd` directories to identify which processes own those sockets.
* If a process is bound to a port above **1024**, the script flags it as potentially suspicious and prints the process ID with the port number.
* This demonstrates a simple **process-to-network mapping technique** often used in security monitoring.

### What Failed

* At first, some processes caused permission errors when accessing their file descriptor folders.
* Certain sockets appeared without a matching process due to timing issues (process exits during scan).
* Some legitimate services running on high ports were flagged as suspicious, creating false positives.

### How I Fixed It

* Added exception handling so the scanner skips processes it cannot access.
* Continued scanning even when directories disappear mid-execution.
* Focused the output only on **high-numbered ports** to reduce noise and highlight potentially unusual services.

### Security Insight

The `/proc` filesystem exposes powerful runtime information about processes, sockets, and system activity. By correlating **socket inodes with process file descriptors**, defenders can identify which applications are opening network ports. This technique is useful in **malware investigation, intrusion detection, and incident response**, because unauthorized backdoors often run as hidden processes that listen on uncommon ports.
