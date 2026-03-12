import hashlib
import time

HASH_FILE = input("Enter file containing password hashes: ")
WORDLIST = input("Enter dictionary wordlist: ")

def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

try:
    with open(HASH_FILE) as f:
        hashes = [line.strip() for line in f if line.strip()]
except:
    print("Hash file not found")
    exit()

try:
    with open(WORDLIST) as f:
        words = [line.strip() for line in f if line.strip()]
except:
    print("Wordlist not found")
    exit()

print("\nStarting dictionary attack simulation...\n")

start_time = time.time()
cracked = {}

for word in words:
    h = hash_password(word)

    for target in hashes:
        if h == target and target not in cracked:
            cracked[target] = word
            print("[CRACKED] Hash:", target)
            print("Password:", word, "\n")

end_time = time.time()

print("Attack finished\n")

print("Total hashes:", len(hashes))
print("Cracked hashes:", len(cracked))
print("Time taken:", round(end_time - start_time, 2), "seconds")

if len(cracked) == 0:
    print("No passwords were cracked")
