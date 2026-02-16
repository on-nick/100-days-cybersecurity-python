import os
import re

SUDOERS_FILES = [
    "/etc/sudoers",
]

SUDOERS_DIR = "/etc/sudoers.d"

DANGEROUS_PATTERNS = [
    r"\(ALL\)\s+NOPASSWD:\s+ALL",
    r"NOPASSWD:\s+/bin/bash",
    r"NOPASSWD:\s+/usr/bin/python",
    r"NOPASSWD:\s+/bin/sh",
    r"ALL=\(ALL\)\s+ALL"
]

print("Sudoers Misconfiguration Scanner Started\n")

def scan_file(path):
    try:
        with open(path, "r", errors="ignore") as f:
            lines = f.readlines()

        for line in lines:
            clean = line.strip()
            if clean.startswith("#") or not clean:
                continue

            for pattern in DANGEROUS_PATTERNS:
                if re.search(pattern, clean):
                    print(f"[CRITICAL] Dangerous sudo rule in {path}")
                    print(" >", clean, "\n")
                    break

    except:
        pass

# Scan main sudoers file
for file in SUDOERS_FILES:
    if os.path.isfile(file):
        scan_file(file)

# Scan sudoers.d directory
if os.path.isdir(SUDOERS_DIR):
    for file in os.listdir(SUDOERS_DIR):
        scan_file(os.path.join(SUDOERS_DIR, file))

print("Scan Complete")
