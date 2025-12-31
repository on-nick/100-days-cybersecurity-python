from datetime import datetime

# Get current date and time
current_time = datetime.now()

# Print raw date and time
print("Current date and time:", current_time)

# Print formatted date and time
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_time)
