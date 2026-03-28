### What I Learned
- How browser history is stored in SQLite databases and can be analyzed programmatically.
- Learned that browsing patterns can reveal sensitive user behavior, such as visits to login or financial pages.
- Understood how keyword-based detection can help identify potentially risky or sensitive activities.
- Gained experience combining database queries with text analysis using regular expressions.

### What I Built
- A Python-based Browser History Analyzer.
- The tool extracts URLs and page titles from a browser history database.
- It scans each entry for predefined sensitive keywords.
- When a match is found, the program flags the entry as potentially risky.
- The tool provides a summary of total entries analyzed and suspicious findings.

### What Failed
- Keyword-based detection produced false positives when harmless pages contained matching words.
- Some relevant risky pages might be missed if they did not include predefined keywords.
- The tool depends on a specific database schema and may not work across all browsers.

### How I Fixed It
- Combined URL and title fields to improve detection accuracy.
- Used case-insensitive matching to ensure broader keyword coverage.
- Added error handling for file access and database query issues.

### Security Insight
- Browser history can expose sensitive user behavior and should be protected from unauthorized access.
- Analyzing history logs can help identify phishing attempts or risky browsing habits.
- Security tools should combine keyword detection with more advanced techniques like domain reputation analysis for better accuracy.
