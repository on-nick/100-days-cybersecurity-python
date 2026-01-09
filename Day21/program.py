import time

password = "secure123"
tries = 0

while tries < 3:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Login Successful")
        break
    else:
        tries += 1
        print("Wrong password")
        time.sleep(2)

if tries == 3:
    print("Too many attempts. Access denied.")
