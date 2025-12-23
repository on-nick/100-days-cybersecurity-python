simple program
```python
import requests
response = requests.get("https://google.com")
print("Status Code:",response.status_code)
