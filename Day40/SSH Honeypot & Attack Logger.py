import datetime

LOG_FILE = "honeypot.log"
FAKE_USERS = ["root", "admin", "test"]

def log_attack(ip, username, password):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} | {ip} | {username} | {password}\n")

while True:
    print("\n--- SSH Login ---")
    ip = input("Source IP: ")
    username = input("Username: ")
    password = input("Password: ")

    if username in FAKE_USERS:
        print("Login failed")
        log_attack(ip, username, password)
    else:
        print("Invalid user")

    cont = input("Continue? (y/n): ")
    if cont.lower() != "y":
        break
