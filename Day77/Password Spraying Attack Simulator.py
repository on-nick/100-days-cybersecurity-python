import hashlib

print("Password Spraying Simulator\n")

# Simulated user database
users = {
    "alice": hashlib.sha256("password123".encode()).hexdigest(),
    "bob": hashlib.sha256("welcome".encode()).hexdigest(),
    "charlie": hashlib.sha256("admin".encode()).hexdigest(),
    "david": hashlib.sha256("letmein".encode()).hexdigest()
}

common_passwords = [
    "123456",
    "password",
    "password123",
    "admin",
    "welcome",
    "letmein"
]

print("Running password spraying attack...\n")

compromised = []

for pwd in common_passwords:
    hashed = hashlib.sha256(pwd.encode()).hexdigest()

    for user, stored_hash in users.items():
        if hashed == stored_hash:
            print("[ALERT] Weak password detected")
            print(" User:", user)
            print(" Password:", pwd, "\n")
            compromised.append(user)

print("Attack simulation complete")

if not compromised:
    print("No weak passwords detected")
