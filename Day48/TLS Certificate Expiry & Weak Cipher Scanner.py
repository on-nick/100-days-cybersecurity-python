import ssl
import socket
import datetime

TIMEOUT = 5
WEAK_KEY_SIZE = 2048

def scan_host(host, port=443):
    ctx = ssl.create_default_context()
    with socket.create_connection((host, port), timeout=TIMEOUT) as sock:
        with ctx.wrap_socket(sock, server_hostname=host) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()

    not_after = datetime.datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
    days_left = (not_after - datetime.datetime.utcnow()).days

    pubkey_bits = cert.get("subjectPublicKeyInfo", {}).get("key_size", None)

    print(f"\nHost: {host}")
    print("Cipher:", cipher[0])
    print("Cert expires in:", days_left, "days")

    if days_left < 30:
        print("[ALERT] Certificate expiring soon")

    if pubkey_bits and pubkey_bits < WEAK_KEY_SIZE:
        print("[ALERT] Weak public key size")

while True:
    target = input("\nEnter domain (or 'exit'): ").strip()
    if target.lower() == "exit":
        break
    try:
        scan_host(target)
    except Exception as e:
        print("[ERROR] Scan failed:", e)
