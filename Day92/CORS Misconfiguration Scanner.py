import requests

print("CORS Misconfiguration Scanner\n")

url = input("Enter target URL (example: https://example.com): ")

test_origins = [
    "https://evil.com",
    "null",
    "https://attacker.com"
]

print("\n[*] Testing CORS policies...\n")

for origin in test_origins:
    try:
        headers = {
            "Origin": origin
        }

        response = requests.get(url, headers=headers)

        acao = response.headers.get("Access-Control-Allow-Origin")
        acc = response.headers.get("Access-Control-Allow-Credentials")

        print(f"[+] Testing Origin: {origin}")

        if acao == "*" and acc == "true":
            print("[CRITICAL] Misconfiguration: '*' with credentials allowed")

        elif acao == origin:
            print("[WARNING] Origin reflected:", origin)

        elif acao:
            print("[INFO] Allowed Origin:", acao)

        else:
            print("[INFO] No CORS header found")

        print()

    except:
        print("[!] Request failed\n")

print("Scan complete")
