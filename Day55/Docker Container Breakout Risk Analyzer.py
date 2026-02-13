import json
import os

RISK_SCORE = 0

HIGH_RISK_FLAGS = [
    "Privileged",
    "PidMode",
    "NetworkMode",
    "CapAdd",
    "Binds"
]

print("Docker Breakout Risk Analyzer\n")

inspect_file = input("Enter docker inspect JSON file path: ")

try:
    with open(inspect_file, "r") as f:
        data = json.load(f)[0]
except:
    print("Invalid inspect file")
    exit()

host_config = data.get("HostConfig", {})
config = data.get("Config", {})

# 1. Privileged mode
if host_config.get("Privileged"):
    print("[CRITICAL] Container running in privileged mode")
    RISK_SCORE += 3

# 2. Host PID namespace
if host_config.get("PidMode") == "host":
    print("[ALERT] Sharing host PID namespace")
    RISK_SCORE += 2

# 3. Host network
if host_config.get("NetworkMode") == "host":
    print("[ALERT] Sharing host network")
    RISK_SCORE += 2

# 4. Dangerous capabilities
caps = host_config.get("CapAdd", [])
if caps:
    print("[ALERT] Added Linux capabilities:", caps)
    RISK_SCORE += len(caps)

# 5. Host filesystem mounts
binds = host_config.get("Binds", [])
if binds:
    for b in binds:
        if b.startswith("/:/"):
            print("[CRITICAL] Host root mounted inside container")
            RISK_SCORE += 3
        else:
            print("[WARNING] Host bind mount:", b)
            RISK_SCORE += 1

print("\nFinal Risk Score:", RISK_SCORE)

if RISK_SCORE >= 5:
    print("[CRITICAL] High container breakout risk")
elif RISK_SCORE >= 2:
    print("[WARNING] Moderate risk configuration")
else:
    print("Container configuration appears low risk")
