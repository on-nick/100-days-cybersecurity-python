Test with weak & strong passwords
```python
import re

password = input("Enter password: ")

if len(password) < 8:
    print("Weak password: Too short")

elif not re.search("[0-9]", password):
    print("Weak password: No number")

else:
    print("Strong password")
  
