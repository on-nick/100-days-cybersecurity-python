import time

print("Timing Attack Simulator\n")

SECRET = "secure123"

def vulnerable_compare(user_input, secret):
    for i in range(min(len(user_input), len(secret))):
        if user_input[i] != secret[i]:
            return False
        time.sleep(0.05)  # delay per correct character
    return len(user_input) == len(secret)

def measure_time(guess):
    start = time.time()
    vulnerable_compare(guess, SECRET)
    return time.time() - start

charset = "abcdefghijklmnopqrstuvwxyz0123456789"
guessed = ""

print("[*] Recovering password using timing attack...\n")

for i in range(len(SECRET)):
    timings = []

    for c in charset:
        attempt = guessed + c
        t = measure_time(attempt)
        timings.append((c, t))

    timings.sort(key=lambda x: x[1], reverse=True)
    best_char = timings[0][0]
    guessed += best_char

    print(f"[+] Discovered so far: {guessed}")

print("\n[!] Final guessed password:", guessed)
