import csv
import os

LOG_FILE = "audit_log.csv"

def checksum(text):
    return sum(ord(c) for c in text)

def write_log(action):
    check = checksum(action)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([action, check])
    print("Action logged")

def verify_logs():
    if not os.path.exists(LOG_FILE):
        print("No logs found")
        return

    with open(LOG_FILE, "r") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader, 1):
            action, saved_check = row
            if checksum(action) != int(saved_check):
                print(f"Tampering detected at log {i}")
                return
    print("All logs are intact")

while True:
    print("\n1. Add Log\n2. Verify Logs\n3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        action = input("Enter action: ")
        write_log(action)
    elif choice == "2":
        verify_logs()
    elif choice == "3":
        break
    else:
        print("Invalid option")
