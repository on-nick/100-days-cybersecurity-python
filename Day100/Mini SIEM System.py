import time
import re
import json
from collections import defaultdict

print("Mini SIEM System (Day 100 Project)\n")

log_file = input("Enter log file path: ")

# Detection rules
rules = [
    {"name": "Multiple Failed Logins", "pattern": r"failed", "threshold": 5},
    {"name": "SQL Injection Attempt", "pattern": r"(union|select|drop|--)", "threshold": 1},
    {"name": "XSS Attempt", "pattern": r"(<script>|javascript:)", "threshold": 1},
    {"name": "Sensitive File Access", "pattern": r"(etc/passwd|/admin)", "threshold": 1}
]

alert_counts = defaultdict(int)

def analyze_line(line):
    alerts = []

    for rule in rules:
        if re.search(rule["pattern"], line.lower()):
            alert_counts[rule["name"]] += 1

            if alert_counts[rule["name"]] >= rule["threshold"]:
                alerts.append(rule["name"])

    return alerts


def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line


print("\n[*] Monitoring logs in real-time...\n")

try:
    with open(log_file, "r") as f:
        for line in follow(f):
            alerts = analyze_line(line)

            if alerts:
                log_entry = {
                    "event": line.strip(),
                    "alerts": alerts,
                    "time": time.strftime("%Y-%m-%d %H:%M:%S")
                }

                print("[ALERT]", json.dumps(log_entry, indent=2))

except:
    print("Error reading log file")
