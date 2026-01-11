import hashlib
import time

users = []

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        users.append({
            "username": username,
            "password": hash_password(password)
        })
        print("User registered successfully")

    elif choice == "2":
        username = input("Username: ")
        password = hash_password(input("Password: "))

        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Login successful")
                break
        else:
            print("Login failed")
            time.sleep(2)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
