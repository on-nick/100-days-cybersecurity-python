import hashlib
import os

def get_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

file_path = input("Enter file path: ")

if not os.path.exists(file_path):
    print("File not found")
    exit()

original_hash = get_hash(file_path)
print("Baseline hash saved")

input("Press Enter after modifying the file...")

new_hash = get_hash(file_path)

if original_hash == new_hash:
    print("File integrity verified (No change detected)")
else:
    print("WARNING: File has been modified!")
