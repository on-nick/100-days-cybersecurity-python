import crypt

SHADOW_FILE = "/etc/shadow"
WEAK_PREFIXES = ["$1$", "$2$", "$2a$", "$2y$"]  # MD5, Blowfish variants
STRONG_PREFIXES = ["$5$", "$6$"]  # SHA-256, SHA-512

print("Shadow Password Weak Hash Detector\n")

try:
    with open(SHADOW_FILE, "r") as f:
        lines = f.readlines()
except PermissionError:
    print("Permission denied. Run as root.")
    exit()
except:
    print("Unable to read shadow file.")
    exit()

for line in lines:
    parts = line.strip().split(":")
    if len(parts) < 2:
        continue

    user = parts[0]
    password_hash = parts[1]

    if password_hash in ["*", "!", "!!"]:
        continue

    if any(password_hash.startswith(prefix) for prefix in WEAK_PREFIXES):
        print(f"[ALERT] Weak hash algorithm used for user: {user}")
        print(" Hash prefix:", password_hash[:4], "\n")

    elif not any(password_hash.startswith(prefix) for prefix in STRONG_PREFIXES):
        print(f"[WARNING] Unknown or custom hash type for user: {user}")
        print(" Hash prefix:", password_hash[:4], "\n")

print("Scan Complete")
