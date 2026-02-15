import os

SYSTEMD_PATHS = [
    "/etc/systemd/system",
    "/lib/systemd/system",
    os.path.expanduser("~/.config/systemd/user")
]

SUSPICIOUS_KEYWORDS = [
    "/tmp",
    "/dev/shm",
    "curl ",
    "wget ",
    "bash -c",
    "nc ",
    "python -c"
]

print("Systemd Persistence Detector Started\n")

def scan_service(path):
    try:
        with open(path, "r", errors="ignore") as f:
            content = f.read()

        for keyword in SUSPICIOUS_KEYWORDS:
            if keyword in content:
                print(f"[ALERT] Suspicious service file detected: {path}")
                print(f"  Matched keyword: {keyword}\n")
                break

    except:
        pass

for base_path in SYSTEMD_PATHS:
    if os.path.isdir(base_path):
        for root, _, files in os.walk(base_path):
            for file in files:
                if file.endswith(".service"):
                    scan_service(os.path.join(root, file))

print("Scan Complete")
