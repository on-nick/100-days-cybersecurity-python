### What I Learned
- How to monitor system-level changes by repeatedly checking a directory
- How set comparisons can quickly detect additions and removals
- Why polling intervals matter for balancing responsiveness and performance
- How naming conventions (like device prefixes) can be used for filtering

### What I Built
- A simple USB device monitor that detects when storage devices are connected or removed
- A lightweight alert system that reports events in real time via the console

### What Failed
- The script initially detected many non-USB system changes
- Some device events were missed if they happened too quickly
- It relied on assumptions about device naming that may not hold on all systems

### How I Fixed It
- Filtered results to only include devices with specific prefixes
- Used set differences to reliably track state changes
- Added a consistent scan interval to stabilize detection

### Security Insight
- Monitoring device connections can help detect unauthorized hardware access
- Simple visibility tools like this are a first step toward intrusion detection
- Relying only on polling is limited and can be bypassed without deeper system hooks
