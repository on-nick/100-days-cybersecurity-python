import os
import pwd

SUSPICIOUS_KEYWORDS = [
    "command=",
    "no-pty",
    "from=",
    "permitopen=",
    "environment="
]

print("SSH authorized_keys Backdoor Detector Started\n")

def scan_authorized_keys(user_home, username):
    ssh_path = os.path.join(user_home, ".ssh", "authorized_keys")
    if not os.path.isfile(ssh_path):
        return

    try:
        with open(ssh_path, "r", errors="ignore") as f:
            lines = f.readlines()

        for line in lines:
            clean = line.strip()
            if not clean or clean.startswith("#"):
                continue

            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in clean:
                    print("[ALERT] Suspicious SSH key option detected")
                    print(" User:", username)
                    print(" File:", ssh_path)
                    print(" >", clean[:120], "\n")
                    break

            if len(clean.split()) < 2:
                print("[WARNING] Malformed SSH key entry")
                print(" User:", username)
                print(" >", clean, "\n")

    except:
        pass

for user in pwd.getpwall():
    home_dir = user.pw_dir
    if os.path.isdir(home_dir):
        scan_authorized_keys(home_dir, user.pw_name)

print("Scan Complete")
