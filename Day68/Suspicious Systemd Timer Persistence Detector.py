import os

SYSTEMD_TIMER_PATHS = [
    "/etc/systemd/system",
    "/lib/systemd/system",
    os.path.expanduser("~/.config/systemd/user")
]

SUSPICIOUS_KEYWORDS = [
    "/tmp/",
    "/dev/shm/",
    "curl ",
    "wget ",
    "nc ",
    "bash -c",
    "python -c"
]

print("Systemd Timer Persistence Detector Started\n")

def scan_timer(timer_path):
    try:
        with open(timer_path, "r", errors="ignore") as f:
            content = f.read()

        for keyword in SUSPICIOUS_KEYWORDS:
            if keyword in content:
                print("[ALERT] Suspicious systemd timer detected")
                print(" File:", timer_path)
                print(" Matched:", keyword, "\n")
                break

    except:
        pass

for base_path in SYSTEMD_TIMER_PATHS:
    if not os.path.isdir(base_path):
        continue

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".timer"):
                scan_timer(os.path.join(root, file))

print("Scan Complete")
