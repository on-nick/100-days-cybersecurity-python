from collections import defaultdict

RATE_LIMIT = 5   # max requests
WINDOW = 10      # time window (simulated)

request_logs = defaultdict(list)

def log_request(ip, time):
    request_logs[ip].append(time)

def analyze_requests():
    print("\n--- API Abuse Report ---")
    for ip, times in request_logs.items():
        if len(times) >= RATE_LIMIT:
            print(f"ALERT: {ip} exceeded rate limit ({len(times)} requests)")
        else:
            print(f"{ip}: normal usage")

# ---- Simulation ----
requests = [
    ("192.168.1.10", 1),
    ("192.168.1.10", 2),
    ("192.168.1.10", 3),
    ("192.168.1.10", 4),
    ("192.168.1.10", 5),
    ("192.168.1.10", 6),
    ("10.0.0.5", 2),
    ("10.0.0.5", 6),
]

for ip, t in requests:
    log_request(ip, t)

analyze_requests()
