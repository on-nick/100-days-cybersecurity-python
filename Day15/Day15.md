### What I Learned
```
- How brute-force password guessing works by generating all possible combinations of characters.
- How nested loops and list comprehensions can be used to build combinations incrementally.
- How to measure execution time in Python using the `time` module.
- Why password length has a major impact on how long brute-force attacks take.
```

### What I Built
```
- A simple Python brute-force password checker that:
  - Takes a user-entered password.
  - Generates all lowercase alphabet combinations up to a certain length.
  - Checks whether the password appears in the generated guesses.
  - Measures and prints the time taken to find the password.
```

### What Failed
```
- The program becomes very slow as the password length increases.
- It stores all guesses in memory, which is inefficient.
- The code only works for lowercase letters and fixed-length limits.
- The password is printed in plain text, which is insecure.
```

### How I Fixed It
```
- Limited the maximum password length to reduce execution time.
- Used `break` to stop guessing as soon as the password is found.
- Structured the guessing logic to build combinations gradually instead of all at once.
- Identified places where the code could be optimized or secured in future versions.
```

### Security Insight
```
- Brute-force attacks are computationally expensive and scale exponentially with password length.
- Even simple passwords become hard to crack when length increases.
- Real systems protect passwords using hashing, salting, and rate limiting.
- Storing or displaying passwords in plain text is unsafe and should be avoided.

```
