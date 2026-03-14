import os
import re
import base64

print("Base64 Payload Detector\n")

TARGET_DIR = input("Enter directory to scan: ")

# pattern for long base64 strings
base64_pattern = r"[A-Za-z0-9+/]{40,}={0,2}"

def try_decode(data):
    try:
        decoded = base64.b64decode(data).decode("utf-8", errors="ignore")
        return decoded
    except:
        return None


print("\nScanning files...\n")

for root, dirs, files in os.walk(TARGET_DIR):
    for file in files:
        path = os.path.join(root, file)

        try:
            with open(path, "r", errors="ignore") as f:
                content = f.read()

            matches = re.findall(base64_pattern, content)

            for match in matches:
                decoded = try_decode(match)

                if decoded and len(decoded.strip()) > 10:
                    print("[ALERT] Encoded payload detected")
                    print("File:", path)
                    print("Encoded:", match[:60])
                    print("Decoded:", decoded[:120], "\n")

        except:
            continue

print("Scan complete")
