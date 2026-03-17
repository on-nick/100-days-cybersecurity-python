### What I Learned
- How ARP (Address Resolution Protocol) is used to map IP addresses to MAC addresses within a local network.
- Learned that ARP spoofing occurs when an attacker sends fake ARP replies to associate their MAC address with another device’s IP.
- Understood how network packet sniffing can be used to monitor and analyze real-time traffic.
- Learned how tools like Scapy can capture and inspect low-level network packets in Python.

### What I Built
- A Python-based ARP Spoofing Detection tool.
- The program listens to ARP traffic on the network in real time.
- It maintains a mapping of IP addresses to their corresponding MAC addresses.
- When a mismatch is detected for the same IP address, the tool raises an alert indicating possible spoofing.
- The system continuously monitors the network without storing packets to keep it lightweight.

### What Failed
- The tool may generate false positives in dynamic networks where IP-to-MAC mappings legitimately change.
- It does not actively verify which MAC address is legitimate; it only detects inconsistencies.
- Requires appropriate permissions (e.g., root access) to capture network packets, which can limit usability.

### How I Fixed It
- Implemented a simple IP-to-MAC mapping table to track known associations.
- Added logic to compare new ARP replies with previously observed mappings.
- Used real-time packet sniffing with a filter to focus only on ARP traffic for efficiency.

### Security Insight
- ARP spoofing is a common technique used in Man-in-the-Middle (MITM) attacks to intercept or manipulate network traffic.
- Monitoring ARP tables for unexpected changes can help detect potential attacks early.
- Effective defenses often include static ARP entries, network segmentation, and intrusion detection systems alongside monitoring tools.
