import difflib

popular_domains = [
    "google.com",
    "facebook.com",
    "github.com",
    "amazon.com",
    "microsoft.com",
    "apple.com",
    "paypal.com"
]

target = input("Enter domain to analyze: ").lower()

print("\nChecking for possible typosquatting...\n")

for domain in popular_domains:
    similarity = difflib.SequenceMatcher(None, target, domain).ratio()

    if similarity > 0.75 and target != domain:
        print("[ALERT] Possible typosquatting detected")
        print(" Target :", target)
        print(" Similar:", domain)
        print(" Similarity:", round(similarity,2), "\n")

print("Scan complete")
