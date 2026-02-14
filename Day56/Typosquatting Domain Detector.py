import difflib

POPULAR_PACKAGES = [
    "requests",
    "flask",
    "django",
    "numpy",
    "pandas",
    "express",
    "react",
    "lodash"
]

SIMILARITY_THRESHOLD = 0.80

print("Typosquatting Detector Started\n")

while True:
    name = input("Enter package/domain name (or 'exit'): ").strip().lower()
    if name == "exit":
        break

    flagged = False

    for legit in POPULAR_PACKAGES:
        ratio = difflib.SequenceMatcher(None, name, legit).ratio()

        # 1. High similarity but not exact
        if ratio >= SIMILARITY_THRESHOLD and name != legit:
            print(f"[ALERT] Possible typosquatting of '{legit}' (similarity: {ratio:.2f})")
            flagged = True

        # 2. Common character substitution check
        substitutions = [
            legit.replace("o", "0"),
            legit.replace("l", "1"),
            legit.replace("a", "@")
        ]

        if name in substitutions:
            print(f"[CRITICAL] Character substitution attack detected for '{legit}'")
            flagged = True

    if not flagged:
        print("No obvious typosquatting detected\n")
