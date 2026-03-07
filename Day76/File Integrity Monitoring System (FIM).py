import os
import hashlib
import json

BASELINE_FILE = "baseline_hashes.json"
TARGET_DIR = input("Directory to monitor: ")

def hash_file(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while chunk := f.read(4096):
                h.update(chunk)
        return h.hexdigest()
    except:
        return None


def create_baseline():
    baseline = {}

    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            path = os.path.join(root, file)
            h = hash_file(path)
            if h:
                baseline[path] = h

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=2)

    print("Baseline created.")


def check_integrity():
    if not os.path.exists(BASELINE_FILE):
        print("No baseline found. Run baseline first.")
        return

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    current = {}

    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            path = os.path.join(root, file)
            h = hash_file(path)
            if h:
                current[path] = h

    for file, h in baseline.items():
        if file not in current:
            print("[ALERT] File deleted:", file)
        elif current[file] != h:
            print("[ALERT] File modified:", file)

    for file in current:
        if file not in baseline:
            print("[INFO] New file added:", file)


print("\n1. Create baseline")
print("2. Check integrity")

choice = input("Choice: ")

if choice == "1":
    create_baseline()
elif choice == "2":
    check_integrity()
