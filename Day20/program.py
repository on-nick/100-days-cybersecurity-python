import re

def check_sensitive_info(text):
    patterns = {
        "Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "Credit Card": r"\b(?:\d[ -]*?){13,16}\b",
        "SSN": r"\b\d{3}-\d{2}-\d{4}\b",
        "IP Address": r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    }
    found = []
    for key, pattern in patterns.items():
        if re.search(pattern, text):
            found.append(key)
    return found

# Example usage
data = input("Enter text to scan for sensitive info: ")
results = check_sensitive_info(data)
if results:
    print("Potential sensitive info found:", ", ".join(results))
else:
    print("No sensitive info detected!")
