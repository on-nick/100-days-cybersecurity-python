import math
from collections import defaultdict

THRESHOLD_ENTROPY = 4.0
QUERY_LIMIT = 5

dns_logs = defaultdict(list)

def entropy(text):
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    ent = 0
    for count in freq.values():
        p = count / len(text)
        ent -= p * math.log2(p)
    return ent

print("DNS Tunneling Detector Started")

while True:
    domain = input("\nDNS Query Domain: ")
    ip = input("Source IP: ")

    subdomain = domain.split(".")[0]
    ent = entropy(subdomain)

    dns_logs[ip].append(ent)

    if ent > THRESHOLD_ENTROPY:
        print(f"[ALERT] High entropy DNS query detected ({ent:.2f})")

    if len(dns_logs[ip]) >= QUERY_LIMIT:
        avg_entropy = sum(dns_logs[ip]) / len(dns_logs[ip])
        if avg_entropy > THRESHOLD_ENTROPY:
            print(f"[CRITICAL] Possible DNS tunneling from {ip}")
        dns_logs[ip].clear()
