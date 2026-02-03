# Supply-Chain Dependency Scanner

A lightweight tool designed to analyze dependency metadata and identify potential supply-chain security risks using heuristic-based checks.

---

## What I Learned
- Supply-chain attacks often rely on abusing trust rather than exploiting traditional vulnerabilities.
- Simple indicators such as naming patterns, maintainer age, and artifact integrity can reveal hidden risks.
- Combining multiple weak signals into a single risk score improves decision-making.

## What I Built
- A dependency risk analysis tool that:
  - Flags suspicious or low-effort package names
  - Identifies dependencies associated with known malicious artifacts
  - Evaluates maintainer trust based on account age
  - Produces a cumulative risk score with clear severity levels

## What Failed
- Relying on a single indicator (such as hashes alone) was insufficient for detecting emerging threats.
- The scanner’s accuracy depends heavily on the quality and completeness of dependency metadata.
- Early versions lacked graceful handling of missing or malformed inputs.

## How I Fixed It
- Introduced a weighted risk scoring system instead of binary trust decisions.
- Added defensive error handling to prevent crashes during scans.
- Structured the logic to allow future expansion with stronger checks and external threat intelligence.

## Security Insight
Supply-chain security is about **proactive risk reduction**, not absolute certainty. Even basic validation of dependencies can significantly reduce the attack surface when applied consistently.
