import time

SUSPICIOUS_COMMANDS = [
    "sudo", "chmod 777", "chown", "/etc/passwd",
    "useradd", "usermod", "su ", "visudo"
]

LOG_FILE = "command.log"
ALERT_LIMIT = 3
events = []

print("Privilege Escalation Detector Running")

while True:
    cmd = input("\nExecuted Command: ").lower()
    timestamp = time.time()

    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {cmd}\n")

    for s in SUSPICIOUS_COMMANDS:
        if s in cmd:
            events.append(timestamp)
            print("[ALERT] Suspicious command detected")
            break

    events = [t for t in events if timestamp - t < 60]

    if len(events) >= ALERT_LIMIT:
        print("\n[CRITICAL] Possible privilege escalation attack!")
        break
