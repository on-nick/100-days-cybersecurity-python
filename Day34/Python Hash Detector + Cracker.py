import hashlib

# ---------- HASH DETECTION ----------
def detect_hash(hash_value):
    length = len(hash_value)

    if length == 32:
        return "md5"
    elif length == 40:
        return "sha1"
    elif length == 56:
        return "sha224"
    elif length == 64:
        return "sha256"
    elif length == 96:
        return "sha384"
    elif length == 128:
        return "sha512"
    else:
        return None


# ---------- HASH GENERATOR ----------
def make_hash(text, algo):
    algo = algo.lower()
    h = hashlib.new(algo)
    h.update(text.encode())
    return h.hexdigest()


# ---------- HASH CRACKER ----------
def crack_hash(hash_value, wordlist):
    hash_type = detect_hash(hash_value)

    if not hash_type:
        print("[-] Unknown hash type")
        return

    print(f"[+] Hash type detected: {hash_type}")

    for word in wordlist:
        word = word.strip()
        if make_hash(word, hash_type) == hash_value:
            print(f"[✓] Hash cracked!")
            print(f"[✓] Plain text: {word}")
            return

    print("[-] Password not found in wordlist")


# ---------- MAIN ----------
if __name__ == "__main__":
    hash_input = input("Enter hash: ")

    # Example wordlist (you can load from a file)
    words = [
        "password",
        "123456",
        "admin",
        "hello",
        "letmein",
        "qwerty"
    ]

    crack_hash(hash_input, words)
