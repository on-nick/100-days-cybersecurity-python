import time
import re
import pyperclip

print("Clipboard Hijacking Detector\n")

# Regex for crypto wallet patterns (BTC, ETH basic)
patterns = {
    "Bitcoin": r"\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b",
    "Ethereum": r"\b0x[a-fA-F0-9]{40}\b"
}

last_clipboard = ""

print("[*] Monitoring clipboard...\n")

while True:
    try:
        current = pyperclip.paste()

        if current != last_clipboard:
            print("[+] Clipboard changed")

            for name, pattern in patterns.items():
                if re.search(pattern, current):
                    print(f"[INFO] Detected possible {name} address in clipboard")
                    print("Value:", current, "\n")

            # Detect sudden replacement (possible hijack)
            if last_clipboard and any(re.search(p, last_clipboard) for p in patterns.values()):
                if current != last_clipboard:
                    print("[ALERT] Clipboard content changed after crypto address copied!")
                    print("Previous:", last_clipboard)
                    print("Current:", current, "\n")

            last_clipboard = current

        time.sleep(1)

    except KeyboardInterrupt:
        print("\n[!] Monitoring stopped")
        break
