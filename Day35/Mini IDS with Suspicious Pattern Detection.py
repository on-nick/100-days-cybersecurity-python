import os
import re
from collections import defaultdict

LOG_FOLDER = "logs"
FAILED_LIMIT = 3

def analyze_logs():
    failed_attempts = defaultdict(int)

    for filename in os.listdir(LOG_FOLDER):
        path = os.path.join(LOG_FOLDER, filename)
        with open(path, "r") as f:
            for line in f:
                ip_match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
                status_match = re.search(r"\s(401|403)\s", line)
                if ip_match and status_match:
                    ip = ip_match.group()
                    failed_attempts[ip] += 1

    print("\n--- Suspicious IP Report ---")
    for ip, count in failed_attempts.items():
        if count >= FAILED_LIMIT:
            print(f"ALERT: {ip} failed {count} times")

def create_sample_logs():
    os.makedirs(LOG_FOLDER, exist_ok=True)
    logs = [
        "192.168.1.10 - - 401",
        "192.168.1.10 - - 401",
        "192.168.1.10 - - 403",
        "10.0.0.5 - - 200",
        "172.16.0.3 - - 401",
        "172.16.0.3 - - 401",
    ]
    with open(os.path.join(LOG_FOLDER, "access.log"), "w") as f:
        for log in logs:
            f.write(log + "\n")
    print("Sample log created")

while True:
    print("\n1. Create Sample Logs")
    print("2. Analyze Logs")
    print("3. Exit")

    choice = input("Choice: ")
    if choice == "1":
        create_sample_logs()
    elif choice == "2":
        analyze_logs()
    elif choice == "3":
        break
    else:
        print("Invalid option")
