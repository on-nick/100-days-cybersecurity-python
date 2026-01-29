### What I Learned
- How to monitor a directory for file changes using Python.  
- Understanding basic HIDS (Host-based Intrusion Detection System) concepts like detecting file creation, modification, and deletion.  
- Using `os.listdir` and `os.path.getsize` to track the state of files over time.  
- Implementing a simple alert mechanism to detect suspicious activity.  
- The importance of maintaining a snapshot of known files to detect changes effectively.  

### What I Built
- A lightweight Python-based HIDS that monitors a directory for any file changes.  
- Alerts for three types of changes: new files, modified files, and deleted files.  
- A threshold system that triggers a critical alert when multiple suspicious changes occur.  
- A simple loop with periodic snapshots to continuously track changes in the target directory.  

### What Failed
- Initially, there was no handling for multiple rapid changes, which could cause repeated alerts for the same file.  
- The system didn’t distinguish between legitimate changes and potentially harmful modifications.  
- If the program crashes or restarts, all prior changes are lost because snapshots are only stored in memory.  

### How I Fixed It
- Introduced a `change_count` variable to track multiple changes before triggering a critical alert.  
- Used `os.makedirs` to ensure the monitored directory exists before starting the HIDS.  
- Updated snapshots after each check to accurately track current file states.  

### Security Insight
- Even a simple script can act as a basic HIDS to alert on unexpected file activity.  
- Monitoring file integrity is crucial for detecting unauthorized changes or potential intrusions.  
- Threshold-based alerts can help reduce noise and focus on significant suspicious activity.  
