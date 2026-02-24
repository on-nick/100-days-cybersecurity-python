import os

SUSPICIOUS_PATTERNS = [
    "nc ",
    "bash -i",
    "curl ",
    "wget ",
    "python -c",
    "/dev/tcp/",
    "base64 -d",
    "nohup "
]

FILES_TO_SCAN = [".bashrc", ".profile", ".bash_profile"]

print("Shell Startup Persistence Detector Started\n")

for home in os.listdir("/home"):
    user_home = os.path.join("/home", home)

    if not os.path.isdir(user_home):
        continue

    for filename in FILES_TO_SCAN:
        path = os.path.join(user_home, filename)

        if not os.path.isfile(path):
            continue

        try:
            with open(path, "r", errors="ignore") as f:
                lines = f.readlines()

            for line in lines:
                clean = line.strip()
                if clean.startswith("#") or not clean:
                    continue

                for pattern in SUSPICIOUS_PATTERNS:
                    if pattern in clean:
                        print("[ALERT] Suspicious persistence found")
                        print(" User:", home)
                        print(" File:", path)
                        print(" >", clean[:120], "\n")
                        break

        except:
            continue

print("Scan Complete")
