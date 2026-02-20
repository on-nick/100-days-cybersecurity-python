import os
import stat

SCAN_PATHS = ["/etc", "/usr", "/var", "/home"]
EXCLUDE_DIRS = {"/proc", "/sys", "/dev"}

print("World-Writable File Auditor Started\n")

for base in SCAN_PATHS:
    if not os.path.exists(base):
        continue

    for root, dirs, files in os.walk(base):
        if any(root.startswith(ex) for ex in EXCLUDE_DIRS):
            continue

        for name in files:
            path = os.path.join(root, name)
            try:
                mode = os.stat(path).st_mode
                if mode & stat.S_IWOTH:
                    print("[ALERT] World-writable file found:")
                    print(" Path:", path, "\n")
            except:
                continue

        for name in dirs:
            path = os.path.join(root, name)
            try:
                mode = os.stat(path).st_mode
                if mode & stat.S_IWOTH:
                    print("[WARNING] World-writable directory found:")
                    print(" Path:", path, "\n")
            except:
                continue

print("Scan Complete")
