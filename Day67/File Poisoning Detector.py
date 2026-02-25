import os

HOSTS_FILE = "/etc/hosts"
TRUSTED_DOMAINS = [
    "google.com",
    "facebook.com",
    "github.com",
    "amazon.com",
    "microsoft.com"
]

LOCAL_IPS = {"127.0.0.1", "0.0.0.0", "::1"}

print("Hosts File Poisoning Detector Started\n")

if not os.path.isfile(HOSTS_FILE):
    print("Hosts file not found")
    exit()

try:
    with open(HOSTS_FILE, "r") as f:
        lines = f.readlines()
except PermissionError:
    print("Permission denied. Try running with elevated privileges.")
    exit()

for line in lines:
    clean = line.strip()

    if not clean or clean.startswith("#"):
        continue

    parts = clean.split()
    if len(parts) < 2:
        continue

    ip = parts[0]
    domains = parts[1:]

    for domain in domains:
        if domain in TRUSTED_DOMAINS and ip not in LOCAL_IPS:
            print("[CRITICAL] Possible DNS poisoning detected!")
            print(" Domain:", domain)
            print(" Redirected To:", ip, "\n")

print("Scan Complete")
