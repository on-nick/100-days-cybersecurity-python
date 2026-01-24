from collections import defaultdict

# Simulated logs from different systems
auth_logs = [
    "192.168.1.10 FAIL",
    "192.168.1.10 FAIL",
    "192.168.1.10 FAIL",
    "10.0.0.5 SUCCESS",
]

web_logs = [
    "192.168.1.10 /admin 403",
    "192.168.1.10 /login 401",
    "10.0.0.5 /home 200",
]

firewall_logs = [
    "192.168.1.10 BLOCK",
    "192.168.1.10 BLOCK",
    "172.16.0.3 ALLOW",
]

threat_db = defaultdict(lambda: {
    "auth_fail": 0,
    "web_fail": 0,
    "fw_block": 0,
    "score": 0
})

# --- Log Processing ---
for log in auth_logs:
    ip, status = log.split()
    if status == "FAIL":
        threat_db[ip]["auth_fail"] += 1
        threat_db[ip]["score"] += 2

for log in web_logs:
    ip, path, code = log.split()
    if code in ["401", "403"]:
        threat_db[ip]["web_fail"] += 1
        threat_db[ip]["score"] += 1

for log in firewall_logs:
    ip, action = log.split()
    if action == "BLOCK":
        threat_db[ip]["fw_block"] += 1
        threat_db[ip]["score"] += 3

# --- Threat Report ---
print("\n=== SIEM THREAT REPORT ===")
for ip, data in threat_db.items():
    if data["score"] >= 6:
        print(f"[HIGH RISK] {ip} -> Score: {data['score']}")
        print(f"  Auth Fails: {data['auth_fail']}")
        print(f"  Web Fails: {data['web_fail']}")
        print(f"  Firewall Blocks: {data['fw_block']}\n")
