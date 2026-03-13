import os
import re

print("Secret Key Leak Scanner\n")

TARGET_DIR = input("Enter directory to scan: ")

patterns = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Generic API Key": r"api[_-]?key\s*=\s*[\"'][A-Za-z0-9_\-]{16,}[\"']",
    "Password Assignment": r"password\s*=\s*[\"'][^\"']{6,}[\"']",
    "Private Key Start": r"-----BEGIN PRIVATE KEY-----",
    "JWT Token": r"eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+"
}

findings = []

for root, dirs, files in os.walk(TARGET_DIR):
    for file in files:
        path = os.path.join(root, file)

        try:
            with open(path, "r", errors="ignore") as f:
                content = f.read()

            for name, pattern in patterns.items():
                matches = re.findall(pattern, content)

                for match in matches:
                    findings.append((name, path, match))

        except:
            continue

print("\nScan Results:\n")

if findings:
    for item in findings:
        print("[ALERT] Possible secret detected")
        print("Type:", item[0])
        print("File:", item[1])
        print("Value:", item[2][:40], "\n")
else:
    print("No secrets detected")

print("Scan complete")
