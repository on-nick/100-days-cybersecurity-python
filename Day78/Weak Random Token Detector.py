import math
from collections import Counter

TOKEN_FILE = input("Enter token file: ")

def entropy(data):
    if not data:
        return 0

    counts = Counter(data)
    total = len(data)

    e = 0
    for c in counts.values():
        p = c / total
        e -= p * math.log2(p)

    return e

try:
    with open(TOKEN_FILE) as f:
        tokens = [line.strip() for line in f if line.strip()]
except:
    print("Token file not found")
    exit()

print("\nAnalyzing tokens...\n")

for token in tokens:
    e = entropy(token)

    if e < 3.5:
        print("[ALERT] Very low randomness token")
        print(" Token:", token)
        print(" Entropy:", round(e,2), "\n")

    elif e < 4.5:
        print("[WARNING] Possibly weak token")
        print(" Token:", token)
        print(" Entropy:", round(e,2), "\n")

print("Analysis complete")
