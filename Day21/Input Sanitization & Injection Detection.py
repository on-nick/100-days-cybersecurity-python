
def detect_sql_injection(user_input):
    # Common SQL injection keywords
    dangerous_words = [
        "select", "insert", "delete", "update", "drop",
        "alter", "truncate", "--", ";", "or", "and", "'"
    ]

    user_input_lower = user_input.lower()

    for word in dangerous_words:
        if word in user_input_lower:
            return True
    return False


def sanitize_input(user_input):
    # Remove dangerous characters
    bad_chars = ["'", '"', ";", "--"]

    for char in bad_chars:
        user_input = user_input.replace(char, "")

    return user_input


# Main Program
print("=== Input Sanitization & Injection Detection ===")

user_input = input("Enter your input: ")

# Check for SQL Injection
if detect_sql_injection(user_input):
    print("\n⚠ WARNING: Possible SQL Injection Detected!")
else:
    print("\n✅ Input seems safe.")

# Sanitize Input
clean_input = sanitize_input(user_input)

print("\nSanitized Input:")
print(clean_input)
