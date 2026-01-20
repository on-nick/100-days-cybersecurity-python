### What I Learned
- How CAPTCHA systems use randomness to reduce automated access
- How to control user attempts using loops and counters
- How string manipulation and random selection work together
- Why even simple validation logic improves basic security

### What I Built
- A basic text-based CAPTCHA verification system
- A retry mechanism that limits incorrect attempts
- A simple access control flow that blocks repeated failures

### What Failed
- The CAPTCHA can still be brute-forced with automation
- It relies on plain text, making it weak against advanced bots
- There is no timeout or session tracking

### How I Fixed It
- Limited the number of attempts to reduce brute-force chances
- Regenerated the CAPTCHA after every failed attempt
- Used mixed characters (letters and digits) to increase complexity

### Security Insight
- CAPTCHA systems should be combined with rate limiting and logging
- Text-based CAPTCHAs alone are not secure against modern bots
- Defense-in-depth is essential for real-world authentication systems
