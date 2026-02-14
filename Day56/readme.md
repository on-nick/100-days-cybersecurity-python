### What I Learned
- How typosquatting attacks exploit small spelling differences.
- How to use `difflib.SequenceMatcher` to measure string similarity.
- How attackers use character substitution (e.g., `o → 0`, `l → 1`, `a → @`) to trick users.
- How to implement a similarity threshold to detect suspicious names.

### What I Built
- A simple CLI-based Typosquatting Detection Tool.
- A similarity-checking system using string comparison.
- A basic character substitution detection mechanism.
- A loop-based interactive scanner for testing package/domain names.

### What Failed
- Exact similarity threshold tuning (too low = false positives, too high = missed attacks).
- Limited substitution checks (only basic character swaps).
- Does not detect advanced homoglyph attacks (e.g., Unicode lookalikes).

### How I Fixed It
- Adjusted the similarity threshold to 0.80 to balance detection accuracy.
- Added common character substitution checks.
- Structured logic to prevent exact matches from being falsely flagged.
- Ensured lowercase normalization to avoid case-sensitivity issues.

### Security Insight
Typosquatting is a real-world supply chain attack vector used in package managers like npm and PyPI. 
Even small character changes can trick developers into installing malicious packages.
Automated similarity detection combined with substitution analysis can significantly reduce this risk.
