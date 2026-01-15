import os

def xor_encrypt(data, key):
    result = ""
    for ch in data:
        result += chr(ord(ch) ^ key)
    return result

while True:
    print("\n1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Choice: ")

    if choice in ["1", "2"]:
        file_path = input("Enter file path: ")

        if not os.path.exists(file_path):
            print("File not found")
            continue

        key = int(input("Enter numeric key (1-255): "))

        with open(file_path, "r") as f:
            content = f.read()

        processed = xor_encrypt(content, key)

        new_file = file_path + (".enc" if choice == "1" else ".dec")
        with open(new_file, "w") as f:
            f.write(processed)

        print("Operation completed:", new_file)

    elif choice == "3":
        break
    else:
        print("Invalid option")
