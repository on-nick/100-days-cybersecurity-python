
api_response = {
    "ip": "8.8.8.8",
    "reputation": "clean",
    "country": "United States",
    "malicious": False
}

# Reading data from the simulated API response
print("IP Address:", api_response["ip"])
print("Reputation:", api_response["reputation"])
print("Country:", api_response["country"])

# Basic security-related logic
if api_response["malicious"]:
    print("Warning: This IP may be malicious")
else:
    print("Status: No malicious activity detected")
