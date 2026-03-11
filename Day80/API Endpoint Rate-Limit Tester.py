import requests
import time

URL = input("Enter API endpoint URL: ")
REQUEST_COUNT = int(input("Number of requests to send: "))
DELAY = float(input("Delay between requests (seconds): "))

success = 0
blocked = 0
errors = 0

print("\nStarting Rate Limit Test...\n")

for i in range(REQUEST_COUNT):
    try:
        response = requests.get(URL)

        status = response.status_code

        if status == 200:
            success += 1
            print(f"[{i+1}] Success - Status 200")

        elif status == 429:
            blocked += 1
            print(f"[{i+1}] Rate Limit Triggered - Status 429")

        else:
            errors += 1
            print(f"[{i+1}] Other Response - Status {status}")

    except Exception as e:
        errors += 1
        print(f"[{i+1}] Request Error")

    time.sleep(DELAY)

print("\nTest Finished\n")

print("Summary:")
print("Successful responses:", success)
print("Rate limited responses:", blocked)
print("Other errors:", errors)

if blocked == 0:
    print("\n[WARNING] No rate limiting detected")
else:
    print("\n[INFO] Rate limiting appears to be active")
