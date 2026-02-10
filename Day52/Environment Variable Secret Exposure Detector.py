import os
import re

SECRET_PATTERNS = {
    "AWS Key": r"AKIA[0-9A-Z]{16}",
    "Private Key": r"-----BEGIN.*PRIVATE KEY-----",
    "JWT": r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+",
    "Generic API Key": r"[A-Za-z0-9]{32,}"
}

print("Environment Variable Secret Scanner\n")

found = False

for key, value in os.environ.items():
    for name, pattern in SECRET_PATTERNS.items():
        if re.search(pattern, value):
            print(f"[ALERT] {name} found in environment variable: {key}")
            found = True

if not found:
    print("No exposed secrets found in environment variables")
