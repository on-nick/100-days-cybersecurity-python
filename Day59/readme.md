### What I Learned
- Homoglyph phishing attacks exploit visual similarities between characters from different alphabets (like Cyrillic and Latin).
- Unicode characters can look identical to normal English letters but actually be completely different characters.
- Simple normalization techniques can help detect suspicious domains.
- Comparing normalized input against trusted popular domains is an effective first-layer defense.

### What I Built
- A Homoglyph Phishing URL Detector.
- It accepts user-input domains and checks them against a list of popular websites.
- It replaces common Cyrillic homoglyphs with their Latin equivalents.
- If the normalized domain matches a trusted site but the original does not, it flags a potential phishing attempt.

### What Failed
- The first version did not account for Unicode homoglyphs, making it vulnerable to visually deceptive domains.
- It initially relied only on direct string comparison, which could not detect disguised characters.
- It does not detect all possible homoglyph variations—only a limited mapped set.

### How I Fixed It
- Added a homoglyph mapping dictionary to convert common Cyrillic characters into Latin equivalents.
- Implemented normalization logic to transform suspicious characters before comparison.
- Added a validation check comparing normalized domains to a list of popular domains.

### Security Insight
Homoglyph phishing is a powerful social engineering technique that leverages Unicode to trick users. Even simple normalization checks can significantly reduce risk. However, comprehensive protection requires expanded character mapping, IDN (Internationalized Domain Name) validation, and possibly browser-level or DNS-level security controls.
