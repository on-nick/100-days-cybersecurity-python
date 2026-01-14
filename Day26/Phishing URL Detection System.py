import re
from urllib.parse import urlparse

suspicious_keywords = [
    "login", "verify", "update", "secure", "account",
    "bank", "free", "bonus", "confirm"
]

def check_url(url):
    score = 0
    parsed = urlparse(url)

    if parsed.scheme != "https":
        score += 1

    if len(url) > 75:
        score += 1

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 1

    for word in suspicious_keywords:
        if word in url.lower():
            score += 1

    if "@" in url or "-" in parsed.netloc:
        score += 1

    return score

while True:
    print("\n1. Check URL")
    print("2. Exit")
    choice = input("Choice: ")

    if choice == "1":
        url = input("Enter URL: ")
        risk = check_url(url)

        print("\n--- Scan Result ---")
        if risk >= 4:
            print("High Risk: Likely Phishing URL")
        elif risk >= 2:
            print("Medium Risk: Suspicious URL")
        else:
            print("Low Risk: URL Looks Safe")

    elif choice == "2":
        break
    else:
        print("Invalid option")
