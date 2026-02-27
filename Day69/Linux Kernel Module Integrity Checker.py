import os
import hashlib

MODULES_FILE = "/proc/modules"
MODULES_DIR = "/lib/modules"

print("Kernel Module Integrity Checker Started\n")

def hash_file(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while chunk := f.read(4096):
                h.update(chunk)
        return h.hexdigest()
    except:
        return None

# Get loaded modules
try:
    with open(MODULES_FILE, "r") as f:
        loaded_modules = [line.split()[0] for line in f.readlines()]
except:
    print("Cannot read /proc/modules")
    exit()

for module in loaded_modules:
    found = False

    for root, _, files in os.walk(MODULES_DIR):
        for file in files:
            if file.startswith(module) and file.endswith(".ko"):
                path = os.path.join(root, file)
                file_hash = hash_file(path)
                print(f"[INFO] Module: {module}")
                print(" Path:", path)
                print(" SHA256:", file_hash, "\n")
                found = True
                break
        if found:
            break

    if not found:
        print(f"[ALERT] Loaded module not found on disk: {module}\n")

print("Scan Complete")
