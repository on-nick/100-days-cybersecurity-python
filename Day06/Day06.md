###  What I Learned
```
How to safely build file paths using os.path.join()
How to check if a path exists using os.path.exists()
How to identify files and directories using:
os.path.isfile()
os.path.isdir()
```

###  What I Built
```
A small Python script that:
Creates a file path using folder and file name
Checks whether the path exists
Determines if the path is a file or a directory
```

###  What Failed
```
The program showed “path does not exist” at first
Confusion between a file and a directory path
```

###  How I Fixed It
```
Created the folder before checking the path
Used os.path.isfile() and os.path.isdir() correctly
Printed the path to understand what Python was checking
```

###  Security Insight
```
Safe path handling prevents file access bugs
Incorrect paths can expose sensitive files
Many security issues start with bad path validation
```
