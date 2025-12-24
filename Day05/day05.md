##  What I Learned
```
How to use the Python os library to interact with the operating system
How to get the current working directory using os.getcwd()
How to list files and folders using os.listdir()
How to check if a file exists with os.path.exists()
How to create a folder with os.mkdir()
```

##  What I Built
```
A simple Python script that:
Prints the current working directory
Lists all files in that directory
Checks if a file named test.txt exists
Creates a folder named myfolder if it doesn’t exist
```

##  What Failed
```
Tried to create a folder that already existed → got an error
Initially forgot to import os → program crashed
```

##  How I Fixed It
```
Added a check using os.path.exists() before creating the folder
Remembered to import os at the top of the script
```
##  Security Insight
```
Security tools often scan directories and files
Checking file/folder existence is a common task in monitoring systems
Understanding system paths is critical for safe automation and log analysis
```
