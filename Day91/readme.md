### What I Learned
- How covert channels can be used to transfer data in ways that are not easily detected by traditional security mechanisms.
- Learned that ICMP (commonly used for ping) can be misused to carry hidden data payloads.
- Understood how encoding techniques like Base64 can help disguise the original data during transmission.
- Gained insight into packet crafting and network-level communication using low-level tools.

### What I Built
- A Python-based ICMP covert data exfiltration simulation tool.
- The program takes input data, encodes it using Base64, and splits it into smaller chunks.
- Each chunk is embedded into ICMP packets and sent to a target IP address.
- The tool simulates how data can be transmitted stealthily over a network using non-traditional channels.

### What Failed
- The tool does not implement a receiving mechanism to reconstruct the transmitted data on the target side.
- Some networks may block or filter ICMP traffic, preventing successful transmission.
- Large data inputs increase the number of packets, making the activity more detectable.

### How I Fixed It
- Divided encoded data into smaller chunks to ensure compatibility with packet size limits.
- Used Base64 encoding to safely convert data into a transmissible format.
- Simplified packet sending with controlled output to track transmission progress.

### Security Insight
- ICMP traffic is often overlooked in security monitoring, making it a potential channel for covert data exfiltration.
- Attackers can exploit trusted protocols to bypass firewalls or detection systems.
- Monitoring unusual ICMP traffic patterns and implementing network filtering rules can help mitigate such risks.
