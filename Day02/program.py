```
import re

# Open the file in read mode
with open("sample.txt", "r") as file:
    for line in file:
        line = line.strip()   # remove newline

        # check if the word 'failed' exists in the line
        if re.search("failed", line):
            print(line)
```
