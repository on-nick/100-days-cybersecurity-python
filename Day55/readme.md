### What I Learned
- How container isolation works in Docker and how certain configuration flags can weaken that isolation.
- The security impact of running containers in privileged mode.
- Why sharing host namespaces (PID and network) increases breakout risk.
- How adding Linux capabilities (`CapAdd`) can expand the attack surface.
- The danger of bind mounts—especially mounting the host root (`/`) inside a container.
- How to translate configuration checks into a simple risk scoring model for faster security assessment.

---

### What I Built
- A lightweight Docker Breakout Risk Analyzer.
- A tool that parses a `docker inspect` JSON file.
- A scoring system that:
  - Flags privileged mode as critical.
  - Detects host PID and network namespace sharing.
  - Identifies added Linux capabilities.
  - Warns about host bind mounts.
  - Assigns a cumulative risk score.
- A clear risk classification output (Low, Moderate, High).

---

### What Failed
- Initially underestimated how common risky configurations are in development environments.
- The script assumed a single-container JSON structure and failed on unexpected formats.
- Error handling was too broad (`except:`), making debugging harder.

---

### How I Fixed It
- Improved validation of the inspect file structure before processing.
- Added clearer error messaging for invalid JSON inputs.
- Refined scoring thresholds to better reflect real-world breakout risk.
- Tested the analyzer against multiple Docker inspect outputs for reliability.

---

### Security Insight
Container breakout risk is rarely caused by a single flag. It’s usually the combination of:
- Privileged mode
- Host namespace sharing
- Excessive Linux capabilities
- Host filesystem mounts

Even one critical misconfiguration (like mounting `/` or enabling privileged mode) can effectively remove container isolation. Security hardening should always follow the principle of least privilege.
