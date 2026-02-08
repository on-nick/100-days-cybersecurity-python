import time
import hashlib
import pyperclip

CHECK_INTERVAL = 2
SENSITIVE_KEYWORDS = ["password", "token", "secret", "apikey"]

last_hash = None

print("Clipboard Monitor Started...\n")

while True:
    time.sleep(CHECK_INTERVAL)
    data = pyperclip.paste()

    if not data:
        continue

    current_hash = hashlib.sha256(data.encode()).hexdigest()

    if current_hash != last_hash:
        last_hash = current_hash
        print("[INFO] Clipboard changed")

        lower = data.lower()
        for key in SENSITIVE_KEYWORDS:
            if key in lower:
                print("[ALERT] Sensitive data copied to clipboard!")
                break
