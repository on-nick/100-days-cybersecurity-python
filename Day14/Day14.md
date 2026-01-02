## Day X

### What I Learned
- Learned how to use the `time` module to measure execution time
- Understood how to calculate Words Per Minute (WPM)
- Used string methods like `.split()` for word counting
- Compared user input with an expected string for validation

### What I Built
- Built a Python typing speed test program
- Displayed a phrase for the user to type
- Measured typing duration using timestamps
- Calculated and displayed typing speed in WPM
- Validated typed input against the original phrase

### What Failed
- Incorrect WPM calculation in early attempts
- Small timing inaccuracies caused wrong speed output
- Program failed completely when user input had minor typos

### How I Fixed It
- Used `time.time()` to accurately record start and end times
- Converted time from seconds to minutes before WPM calculation
- Rounded WPM output for cleaner display
- Performed exact string comparison for validation

### Security Insight
- Demonstrated the importance of strict input validation
- Highlighted how timing measurements are used in security systems
- Showed how timing differences ca
