import os
import time

WATCH_DIR = "monitor"
known_files = {}
ALERT_THRESHOLD = 3
change_count = 0

os.makedirs(WATCH_DIR, exist_ok=True)

def snapshot():
    state = {}
    for f in os.listdir(WATCH_DIR):
        path = os.path.join(WATCH_DIR, f)
        if os.path.isfile(path):
            state[f] = os.path.getsize(path)
    return state

print("HIDS started... Monitoring directory:", WATCH_DIR)
known_files = snapshot()

while True:
    time.sleep(2)
    current = snapshot()

    for f in current:
        if f not in known_files:
            print(f"[ALERT] New file created: {f}")
            change_count += 1
        elif current[f] != known_files[f]:
            print(f"[ALERT] File modified: {f}")
            change_count += 1

    for f in known_files:
        if f not in current:
            print(f"[ALERT] File deleted: {f}")
            change_count += 1

    if change_count >= ALERT_THRESHOLD:
        print("\n[CRITICAL] Multiple suspicious changes detected!")
        break

    known_files = current
