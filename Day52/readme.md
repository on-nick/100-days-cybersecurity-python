### What I Learned
- Environment variables can unintentionally expose sensitive credentials  
- Regular expressions are useful for detecting common secret formats  
- Automated checks help catch security issues early in development  
- Secrets should never be assumed safe just because they’re not hard-coded  

### What I Built
- A simple security scanner that inspects environment variables  
- A pattern-based detection system for common secrets like API keys and tokens  
- A lightweight alert mechanism to flag potential exposures  

### What Failed
- Some patterns can produce false positives  
- Generic key detection may flag non-secret values  
- It cannot validate whether a detected secret is active or real  

### How I Fixed It
- Grouped secret patterns by type for clearer alerts  
- Limited detection to environment variable values only  
- Designed the tool as a warning system rather than a validator  

### Security Insight
- Environment variables are not inherently secure  
- Secrets should be rotated, scoped, and monitored  
- Automated secret scanning is a critical part of secure development workflows  
