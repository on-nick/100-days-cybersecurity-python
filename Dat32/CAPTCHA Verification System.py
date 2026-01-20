import random
import string

def generate_captcha(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

attempts = 3

while attempts > 0:
    captcha = generate_captcha()
    print("\nCAPTCHA:", captcha)
    user_input = input("Enter CAPTCHA: ")

    if user_input == captcha:
        print("Verification successful. Access granted.")
        break
    else:
        attempts -= 1
        print("Incorrect CAPTCHA. Attempts left:", attempts)

if attempts == 0:
    print("Access blocked. Possible bot detected.")
