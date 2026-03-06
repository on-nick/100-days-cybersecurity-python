import os

print("Hidden File and Directory Detector\n")

suspicious_paths = ["/tmp", "/var/tmp", "/dev/shm", os.path.expanduser("~")]

hidden_items = []

for base in suspicious_paths:
    if not os.path.exists(base):
        continue

    for root, dirs, files in os.walk(base):
        for name in dirs + files:
            if name.startswith(".") and len(name) > 2:
                path = os.path.join(root, name)
                hidden_items.append(path)

print("Scanning complete...\n")

if hidden_items:
    print("Suspicious hidden items found:\n")
    for item in hidden_items:
        print(item)
else:
    print("No suspicious hidden files detected")
