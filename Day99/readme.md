### What I Learned
- How clipboard hijacking malware targets copied cryptocurrency wallet addresses and replaces them with attacker-controlled ones.
- Learned how clipboard monitoring can be used to detect suspicious changes in real time.
- Understood how regular expressions help identify patterns for Bitcoin and Ethereum wallet addresses.
- Gained insight into how simple automation can be used for behavioral security detection.

### What I Built
- A Python-based Clipboard Hijacking Detector.
- The tool continuously monitors clipboard content for changes.
- It detects when cryptocurrency wallet addresses are copied.
- If the clipboard content changes immediately after copying a wallet address, it raises an alert.
- The program provides real-time feedback about clipboard activity and potential threats.

### What Failed
- Frequent clipboard changes (normal usage) could trigger unnecessary alerts.
- The detection relies on basic regex patterns and may not cover all cryptocurrency formats.
- Continuous monitoring may consume system resources over time.

### How I Fixed It
- Implemented a comparison between current and previous clipboard content to detect meaningful changes.
- Added pattern checks specifically for crypto wallet formats to reduce noise.
- Used a short delay loop to balance responsiveness and resource usage.

### Security Insight
- Clipboard hijacking is a common attack in cryptocurrency transactions, where users may unknowingly send funds to attackers.
- Monitoring clipboard behavior can help detect suspicious replacements early.
- Users should always verify wallet addresses before completing transactions, even if they were copied directly.
