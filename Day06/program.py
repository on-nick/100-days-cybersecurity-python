import os

path = os.path.join("myfolder", "test.txt")

print("Checking path:", path)

if os.path.exists(path):
    print("Path exists")
else:
    print("Path does not exist")

if os.path.isdir("myfolder"):
    print("myfolder is a directory")

if os.path.isfile(path):
    print("test.txt is a file")
