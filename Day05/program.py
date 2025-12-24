import os

# Current directory
print("Current Directory:", os.getcwd())

# List files
print("Files and Folders:", os.listdir())

# Check if a file exists
if os.path.exists("test.txt"):
    print("File exists")
else:
    print("File not found")

# Create a folder if it doesn't exist
if not os.path.exists("myfolder"):
    os.mkdir("myfolder")
    print("Folder created")
else:
    print("Folder already exists")
