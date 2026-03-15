import requests

print("HTTP Security Header Analyzer\n")

url = input("Enter website URL (example: https://example.com): ")

security_headers = {
    "Strict-Transport-Security": "Protects against protocol downgrade attacks",
    "Content-Security-Policy": "Prevents many XSS attacks",
    "X-Frame-Options": "Protects against clickjacking",
    "X-Content-Type-Options": "Prevents MIME sniffing",
    "Referrer-Policy": "Controls referrer information",
    "Permissions-Policy": "Restricts browser features"
}

try:
    response = requests.get(url)
except:
    print("Could not connect to the website")
    exit()

headers = response.headers

print("\nSecurity Header Report\n")

missing = []

for header, description in security_headers.items():
    if header in headers:
        print("[OK]", header)
        print("Value:", headers[header])
        print()
    else:
        print("[WARNING] Missing header:", header)
        print("Purpose:", description)
        print()
        missing.append(header)

print("Summary\n")

print("Total headers checked:", len(security_headers))
print("Missing headers:", len(missing))

if missing:
    print("\nPotential security improvements needed.")
else:
    print("\nAll recommended security headers detected.")
