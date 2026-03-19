import sqlite3
import os

print("Browser Cookie Security Analyzer\n")

cookie_db = input("Enter path to browser cookie database: ")

if not os.path.isfile(cookie_db):
    print("File not found")
    exit()

try:
    conn = sqlite3.connect(cookie_db)
    cursor = conn.cursor()
except:
    print("Could not open database")
    exit()

# Chrome/Chromium cookie schema example
query = "SELECT host_key, name, is_secure, is_httponly FROM cookies"

try:
    cursor.execute(query)
    cookies = cursor.fetchall()
except:
    print("Invalid cookie database format")
    exit()

print("\nAnalyzing cookies...\n")

insecure_count = 0

for host, name, secure, httponly in cookies:
    
    # Check missing Secure flag
    if secure == 0:
        print("[WARNING] Cookie without Secure flag")
        print("Domain:", host)
        print("Cookie:", name, "\n")
        insecure_count += 1

    # Check missing HttpOnly flag
    if httponly == 0:
        print("[WARNING] Cookie without HttpOnly flag")
        print("Domain:", host)
        print("Cookie:", name, "\n")
        insecure_count += 1

print("Analysis complete\n")
print("Total cookies checked:", len(cookies))
print("Potentially insecure cookies:", insecure_count)
