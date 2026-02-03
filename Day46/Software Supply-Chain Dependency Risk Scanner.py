import json
import hashlib
import time

KNOWN_BAD_HASHES = {
    "e3b0c44298fc1c149afbf4c8996fb924": "Malicious placeholder package",
    "098f6bcd4621d373cade4e832627b4f6": "Backdoored dependency"
}

RISKY_NAMES = ["test", "tmp", "demo", "example"]

def file_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

print("Supply-Chain Dependency Scanner Started")

dep_file = input("Dependency file (json): ")

try:
    with open(dep_file) as f:
        deps = json.load(f)
except:
    print("Invalid dependency file")
    exit()

risk_score = 0

for dep, meta in deps.items():
    print(f"\nChecking dependency: {dep}")

    for r in RISKY_NAMES:
        if r in dep.lower():
            print("[ALERT] Suspicious package name")
            risk_score += 1

    if "file" in meta:
        try:
            h = file_hash(meta["file"])
            if h in KNOWN_BAD_HASHES:
                print("[CRITICAL] Known malicious dependency detected")
                risk_score += 5
        except:
            print("File not found, skipping hash check")

    if meta.get("maintainer_age_days", 365) < 30:
        print("[ALERT] Very new maintainer")
        risk_score += 1

    time.sleep(0.3)

print("\nScan Complete")
print("Total Risk Score:", risk_score)

if risk_score >= 5:
    print("[CRITICAL] High supply-chain attack risk detected")
elif risk_score >= 2:
    print("[WARNING] Moderate dependency risk detected")
else:
    print("Dependencies look safe")
