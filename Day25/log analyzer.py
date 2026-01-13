import os
import re

LOG_FILE = "access.log"
FAILED_LIMIT = 3

failed_attempts = {}

def analyze_log():
    if not os.path.exists(LOG_FILE):
        print("Log file not found")
        return

    with open(LOG_FILE, "r") as file:
        lines = file.readlines()

    for line in lines:
        ip_match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
        status_match = re.search(r"\s(401|403)\s", line)

        if ip_match and status_match:
            ip = ip_match.group()
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    print("\n--- Suspicious IP Report ---")
    for ip, count in failed_attempts.items():
        if count >= FAILED_LIMIT:
            print(f"ALERT: {ip} failed {count} times")

def create_sample_log():
    sample_logs = [
        "192.168.1.10 - - 401",
        "192.168.1.10 - - 401",
        "192.168.1.10 - - 403",
        "10.0.0.5 - - 200",
        "172.16.0.3 - - 401",
        "172.16.0.3 - - 401",
    ]
    with open(LOG_FILE, "w") as f:
        for log in sample_logs:
            f.write(log + "\n")
    print("Sample log file created")

while True:
    print("\n1. Create Sample Log")
    print("2. Analyze Logs")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        create_sample_log()
    elif choice == "2":
        analyze_log()
    elif choice == "3":
        break
    else:
        print("Invalid option")
