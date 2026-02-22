import hashlib

print("Password Reuse Risk Analyzer\n")

users = {}
hash_map = {}

while True:
    print("\n1. Add User")
    print("2. Analyze Reuse")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")

        hashed = hashlib.sha256(password.encode()).hexdigest()
        users[username] = hashed

        hash_map.setdefault(hashed, []).append(username)
        print("User added")

    elif choice == "2":
        print("\nAnalyzing password reuse...\n")
        found = False

        for hashed, user_list in hash_map.items():
            if len(user_list) > 1:
                found = True
                print("[ALERT] Password reused by users:", ", ".join(user_list))

        if not found:
            print("No password reuse detected")

    elif choice == "3":
        break

    else:
        print("Invalid choice")
