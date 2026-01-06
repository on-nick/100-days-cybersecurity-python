### What I Learned
- Learned how to use the `requests` library to send HTTP requests and check website status codes.
- Learned how to handle exceptions like connection errors and timeouts using `try-except`.
- Learned to add `https://` prefix if the user does not provide it.

### What I Built
- A Python script that takes a website URL as input and checks its HTTP status.
- It prints whether the website is reachable (status 200) or if it failed/was redirected.
- Handles incorrect URLs or request timeouts gracefully.

### What Failed
- Initially, the code threw an error because `request.get` was used instead of `requests.get`.
- URLs without `http` or `https` caused the request to fail.
- Some websites with redirects did not return status 200, so extra handling was needed.

### How I Fixed It
- Corrected `request.get` to `requests.get` to properly call the library.
- Added logic to prepend `https://` to URLs missing the protocol.
- Used exception handling (`requests.exceptions.RequestException`) to catch connection errors and timeouts.

### Security Insight
- Always validate user input when dealing with URLs to avoid malformed requests.
- Using timeouts in requests prevents the script from hanging indefinitely.
- Be cautious when sending requests to unknown URLs to avoid potential security risks or malicious responses.
