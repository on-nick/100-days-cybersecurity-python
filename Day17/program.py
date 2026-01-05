import string
import secrets

def generate_password(length= 15):
  alphabet = (
    string.ascii_letters +
    string.digits +
    string.punctuation
  )
  return ''.join(secrets.choice(alphabet)
    for _ in range(length))
password = generate_password()
print(f"your new password : (password)")
