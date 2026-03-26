import requests
from urllib.parse import urlparse, parse_qs

print("OAuth Token Leakage Detector\n")

url = input("Enter OAuth redirect URL (example: https://example.com/callback#access_token=XYZ): ")

parsed = urlparse(url)

print("\n[*] Analyzing URL...\n")

# Check fragment (after #)
if parsed.fragment:
    params = parse_qs(parsed.fragment)

    if "access_token" in params:
        print("[CRITICAL] Access token exposed in URL fragment!")
        print("Token:", params["access_token"][0], "\n")

# Check query parameters
if parsed.query:
    params = parse_qs(parsed.query)

    if "access_token" in params:
        print("[CRITICAL] Access token exposed in query parameters!")
        print("Token:", params["access_token"][0], "\n")

    if "code" in params:
        print("[INFO] Authorization code found (normal in OAuth flow)")
        print("Code:", params["code"][0], "\n")

# Check for open redirect risk
redirect_param = ["redirect_uri", "redirect", "url", "next"]

for param in redirect_param:
    if param in parsed.query:
        print("[WARNING] Possible open redirect parameter detected:", param)

print("Analysis complete")
