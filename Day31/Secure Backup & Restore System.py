import shutil
import os
import pathlib

BACKUP_DIR = "backup"

def checksum(file_path):
    with open(file_path, "rb") as f:
        return sum(f.read())

os.makedirs(BACKUP_DIR, exist_ok=True)

while True:
    print("\n1. Backup File\n2. Restore File\n3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        src = input("Enter file path: ")
        if not os.path.exists(src):
            print("File not found")
            continue

        name = pathlib.Path(src).name
        dst = os.path.join(BACKUP_DIR, name)
        shutil.copy(src, dst)

        with open(dst + ".chk", "w") as f:
            f.write(str(checksum(dst)))

        print("Backup completed securely")

    elif choice == "2":
        name = input("Enter file name to restore: ")
        src = os.path.join(BACKUP_DIR, name)

        if not os.path.exists(src):
            print("Backup not found")
            continue

        with open(src + ".chk", "r") as f:
            saved = int(f.read())

        if checksum(src) != saved:
            print("Backup corrupted! Restore blocked")
        else:
            shutil.copy(src, name)
            print("File restored successfully")

    elif choice == "3":
        break
    else:
        print("Invalid option")
