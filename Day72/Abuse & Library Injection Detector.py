import os

SUSPICIOUS_PATHS = ["/tmp", "/dev/shm", "/var/tmp"]
LD_FILES = ["/etc/ld.so.preload"]

print("LD_PRELOAD Injection Detector Started\n")

# 1. Check global preload file
for file in LD_FILES:
    if os.path.isfile(file):
        with open(file, "r", errors="ignore") as f:
            for line in f:
                lib = line.strip()
                if lib:
                    print("[CRITICAL] Global LD_PRELOAD detected:")
                    print(" File:", file)
                    print(" Library:", lib, "\n")

# 2. Check environment variable
ld_env = os.environ.get("LD_PRELOAD")
if ld_env:
    print("[ALERT] LD_PRELOAD environment variable set:")
    print(" Value:", ld_env, "\n")

# 3. Check suspicious shared libraries on disk
for root, _, files in os.walk("/"):
    for file in files:
        if file.endswith(".so"):
            path = os.path.join(root, file)
            for sp in SUSPICIOUS_PATHS:
                if path.startswith(sp):
                    print("[ALERT] Suspicious shared library location:")
                    print(" Path:", path, "\n")
