import json
import getpass

DATA_FILE = "vault.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {"pin": None, "notes": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

if data["pin"] is None:
    data["pin"] = getpass.getpass("Set new PIN: ")
    save_data(data)
    print("PIN set successfully")

pin = getpass.getpass("Enter PIN: ")

if pin != data["pin"]:
    print("Access denied")
    exit()

while True:
    print("\n1. Add Note\n2. View Notes\n3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        note = input("Enter note: ")
        data["notes"].append(note)
        save_data(data)
        print("Note saved securely")

    elif choice == "2":
        print("\n--- Your Secure Notes ---")
        for i, n in enumerate(data["notes"], 1):
            print(i, n)

    elif choice == "3":
        break

    else:
        print("Invalid option")
