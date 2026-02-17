import unicodedata

# Common Cyrillic homoglyph mappings
HOMOGLYPH_MAP = {
    "а": "a",  # Cyrillic a
    "е": "e",  # Cyrillic e
    "о": "o",  # Cyrillic o
    "р": "p",  # Cyrillic r
    "с": "c",  # Cyrillic s
    "х": "x",  # Cyrillic x
    "і": "i",  # Cyrillic i
    "ӏ": "l"   # Cyrillic small el
}

POPULAR_DOMAINS = [
    "google.com",
    "facebook.com",
    "amazon.com",
    "microsoft.com",
    "github.com"
]

def normalize_domain(domain):
    normalized = ""
    for char in domain:
        if char in HOMOGLYPH_MAP:
            normalized += HOMOGLYPH_MAP[char]
        else:
            normalized += char
    return normalized

print("Homoglyph Phishing URL Detector Started\n")

while True:
    domain = input("Enter domain (or 'exit'): ").strip().lower()
    if domain == "exit":
        break

    normalized = normalize_domain(domain)

    if normalized in POPULAR_DOMAINS and domain != normalized:
        print("[CRITICAL] Possible homoglyph phishing detected!")
        print("Original:", domain)
        print("Looks like:", normalized, "\n")
    else:
        print("No obvious homoglyph attack detected\n")
