import sqlite3
import os
import re

print("Browser History Analyzer\n")

db_path = input("Enter path to browser history database: ")

if not os.path.isfile(db_path):
    print("File not found")
    exit()

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
except:
    print("Could not open database")
    exit()

# Chrome/Chromium history table
query = "SELECT url, title FROM urls"

try:
    cursor.execute(query)
    rows = cursor.fetchall()
except:
    print("Invalid history database format")
    exit()

suspicious_keywords = [
    "login",
    "admin",
    "bank",
    "secure",
    "password",
    "verify",
    "account"
]

print("\n[*] Analyzing browsing history...\n")

alerts = 0

for url, title in rows:
    text = (url + " " + (title or "")).lower()

    for keyword in suspicious_keywords:
        if re.search(keyword, text):
            print("[WARNING] Sensitive or risky page visited")
            print("URL:", url)
            print("Title:", title, "\n")
            alerts += 1
            break

print("Analysis complete\n")
print("Total entries checked:", len(rows))
print("Suspicious entries found:", alerts)
