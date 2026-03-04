# GTFOBins SUID Abuse Detector

## What I Learned
- How SUID (Set User ID) permissions work in Linux and why they can introduce privilege escalation risks.
- How attackers abuse legitimate binaries listed in GTFOBins to gain elevated access.
- How to use Python’s built-in modules to inspect file metadata and permission bits.
- The importance of automating security checks during system audits.
- Why monitoring trusted system paths like `/bin`, `/usr/bin`, and `/usr/local/bin` is critical for system hardening.

## What I Built
- A Python-based SUID scanner that recursively searches common system binary directories.
- A detection mechanism that identifies files with the SUID permission bit enabled.
- A high-risk alert system that flags binaries commonly abused for privilege escalation (e.g., `find`, `vim`, `nano`, `awk`, `perl`, etc.).
- A categorized output system that distinguishes between:
  - **[CRITICAL]** High-risk GTFOBins-listed SUID binaries
  - **[INFO]** Other SUID binaries detected

## What Failed
- Initially, the script did not properly handle permission errors when accessing certain directories.
- Some system paths generated exceptions due to restricted access.
- Early output formatting was cluttered and difficult to read during larger scans.

## How I Fixed It
- Implemented exception handling to gracefully skip inaccessible files and directories.
- Improved output formatting to clearly separate critical findings from informational results.
- Limited scanning to common executable paths to reduce noise and improve performance.

## Security Insight
SUID binaries are not inherently malicious, but when combined with GTFOBins-listed tools, they can become powerful privilege escalation vectors. Regular auditing of SUID permissions helps detect misconfigurations before attackers can exploit them. Automating this process strengthens defensive security posture and reduces manual review errors.
