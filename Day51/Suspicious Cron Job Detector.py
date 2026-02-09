import os

CRON_PATHS = [
    "/etc/crontab",
    "/etc/cron.d",
    "/var/spool/cron"
]

SUSPICIOUS_KEYWORDS = ["curl", "wget", "nc", "bash", "python", "sh"]

print("Cron Job Scanner Started\n")

def scan_file(path):
    try:
        with open(path, "r", errors="ignore") as f:
            for line in f:
                for key in SUSPICIOUS_KEYWORDS:
                    if key in line:
                        print(f"[ALERT] Suspicious cron command in {path}")
                        print(" >", line.strip())
    except:
        pass

for path in CRON_PATHS:
    if os.path.isfile(path):
        scan_file(path)
    elif os.path.isdir(path):
        for file in os.listdir(path):
            scan_file(os.path.join(path, file))
