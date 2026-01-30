import os
import math
import time

WATCH_DIR = "watch_folder"
ENTROPY_THRESHOLD = 7.5
SUSPICIOUS_COUNT = 3

os.makedirs(WATCH_DIR, exist_ok=True)
alert_count = 0

def calculate_entropy(data):
    if not data:
        return 0
    freq = {}
    for b in data:
        freq[b] = freq.get(b, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / len(data)
        entropy -= p * math.log2(p)
    return entropy

print("Ransomware Detection Engine Running...")

while True:
    time.sleep(3)
    for file in os.listdir(WATCH_DIR):
        path = os.path.join(WATCH_DIR, file)
        if not os.path.isfile(path):
            continue

        try:
            with open(path, "rb") as f:
                data = f.read(2048)
            entropy = calculate_entropy(data)

            if entropy > ENTROPY_THRESHOLD:
                print(f"[ALERT] High entropy detected: {file} ({entropy:.2f})")
                alert_count += 1
        except:
            continue

    if alert_count >= SUSPICIOUS_COUNT:
        print("\n[CRITICAL] Possible ransomware activity detected!")
        break
