import uuid

sessions = {}
TIMEOUT = 3  # allowed actions per session

while True:
    print("\n1. Login\n2. Do Action\n3. Logout\n4. Exit")
    choice = input("Choice: ")

    if choice == "1":
        user = input("Username: ")
        session_id = str(uuid.uuid4())
        sessions[session_id] = {"user": user, "actions": 0}
        print("Logged in. Session ID:", session_id)

    elif choice == "2":
        sid = input("Enter session ID: ")
        if sid in sessions:
            sessions[sid]["actions"] += 1
            if sessions[sid]["actions"] > TIMEOUT:
                print("Session expired")
                del sessions[sid]
            else:
                print("Action allowed for", sessions[sid]["user"])
        else:
            print("Invalid or expired session")

    elif choice == "3":
        sid = input("Enter session ID: ")
        if sid in sessions:
            del sessions[sid]
            print("Logged out")
        else:
            print("Session not found")

    elif choice == "4":
        break

    else:
        print("Invalid option")
