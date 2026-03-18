from collections import Counter
import re

print("Log Anomaly Detector\n")

log_file = input("Enter log file path: ")

# Example pattern: extract username from logs (customize as needed)
pattern = r"user=(\w+)"

try:
    with open(log_file) as f:
        logs = f.readlines()
except:
    print("Log file not found")
    exit()

user_activity = Counter()
failed_logins = Counter()

for line in logs:
    match = re.search(pattern, line)
    
    if match:
        user = match.group(1)
        user_activity[user] += 1

        if "failed" in line.lower():
            failed_logins[user] += 1

print("\nAnalyzing behavior...\n")

# Detect unusually high activity
avg_activity = sum(user_activity.values()) / len(user_activity) if user_activity else 0

for user, count in user_activity.items():
    if count > avg_activity * 2:
        print("[ALERT] Unusual activity spike")
        print("User:", user)
        print("Activity count:", count, "\n")

# Detect excessive failed logins
for user, count in failed_logins.items():
    if count > 5:
        print("[WARNING] Multiple failed login attempts")
        print("User:", user)
        print("Failed attempts:", count, "\n")

print("Analysis complete")
